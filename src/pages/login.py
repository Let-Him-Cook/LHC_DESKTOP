import customtkinter as ctk
from PIL import Image
from src.components.login_form import LoginForm
from src.handlers.auth import authenticate

class LoginPage(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.render()

	def render(self):
		# Configure the grid to have two columns with equal weight
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)

		# Create a frame for the form and image
		self.form_frame = ctk.CTkFrame(self)
		self.form_frame.grid(row=0, column=0, sticky="enws")
		
		self.image_frame = ctk.CTkFrame(self, fg_color="#cb6d30")
		self.image_frame.grid(row=0, column=1, sticky="wnes")
		
		# Add the login form
		self.login_form = LoginForm(self.form_frame, self.handle_login)
		self.login_form.pack(expand=True)
		
		logo_image_instance = Image.open("assets/images/logo.png")
		self.logo_image_picture = ctk.CTkImage(logo_image_instance, size=(500, 500))
		
		self.logo_image_picture = ctk.CTkLabel(
			self.image_frame, 
			image=self.logo_image_picture, 
			text="", 
			anchor="center",
		)
		
		self.logo_image_picture.pack(fill="both", expand=True)
		
		self.copyright_label = ctk.CTkLabel(
			self.image_frame,
			text="© copyright Let Him Cook 2024", 
			font=ctk.CTkFont(size=20,weight="normal"),
			text_color="#FFFFFF",
		)
		
		self.copyright_label.pack(
			fill="x", expand=False, anchor="center",
			pady=32
		)
			
	def handle_login(self, username, password):
		if authenticate(username, password):
			from src.pages.dashboard import DashboardPage
			self.master.show_page(DashboardPage)
		else:
			print("Login failed")
