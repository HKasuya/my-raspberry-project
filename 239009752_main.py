import boto3
import pprint

image_path = ["001.jpg","002.jpg","003.jpg","004.jpg"]

rekognition = boto3.client(service_name="rekognition")

for image in image_path:
    with open(image, "rb") as f:
        image_data = f.read()
        detect_data = rekognition.detect_text(Image={"Bytes":image_data})
        texts = detect_data["TextDetections"]

#typeの確認
#pprint.pprint(texts, sort_dicts=False)

    for text in texts:
        if text["Type"] == "WORD":
            if text["DetectedText"] == "OK":
                print(image +":"+"OK")
            elif text["DetectedText"] == "Warning":
                print(image +":"+"Warning")
            elif text["DetectedText"] == "Danger":
                print(image +":"+"Danger")

