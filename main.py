import customtkinter as ctk
from src.pages.login import LoginPage

class Application(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Let Him Cook - Reports")
    self.geometry("1440x900")
    # self.resizable(False, False)
    
    self.current_frame = None
    self.show_page(LoginPage)

  def show_page(self, page_class):
    if self.current_frame:
      self.current_frame.destroy()
    self.current_frame = page_class(self)
    self.current_frame.pack(fill="both", expand=True, anchor="center")

if __name__ == "__main__":
  ctk.set_appearance_mode("light")
  ctk.set_default_color_theme("./custom_theme.json")
  app = Application()
  app.minsize(1200,768)
  app.mainloop()
