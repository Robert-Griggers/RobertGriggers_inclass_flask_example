from http.cookiejar import debug

from app import app

if __name__ == '__main__':
    app.run(debug=True)