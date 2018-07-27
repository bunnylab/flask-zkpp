from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask import Flask
from flask_login import current_user
from Crypto.Hash import SHA256
import flask, flask_login
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Random import random
from cStringIO import StringIO
from flaskloginintegration import User

# I don't get where the templates need to be located for this combination of
# extension containing package containing blueprint

login_views = Blueprint('login_views', __name__,
                        template_folder='templates')


@login_views.route('/test/')
def test():
    return 'I am the best'


@login_views.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <textarea name='pubkey' id='pubkey' placeholder='pubkey' rows="10" cols="50"></textarea>
                <input type='submit' name='submit'/>
               </form>
               '''
    if flask.request.method == 'POST':
        userpubkey = flask.request.form['pubkey']
        try:
            pubkey = RSA.importKey(userpubkey)
        except Exception as e:
            print e
            return 'Bad Pubkey', 400

        flask_login.login_user( User(pubkey.exportKey(format='PEM')) )
        return flask.redirect(flask.url_for('login_views.challenge'))


@login_views.route('/challenge', methods=['GET','POST'])
def challenge():
    if flask.request.method == 'GET':
        print current_user.get_id()
        pubkey = current_user.pubkey

        challenge = random.getrandbits(10)
        print 'challenge coming'
        print challenge
        e_challenge = pubkey.encrypt(challenge, 32)[0]
        current_user.e_challenge = e_challenge
        return '''
                {}
               <form action='challenge' method='POST'>
                <textarea name='response' id='response' placeholder='response' rows="10" cols="50"></textarea>
                <input type='submit' name='submit'/>
               </form>
               '''.format(e_challenge), 200

    if flask.request.method == 'POST':
        response = flask.request.form['response']
        try:
            print response
            response = long(response)
            e_response = current_user.pubkey.encrypt(response, 32)[0]
            print e_response
            if e_response == current_user.e_challenge:
                print 'it worked!'
                current_user.authenticated = True
            else:
                print 'not equal the stuff'
                current_user.autenticated = False
        except Exception as e:
            print e
            return 'Something went wrong', 400

        return flask.redirect(flask.url_for('login_views.protected'))


@login_views.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_views.route('/protected')
@flask_login.login_required
def protected():
    print 'test'
    return 'Logged in as: ' + str(flask_login.current_user.id)
    #return render_template('zkpp/protected.html')
