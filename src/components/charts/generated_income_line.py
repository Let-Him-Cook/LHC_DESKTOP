import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.utils.options import YEARS
  
class GeneratedIncomeLine(ctk.CTkFrame):
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
      text="Renda Gerada",
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
    
    self.year.pack(side="left", anchor="w", padx=16, pady=36)
    
    # ---------------- chart -----------------
    
    self.chartframe = ctk.CTkFrame(
      self.mainframe,
      fg_color="#FFFFFF",
      corner_radius=24,
    )
    
    self.chartframe.pack(fill="both",expand=True, anchor="n")
    
    fig, ax = plt.subplots()
    
    # Adicionar a grade horizontal
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y')

    counts = [13000, 27000, 50300, 22600, 13400, 18548, 12374, 57443, 33222, 44192, 27321, 17000]
    months = ['Jan', 'Fev', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Set', 'Out', 'Nov', 'Dez']
    bar_colors = ['tab:green']

    ax.bar(months, counts, color=bar_colors)

    ax.set_ylabel('Renda (R$)')
    
    canvas = FigureCanvasTkAgg(fig, master=self.chartframe)
    canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8, anchor="n")
    canvas.draw()
