import web
from Models import RegisterModel, LoginModel


urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration',
    '/discover', 'Discover',
    '/profile', 'Profile',
    '/settings', 'Settings',
    '/login', "Login",
    '/check-login', 'CheckLogin'
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


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
        print("in the post")
        data = web.input()
        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_user(data)
        if isCorrect:
            print("success")
            return isCorrect

        return "error"


class Login:
    def GET(self):
        return render.Login()


if __name__ == "__main__":
    app.run()