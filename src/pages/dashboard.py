import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.components.header import Header

class DashboardPage(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master)
    self.render()

  def render(self):
    self.mainframe = ctk.CTkFrame(self, fg_color="#F0F2F5")
    self.mainframe.pack(padx=32, fill="x", expand=True, anchor="n")
    
    # Dashboard Header
    self.header = Header(self.mainframe, self.logout)
    self.header.pack(fill="x", expand=True)
     
    # Title Page Frame
    self.title_page_frame = ctk.CTkFrame(self.mainframe)
    self.title_page_frame.pack(fill="both", expand=True, anchor="center", pady=32)
    
    # Title
    ctk.CTkLabel(
      self.title_page_frame, 
      text="Relatórios", 
      text_color="#92542F",
      font=ctk.CTkFont(size=36, weight="bold")
    ).pack(anchor="w")
    
    # Divider
    ctk.CTkFrame(self.title_page_frame, width=100, height=2, fg_color="#CA6E33").pack(anchor="w", pady=4)
    
    # Rest of the contet here (Charts etc...)
    
  def logout(self):
    # Logic for logging out
    from src.pages.login import LoginPage
    self.master.show_page(LoginPage)

