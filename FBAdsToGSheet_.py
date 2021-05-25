from __future__ import print_function

# used to interact with Marketing API (Facebook Ads)
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

# used to interact with Sheets API
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# my Facebook credentials
my_app_id = 'XXXXXXXXXXXXXXX'
my_app_secret = 'XXXXXXXXXXXXXXXXXXX'
my_access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_XXXXXXXXXXXXX')

# This Sheets API scope is for read/write to spreadsheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
SAMPLE_RANGE_NAME = 'Sheet2!A1:B2'


### GET ADSET STATS
#https://developers.facebook.com/docs/instagram/ads-api/guides/get-ad-insights/
#https://github.com/facebook/facebook-python-business-sdk/blob/master/facebook_business/adobjects/adset.py
from facebook_business.adobjects.adset import AdSet
# The id of the Ad Set
id = 'XXXXXXXXXXXXXXXXXXXXXXXX'

# The metrics we want to fetch
fields = [
  'impressions',
  'clicks',
  'spend'
]
# The date range we want
params = {
  'time_range': {'since':'2021-04-22','until':'2021-04-26'}
}
# The fetching :-)
adset = AdSet(id).get_insights(
  fields=fields,
  params=params,
)
# The result of the fetch.
adsetSpend = adset[0]["spend"]
print(adsetSpend)

# The authentication for Sheets API. Remember to have the credentials.json in place
creds = None
if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
  else:
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
  with open('token.json', 'w') as token:
      token.write(creds.to_json())
service = build('sheets', 'v4', credentials=creds)

# What we want to write to our spreadsheet
body = {
  "range": SAMPLE_RANGE_NAME,
  "majorDimension": "ROWS",
  "values": [
    ["adsetSpend", "revenue"],
    [adsetSpend, "20.50"]
  ],
}
result = service.spreadsheets().values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
    valueInputOption='USER_ENTERED', body=body).execute()
print('{0} cells updated.'.format(result.get('updatedCells')))