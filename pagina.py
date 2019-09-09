from flask import Flask
from flask import render_template
app = Flask(_name_)

@app.router("/")
def index():
    name = "codi"

return render_template("index.html",username=username)

if __name__ == '__main__':
  app:run(debug=True,port=5050)
