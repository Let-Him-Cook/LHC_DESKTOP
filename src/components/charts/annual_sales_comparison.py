import customtkinter as ctk
import matplotlib.pyplot as plt
import requests
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.utils.options import YEARS
from src.utils.api import API_BASE_URL
from tkinter import messagebox

class AnnualSalesComparison(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master)
    self.selected_dish = None
    self.selected_first_year = YEARS[0]
    self.selected_second_year = YEARS[1]
    self.dishesLabels = []
    self.dishesIds = []
    self.dishesIdsMap = {}
    
    self.render()
    
  def fetchDishesMenuOptions(self):
    url = f"{API_BASE_URL}/dishes"
    
    try:
      response = requests.get(url)
      if int(response.status_code) == 200:
        data = response.json()
        self.dishesIds = [item["id"] for item in data]
        self.dishesLabels = [item["name"] for item in data]
        
        for i in range(len(data)):
          self.dishesIdsMap[self.dishesLabels[i]] = self.dishesIds[i]
          
        self.selected_dish = self.dishesLabels[0]
        
        print(f"\nDishes IDS: {self.dishesIds}")
        print(f"\nDishes Labels: {self.dishesLabels}")
        print(f"\nDishes Map: {self.dishesIdsMap}")
        print(f"\nDishes Selected: {self.selected_dish}")
        
      else:
        print(f"{response}")
        messagebox.showerror("Pratos", "Um erro ocorreu para recuperar as informações")
    except requests.RequestException as e:
      messagebox.showerror("Pratos", "Impossível obter as informações no momento, tente mais tarde.")
      print(f"Request failed: {e}")
    
  def fetchData(self, dishID, firstYear, secondYear):
    url = f"{API_BASE_URL}/statistics/comparison?dish={dishID}&firstYear={firstYear}&secondYear={secondYear}"
    
    try:
      response = requests.get(url)
      if int(response.status_code) == 200:
        data = response.json()
        firstYearData = data["firstYear"]["sales"]
        secondYearData = data["secondYear"]["sales"]
        return [item["sales"] for item in firstYearData], [item["sales"] for item in secondYearData]
      else:
        print(f"{response}")
        messagebox.showerror("Comparação Anual", "Um erro ocorreu para recuperar as informações")
        return [], []
    except requests.RequestException as e:
      messagebox.showerror("Comparação Anual", "Impossível obter as informações no momento, tente mais tarde.")
      print(f"Request failed: {e}")
      return [], []
  
  def render(self):
    self.fetchDishesMenuOptions()
    
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
      text="Comparação anual de venda",
      font=ctk.CTkFont(weight='bold', size=24),
      text_color="#141D24"
    )
    self.title.pack(side="left", anchor="w")
    
    # Dish 
    def dish_options_callback(choice):
      self.selected_dish = choice
      self.update_chart()
    
    self.dish = ctk.CTkOptionMenu(
      self.actionsframe, 
      values=self.dishesLabels, # Substituir com uma chamada a API
      command=dish_options_callback,
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
    
    self.dish.pack(side="left", anchor="w", padx=16)
    
    # First Year 
    def first_year_options_callback(choice):
      self.selected_first_year = choice
      self.update_chart()
    
    self.firstYear = ctk.CTkOptionMenu(
      self.actionsframe, 
      values=YEARS,
      command=first_year_options_callback,
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
    
    self.firstYear.pack(side="left", anchor="w", padx=16)
      
    # Second Year
    def second_year_options_callback(choice):
      self.selected_second_year = choice
      self.update_chart()
    
    self.secondYear = ctk.CTkOptionMenu(
      self.actionsframe, 
      values=YEARS,
      command=second_year_options_callback,
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
    
    self.secondYear.pack(side="left", anchor="w")
    
    # ---------------- chart -----------------
    
    self.chartframe = ctk.CTkFrame(
      self.mainframe,
      fg_color="#FFFFFF",
      corner_radius=24,
    )
    
    self.chartframe.pack(fill="both",expand=True, anchor="n", pady=32)
    
    self.fig, self.ax = plt.subplots()
    
    self.canvas = FigureCanvasTkAgg(self.fig, master=self.chartframe)
    self.canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8, anchor="n")
    
    # Inicializar com os primeiros valores da lista
    self.update_chart()

  def update_chart(self):
    # Obtenha os dados com base nas seleções atuais
    dish1, dish2 = self.fetchData(self.dishesIdsMap[self.selected_dish], self.selected_first_year, self.selected_second_year)
    months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    # Limpe o gráfico atual
    self.ax.clear()

    # Crie o gráfico de linha usando seaborn
    sns.lineplot(x=months, y=dish1, marker='o', ax=self.ax, label=str(self.selected_first_year))
    sns.lineplot(x=months, y=dish2, marker='o', ax=self.ax, label=str(self.selected_second_year))

    self.ax.set_ylabel('Renda (R$)')
    self.ax.set_xlabel('Meses')
    self.ax.legend()

    # Adicionar a grade horizontal
    self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y')

    # Atualize o canvas
    self.canvas.draw()