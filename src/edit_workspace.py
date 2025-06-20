


mode_list = [['1. Аудиодорожки\n2. Титры\n:'], ]


def edit_workspace(content):
    print('Включен режим редактирования\nНажмите [ENTER], чтобы выйти')
    while True:
        mode = int(input('1. Аудиодорожки\n2. Титры\n:'))
        if mode == 1:
            print('Редактирование аудиодорожек')
            audio_mode = int(input('\n1. Изменить параметры\n2. Удалить\n3. Назад'))
