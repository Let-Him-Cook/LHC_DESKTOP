import customtkinter as ctk
import matplotlib.pyplot as plt
import tkinter.filedialog as filedialog
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import requests
import numpy as np
from src.utils.options import MONTHS_MAP, MONTHS, YEARS
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
                print(f"{response}")
                messagebox.showerror("Maiores vendas", "Um erro ocorreu para recuperar as informações")
                return []
        except requests.RequestException as e:
            messagebox.showerror("Maiores vendas", "Impossível obter as informações no momento, tente mais tarde.")
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
        self.year_var = ctk.StringVar(value=YEARS[0])
        
        def year_options_callback(choice):
            self.update_chart(choice, MONTHS_MAP[self.month_var.get()])
    
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
            ),
            variable=self.year_var
        )
        
        self.year.pack(side="left", anchor="w", padx=16)
        
        # MONTH
        self.month_var = ctk.StringVar(value=MONTHS[0])
        
        def month_options_callback(choice):
            self.update_chart(self.year_var.get(), MONTHS_MAP[choice])
    
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
            ),
            variable=self.month_var
        )
        
        self.month.pack(side="left", anchor="w", padx=16)
        
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
        
        self.chartframe.pack(fill="both",expand=True, anchor="n")
        
        self.fig, self.ax = plt.subplots(figsize=(4, 4.4), subplot_kw=dict(aspect="equal"))
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chartframe)
        self.canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=8, pady=8, anchor="n")

        # Inicializar com o primeiro ano e mês da lista
        self.update_chart(YEARS[0],MONTHS_MAP[MONTHS[0]])

    def update_chart(self, year, month):
        data = self.fetchData(year, month)
        
        # Limpar o gráfico existente
        self.ax.clear()

        if data:
            # Obter uma lista de valores de quantity
            quantities = [item["quantity"] for item in data]

            # Obter uma lista de valores de name
            names = [item["name"] for item in data]

            def func(pct, allvals):
                absolute = int(np.round(pct/100.*np.sum(allvals)))
                return f"{pct:.1f}%\n({absolute:d})"
            
            wedges, texts, autotexts = self.ax.pie(
                quantities, 
                autopct=lambda pct: func(pct, quantities),
                labels=names,
            )

            plt.setp(autotexts, size=10, weight="normal", color="white")

        self.canvas.draw()

    def export_chart(self):
        filetypes = [('PNG', '*.png'), ('PDF', '*.pdf')]
        
        file_path = filedialog.asksaveasfilename(
            title="Gráfico de Maiores Vendas",
            initialfile="maiores_vendas",
            defaultextension=".png", 
            filetypes=filetypes
        )
        
        if file_path:
            self.fig.savefig(file_path)
            messagebox.showinfo("Exportar", "Gráfico salvo com sucesso!")
        else:
            messagebox.showerror("Exportar", "Erro ao salvar o gráfico!")