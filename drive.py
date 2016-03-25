import httplib2

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from apiclient.discovery import build
from oauth2client.tools import run_flow, argparser
from apiclient.http import MediaFileUpload

CLIENT_SECRETS_FILE = 'client_secrets.json' 
SCOPE = 'https://www.googleapis.com/auth/drive'
SERVICE_NAME = 'drive'
API_VERSION = 'v3'

def authentication():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPE)
    storage = Storage(SERVICE_NAME+'-oauth2.json')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)

    http = credentials.authorize(httplib2.Http())

    return build(SERVICE_NAME, API_VERSION, http=http)


def upload(args):
	drive_service = authentication()
	print('Uploading...')
	file_metadata = {'name' : str(FILE_NAME), 'description' : str(FILE_D)}
	media = MediaFileUpload(FILE_PATH)
	file = drive_service.files().create(body=file_metadata,
	media_body=media, fields='id').execute()

	print('\nFile Sucessfully Uploaded to Drive. File ID: %s' % file.get('id'))

if __name__ == '__main__':
	argparser.add_argument('--f', required=True)
	argparser.add_argument('--t')
	argparser.add_argument('--d')
	args = argparser.parse_args()

	FILE_PATH = args.f
	FILE_NAME = args.t
	FILE_D = args.d
	upload(args)

