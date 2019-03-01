from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:a>/<int:b>")
def bmi(a,b):
    c = b/100
    bmi = a / (c*c)
    if bmi < 16:
        return "Thiếu cân nặng"
    elif 16 <= bmi < 18.5:
        return "Thiếu cân"
    elif 18.5 <= bmi < 25:
        return "Bình thường"
    elif 25 <= bmi < 30:
        return "Thừa cân"
    elif bmi > 30:
        return "Béo phí"   

    return str(bmi)

if __name__ == '__main__':
  app.run(debug=True)