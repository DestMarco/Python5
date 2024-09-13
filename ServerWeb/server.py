from flask import Flask, render_template


api=Flask(__name__)



@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/pippo', methods=['GET'])
def index2():
    return render_template('index2.html')


@api.route('/reggistrati', methods=['GET'])
def reg_ko():
    return render_template('reg_ko.html')


@api.route('/reok', methods=['GET'])
def reg_ok():
    return render_template('reg_ok.html')







api.run(host="0.0.0.0",port=8085)