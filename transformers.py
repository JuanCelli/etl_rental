class Transformer():
    def __init__(self, data):
        self.data = data

    def get_data(self):
        data = self.data
        data["full_price"] = data["price"] + data["bills"]
        return data