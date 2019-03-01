from flask import Flask, redirect
app = Flask(__name__)

@app.route("/about-me")
def dat():
    dat = [
        "Họ và tên: Nguyễn Hữu Đạt",
        "Đang là Sinh viên năm nhất",
        "Đang học tại Học viện Kỹ thuật Mật mã"
    ]
    return str(dat)
@app.route("/school")
def school():
    return redirect ("http://techkids.vn")    

if __name__ == '__main__':
  app.run(debug=True)