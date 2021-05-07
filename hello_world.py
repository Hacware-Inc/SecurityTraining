import requests
import pprint

domain = 'hacwareinc.hacware.com'

path = '/api/v1/auth/'
base_url = 'https://%s' % (domain);
route = base_url + path


data = { 'uid':'a537bedb0ddacdee597bc7c762', 'sec':'D7KY1SJ4R6XVGFI6R9WGDTA0FHE263M92NSSYXWNCU1WCYP3XCWQCDFNQVNFGO' }

r = requests.post(route, data = data)
connection_info = r.json()

token = connection_info['access_token']

path = '/api/v1/train/courselist/'
base_url = 'https://%s' % (domain);
route = base_url + path

headers = { 'Authorization': 'Bearer %s' % token}

r = requests.get(route, headers = headers)
pprint.pprint(r.json())
