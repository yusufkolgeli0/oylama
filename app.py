from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/toplam", methods = ["GET","POST"])
def toplam():
    print(request.method)
    if request.method == "POST":
        number1=request.form.get("number1")
        number2=request.form.get("number2")
        print(number2, number1)
        return render_template("number.html",total=(int(number1)+int(number2)),number1=number1,number2=number2)
    else:
        return render_template("number.html")



if __name__ == "__main__":
    app.run(debug = True)


