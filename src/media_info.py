import ffmpeg
import os

class Info():
    def __init__(self):
        self.container = []
        self.info_main_lib = []
        self.conteg = {}
        self.debug_message = ''


    def data_debug(self):
        self.debug_message = ''

        for x in range(len(self.info_main_lib)):
            content = self.container[x]

            temp_audio_list = []
            for y in self.info_main_lib[x][content]['audio']:
                if not (y['title'] in temp_audio_list):
                    temp_audio_list.append(y['title'])
                else:
                    self.debug_message += f'В медиа пространстве ({content}) есть дорожки с одинаковым именем!'



    def start_getinfo(self, container):
        self.container = container

        for x in range(len(self.container)):
            name_path = self.container[x]

            self.conteg = {name_path: {
                'video': [],
                'audio': [],
                'subtitle': []
                }}
            
            probe = ffmpeg.probe(name_path)
            for stream in probe['streams']:

                if stream['codec_type'] == 'video':
                    video_data_add = self.video_info(stream)
                    self.conteg[name_path]['video'].append(video_data_add)

                if stream['codec_type'] == 'audio':
                    audio_data_add = self.audio_info(stream)
                    self.conteg[name_path]['audio'].append(audio_data_add)

                if stream['codec_type'] == 'subtitle':
                    subtitle_data_add = self.subtitle_info(stream)
                    self.conteg[name_path]['subtitle'].append(subtitle_data_add)

            self.info_main_lib.append(self.conteg)



    def update_chanel(self, new_data):
        for x in range(len(new_data)):
            print(new_data[x], 'kk')
            probe = ffmpeg.probe(new_data[x])
            for stream in probe['streams']:
                if stream['codec_type'] == 'audio':

                    new_audio_chanel = self.audio_info(stream, new_data[x])
                    self.info_main_lib[x][self.container[x]]['audio'].append(new_audio_chanel)

                if stream['codec_type'] == 'subtitle':
                    new_subtitle_chanel = self.subtitle_info(stream, new_data[x])
                    self.info_main_lib[x][self.container[x]]['subtitle'].append(new_subtitle_chanel)


        # if len(os.listdir(aud_lt)) < len(self.main_data):
        #     print(f'Предупреждение! В директории {aud_lt} с аудио, файлов меньше, чем в основной директории!')


    def summary_data(self):
        summary_message = f'Всего файлов: {len(self.info_main_lib)}\n'

        for x in range(len(self.info_main_lib)):

            pth = self.info_main_lib[x]
            name = list(pth.keys())[0]
            summary_message += f'{x+1}.{name}: \n'

            summary_message += 'video: '
            for y in pth[name]['video']:
                summary_message += f'{y['width']}x{y['height']}; pix_fmt: {y['pix_fmt']}'

            summary_message += '\naudio: \n'
            for z in range(len(pth[name]['audio'])):
                cont = pth[name]['audio'][z]
                summary_message += f'--{z}.{cont['title']}; language: {cont['language']}; codec_name: {cont['codec_name']}; channels: {cont['channels']}; path: {cont['path']}\n'

            summary_message += 'subtitle: \n'
            for j in range(len(pth[name]['subtitle'])):
                cont = pth[name]['subtitle'][j]
                summary_message += f'--{j}.{cont['title']}; language: {cont['language']}; format: {cont['format']}; path: {cont['path']}\n'

            summary_message += '\n'
            
        return summary_message

                



    def video_info(self, stream):
        data = {
            'width': stream.get('width'),
            'height': stream.get('height'),
            'pix_fmt': stream.get('pix_fmt', 'unknown'),
            'profile': stream.get('profile', 'unknown'),
            'is_avc': int('avc' in stream.get('codec_name', '').lower()),
            'status': 1
        }
        return data
        

    def audio_info(self, stream, path=0):
        tags = stream.get('tags', {})  # Получаем мета-теги потока

        data = {
            'index': stream['index'],  # Индекс потока
            'codec_name': stream.get('codec_name', 'unknown'),  # Кодек
            'language': stream.get('tags', {}).get('language', 'unknown'),  # Язык (если есть)
            'title': tags.get('title', f'unknown'),  # Название дорожки (если есть)
            'channels': stream.get('channels', 'unknown'),  # Количество каналов
            'sample_rate': stream.get('sample_rate', 'unknown'),  # Частота дискретизации
            'bit_rate': stream.get('bit_rate', 'unknown'),  # Битрейт
            'status': 1,
            'path': path
        }
        return data
    
    def subtitle_info(self, stream, path=0):
        data = {
            'format': stream.get('codec_name', 'unknown'),
            'language': stream.get('tags', {}).get('language', 'unknown'),
            'title':  stream.get('tags', {}).get('title', 'unknown'),
            # 'title': 'subs',
            'forced': int(stream.get('disposition', {}).get('forced', 0) == 1),
            'default': int(stream.get('disposition', {}).get('default', 0) == 1),
            'is_bitmap': int(stream.get('codec_name', '').lower() in ['dvd_subtitle', 'hdmv_pgs_subtitle', 'xsub']),
            'is_text': int(stream.get('codec_name', '').lower() in ['subrip', 'ass', 'ssa', 'mov_text', 'webvtt']),
            'status': 1,
            'path': path
        }
        return data








