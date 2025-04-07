# src/player.py
# Clase que abre una ventana emergente y reproduce el audio desde una URL (YouTube)

import tkinter as tk
import threading
import tempfile
import os
from ffpyplayer.player import MediaPlayer
from yt_dlp import YoutubeDL

class AudioPlayerWindow:
    def __init__(self, parent, video_url, title="Reproduciendo"):
        self.parent = parent
        self.video_url = video_url
        self.temp_file = None
        self.player = None
        self.window = tk.Toplevel(self.parent)
        self.window.title(f"🎵 {title}")
        self.window.geometry("400x150")
        self.window.configure(bg="#111111")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        tk.Label(self.window, text=title, bg="#111111", fg="white", font=("Segoe UI", 11, "bold"), wraplength=380).pack(pady=20)
        tk.Label(self.window, text="Reproduciendo audio desde YouTube...", bg="#111111", fg="gray").pack()

        # Inicia la reproducción en segundo plano
        threading.Thread(target=self.play_audio, daemon=True).start()

    def get_audio_stream(self):
        ydl_opts = {
            'quiet': True,
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(tempfile.gettempdir(), '%(id)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.video_url, download=True)
            filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            return filename

    def play_audio(self):
        try:
            self.temp_file = self.get_audio_stream()
            self.player = MediaPlayer(self.temp_file)
            self.player.set_volume(1.0)

            while True:
                frame, val = self.player.get_frame()
                if val == 'eof' or self.player is None:
                    break
        except Exception as e:
            print(f"❌ Error al reproducir audio: {e}")
        finally:
            self.close()

    def close(self):
        if self.player:
            self.player.close_player()
            self.player = None

        if self.temp_file and os.path.exists(self.temp_file):
            os.remove(self.temp_file)

        if self.window.winfo_exists():
            self.window.destroy()
