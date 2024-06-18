import customtkinter as ctk
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.utils.options import MONTHS, YEARS

class AnnualSalesComparison(ctk.CTkFrame):
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
      text="Comparação anual de venda",
      font=ctk.CTkFont(weight='bold', size=24),
      text_color="#141D24"
    )
    self.title.pack(side="left", anchor="w")
    
    # Dish 
    
    def dish_options_callback(choice):
      print("Ano selecionado:", choice)
    
    self.dish = ctk.CTkOptionMenu(
      self.actionsframe, 
      values=['Lasanha', 'Hamburguer', 'Strognoff', 'Meio Filé com Ervas', "Picanha"], # Substituir com chamada a API
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
    
    self.chartframe.pack(fill="both",expand=True, anchor="n", pady=32)
    
    fig, ax = plt.subplots()

    # Dados para o gráfico
    dish1 = [13000, 27000, 50300, 22600, 13400, 18548, 12374, 57443, 33222, 44192, 27321, 17000]
    dish2 = [18000, 50000, 48000, 24000, 14000, 30000, 12000, 36000, 34000, 45000, 28000, 23000]
    months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    # Criação do gráfico de linha usando seaborn
    sns.lineplot(x=months, y=dish1, marker='o', ax=ax, label='2023')
    sns.lineplot(x=months, y=dish2, marker='o', ax=ax, label='2024')
    
    ax.set_ylabel('Renda (R$)')
    ax.set_xlabel('Meses')
    ax.legend()
    
    # Adicionar a grade horizontal
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y')

    canvas = FigureCanvasTkAgg(fig, master=self.chartframe)
    canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8, anchor="n")
    canvas.draw()
   
