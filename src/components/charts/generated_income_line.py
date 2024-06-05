import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GeneratedIncomeLine(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master)
    self.render()
    
  def fetchData(year, month):
    print(year, month)
    
  def render(self):
    self.mainframe = ctk.CTkFrame(
      self,
      fg_color="#FFFFFF",
      corner_radius=24,
    )
    
    self.mainframe.pack(
      padx=4,
      pady=4,
      fill="both", 
      expand=True,
    )
    
    fig, ax = plt.subplots()

    counts = [13000, 27000, 50300, 22600, 13400, 18548, 12374, 57443, 33222, 44192, 27321, 17000]
    months = ['Jan', 'Fev', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Set', 'Out', 'Nov', 'Dez']
    bar_colors = ['tab:green']

    ax.bar(months, counts, color=bar_colors)

    ax.set_ylabel('Renda (R$)')
    
    canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
    canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8)
    canvas.draw()
