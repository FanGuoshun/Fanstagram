# -*- encoding=UTF-8 -*-

from fanstagram import app
from qiniu import  Auth, put_stream, put_data
import os

access_key = app.config['QINIU_ACCESS_KEY']
secret_key = app.config['QINIU_SECRET_KEY']

q = Auth(access_key, secret_key)

bucket_name = app.config['QINIU_BUCKET_NAME']
domain_prefix = app.config['QINIU_DOMAIN']


def qiniu_upload_file(source_file, save_file_name):
    token = q.upload_token(bucket_name, save_file_name)

    ret, info = put_data(token, save_file_name, source_file.stream)

    if info.status_code == 200:
        return domain_prefix + save_file_name
    return None

