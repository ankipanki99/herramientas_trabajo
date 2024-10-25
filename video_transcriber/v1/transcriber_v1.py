# v1 - Versión Básica
# Este script realiza la transcripción de audio desde archivos de video utilizando el modelo "medium" de Whisper.
# Funcionalidades:
# - Extrae el audio del video.
# - Transcribe el audio a texto.
# - Guarda el resultado en un archivo de texto.

import whisper
import moviepy.editor as mp
import os

# Función para extraer el audio del video y guardarlo como un archivo WAV temporal
def extract_audio_from_video(video_path, output_audio_path):
    try:
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path, codec='pcm_s16le')
    except Exception as e:
        print(f"Error extrayendo el audio del video {video_path}: {e}")

# Función para listar los archivos de video en el directorio
def list_video_files(folder_path):
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
    return [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in video_extensions]

# Función para realizar la transcripción de un video seleccionado
def transcribe_video(video_path, model):
    audio_path = os.path.splitext(video_path)[0] + ".wav"
    try:
        # Extraer audio del video
        extract_audio_from_video(video_path, audio_path)

        # Realizar la transcripción
        result = model.transcribe(audio_path, language="es")

        # Mostrar y guardar la transcripción
        print("Transcripción del audio:")
        print(result["text"])

        output_file = os.path.splitext(video_path)[0] + "_transcripcion.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"La transcripción ha sido guardada en {output_file}")
    except Exception as e:
        print(f"Error transcribiendo el video {video_path}: {e}")
    finally:
        # Borrar el archivo de audio temporal
        if os.path.exists(audio_path):
            os.remove(audio_path)

# Función principal para gestionar el flujo del programa
def main():
    try:
        # Cargar el modelo de Whisper
        model = whisper.load_model("medium")
    except Exception as e:
        print(f"Error cargando el modelo Whisper: {e}")
        return

    folder_path = input("Ingrese la ruta de la carpeta que contiene los archivos de video: ")
    if not os.path.exists(folder_path):
        print("La ruta especificada no existe.")
        return

    while True:
        # Listar los archivos de video en la carpeta
        video_files = list_video_files(folder_path)

        if not video_files:
            print("No se encontraron archivos de video en la carpeta.")
            break

        print("Archivos de video disponibles:")
        for i, file_name in enumerate(video_files, 1):
            print(f"{i}. {file_name}")

        # Preguntar al usuario qué video desea transcribir
        try:
            video_choice = int(input("Ingrese el número del video que desea transcribir: "))
            if video_choice < 1 or video_choice > len(video_files):
                print("Selección inválida. Inténtalo de nuevo.")
                continue
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")
            continue

        selected_video = os.path.join(folder_path, video_files[video_choice - 1])

        # Realizar la transcripción
        transcribe_video(selected_video, model)

        # Preguntar si está satisfecho con el resultado
        satisfied = input("¿Estás satisfecho/a con la transcripción? (s/n): ").lower()
        if satisfied != 's':
            print("Proceso finalizado.")
            break

if __name__ == "__main__":
    main()
