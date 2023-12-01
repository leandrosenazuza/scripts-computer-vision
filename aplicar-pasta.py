import cv2
from ultralytics import YOLO

# Carregar a imagem
image_path = './img.JPG'
output_path = './output_img.jpg'

image = cv2.imread(image_path)

# Inicializar o modelo YOLO
model_path = r'C:\Mestrado\treinamentos\train3\weights\best.pt'
model = YOLO(model_path)

# Executar detecção de objetos na imagem
results = model(image)
labels=[]
# Process results list
for result in results:
    boxes = result.boxes.xyxy.tolist()
    classes = result.boxes.cls.tolist()
    names = result.names
    confidences = result.boxes.conf.tolist()
    print(boxes)
    for box, cls, conf in zip(boxes, classes, confidences):
        x1, y1, x2, y2 = box
        x1=x1/640
        x2=x2/640
        y1=y1/640
        y2=y2/640
        print(cls,names[int(cls)],x1,y1,x2,y2)
        confidence = conf
        detected_class = cls
        name = names[int(cls)]