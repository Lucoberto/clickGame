from dependencies import *

class save_engine_class:
    
    def __init__(self):

        self.file_path = "save.json"
        self.read_data = ""

    def func_read_data(self):
        with open(self.file_path, 'r') as read_save_data:
            self.read_data = json.load(read_save_data)
            print(self.read_data)

    def func_save_data(self):
        with open(self.file_path, 'w') as save_data:
            json.dump(self.read_data, save_data, indent=4)