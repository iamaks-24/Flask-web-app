# flask-login module helps in login creation
# flask-sqlalchemy module helps to create database 

from website import create_app #as website vl b acting as python package,whenever its called __init__.py file is executed collects respective need

app=create_app()
if __name__ == '__main__':#it makes sure that this file is runned only when main file is runned and not importing of main file in another file
    app.run(debug=True) #debug=True means whenever i make changes to code,it automatically reruns the flask web server
 