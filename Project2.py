# -*- coding: UTF-8 -*-
from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import re

app = Flask(__name__)
bootstrap = Bootstrap(app)
data = open('Data/data.txt')
tel = data.read()

@app.route('/', methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        inner = request.form.get('input')
        if inner:
            num = re.search('(1\d{6})(\d{4})?', inner)
            if num:
                n = num.group(1)
            else:
                n = 'QWER'
            a = re.search(n + '.{5}(.{2}).{5}(.{2}).{5}(.{4})', tel)
            if a:
                outer = '归属地:'+a.group(1)+a.group(2)+'\n运营商:'+a.group(3)
            else:
                outer = '查无结果'
            output = outer
        else:
            output = "No Input"
    return render_template('index.html', output=output)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
