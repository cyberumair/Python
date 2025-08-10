import os

def create_folder(folder):
    if not(os.path.exists(folder)):
        os.mkdir(folder)

def data(extensions_list):
    return [file for file in files if os.path.splitext(file)[1].lower() in extensions_list]

def move_files(folder, data):
    for file in data:
        os.rename(file, f'{folder}/{file}')
        
files = os.listdir()
files.remove('main.py')

folders = ['Images', 'Docs', 'Media']

for folder in folders:
    create_folder(folder)

imgExtensions = ['.png', '.jpg', '.jpeg']
images = data(imgExtensions)

docExtensions = ['.doc', 'docx', '.txt', '.pdf']
docs = data(docExtensions)

mediaExtensions = ['.mp3', '.mp4']
medias = data(mediaExtensions)

move_files('Images', images)
move_files('Docs', docs)
move_files('Media', medias)
