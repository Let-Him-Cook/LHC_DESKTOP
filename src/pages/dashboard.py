import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the plot
        self.plot_frame = ctk.CTkFrame(self)
        self.plot_frame.pack(fill="both", expand=True)

        # Generate some data
        categories = ['A', 'B', 'C', 'D']
        values = [3, 12, 5, 18]

        # Create a figure
        fig = Figure(figsize=(5, 4), dpi=100,facecolor="#F0F2F5")
        ax = fig.add_subplot(111)
        ax.bar(categories, values)
        ax.set_title("Sample Bar Chart")
        ax.set_xlabel("Category")
        ax.set_ylabel("Values")

        # Add the plot to the Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # Add a navigation bar or menu here if needed
        self.menu_button = ctk.CTkButton(self, text="Menu", command=self.show_menu)
        self.menu_button.pack(side="left", padx=10, pady=10)

        self.logout_button = ctk.CTkButton(self, text="Logout", command=self.logout)
        self.logout_button.pack(side="right", padx=10, pady=10)

    def show_menu(self):
        # Logic for showing the menu
        print("Show menu")

    def logout(self):
        # Logic for logging out
        print("Logout")
        self.master.show_page(LoginPage)

# Import LoginPage at the end to avoid circular import
from src.pages.login import LoginPage
