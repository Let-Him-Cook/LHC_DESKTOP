import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import requests
import numpy as np
from src.utils.options import MONTHS, YEARS
from src.utils.api import API_BASE_URL

class BiggestSalesPie(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master)
    self.render()
    
  def fetchData(self, year, month):
    url = f"{API_BASE_URL}/statistics/biggestsales?year={year}&month={month}"
        
    try:
        response = requests.get(url)
     
        if int(response.status_code) == 200:
            data = response.json()
            return data
        else:
            messagebox.showerror("Maiores vendas", "Um erro ocorreu para recuperar as informações")
            return []
    except requests.RequestException as e:
        messagebox.showerror("Maiores vendas", "Impossível obter as informaçõe no momento, tente mais tarde.")
        print(f"Request failed: {e}")
        return []
    
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

    data = self.fetchData(year=2024, month=6)

    # Obter uma lista de valores de quantity
    quantities = [item["quantity"] for item in data]

    # Obter uma lista de valores de name
    names = [item["name"] for item in data]

    def func(pct, allvals):
      absolute = int(np.round(pct/100.*np.sum(allvals)))
      return f"{pct:.1f}%\n({absolute:d})"
      
    wedges, texts, autotexts = ax.pie(
      quantities, 
      autopct=lambda pct: func(pct, quantities),
      labels=names,
    )

    plt.setp(autotexts, size=10, weight="normal", color="white")
    
    canvas = FigureCanvasTkAgg(fig, master=self.chartframe)
    canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8, anchor="n")
    canvas.draw()
