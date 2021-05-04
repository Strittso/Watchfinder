class Watch:

    def __init__(self, watchdata):
        self.watchdata = watchdata
        self.brand = watchdata["Brand"]
        self.size = watchdata["Size"]

    def get_data(self):
        return self.watchdata