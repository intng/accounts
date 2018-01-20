from flask import Flask, request
import os
from app.api import users

app = Flask(__name__)


@app.route('/api/create_user/', methods=['POST'])
def create_user():
    res = request.get_json()
    if 'schoolcard' not in res: res['schoolcard'] = None
    if 'vk_id' not in res: res['vk_id'] = None
    if 'tg_id' not in res: res['schoolcard'] = None
    return users.create(res['name'], res['surname'], res['form'], res['schoolcard'], res['vk_id'], res['tg_id'])


@app.route('/api/check/vk_id/<vk_id>')
def check_vk_id(vk_id):
    return users.check_vk_id(vk_id)


@app.route('/api/check/tg_id/<tg_id>')
def check_tg_id(tg_id):
    return users.check_tg_id(tg_id)


@app.route('/api/check/schoolcard/<schoolcard>')
def check_schoolcard(schoolcard):
    return users.check_schoolcard(schoolcard)


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=int(os.getenv('flask_port')))
