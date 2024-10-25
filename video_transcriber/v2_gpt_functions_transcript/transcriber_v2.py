# v2 - Versión con Funciones Adicionales utilizando GPT
# Esta versión añade monitoreo de recursos del sistema y una interfaz de usuario mejorada.
# Funcionalidades:
# - Monitoreo del uso de CPU y RAM durante la transcripción.
# - Extracción del audio del video.
# - Transcripción del audio a texto.
# - Guarda el resultado en un archivo de texto.
# - Interfaz interactiva para elegir entre varios videos o cambiar de carpeta.

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

def process_folder(folder_path, model):
    videos = [f for f in os.listdir(folder_path) 
              if f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]
    
    if not videos:
        print("No se encontraron videos en esta carpeta.")
        return True
    
    while True:
        print("\nVideos disponibles:")
        for i, file in enumerate(videos, 1):
            print(f"{i}. {file}")
        
        try:
            choice = int(input("\nSeleccione el número del video (0 para cambiar carpeta): "))
            if choice == 0:
                return True
            if 1 <= choice <= len(videos):
                video_path = os.path.join(folder_path, videos[choice-1])
                transcribe_video(video_path, model)
            else:
                print("Selección no válida")
        except ValueError:
            print("Por favor, ingrese un número válido")
        
        continuar = input("\n¿Qué desea hacer?\n"
                         "1: Procesar otro video en la misma carpeta\n"
                         "2: Cambiar de carpeta\n"
                         "3: Salir\n"
                         "Seleccione una opción (1/2/3): ").strip()
        
        if continuar == '2':
            return True
        elif continuar == '3':
            return False
        elif continuar != '1':
            print("Opción no válida, continuando en la misma carpeta...")

def main():
    try:
        print("Cargando modelo Whisper...")
        model = whisper.load_model("medium")
        print("Modelo cargado exitosamente")
        
        last_path = None
        change_folder = True
        
        while True:
            if change_folder:
                if last_path:
                    print(f"\nÚltima carpeta utilizada: {last_path}")
                    use_last = input("¿Desea usar la misma carpeta? (s/n): ").lower()
                    if use_last == 's':
                        folder_path = last_path
                    else:
                        folder_path = input("Ingrese la nueva ruta de la carpeta: ").strip()
                else:
                    folder_path = input("Ingrese la ruta de la carpeta: ").strip()
                
                if folder_path.lower() == 'salir':
                    break
                    
                if not os.path.exists(folder_path):
                    print("Ruta no válida.")
                    continue
                
                last_path = folder_path
                
            change_folder = process_folder(folder_path, model)
            
            if not change_folder:
                break
                
    except Exception as e:
        print(f"Error en el programa: {e}")
        raise e

if __name__ == "__main__":
    main()
