import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.components.header import Header
from src.components.charts.biggest_sales_pie import BiggestSalesPie
from src.components.charts.generated_income_line import GeneratedIncomeLine

class DashboardPage(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master)
    self.render()

  def render(self):
    self.scrollableArea = ctk.CTkScrollableFrame(self, orientation="vertical")
    self.scrollableArea.pack(fill="both", expand=True)
    
    self.mainframe = ctk.CTkFrame(self.scrollableArea, fg_color="#F0F2F5")
    self.mainframe.pack(padx=32, fill="x", expand=True, anchor="n")
    
    # Dashboard Header
    self.header = Header(self.mainframe, self.logout)
    self.header.pack(fill="x", expand=True)
     
    # Title Page Frame
    self.title_page_frame = ctk.CTkFrame(self.mainframe)
    self.title_page_frame.pack(fill="x", expand=True, anchor="n", pady=32)
    
    # Title
    ctk.CTkLabel(
      self.title_page_frame, 
      text="Relatórios", 
      text_color="#92542F",
      font=ctk.CTkFont(size=36, weight="bold")
    ).pack(anchor="nw")
    
    # Divider
    ctk.CTkFrame(
      self.title_page_frame, 
      width=100, height=2, 
      fg_color="#CA6E33"
    ).pack(anchor="nw", pady=4)
    
    # ------------------ Charts ------------------
    
    # First Section
    top_chart_grid_frame = ctk.CTkFrame(self.mainframe)
    
    top_chart_grid_frame.grid_rowconfigure(0, weight=1)
    top_chart_grid_frame.grid_columnconfigure(0, weight=1)
    top_chart_grid_frame.grid_columnconfigure(1, weight=1)
    
    top_chart_grid_frame.pack( 
      fill="x", 
      expand=True, 
      pady=16
    )
    
    self.biggestSalesPieChart = BiggestSalesPie(top_chart_grid_frame)
    self.biggestSalesPieChart.grid(row=0, column=0, sticky="wnes")
    
    self.generatedIncomeLineChart = GeneratedIncomeLine(top_chart_grid_frame)
    self.generatedIncomeLineChart.grid(row=0, column=1, sticky="wnes")
    
    # Second Section
    
    # Third Section
    
  def logout(self):
    # Logic for logging out
    from src.pages.login import LoginPage
    self.master.show_page(LoginPage)

