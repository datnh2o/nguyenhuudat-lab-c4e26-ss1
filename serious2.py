from flask import Flask
app = Flask(__name__)

Users = {
	"huy" :         {
		"name" : "Nguyen Quang Huy",
		"age" : 29
       },
    "tuananh" : {
		"name" : "Huynh Tuan Anh",
		"age" : 22
       },
    "dat" : {
        "name" : "Nguyn Huu Dat",
        "age" : 19
    }   

}
@app.route("/user/<username>")

def user(username):
    
    return str(Users[username])    


if __name__ == '__main__':
  app.run(debug=True)