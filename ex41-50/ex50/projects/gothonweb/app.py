from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "World"
    return f'hello, {greeting}!'

if __name__ == "__main__":
    app.run()


# ➜  gothonweb git:(master) ✗ python3.6 app.py
#  * Serving Flask app "app" (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: off
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 127.0.0.1 - - [05/Aug/2019 22:21:55] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [05/Aug/2019 22:21:55] "GET /favicon.ico HTTP/1.1" 404 -

