from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
from pprint import pprint

app = ClarifaiApp(api_key='d91fe39d217f482f974ae913641cc989')

# gets the moderation model
model = app.models.get('moderation')

# get media info from cloud
image = ClImage(url = 'https://image.shutterstock.com/image-photo/rolled-marijuana-joint-half-burnt-260nw-135662744.jpg')

jsonString = model.predict([image])
#model.predict([video])
print(jsonString)

# creates json file with response content
with open('Image Recognition/data.json', 'w') as outline:
    json.dump(jsonString, outline)

with open('Image Recognition/data.json') as f:
    data = json.load(f)

pprint(data['outputs'][0]['data']['concepts'])

finalSTR = ""

# goes through all the json output and picks out things that likely appear in image (i.e. the 0.65 value)
for entry in data['outputs'][0]['data']['concepts']:
    if entry['value'] >= 0.65:
        finalSTR = finalSTR + entry['name']

print(finalSTR)
