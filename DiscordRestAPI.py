import requests
from DiscordClient import DiscordClient
from pprint import pprint

base_url_api = 'https://discord.com/api/v8'
base_url_auth = 'https://discord.com/api'

def get_client_authorization(client):
    url = base_url_auth + '/oauth2/authorize'
    params = {'client_id': client.get_client_id(), 'permissions': client.permissions, 'redirect_uri': client.redirect_uri, 'scope': client.convert_scopes()}
    json_response = requests.get(url,params=params)
    return json_response.status_code == 200

def get_bot_authorization(client):
    pass

def get_client_token(client):
    url = base_url_auth + '/oauth2/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials', 'scope': client.convert_scopes()}

    request = requests.post(url,data=data,headers=headers,auth=(client.client_id,client.secret_key)).json()
    client.access_token = request['access_token']
    client.expires_in = request['expires_in']





def get_global_application_commands(client):
    url = base_url_api + '/applications/{}/commands'.format(client.client_id)

    ## get request

    json_response = requests.get(url,auth=(client.client_id,client.access_token))
    pprint(json_response)

def create_global_application_command(client):
    url = base_url_api + '/applications/{}/commands'.format(client.getapikey())

    params = client.create_global_application('name','description')








if __name__ == '__main__':
    client = DiscordClient('clientid')
    client.add_scope('applications.commands')
    client.add_scope('applications.commands.update')
    client.add_redirect_uri('http://localhost:8888/callback/')
    client.add_client_permissions(8)
    client.add_secret_key('secretkey')
    get_client_token(client)
    get_global_application_commands(client)