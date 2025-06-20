
import threading
import json
import os

from dash_master import start_dash_converted

def start_converted():
    main_data_list = []

    config_list = [f for f in os.listdir('./options') if f.endswith('.json')]

    for index in config_list:
        with open(f'./options/{index}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            main_data_list.append(data)


    for data in main_data_list:
        start_dash_converted(data)



start_converted()
