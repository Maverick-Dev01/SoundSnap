# src/search.py
# Lógica de búsqueda usando yt_dlp para obtener títulos y URLs desde YouTube

from yt_dlp import YoutubeDL

def search_youtube(query: str, max_results=20):
    """
    Recibe un texto (query), busca en YouTube y devuelve una lista de resultados con título y URL.
    """
    ydl_opts = {
        'quiet': True,              # No mostrar logs
        'extract_flat': True,       # No descarga, solo extrae info básica
        'skip_download': True,
        'force_generic_extractor': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
            entries = result.get('entries', [])
            return [
                {
                    "title": e.get("title", "Sin título"),
                    "id": e.get("id", ""),
                    "url": f"https://www.youtube.com/watch?v={e.get('id', '')}"
                }
                for e in entries
            ]
        except Exception as e:
            print(f"❌ Error al buscar en YouTube: {e}")
            return []
