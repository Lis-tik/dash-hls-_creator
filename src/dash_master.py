import subprocess



    # cmd = [
    #     'ffmpeg',
    #     '-i', work_mkv,  # Входной файл
    #     '-c:v', 'libsvtav1',  # Кодек
    #     '-preset', str(speed),  # Скорость/качество
    #     '-crf', str(quality['crf']),  # Качество (CRF)
    #     '-pix_fmt', 'yuv420p10le',  # Формат пикселей
    #     '-an', '-sn',  # Без аудио и субтитров
    #     '-f', 'dash',  # Формат вывода (DASH)
    #     '-seg_duration', str(self.hls_time),  # Длительность сегментов
    #     '-use_timeline', '1',  # Включить временную шкалу
    #     '-init_seg_name', 'init-stream$RepresentationID$.m4s',  # Имя init-сегмента
    #     '-media_seg_name', 'chunk-stream$RepresentationID$-$Number%05d$.m4s',  # Имя чанков
    #     '-vf', quality['vf'],  # Фильтры (если есть)
    #     f"{save_path}/video/{quality['name']}/video.mpd"  # Выходной файл
    # ]

class ReadyVideoConfiguration:
    def __init__(self, data):
        self.data = data
        self.qualities = []
        self.cmd = []

    def qualities_calculation():
        qualities = []
        qualities = [
            {'name': '4K', 'caf': '3840x2160', 'vf': 'scale=-2:2160', 'b:v': '35000k', 'crf': '28'},
            {'name': '2K', 'caf': '2560x1440', 'vf': 'scale=-2:1440', 'b:v': '12000k', 'crf': '30'},
            {'name': '1080p', 'caf': '1920x1080', 'vf': 'scale=-2:1080', 'b:v': '8000k', 'crf': '32'},
            {'name': '720p', 'caf': '1280x720', 'vf': 'scale=-2:720', 'b:v': '5000k', 'crf': '34'},
            {'name': '480p', 'caf': '854x480', 'vf': 'scale=-2:480', 'b:v': '2500k', 'crf': '36'},
            {'name': '360p', 'caf': '640x360', 'vf': 'scale=-2:360', 'b:v': '1200k', 'crf': '38'}
        ]

            # cmd = [
            #     'ffmpeg',
            #     '-i', work_mkv,  # Входной файл
            #     '-c:v', 'libsvtav1',  # Кодек
            #     '-preset', str(speed),  # Скорость/качество
            #     '-crf', str(quality['crf']),  # Качество (CRF)
            #     '-pix_fmt', 'yuv420p10le',  # Формат пикселей
            #     '-an', '-sn',  # Без аудио и субтитров
            #     '-f', 'dash',  # Формат вывода (DASH)
            #     '-seg_duration', str(self.hls_time),  # Длительность сегментов
            #     '-use_timeline', '1',  # Включить временную шкалу
            #     '-init_seg_name', 'init-stream$RepresentationID$.m4s',  # Имя init-сегмента
            #     '-media_seg_name', 'chunk-stream$RepresentationID$-$Number%05d$.m4s',  # Имя чанков
            #     '-vf', quality['vf'],  # Фильтры (если есть)
            #     f"{save_path}/video/{quality['name']}/video.mpd"  # Выходной файл
            # ]

    def start(self):
        try:
            subprocess.run(self.cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка FFmpeg: {e.stderr}")