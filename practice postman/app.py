from flask import Flask,request ,jsonify



app=Flask(__name__)


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
        }]


@app.route('/')
def hello():
    return "hello to api"


@app.route('/store')
def get_al_store_names():
     return jsonify({'stores':stores})


@app.route('/store',methods=['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item',methods=['POST'])
def create_store_name(name):w3
    request_data=request.get_json()
    for store in stores:
        if(store['name']==name):
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})    
    
     


if __name__=='__main__':
    app.run(debug=True)