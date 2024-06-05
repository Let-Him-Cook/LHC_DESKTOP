import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class BiggestSalesPie(ctk.CTkFrame):
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
    
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"))

    recipe = ["375 Hamburguer",
              "75 Feijoada",
              "250 Pizza",
              "300 Guaraná_300ml"]

    data = [float(x.split()[0]) for x in recipe]
    dishes = [x.split()[-1] for x in recipe]

    def func(pct, allvals):
      absolute = int(np.round(pct/100.*np.sum(allvals)))
      return f"{pct:.1f}%\n({absolute:d})"
      
    wedges, texts, autotexts = ax.pie(
      data, 
      autopct=lambda pct: func(pct, data),
      labels=dishes,
    )

    plt.setp(autotexts, size=10, weight="normal", color="white")
    
    canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
    canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8)
    canvas.draw()
