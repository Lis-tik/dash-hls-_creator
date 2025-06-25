import os
from pathlib import Path


def create_manifest(data, global_path):
    Path(f'{global_path}/converted/manifest.mpd').mkdir(parents=True, exist_ok=True)


text = ''
