from extraction import Extractor
from transformers import Transformer

class Etl():
    def __init__(self,url_list):
        self.url_list = url_list

    @property
    def _pre_data_list(self):
        pre_data = [Extractor(url).get_data() for url in self.url_list]
        return pre_data

    def get_data(self):
        data = [Transformer(pre_data).get_data() for pre_data in self._pre_data_list]
        return data

