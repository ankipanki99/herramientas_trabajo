# Downloader v1 - Basic Version
# This script allows downloading YouTube videos using yt-dlp.
# Features:
# - Prompts the user for the video URL and output directory.
# - Displays available quality options for selection.
# - Downloads the video with a formatted filename.

import yt_dlp

def download_video(url, output_path='.'):
    try:
        # Obtener y mostrar las opciones de calidad disponibles
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            
            recommended_format = None
            print("\nOpciones de calidad disponibles:")
            for i, f in enumerate(formats):
                format_note = f.get('format_note', 'N/A')
                ext = f.get('ext', 'N/A')
                vcodec = f.get('vcodec', 'N/A')
                acodec = f.get('acodec', 'N/A')
                filesize = f.get('filesize', 'Desconocido')
                
                print(f"{i + 1}. {format_note} - {ext} - {vcodec} - {acodec} - {filesize} bytes")
                
                # Identificar una opción equilibrada (360p, mp4, H.264, con audio)
                if format_note == '360p' and ext == 'mp4' and vcodec == 'avc1.42001E' and acodec == 'mp4a.40.2':
                    recommended_format = i + 1
        
        # Mostrar la opción recomendada
        if recommended_format:
            print(f"\nOpción recomendada: {recommended_format}. 360p - mp4 - H.264 - con audio")
        else:
            print("\nNo se encontró ninguna opción recomendada (360p, mp4, H.264, con audio).")
        
        # Solicitar la calidad al usuario
        quality_index = int(input("\nElige el número de la calidad del video que deseas descargar: ").strip()) - 1
        if 0 <= quality_index < len(formats):
            selected_format = formats[quality_index]['format_id']
        else:
            print("\nSelección no válida, descargando en calidad mejor por defecto.")
            selected_format = 'bestvideo+bestaudio/best'
        
        # Formatear el nombre del archivo como ANOmesdia_nombre de la ponencia_autor
        upload_date = info_dict.get('upload_date', 'Desconocido')
        title = info_dict.get('title', 'Desconocido').replace(' ', '_')
        uploader = info_dict.get('uploader', 'Desconocido').replace(' ', '_')
        filename = f"{upload_date}_{title}_{uploader}.%(ext)s"
        
        ydl_opts = {
            'outtmpl': f'{output_path}/{filename}',
            'format': selected_format
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nDescarga completa. Guardado en: {output_path}")
    except Exception as e:
        print(f"\nError al descargar el video: {e}")

if __name__ == "__main__":
    # Solicitar URL del video al usuario
    url = input("Introduce la URL del video de YouTube: ")
    output_path = input("Introduce el directorio donde deseas guardar el video (deja vacío para el actual): ").strip()

    # Descargar el video
    download_video(url, output_path if output_path else '.')
