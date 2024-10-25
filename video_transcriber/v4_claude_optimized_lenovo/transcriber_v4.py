# v4 - Optimized for Lenovo Laptop Blankis (Optimized by Claude 3.5)
# This version has been specifically optimized for use on a Lenovo laptop (Blankis model).
# The optimization was performed using Claude 3.5 to ensure efficient resource utilization.
# Features:
# - Monitors CPU and RAM usage during transcription.
# - Extracts audio from video files and transcribes it to text.
# - Saves the transcription result in a text file.
# - Simple user interface to select a folder, choose a video, and initiate transcription.

import whisper
import moviepy.editor as mp
import os
import time
import psutil

def monitor_resources():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    return f"CPU: {cpu_percent}% | RAM: {memory.percent}% | RAM Disponible: {memory.available / (1024 * 1024 * 1024):.2f}GB"

def extract_audio_from_video(video_path, output_audio_path):
    try:
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path, codec='pcm_s16le')
        video.close()
    except Exception as e:
        print(f"Error extrayendo el audio: {e}")
        raise e

def transcribe_video(video_path, model):
    audio_path = os.path.splitext(video_path)[0] + ".wav"
    try:
        print("Iniciando proceso de transcripción...")
        print("Estado del sistema:", monitor_resources())
        
        print("Extrayendo audio...")
        extract_audio_from_video(video_path, audio_path)
        print("Audio extraído exitosamente")
        
        print("Comenzando transcripción...")
        start_time = time.time()
        
        # Transcripción básica sin parámetros adicionales
        result = model.transcribe(audio_path)
        
        duration = time.time() - start_time
        
        output_file = os.path.splitext(video_path)[0] + "_transcripcion.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"\nTranscripción completada en {duration:.2f} segundos")
        print("Estado final del sistema:", monitor_resources())
        print(f"Transcripción guardada en: {output_file}")
        
    except Exception as e:
        print(f"Error en la transcripción: {e}")
        raise e
    finally:
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except:
                pass

def main():
    try:
        print("Cargando modelo Whisper...")
        model = whisper.load_model("medium")
        print("Modelo cargado exitosamente")
        
        while True:
            folder_path = input("\nRuta de la carpeta de videos (o 'salir'): ").strip()
            if folder_path.lower() == 'salir':
                break
                
            if not os.path.exists(folder_path):
                print("Ruta no válida.")
                continue
            
            videos = [f for f in os.listdir(folder_path) 
                     if f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]
            
            if not videos:
                print("No se encontraron videos.")
                continue
                
            print("\nVideos disponibles:")
            for i, file in enumerate(videos, 1):
                print(f"{i}. {file}")
            
            try:
                choice = int(input("\nSeleccione el número del video: "))
                if 1 <= choice <= len(videos):
                    video_path = os.path.join(folder_path, videos[choice-1])
                    transcribe_video(video_path, model)
                else:
                    print("Selección no válida")
            except ValueError:
                print("Por favor, ingrese un número válido")
            
            if input("\n¿Desea procesar otro video? (s/n): ").lower() != 's':
                break
                
    except Exception as e:
        print(f"Error en el programa: {e}")
        raise e

if __name__ == "__main__":
    main()

    