from flask import Flask, render_template
import psutil
import flaskwebgui

app = Flask(__name__)
gui = flaskwebgui.FlaskUI(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/cpu')
def api():
    return str(psutil.cpu_percent(interval=0.3))

if __name__ == '__main__':
    # app.run(debug=True)
    gui.run()