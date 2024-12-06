from app import app

@app.route("/<string:name>", methods = ['GET'])
def hello(name):
    return f"<p>Hello, {name}!</p>"