import logging
import json
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):

  logger.info('Incoming event: {}'.format(event))

  r = requests.get('https://www.google.com')
  response_status_code = r.status_code

  return_statement = "Google Status code: {}".format(response_status_code)

  return {
    'statusCode': 200,
    'body': json.dumps(return_statement)
  }