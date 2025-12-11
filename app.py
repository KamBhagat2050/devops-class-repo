from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        try:
            expression = request.form.get('expression', '')
            result = str(eval(expression))  # simple eval for demo, not safe for production
        except Exception as e:
            result = "Error: " + str(e)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
