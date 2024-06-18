import customtkinter as ctk
from tkinter import messagebox

class LoginForm(ctk.CTkFrame):
	def __init__(self, master, on_login):
		super().__init__(master)
		self.on_login = on_login
		self.render()

	def render(self):
		self.title = ctk.CTkLabel(
    	self,  
     	text="Login".upper(), 
      width=350, 
      anchor="w", 
      font=ctk.CTkFont(
        size=36, 
				weight="bold",
				family="Inter"
    	), 
      text_color="#92542F"
    )
		self.title.pack(pady=46)
		
		self.username_label = ctk.CTkLabel(
    	self,  
			text="Login",
			width=350, 
			anchor="w", 
			text_color="#92542F"
		)
		self.username_label.pack(pady=10)
		
		self.username_entry = ctk.CTkEntry(
    	self,
			placeholder_text="Insira seu E-mail",
			placeholder_text_color="#E5C7B5",
     	width=350, 
      height=48, 
      text_color="#CA6E33", 
      font=ctk.CTkFont(
        size=20, 
        weight="normal"
      )
    )
		self.username_entry.pack()
		
		self.password_label = ctk.CTkLabel(
    	self, 
     	text="Password", 
      width=350, 
      anchor="w", 
      text_color="#92542F"
    )
		self.password_label.pack(pady=10)
		
		self.password_entry = ctk.CTkEntry(
    	self, 
			placeholder_text="Insira sua senha",
      placeholder_text_color="#E5C7B5",
     	show="*", 
    	width=350, 
     	height=48, 
      text_color="#CA6E33", 
      font=ctk.CTkFont(
        size=20, 
        weight="normal"
      )
    )
		self.password_entry.pack()
	
		self.error_warning_label_var = ctk.StringVar()
		self.error_warning_label = ctk.CTkLabel(self, 
			textvariable=self.error_warning_label_var,
			text_color="#EB4343",
			font=ctk.CTkFont(
     		size=18, 
       	weight="normal", 
				slant='roman',
    	)
	 	)
		self.error_warning_label.pack(pady=8)
		
		self.login_button = ctk.CTkButton(self, 
			text="Entrar".upper(), 
   		command=self.login, 
    	font=ctk.CTkFont(
      	size=24, 
      	weight="bold"
      ), 
     	width=350, 
      height=60, 
      corner_radius=6
    )
		self.login_button.pack(pady=24)
	
	def login(self):
		username = self.username_entry.get()
		password = self.password_entry.get()
		isAuthenticated = self.on_login(username, password)
		if not isAuthenticated:
			self.error_warning_label_var.set("E-mail ou senha inválida")
