import requests
from DiscordClient import DiscordClient
from DiscordBot import DiscordBot
from pprint import pprint

base_url_api = 'https://discord.com/api/v8'
base_url_auth = 'https://discord.com/api'

### AUTH - SECTION

def get_bot_headers(bot):
    return {'Authorization': 'Bot {}'.format(bot.token),'Content-Type': 'application/json'}

def get_client_authorization(client):
    url = base_url_auth + '/oauth2/authorize'
    params = {'client_id': client.get_client_id(), 'permissions': client.permissions, 'redirect_uri': client.redirect_uri, 'scope': client.convert_scopes()}
    json_response = requests.get(url,params=params)
    return json_response.status_code == 200

def get_bot_authorization(bot,client):
    url = base_url_auth + '/oauth2/authorize'
    params={'client_id': client.client_id, 'scope': bot.scope, 'permissions': bot.permission}
    response = requests.get(url,params=params)
    return response.status_code == 200


def get_client_token(client):
    url = base_url_auth + '/oauth2/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials', 'scope': client.convert_scopes()}

    request = requests.post(url,data=data,headers=headers,auth=(client.client_id,client.secret_key)).json()
    client.access_token = request['access_token']
    client.expires_in = request['expires_in']


### Get Commands Methods


def get_global_application_commands(client,bot):
    url = base_url_api + '/applications/{}/commands'.format(client.client_id)

    ## get request

    headers = {'Authorization': 'Bot {}'.format(bot.token),'Content-Type': 'application/json'}

    json_response = requests.post(url,headers=headers)
    pprint(json_response)

def create_global_application_command(client,bot,commandname,commanddescription):
    url = base_url_api + '/applications/{}/commands'.format(client.client_id)

    headers = get_bot_headers(bot)
    json_params = {'name': commandname,'description': commanddescription}

    response = requests.post(url,headers=headers,json=json_params).json()

    client.global_commands[response['name']] = response['id']

    return len(response) > 0

def get_global_application_command(client,bot,command_name):
    url = base_url_api + '/applications/{}/commands/{}'.format(client.client_id,client.global_commands[command_name])

    headers = get_bot_headers(bot)

    response = requests.get(url,headers=headers).json()

    return len(response) > 0

def edit_global_application_command(client,bot,original_command_name,new_command_name,new_command_description):
    
    params = {'name': new_command_name, 'description': new_command_description}

    headers = get_bot_headers(bot)
    
    url = base_url_api + '/applications/{}/commands/{}'.format(client.client_id,client.global_commands[original_command_name])
    
    response = requests.patch(url,data=params,headers=headers).json()
    
    return len(response) > 0

def delete_global_application_command(client,bot,command_name):
    
    headers = get_bot_headers(bot)
    
    url = base_url_api + "/applications/{}/commands/{}".format(client.client_id,client.global_commands[command_name])
    
    response = requests.delete(url,headers=headers)
    
    return response.status_code == 200

    





### Main function



if __name__ == '__main__':

    bot = DiscordBot('botkey')
    bot.permissions = 8
    bot.scope = 'bot'

    client = DiscordClient('clientid')
    client.add_scope('applications.commands')
    client.add_scope('applications.commands.update')
    client.add_redirect_uri('http://localhost:8888/callback/')
    client.add_client_permissions(8)
    client.add_secret_key('secretkey')
    
    get_bot_authorization(bot,client)
    #get_client_token(client)
    create_global_application_command(client,bot,'firstcommand','this is the first command')
    #get_global_application_commands(client,bot)
    get_global_application_command(client,bot,'firstcommand')
    #edit_global_application_command(client,bot,'firstcommand','secondcommand','this is the secondcommand')
    #get_global_application_command('secondcommand')
    delete_global_application_command(client,bot,'firstcommand')