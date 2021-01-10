import web
from Models import RegisterModel


urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration',
    '/discover', 'Discover',
    '/profile', 'Profile',
    '/settings', 'Settings'
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
        reg_model.insert_email(data)
        return data.email


if __name__ == "__main__":
    app.run()