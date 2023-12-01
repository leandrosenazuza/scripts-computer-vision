import os
import cv2
from ultralytics import YOLO
import yaml

IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'teste3.JPG')  # Caminho para a imagem de entrada

# Carrega a imagem
image = cv2.imread(IMAGE_PATH)

# Inicializa o modelo YOLO
model_path = r'C:\Mestrado\treinamentos\train3\weights\best.pt'
model = YOLO(model_path)  # Carrega um modelo personalizado
model.predict(IMAGE_PATH, save = True , save_txt = True)
