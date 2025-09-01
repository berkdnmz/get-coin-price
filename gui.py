from tkinter import *

class MyGui():
    def __init__(self,api_manager):
        self.api_manager = api_manager
        self.root = Tk()
        self.root.title("Get Coin Price")
        self.root.minsize(500,400)
        self.root.config(bg="#004030")
        self.root.bind("<Escape>",self.close_root)

        #center
        self.height = 400
        self.width = 500
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        y = (screen_height - self.height) // 2
        x = (screen_width - self.width) // 2
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

        #title
        self.label_title = Label(self.root, text="Get Coin Price", font=("Impact", 20, "roman"), padx=30, pady=10, bg="#FFF9E5", fg="#004030")
        self.label_title.place(rely=0.12, relx=0.5, anchor="center")

        # label ask coin name
        self.label_ask_name = Label(self.root, text="Enter coin name", font=("Helvetica", 15, "roman bold"), pady=10, padx=10, bg="#4A9782", fg="#FFF9E5")
        self.label_ask_name.place(rely=0.40, relx=0.5, anchor="center")

        # label entry coin name
        self.entry_coin_name = Entry(self.root, font=("Helvetica", 10, "roman bold"), width=25, bg="#FFF9E5")
        self.entry_coin_name.place(rely=0.50, relx=0.5, anchor="center")
        self.entry_coin_name.bind("<Return>",self.enter_pressed)
        self.entry_coin_name.focus()

        # label coin price
        self.label_coin_price = Label(self.root, text="", font=("Helvetica", 20, "roman bold"), pady=10, padx=20, bg="#FFF9E5", fg="#004030")
        self.label_coin_price.place(rely=0.75, relx=0.5, anchor="center")
        self.label_coin_price.place_forget()

        # Creator label
        self.label_creator = Label(self.root, text="Created by Berk", font=("Times", 10, "bold italic"), pady=5, padx=5, bg="#FFF9E5", fg="#004030")
        self.label_creator.place(relx=1.0, rely=1.0, anchor="se")

    def enter_pressed(self, event = None):
        self.api_manager.get_price(coin=self.entry_coin_name.get().replace("ı","i").replace("İ","i"))
        self.entry_coin_name.delete(0,END)

    def close_root(self, event=None):
        self.root.destroy()
    def run_root(self):
        self.root.mainloop()