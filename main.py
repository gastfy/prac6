from flask import Flask, url_for
from random import randint
import base64
import os
import shutil

app = Flask(__name__)

@app.route('/volume/')
def volume():
    files = os.listdir('/app/static')
    if len(files) > 0:
        index = randint(0, len(files)-1)
        filename = os.getcwd() + "/static/" + files[index]
        with open(filename, 'rb') as fd:
            image_as_base64_html = f"""
                <img src="data:image/png;base64,{base64.encodebytes(fd.read()).decode()}">"""
    
        return image_as_base64_html + f"<br><h1>Total files: {len(files)}</h1>"
    else:
        return "<h1>No files!</h1>"


@app.route('/send/')
def send():
    files = os.listdir('/app/bind')
    for file in files:
        shutil.copyfile(os.getcwd() + "/bind/" + file, "/app/static/" + file)
        
    return "<h1>Files sent!</h1>"


@app.route("/clear/")
def clear():
    files = os.listdir('/app/static')
    for file in files:
        os.remove(os.getcwd() + "/static/" + file)
    
    return "<h1>Volume cleaned!</h1>"


@app.route('/bind/')
def bind():
    files = os.listdir('/app/bind')
    if len(files) > 0:
        index = randint(0, len(files)-1)
        filename = os.getcwd() + "/bind/" + files[index]
        with open(filename, 'rb') as fd:
            image_as_base64_html = f"""
                <img src="data:image/png;base64,{base64.encodebytes(fd.read()).decode()}">"""
    
        return image_as_base64_html + f"<br><h1>Total files: {len(files)}</h1>"
    else:
        return "<h1>No files!</h1>"
    

if __name__ == "__main__":
    app.run(debug=True)