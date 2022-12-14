import os
import json

FULL_PATH = os.path.dirname(os.path.realpath(__file__))

cred_path = str(FULL_PATH)+'\\test_data\\creds.json'
creds_file = open(cred_path, 'rb')
creds = json.load(creds_file)



USERNAME = creds['correct_username']
PASSWORD = creds['correct_password']
INCORRECT_PASSWORD = creds['incorrect_password']