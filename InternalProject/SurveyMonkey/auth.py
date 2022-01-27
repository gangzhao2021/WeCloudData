import http.client

# Survey Monkey
access_token = ''
conn = http.client.HTTPSConnection("api.surveymonkey.com")
headers = {
            'Accept': "application/json",
            'Authorization': "Bearer %s" % access_token
          }

# AWS S3
aws_access_key_id = ''
aws_secret_access_key = ''