# src/ui.py
# Interfaz principal de la aplicación: muestra el título, buscador, y prepara todo para los resultados.

import customtkinter as ctk
from src.search import search_youtube

class MainUI(ctk.CTk):  # Heredamos de CTk (ventana principal)
    def __init__(self):
        super().__init__()  # Inicializa la ventana

        # Configuración general de la ventana
        self.title("🎧 SoundSnap V2")
        self.geometry("950x600")
        self.resizable(False, False)

        # Variables de estado (se usan para obtener texto del usuario)
        self.search_var = ctk.StringVar()

        self.build_ui()  # Llama al método que construye los elementos visuales

    def build_ui(self):
        # Título
        title = ctk.CTkLabel(self, text="SoundSnap 🎵", font=("Segoe UI", 24, "bold"))
        title.pack(pady=20)

        # Frame del buscador
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=10)

        # Campo de entrada de texto para buscar canciones o artistas
        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Buscar canción, artista o álbum", width=400, textvariable=self.search_var)
        search_entry.pack(side="left", padx=10)

        # Botón para lanzar la búsqueda
        search_btn = ctk.CTkButton(search_frame, text="Buscar", command=self.search_music)
        search_btn.pack(side="left")

    def search_music(self):
        """
        Esta función se ejecuta cuando el usuario hace clic en 'Buscar'.
        Toma el texto ingresado, lo envía a YouTube a través de yt_dlp, y muestra resultados en consola (por ahora).
        """
        query = self.search_var.get()  # Obtiene lo que el usuario escribió
        if not query:
            print("⚠️ Campo de búsqueda vacío.")
            return

        results = search_youtube(query)  # Llama a la función de búsqueda
        print(f"🔍 Resultados para '{query}':")
        for r in results:
            print(f"🎵 {r['title']} → {r['url']}")  # Muestra título y enlace
