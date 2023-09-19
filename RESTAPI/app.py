from flask import Flask, request, jsonify

app = Flask(__name__)


num = [1,10,202,12,12,12,20]

@app.route('/')
def hello_world():
    return "Hello World"

@app.route("/evenodd<int:num>")
def evenodd(num):
    status = None
    if num %2 == 0:
        status = "Even"
    else:
        status= "Odd"

    return jsonify({"status:" :status})


@app.route("/addnum", methods = ['POST'])
def addnum():
    request_data= request.get_json()
    print(request_data['num'])
    num.append(request_data['num'])

@app.route('/showlist')
def show():
    return jsonify({'list':num})

if __name__=="__main__":
    app.run(debug=True)
