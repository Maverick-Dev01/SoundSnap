# src/app.py
# Aquí configuramos los ajustes globales de la interfaz (tema, apariencia, tamaño)
# y lanzamos la ventana principal desde la clase MainUI.

import customtkinter as ctk
from src.ui import MainUI  # Importamos la interfaz principal

def run_app():
    # Configura el tema: puede ser 'light', 'dark' o 'system'
    ctk.set_appearance_mode("dark")
    # Color principal (puedes cambiarlo por 'green', 'blue', 'dark-blue', etc.)
    ctk.set_default_color_theme("blue")

    # Creamos la instancia de la interfaz
    app = MainUI()
    app.mainloop()  # Inicia el loop principal de la app (abre la ventana)
