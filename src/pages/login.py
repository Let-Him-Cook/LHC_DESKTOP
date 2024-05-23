import customtkinter as ctk
from PIL import Image
from src.components.login_form import LoginForm
from src.handlers.auth import authenticate

class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Configure the grid to have two columns with equal weight
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        # Create a frame for the form and image
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=0, column=0, sticky="nsew")
        
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0, column=1, sticky="nsew")
        
        # Add the login form
        self.login_form = LoginForm(self.form_frame, self.handle_login)
        self.login_form.pack(expand=True)

        # Load the image with a delay to ensure the frame size is accurate
        self.after(100, self.load_image)
        
    def load_image(self):
        logo_image = Image.open("assets/images/login_right_banner.png")
        
        # Get the frame dimensions
        frame_width = self.image_frame.winfo_width()
        frame_height = self.image_frame.winfo_height()

        # Resize the image to fit the image_frame
        resized_image = logo_image.resize((frame_width, frame_height))
        
        # Convert the resized image to CTkImage with the correct size
        logo_photo = ctk.CTkImage(resized_image, size=(frame_width, frame_height))
        
        self.logo_label = ctk.CTkLabel(self.image_frame, image=logo_photo, text="", anchor="center", bg_color="#cb6d30")
        self.logo_label.pack(fill="both", expand=True, anchor="center")

    def handle_login(self, username, password):
        if authenticate(username, password):
            self.master.show_page(DashboardPage)
        else:
            print("Login failed")

# Import DashboardPage at the end to avoid circular import
from src.pages.dashboard import DashboardPage