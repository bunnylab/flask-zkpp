from flask import current_app, _app_ctx_stack
import flask_login
from flaskloginintegration import _user_loader, User
from views import login_views

class ZKPP(object):

    def __init__(self, app=None, login_manager=flask_login.LoginManager()):
        self.app = app
        self.login_manager = login_manager
        if app is not None:
            self.init_app(app)


    def init_app(self, app):
        self.login_manager.init_app(app)
        self.init_login(self.login_manager)
        app.config.setdefault('my_greeting', self.greet())
        app.teardown_appcontext(self.teardown)

        print 'initializing application'
        print 'root path: ' + login_views.root_path
        app.register_blueprint(login_views)  # set login views


    def init_login(self, login_manager):
        login_manager.user_loader(_user_loader)
        #login_manager.request_loader(_request_loader)


    def greet(self):
        return 'hello my friend why so serious?'

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'my_greeting'):
            pass
            #ctx.sqlite3_db.close()
        print 'teardown called'

    @property
    def greeting(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'my_greeting'):
                ctx.my_greeting = self.greet()
            return ctx.my_greeting
