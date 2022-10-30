import pokepy


class WebClient():
    def __init__(self):
        self.client = pokepy.V2Client()

    def get_client(self):
        return self.client




web = WebClient()