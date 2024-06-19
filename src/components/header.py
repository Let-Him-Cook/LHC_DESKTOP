from PIL import Image
import customtkinter as ctk
from src.utils.greeting import greeting
from src.context.user import loggedin_user

class Header(ctk.CTkFrame):
  def __init__(self, master, logout):
    super().__init__(master)
    self.logout = logout
    self.render()
    
  def render(self):
    self.mainframe = ctk.CTkFrame(self)
    self.mainframe.pack(pady=32, fill="x", expand=True)
        
    # ------------- Center Container  -----------------
    
    self.centerframe = ctk.CTkFrame(self.mainframe)
    self.centerframe.pack(
      side="left",
      anchor="center", 
      fill="both", 
      expand=True,
    )
    
    self.welcome_message_frame = ctk.CTkFrame(self.centerframe)
    self.welcome_message_frame.pack(anchor="w")
    
    ctk.CTkLabel(
      self.welcome_message_frame, 
      text=greeting()  + ", ",
      font=ctk.CTkFont(weight="bold", size=24)
    ).pack(side="left", anchor="w")

    self.username = ctk.CTkLabel(
      self.welcome_message_frame, 
      text=loggedin_user.get("name"),
      text_color="#CA6E33",
      font=ctk.CTkFont(weight="bold", size=24)
    )
    
    self.username.pack(side="left", anchor="w")
    
    # Gap 8px
    ctk.CTkFrame(self.centerframe, height=8).pack(anchor="w")
    
    ctk.CTkLabel(
      self.centerframe, 
      text="Sistema de Análise e relatórios",
      text_color="#6C7278",
      font=ctk.CTkFont(weight="normal", size=18)
    ).pack(anchor="w")
    
    # ------------- Logout Button  -----------------
    
    logout_image = Image.open("assets/images/logout.png")
    self.logout_button_image = ctk.CTkImage(logout_image, size=(120, 60))
  
    ctk.CTkButton(
      self.mainframe, 
      command=self.logout, 
      text="", 
      image=self.logout_button_image,
      fg_color="transparent",
      hover_color="#F0F2F5"
    ).pack(side="right", fill="both", anchor="e")
