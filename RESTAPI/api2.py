from flask import Flask, request, jsonify

app2 = Flask(__name__)

stores = [
    {
        'name': 'beautiful store',
        'items': [
                    {'name': 'flowers', 'price': 100 }
                  ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
                  {'name': 'books', 'price': 100 }
                 ]
    }
]

@app2.route('/')
def home():
    return "Welcome to My Store"

@app2.route('/store')
def get_all_store_num():
    return jsonify({'stores':stores})

@app2.route('/store<string:name>')
def get_Store_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message': 'Store is not found'})




@app2.route('/store', methods = ['POST'])
def create_store():
    requested_data = request.get_json()
    new_store = {
        'name': requested_data['name'],
        'items' : requested_data['items']
    }
    stores.append(new_store)
    return jsonify(new_store)



if __name__=="__main__":
    app2.run(debug=True)
