import os
import shutil

inicial = 'C:/Users/USUARIO/Desktop/Luciano Filho Arquivos/Byjus/Byjus - Aula 102' 
finalize = 'C:/Users/USUARIO/Desktop/Luciano Filho Arquivos/Byjus/Byjus - Aula 102/Images'
FileList = os.listdir(inicial)


for file in FileList:
    raiz, ext = os.path.splitext(file)
    if ext in ['.png','.jpg','.gif','.WebP', '.jfif']:
        shutil.move(inicial + '/' + file, finalize + '/' + file)
        print('Arquivos Direcioná-dos')