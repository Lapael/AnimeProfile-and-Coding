def labeling(url):
    from google.cloud import vision
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\EunSung\Desktop\GoogleKey\eunsung5oh\animecoding-96c2871e26a6.json" # API Key path

    try:
        client = vision.ImageAnnotatorClient()

        image = vision.Image()
        image.source.image_uri = str(url)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        result = []
        for label in labels:
            result.append({'description': label.description, 'score': int(label.score * 100)})
        return result

    except Exception as e:
        print(f'Error : {e}')
        return []

def is_anime(url):
    labels = labeling(url)

    ani_num = 0
    keywords = ['Anime', 'Animation', 'Animated cartoon', 'Cartoon']

    for label in labels: # dict{}
        if any(keyword.lower() in label['description'].lower() for keyword in keywords):
            if label['score'] >= 70:
                ani_num += 1

    return ani_num