from src.views.user_view import UserView

user_view = UserView()

if __name__ == '__main__':
    
    username = user_view.get_login_details()

    while (not username):
        username = user_view.get_login_details()