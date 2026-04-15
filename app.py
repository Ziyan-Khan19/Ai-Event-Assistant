from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 AI Event Assistant is running!"

if __name__ == '__main__':
    app.run()
