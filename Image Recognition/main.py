from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
from pprint import pprint

app = ClarifaiApp(api_key='d91fe39d217f482f974ae913641cc989')

# gets the moderation model
model = app.models.get('moderation')

# get media info from cloud
image = ClImage(url = 'https://i.pinimg.com/originals/97/ab/99/97ab998a340316e05fd11b6c6a7680e5.jpg')
#video = ClVideo(url = "put video url here")

jsonString = model.predict([image])
#model.predict([video])
print(jsonString)

# creates json file with response content
with open('Image Recognition/data.json', 'w') as outline:
    json.dump(jsonString, outline)

with open('data.json') as f:
    data = json.load(f)

# have line go through all the names
i = 0
jsonSTR = data

#num = sum(1 for line in open(data['outputs'][0]['data']['concepts']))

#print num

pprint(data['outputs'][0]['data']['concepts'])

finalSTR = ""

for entry in data['outputs'][0]['data']['concepts']:
    if entry['value'] >= 0.8:
        print entry['name']
        finalSTR = finalSTR + entry['name']

print(finalSTR)
