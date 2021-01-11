import web
from Models import RegisterModel, LoginModel


web.config.debug = False
urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration',
    '/discover', 'Discover',
    '/profile', 'Profile',
    '/settings', 'Settings',
    '/login', 'Login',
    '/logout', 'Logout',
    '/check-login', 'CheckLogin'
)


app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})



#Classes/Routes
class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class Profile:
    def GET(self):
        return render.Profile()


class Settings:
    def GET(self):
        return render.Settings()


class Discover:
    def GET(self):
        return render.Discover()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.email


class CheckLogin:
    def POST(self):
        data = web.input()
        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_login(data)
        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class Logout:
    def GET(self):
        session['user']= None
        session_data['user'] = None
        session.kill()
        return "success"


class Login:
    def GET(self):
        return render.Login()


if __name__ == "__main__":
    app.run()