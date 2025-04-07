import customtkinter as ctk
from tkinter import ttk
from src.search import search_youtube

class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎧 SoundSnap V2")
        self.geometry("950x600")
        self.resizable(False, False)

        # 🌙 Estilo para Treeview (modo oscuro)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#1e1e1e",
                        foreground="white",
                        fieldbackground="#1e1e1e",
                        font=("Segoe UI", 10),
                        rowheight=28)
        style.map('Treeview',
                  background=[('selected', '#3a7ebf')],
                  foreground=[('selected', 'white')])
        style.configure("Treeview.Heading",
                        font=('Segoe UI', 11, 'bold'),
                        background="#292929",
                        foreground="white")

        # Variables
        self.search_var = ctk.StringVar()
        self.results_frame = None
        self.tree = None

        self.build_ui()

    def build_ui(self):
        # Título principal
        title = ctk.CTkLabel(self, text="SoundSnap 🎵", font=("Segoe UI", 24, "bold"))
        title.pack(pady=20)

        # Sección del buscador
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=10)

        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Buscar canción, artista o álbum", width=400, textvariable=self.search_var)
        search_entry.pack(side="left", padx=10)
        search_entry.bind("<Return>", lambda event: self.search_music())  # Hacer búsqueda al presionar Enter

        search_btn = ctk.CTkButton(search_frame, text="Buscar", command=self.search_music)
        search_btn.pack(side="left")

    def search_music(self):
        query = self.search_var.get()
        if not query:
            print("⚠️ Campo de búsqueda vacío.")
            return

        results = search_youtube(query)

        # Limpiar resultados anteriores
        if self.results_frame:
            self.results_frame.destroy()

        # Crear nuevo contenedor de resultados
        self.results_frame = ctk.CTkFrame(self)
        self.results_frame.pack(pady=20, fill="both", expand=True)

        # Subframe para tabla y scrollbar
        table_frame = ctk.CTkFrame(self.results_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Tabla (Treeview)
        self.tree = ttk.Treeview(table_frame, columns=("Título", "Enlace"), show="headings")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Enlace", text="Enlace")
        self.tree.column("Título", width=500)
        self.tree.column("Enlace", width=400)

        # Agregar resultados a la tabla
        for result in results:
            self.tree.insert("", "end", values=(result["title"], result["url"]))

        # Scrollbar vertical única
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # Layout
        self.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
