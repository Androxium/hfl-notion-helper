import requests
import datetime
import sys
import os
from dotenv import load_dotenv

URL = 'https://api.notion.com/v1/pages'
load_dotenv()
TOKEN = os.getenv('TOKEN')
DB_ID = os.getenv('DB_ID')
CONTENT = ' '.join(sys.argv[1:])[1:-1]

HEADERS = {
	'Authorization': f'Bearer {TOKEN}'
}
DATA = {
	'parent': {
		'database_id': f'{DB_ID}'
	},
    'properties': {
        'Highlights': {
                'title': [
                    {
                        'text': {
                        	'content': CONTENT
                        }
                    }
            ]  
        },
        'Date': {
            'date': {
                'start': f'{datetime.date.today()}'
            }
        }
    }
}

response = requests.post(URL, json=DATA, headers=HEADERS)

if response.status_code == 200:
	print('Successfully posted!')
elif response.status_code == 400:
	print('Error')