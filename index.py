from flask import Flask, request

app = Flask(__name__)

kv_dict = {'abc-1':'value1', 'abc-2':'value2', 'xyz-1':'value3', 'xyz-2':'value4'}

@app.route("/get/<string:key>", methods=["GET", "POST"])
def index(key):
    if request.method in ["GET", "POST"]:
        if key in kv_dict:
            res = kv_dict[key]
            return res
        else:
            return 'Key does not exist'

@app.route("/key/set", methods=["POST"])
def add_new_kv():
    new_addition = request.get_json()
    print(new_addition)
    if not new_addition:
        return 'No payload was passed', 404
    kv_dict.update(new_addition)
    print(kv_dict)
    return 'New KV added'

@app.route("/search", methods=["GET","POST"])
def search_key():
    url = request.url
    if '=' in url:
        search_element = url.split("=")[1]
        print(search_element)
        if '?prefix' in url:
            res = [key for key in kv_dict.keys() if key.startswith(search_element)]
            if not res:
                return 'Not found'
            else:
                return res
        elif '?suffix' in url:
            res = [key for key in kv_dict.keys() if key.endswith(search_element)]
            if not res:
                return 'Not found'
            else:
                return res
        else: 
            return 'Wrong argument passed, only prefix or suffix is supported', 404
    else:
        return 'Invalid search url, please add prefix or suffix argument', 404



if __name__ == "__main__":
    app.run(debug=True)