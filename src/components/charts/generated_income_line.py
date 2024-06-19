import customtkinter as ctk
import matplotlib.pyplot as plt
import tkinter.filedialog as filedialog
from PIL import Image
from tkinter import messagebox
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.utils.options import YEARS
from src.utils.api import API_BASE_URL
  
class GeneratedIncomeLine(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master)
    self.render()
    
  def fetchData(self, year):
      url = f"{API_BASE_URL}/statistics/income?year={year}"
          
      try:
          response = requests.get(url)
       
          if int(response.status_code) == 200:
              data = response.json()
              return data
          else:
              messagebox.showerror("Receita", "Um erro ocorreu para recuperar as informações")
              return []
      except requests.RequestException as e:
          messagebox.showerror("Receita", "Impossível obter as informaçõe no momento, tente mais tarde.")
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
      text="Receita",
      font=ctk.CTkFont(weight='bold', size=24),
      text_color="#141D24"
    )
    self.title.pack(side="left", anchor="w")
    
    # YEAR 
    
    def year_options_callback(choice):
      self.update_chart(choice)
    
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
    
    # Export Button
        
    download_icon = Image.open("assets/images/download.png")
    self.download_icon_image = ctk.CTkImage(download_icon, size=(44, 44))

    self.export_button = ctk.CTkButton(
      self.actionsframe, 
      text="",
      image=self.download_icon_image,
      command=self.export_chart,
      width=72,
      height=72,
      hover_color="#f0f2f5",
      fg_color="#f0f2f5"
    )
    
    self.export_button.pack(side="left", anchor="w")
    
    # ---------------- chart -----------------
    
    self.chartframe = ctk.CTkFrame(
      self.mainframe,
      fg_color="#FFFFFF",
      corner_radius=24,
    )
    
    self.chartframe.pack(fill="both", expand=True, anchor="n")
    
    self.fig, self.ax = plt.subplots()
    
    # Adicionar a grade horizontal
    self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y')

    self.canvas = FigureCanvasTkAgg(self.fig, master=self.chartframe)
    self.canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8, anchor="n")

    # Inicializar com o primeiro ano da lista
    self.update_chart(YEARS[0])
    
  def update_chart(self, year):
    data = self.fetchData(year)
    
    # Limpar o gráfico existente
    self.ax.clear()

    # Adicionar a grade horizontal novamente
    self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y')

    if data:
      counts = [item["income"] for item in data]
      months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
      bar_colors = ['tab:green']

      bars = self.ax.bar(months, counts, color=bar_colors)

      # Adicionar labels em cima de cada barra
      for bar, count in zip(bars, counts):
        height = bar.get_height()
        self.ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{count}', ha='center', va='bottom')

      self.ax.set_ylabel('Renda (R$)')
      self.ax.set_xlabel('Meses')
      self.ax.set_title(f'Receita para o Ano {year}')
      
    self.canvas.draw()
    
  def export_chart(self):
    filetypes = [('PNG', '*.png'), ('PDF', '*.pdf')]
    
    file_path = filedialog.asksaveasfilename(
      title="Gráfico de renda gerada",
      initialfile="renda_gerada",
      defaultextension=".png", 
      filetypes=filetypes
    )
    
    if file_path:
      self.fig.savefig(file_path)
      messagebox.showinfo("Exportar", "Gráfico salvo com sucesso!")
    else:
      messagebox.showerror("Exportar", "Erro ao salvar o gráfico!")