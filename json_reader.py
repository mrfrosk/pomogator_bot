import json


class JsonReader:

    def __init__(self, path):
        self.path = path

    def write(self, data: dict):
        
        with open(self.path, encoding='utf-8') as file:
            old_data = json.load(file)
            file.close()

        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(old_data | data, file, ensure_ascii=False)
            file.close()

    def read_id(self, name) -> int:
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)
            chat_id = data.get(name, None)
            file.close()
        return chat_id
