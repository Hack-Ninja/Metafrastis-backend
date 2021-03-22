from flask import Flask,request,jsonify
# from googletrans import Translator
# translator = Translator()
app = Flask(__name__)


# @app.route('/translate',methods=['POST'])
# def translate():
#     data=request.get_json()
#     text = data['text']
#     lang = data['lan']
#     out = translator.translate(text, dest=lang)
#     return jsonify({"output":out.text})

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__== '__main__':
    print("The App is running .")
    app.run(threaded=True, port=5000)
