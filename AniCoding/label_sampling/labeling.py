from google.cloud import vision
import os
import io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\EunSung\Desktop\GoogleKey\eunsung5oh\animecoding-96c2871e26a6.json" # API Key path

client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('src/') # image path

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

file = open('label.txt', 'a')
print('Labels :')
for label in labels:
    print(label.description)
    w = file.write(f'\n{label.description}')

w = file.write('\n')