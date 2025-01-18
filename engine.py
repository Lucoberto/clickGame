from dependencies import *
from save_engine import *

class engine_class:

    def __init__(self):
        """ Valores """
        self.point = 0
        self.record = 0
        self.platica = 0

        """ Informacion de guardado """
        self.save_engine = save_engine_class()
        self.file_path = self.save_engine.file_path
        self.data = self.save_engine.read_data
        self.load_data = self.save_engine.func_read_data()


        """ Lógica del juego """
    def points_up(self):
        self.point += 1
        if self.point > self.record:
            self.record = self.point
        #self.show_points()
        self.auto_save()
        self.coins_generator()
    
    def coins_generator(self):
        posibiliti_coin = self.point % 10
        if posibiliti_coin == 0:
            self.platica += 1
            
        self.auto_save()
        self.show_platica()



    """ Borrar guardados """
    def clean(self):
        self.point = 0
        self.show_points()
    
    def clean_save(self):
        with open(self.file_path, 'r') as read_save:
            read_save_delete = json.load(read_save)
        
        read_save_delete["point"] = 0
        read_save_delete["record"] = 0
        read_save_delete["platica"] = 0
    
        with open(self.file_path, 'w') as delete_all:
            json.dump(read_save_delete, delete_all, indent=4)
        
        self.load_record()
        self.load_points()
        self.load_platica()
        self.show_record()
        self.show_points()
        self.show_platica()



    """ Guardados """
    def auto_save(self):
        # Lee el json para poder guardar mas tarde los datos
        self.load_data
        # Actualizar record
        self.data["record"] = self.record
        self.data["platica"] = self.platica
        
        self.save_engine.func_save_data()
        
        #self.show_record()

    def save_game(self):
        """Guarda los datos en un archivo JSON."""
        try:
            with open(self.file_path, 'r') as file:
                save_data = json.load(file)
        except FileNotFoundError:
            save_data = {"point": 0, "record": 0, "platica": 0}

        # Actualizar datos
        save_data["point"] = self.point

        # Guardar en el archivo
        with open(self.file_path, 'w') as file:
            json.dump(save_data, file, indent=4)


    """ Carga datos """
    def load_points(self):
        """Carga los puntos desde el archivo."""
        try:
            with open(self.file_path, 'r') as file:
                save_data = json.load(file)
                self.point = save_data.get("point", 0)
        except FileNotFoundError:
            self.point = 0
        self.show_points()

    def load_record(self):
        """Carga el récord desde el archivo."""
        try:
            with open(self.file_path, 'r') as file:
                save_data = json.load(file)
                self.record = save_data.get("record", 0)
        except FileNotFoundError:
            self.record = 0

    def load_platica(self):
        """Carga el dinero desde el archivo."""
        try:
            with open(self.file_path, 'r') as file:
                save_data = json.load(file)
                self.platica = save_data.get("platica", 0)
        except FileNotFoundError:
            self.platica = 0

    """ Actualizar datos """
    def update_money(self, discount):
        if self.platica < 20:
            self.label_info_no_money.place(x=20 , y=70)
        else:
            self.platica = self.platica - discount
            self.auto_save()
            self.show_platica()

intancia = engine_class()
intancia.auto_save()