import os
import threading
from src.media_info import Info

start_message = 'Github разработчика: https://github.com/Lis-tik/dash-hls-_creator \n' \
'Данная программа создана для комфортного перекодирования медиа контента под dash (hls). База - ffmpeg\n\n' \
'Перед началом работы программы, зполните файл конфигурации (config.txt) по шаблону\n' \
'Либо выберете режим manual для ручного заполнения\n'

print(start_message)

class Main:
    def __init__(self):
        self.global_path = None
        self.main_data = None
        self.container_files = None
        self.additionally_audio = []

        self.subtitles_formats = ['.srt', '.ass', '.vtt', '.sub', '.ttml', '.pgs']

    def format_control(self, file):
        for x in self.subtitles_formats:
            return any(file.endswith(x) for x in self.subtitles_formats)




    def start(self):
        mode = int(input('1. Create\n2. Editing\n3. Exit\n:'))
        if mode == 1:
            print('Включен режим создания dash проекта')
            self.manual_mode()
        elif mode == 2:
            print('Включен режим редактирования готового dash проекта')

    def manual_mode(self):


        self.global_path = input('Шаг №1\nВведите полный путь к основной директории с проектом\n:')
        self.container_files = [f'{self.global_path}\{f}' for f in os.listdir(self.global_path) if (f.endswith('.mkv'))]
        print(f'В директории [{self.global_path}]: \n')

        info_main_video = Info()
        info_main_video.start_getinfo(self.container_files)
        self.main_data = info_main_video.info_main_lib

        # for value in self.main_data:
        #     print(value)

        print(info_main_video.summary_data())

        print('Шаг №2')
        while True:
            aud_lt = input('\nДобавьте дополнительные файлы с аудиодорожками (mka и т.п.)\nНажмите [ENTER], чтобы пропустить\n:')
            
            if not aud_lt:
                break

            temp_list = [f'{aud_lt}\{f}' for f in os.listdir(aud_lt)]
            info_main_video.update_chanel(temp_list)


        print('Шаг №3')
        while True:
            sub_lt = input('\nДобавьте дополнительные файлы с субтитрами (ass, aas и т.п.)\nНажмите [ENTER], чтобы пропустить\n:')
            
            if not sub_lt:
                break
            
            temp_list = [f'{aud_lt}\{f}' for f in os.listdir(sub_lt) if (self.format_control(f))]
            info_main_video.update_chanel(temp_list)

        self.main_data = info_main_video.info_main_lib
        print(info_main_video.summary_data(), '\n')




if __name__ == '__main__':
    app = Main()
    app.start()

