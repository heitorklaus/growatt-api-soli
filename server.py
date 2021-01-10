import os
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

import sys
import datetime
from growatt import hash_password, GrowattApi, Timespan




username = "solienergiasolar"
password = "soli2020"



with GrowattApi() as api:
    api.login(username, password)
    plant_info = api.plant_list()
    #print(plant_info)

    plant_id = plant_info["data"][0]["plantId"]
    plant_detail = api.plant_detail(plant_id, Timespan.day, datetime.date.today())
    #print(plant_detail)

app = Flask(__name__)

@app.route('/')
def server():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify(plant_detail)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
