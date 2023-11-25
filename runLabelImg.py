import subprocess
import os
#script para rodar o labelImg, responsavel por anotar as fotos
diretorioCloneLabelImg = r'C:\Mestrado\labelImg'
caminho_env_anaconda = r'C:\Users\leand\anaconda3'
caminhoParaPythonAnaconda = os.path.join(r'C:\Users\leand\anaconda3', 'python.exe')
executavelLabelImg = 'labelImg.py'

if os.path.exists(diretorioCloneLabelImg):
    comando_completo = f'cd /d {diretorioCloneLabelImg} && "{caminhoParaPythonAnaconda}" {executavelLabelImg}'
    subprocess.run(comando_completo, shell=True)
else:
    print("O diretório não foi encontrado.")
