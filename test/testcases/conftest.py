import os
import smtplib
import sys
import pytest
import requests

from test.config.config import Config

from src.util.foo import Foo

sys.path.append(os.getcwd())

def pytest_configure(config):
    config.addinivalue_line("markers", "a: group a")
    config.addinivalue_line("markers", "b: group b")
    config.addinivalue_line("markers", "c: group c")
    config.addinivalue_line("markers", "must: group must")

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return ["Comparing Foo instances:"," vals: {} != {}".format(left.val, right.val)]

@pytest.fixture(scope="module")
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print("finalizing {} ({})".format(smtp_connection, server))
    smtp_connection.close()

@pytest.fixture(scope="session")
def valid_user():
    login_info = {'username':'fm','password':'123456','client_id':'webapp-client','grant_type':'password'}
    yield login_info
    del login_info

@pytest.fixture(scope="session")
def invalid_user():
    login_info = {'username':'fm','password':'12345678','client_id':'webapp-client','grant_type':'password'}
    yield login_info
    del login_info


@pytest.fixture(scope="session")
def login_tokens(valid_user):
    config_ = Config()
    api = config_.config('default', 'token_api')
    r = requests.post(url=api, data=valid_user, verify=False)
    # r = requests.post(url = api, data=valid_user,cert=r'C:\Users\yinxli00\AppData\Local\Programs\Python\Python37\lib\site-packages\certifi\cacert.pem')
    json_r = r.json()
    return {'access_token':json_r['access_token'],'refresh_token':json_r['refresh_token']}


