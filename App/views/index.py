from flask import Blueprint, render_template
import os
blue = Blueprint('blue', __name__)

@blue.route('/')
def index():
    # return 'hahah'
    pwd = os.getcwd()
    print(pwd)
    print(os.listdir(pwd))
    # print(os.listdir('templates'))
    return render_template('index.html')