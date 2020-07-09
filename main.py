from flask import Flask, request, redirect, jsonify
from flask import render_template
from base.cfg_parser import BaseConfig
from examinee_info import ExamineeInfo

app = Flask(__name__)


@app.route("/search", methods=['GET', 'POST'])
def search_examinee_number():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        print(request.json)
        print(request.remote_addr)
        name = request.json.get('name')
        user_id = request.json.get("password")
        if user_id in ExamineeInfo:
            res = ExamineeInfo[user_id]
            res['userid'] = user_id
            return jsonify({"code": 200, "data": res})
        return jsonify({"code": 400, "msg": "未查询到考生信息"})
    else:
        return render_template('index.html')


@app.route("/download/<user_id>", methods=['GET'])
def download_file(user_id):
    filepath = 'img/%s.jpg' % user_id
    return app.send_static_file(filepath)


if __name__ == '__main__':
    app.run(host=BaseConfig.server_addr, port=BaseConfig.server_port)
