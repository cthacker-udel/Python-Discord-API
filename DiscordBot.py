from DiscordClient import DiscordClient

class DiscordBot:
    def __init__(self, token):
        self.token = token
        self.access_token = ''
        self.scope = ''
        self.permission = 0