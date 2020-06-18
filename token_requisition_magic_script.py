from secure import secrets

import datetime
import requests


HOST = secrets.HOST
CLIENT_ID = secrets.CLIENT_ID
CLIENT_SECRET = secrets.CLIENT_SECRET
SCOPE = secrets.SCOPE


def request_token(host, scope):

    if host == "degreed":
        client_id = CLIENT_ID
        client_secret = CLIENT_SECRET
        url = 'https://degreed.com/oauth/token'
    elif host == "betatest":
        client_id = CLIENT_ID
        client_secret = CLIENT_SECRET
        url = 'https://betatest.degreed.com/oauth/token'
    else:
        print('You have selected a wrong working environment, please see documentation')
        client_id = "Wrong selection of the working environment"
        client_secret = "wrong selection of the working environment"
        url = "Something is definately wrong with your URL please refer to seleciton of production environment"

    payload = {
        'grant_type': "client_credentials",
        'client_id': '{0}'.format(client_id),
        'client_secret': '{0}'.format(client_secret),
        'scope': '{0}'.format(scope)
    }

    headers = {'content_type': 'application/json'}
    response = requests.request("POST", url=url, headers=headers, data=payload)
    access_details = response.json()
    try:
        access_tok = access_details['access_token']
    except KeyError:
        access_tok = "Your API keys are incorrect. Check them and try again.If error persists check with Ron or Degreed."
    return access_tok

print(">>>>>>Requesting the token now...")
token = request_token(HOST,SCOPE)
if token == "Your API keys are incorrect. Check them and try again.If error persists check with Ron or Degreed.":
    expiry_date = "No token requested"
else:
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=60)

print("""
      HERE IS YOUR TOKEN:
      >>>>>>>>>>>>>>>>>>>>>>>>>
      {}
      -------------------------
      EXPIRES ON: {}
      >>>>>>>>>>>>>>>>>>>>>>>>>>""".format(token,expiry_date))