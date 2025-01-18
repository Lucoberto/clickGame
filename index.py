from dependencies import *
from engine import *


class ClickGameApp:
    def __init__(self, root):
        self.root = root
        self.point = 0
        self.record = 0
        self.platica = 0
        self.file_path = "save.json"

        self.root.title("Click Game")
        self.root.config(height=300, width=200)

        # Crear elementos de la interfaz
        self.label_info = ttk.Label(text="Your points 0")
        self.label_info.place(x=20, y=10)

        self.label_info_record = ttk.Label(text="Your record is 0")
        self.label_info_record.place(x=20, y=30)

        self.label_info_platica = ttk.Label(text="Your platica is 0")
        self.label_info_platica.place(x=20, y=100)

        self.confirm = ttk.Button(text="Click", command=self.points_up)
        self.confirm.place(x=60, y=70)

        """ Menu de la tienda """
        self.label_shop_multiplier = ttk.Label(text="x2 in coins")
        self.label_shop_multiplier.place_forget()

        self.label_shop_back = ttk.Button(text="back", command=self.show_interface)
        self.label_shop_back.place_forget()

        self.buy = ttk.Button(text="Buy 20", command=lambda: self.update_money(20) )
        self.buy.place_forget()

        self.label_info_no_money = ttk.Label(text="You don't have money!")

        # Crear menú superior
        self.load_menu = Menu(self.root)

        self.top_menu = Menu(self.load_menu, tearoff=0)
        self.load_menu.add_cascade(label="Settings", menu=self.top_menu)

        self.top_menu.add_command(label="Save", command=self.save_game)
        self.top_menu.add_command(label="Load", command=self.load_points)

        self.clear_sub_menu = Menu(self.top_menu, tearoff=0)
        self.top_menu.add_cascade(label="Clean", menu=self.clear_sub_menu)

        self.clear_sub_menu.add_command(label="Clean points", command=self.clean)
        self.clear_sub_menu.add_command(label="Clean all history", command=self.clean_save)

        self.load_menu.add_command(label="Shop", command=self.hide_interface)
        self.root.config(menu=self.load_menu)

        self.load_menu.add_command(label="Exit", command=self.root.quit)
        self.root.config(menu=self.load_menu)
        

        # Cargar datos iniciales
        self.load_record()
        self.load_platica()
        self.show_platica()
        self.show_record()

    # Lógica del juego
    def points_up(self):
        self.point += 1
        if self.point > self.record:
            self.record = self.point
        self.show_points()
        self.auto_save()
        self.coins_generator()
    
    def coins_generator(self):
        posibiliti_coin = self.point % 10
        if posibiliti_coin == 0:
            self.platica += 1
            
        self.auto_save()
        self.show_platica()

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

    """ Motor de guardado """
    def auto_save(self):
        # Lee el json para poder guardar mas tarde los datos
        with open(self.file_path, 'r') as read_json_file:
            read_json = json.load(read_json_file)
        
        # Actualizar record
        read_json["record"] = self.record
        read_json["platica"] = self.platica
        
        with open(self.file_path, 'w') as save_record:
            json.dump(read_json, save_record, indent=4)
        
        self.show_record()

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

    def show_points(self):
        """Actualiza el texto del Label de puntos."""
        self.label_info.config(text=f"Your points {self.point}")

    def show_record(self):
        """Actualiza el texto del Label de récord."""
        self.label_info_record.config(text=f"Your record is {self.record}")
    
    def show_platica(self):
        """Actualiza el texto del Label de dinero."""
        self.label_info_platica.config(text=f"Your platica is {self.platica}")

    # Oculta la interfaz principal
    def hide_interface(self):
        self.label_info.place_forget()
        self.label_info_record.place_forget()
        self.confirm.place_forget()
        # llamada a la funcion
        self.shop()
    
    def show_interface(self):
        self.label_info.place(x=20, y=10)
        self.label_info_record.place(x=20, y=30)
        self.confirm.place(x=60, y=70)

        self.buy.place_forget()
        self.label_shop_back.place_forget()
        self.label_shop_multiplier.place_forget()
        self.label_info_no_money.place_forget()

    def shop(self):
        self.label_shop_multiplier.place(x=20, y=10)
        self.buy.place(x=90, y=10)
        self.label_shop_back.place(x=90, y=30)
    
    def update_money(self, discount):
        if self.platica < 20:
            self.label_info_no_money.place(x=20 , y=70)
        else:
            self.platica = self.platica - discount
            self.auto_save()
            self.show_platica()

# Crear ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ClickGameApp(root)
    root.mainloop()
