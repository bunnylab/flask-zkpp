import flask_login
from Crypto.PublicKey import RSA
print 'loading shit for flask login'


class User(object):

    def __init__(self, pubkey, active=True, authenticated=False, anonymous=False):
        self.id = pubkey
        self.active = active
        self.authenticated = authenticated
        self.anonymous = anonymous
        self.e_challenge = None
        # some weird behavior here
        try:
            self.pubkey = RSA.importKey(pubkey)
        except Exception as e:
            print e
            return None

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return self.anonymous

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return self.authenticated

    def get_id(self):
        return self.id

    @staticmethod
    def get(pub_key):
        if pub_key:
            return User(pub_key)  # must return a unicode identifier user pubkey
        else:
            return None


#@login_manager.user_loader
def _user_loader(pub_key):
    return User.get(pub_key)

'''
#@login_manager.request_loader
def _request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user
'''
