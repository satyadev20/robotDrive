import robotDrive as robo
from flask import Flask,render_template,json,request,jsonify

app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def controlsImplemetion():
    content = request.get_json()
    if(content["action"] == "forward"):
        robo.forward()
    if(content["action"] == "back"):
        robo.back()
    if(content["action"] == "left"):
        robo.left()
    if(content["action"] == "right"):
        robo.right()
    x={'result':content["action"]}
    return jsonify(x)

if __name__=="__main__":
    app.run(port=8001)

