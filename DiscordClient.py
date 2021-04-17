class DiscordClient:
    def __init__(self,client_id):
        self.client_id = client_id
        self.scopes = []
        self.secret_key = ''
        self.permissions = ''
        self.redirect_uri = ''
        self.access_token = ''
        self.expires_in = 0
        self.commands = {}
        self.guild_id = ''
        self.interaction_id = ''
        self.interaction_token = ''


    def create_global_application(self,name,description,options=None,default_permission=None):
        default_params = {'name': name, 'description': description}
        if options == None and default_permission == None:
            return default_params
        elif default_permission != None and options == None:
            default_params['default_permissions'] = default_permission
            return default_params
        elif default_permission == None and options != None:
            default_params['options'] = options
            return default_params
        else:
            default_params['options'] = options
            default_params['default_permissions'] = default_permission
            return default_params

    def add_secret_key(self,secret_key):
        self.secret_key = secret_key

    def add_scope(self,scope):
        self.scopes.append(scope)

    def convert_scopes(self):
        return ' '.join(self.scopes)

    def add_redirect_uri(self,uri):
        self.redirect_uri = uri


    def add_client_permissions(self,permission):
        self.permissions = permission

    def get_client_id(self):
        return self.client_id