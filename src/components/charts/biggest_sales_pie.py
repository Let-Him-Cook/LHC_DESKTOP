import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from src.utils.options import MONTHS, YEARS

class BiggestSalesPie(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master)
    self.render()
    
  def fetchData(year, month):
    print(year, month)
    
  def render(self):
    self.mainframe = ctk.CTkFrame(self)
    self.mainframe.pack(
      padx=4,
      pady=4,
      fill="both", 
      expand=True,
    )

    # --------------- actions header ------------------
    
    self.actionsframe = ctk.CTkFrame(self.mainframe)
    self.actionsframe.pack(fill="both", expand=True, anchor="n")
    
    # Title
    
    self.title = ctk.CTkLabel(
      self.actionsframe, 
      text="Maiores Vendas",
      font=ctk.CTkFont(weight='bold', size=24),
      text_color="#141D24"
    )
    self.title.pack(side="left", anchor="w")
    
    # YEAR 
    
    def year_options_callback(choice):
      print("Ano selecionado:", choice)
    
    self.year = ctk.CTkOptionMenu(
      self.actionsframe, 
      values=YEARS,
      command=year_options_callback,
      
      dynamic_resizing=True, 
      corner_radius=6,
      text_color="#92542F",
      fg_color="#FFE7B8",
      height=42,
      width=140,
      button_color="#CA6E33",
      button_hover_color="#CA6E33",
      dropdown_text_color="#92542F",
      dropdown_fg_color="#FFF",
      dropdown_hover_color="#FFE7B8",
      dropdown_font=ctk.CTkFont(
        size=18,
        weight="normal"
      ),
      font=ctk.CTkFont(
        size=20,
        weight="bold"
      )
    )
    
    self.year.pack(side="left", anchor="w", padx=16)
    
    # MONTH
    
    def month_options_callback(choice):
      print("Mês selecionado", choice)
    
    self.month = ctk.CTkOptionMenu(
      self.actionsframe, 
      values=MONTHS,
      command=month_options_callback,
      
      dynamic_resizing=True, 
      corner_radius=6,
      text_color="#92542F",
      fg_color="#FFE7B8",
      height=42,
      width=140,
      button_color="#CA6E33",
      button_hover_color="#CA6E33",
      dropdown_text_color="#92542F",
      dropdown_fg_color="#FFF",
      dropdown_hover_color="#FFE7B8",
      dropdown_font=ctk.CTkFont(
        size=18,
        weight="normal"
      ),
      font=ctk.CTkFont(
        size=20,
        weight="bold"
      )
    )
    
    self.month.pack(side="left", anchor="w")
    
    # ---------------- chart -----------------
    
    self.chartframe = ctk.CTkFrame(
      self.mainframe,
      fg_color="#FFFFFF",
      corner_radius=24,
    )
    
    self.chartframe.pack(fill="both",expand=True, anchor="n")
    
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
    
    canvas = FigureCanvasTkAgg(fig, master=self.chartframe)
    canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8, anchor="n")
    canvas.draw()
