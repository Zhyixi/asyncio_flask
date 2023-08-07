import asyncio
# from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify
import time
import uvicorn
import os
from flask import (Blueprint, request, jsonify, send_file, render_template, redirect, flash, g)
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import math
import pandas as pd
import shutil

app = Flask(__name__)

@app.route('/schedule_task', methods=['GET'])
async def schedule_task():
    while 1:
        await asyncio.sleep(2)
        print("annomely detect!!!")

@app.route('/', methods=['GET'])
async def index():
    return jsonify({'message': "OK"})


# # 下載excel
# @bp.route('/download_file', methods=('GET', 'POST'))
# def download_file():
#     return send_file("..\\..\\path", as_attachment=True)


# GET METHOD EXAMPLE
@app.route('/get_example', methods=['GET'])
async def get_example():
    try:
        # do something
        # http://120.0.0.1:8000/?input_number=5
        input_number = request.args.get('input_number')
    except Exception as e:
        raise AssertionError(f"{e}")
    finally:
        pass
    return jsonify({'message': "OK"})

# 以下是測試
@app.route('/test_api', methods=['GET', 'POST'])
async def test_api():
    print("test_api")
    return jsonify({'message': "OK"})
    


if __name__ == '__main__':
    app.run()


