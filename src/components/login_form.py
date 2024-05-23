import customtkinter as ctk

class LoginForm(ctk.CTkFrame):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.on_login = on_login
        self.create_widgets()

    def create_widgets(self):
        self.username_label = ctk.CTkLabel(self,  text="Login", width=350, anchor="w")
        self.username_label.pack(pady=10)
        
        self.username_entry = ctk.CTkEntry(self, width=350, height=48, text_color="#CA6E33", font=ctk.CTkFont(size=20, weight="normal"))
        self.username_entry.pack()
        
        self.password_label = ctk.CTkLabel(self, text="Password", width=350, anchor="w")
        self.password_label.pack(pady=10)
        
        self.password_entry = ctk.CTkEntry(self, show="*", width=350, height=48, text_color="#CA6E33", font=ctk.CTkFont(size=20, weight="normal"))
        self.password_entry.pack()
        
        self.login_button = ctk.CTkButton(self, text="Entrar".upper(), command=self.login, font=ctk.CTkFont(size=24, weight="bold"), width=350, height=60, corner_radius=6)
        self.login_button.pack(pady=46)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.on_login(username, password)
