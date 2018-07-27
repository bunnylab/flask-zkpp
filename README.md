# Flask-ZKPP

Flask-ZKPP adds a interactive login proof based on public key cryptography
to flask-login. The goal is to have a simple and secure way to use public key
crypto in addition to or instead of classic username/password based login
systems.

Flask-ZKPP login proof does not require any user data to be persisted so it
can be used without a database. Everything still under construction don't use
lol.

## Installation

```sh
$ python setup.py install
```

## Usage

Install, and import the extension into your flask application. Requires
flask-login and PyCrypto. Extension can be initialized with a flask application
and a loginmanager from flask_login. If you don't provide a loginmanager on
initialization the extension will create one for you.

```python
import flask
from flask_zkpp import ZKPP

app = flask.Flask(__name__)
app.secret_key = 'no one will ever guess this'
zkpp = ZKPP()
zkpp.init_app(app)

```
