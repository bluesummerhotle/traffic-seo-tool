from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Tool SEO chạy ngon!"

if __name__ == '__main__':
    app.run()
