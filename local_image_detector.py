# this example uses requests
import requests
import json

params = {
  'models': 'nudity-2.0,wad,offensive,gore,tobacco',
  'api_user': '1896820637',
  'api_secret': 'b93gb2p94aBDaEqyEayJ'
}

files = {'media': open('/Users/duke/Desktop/lion.jpg', 'rb')}
r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)

res = json.loads(r.text)

nudityJsonData = res["nudity"]['sexual_display']
weaponsJsonData = res['weapon']
drugsJsonData = res['drugs']
medicalDrugsJsonData = res['medical_drugs']
offensiveJsonData = res['offensive']['prob']
tobaccoJsonData = res['tobacco']['prob']

detectionProbability = {
  "Nudity": nudityJsonData,
  "Weapon": weaponsJsonData,
  "Drugs": drugsJsonData,
  "Medical Drugs": medicalDrugsJsonData,
  "Offensive": offensiveJsonData,
  "Tobacco": tobaccoJsonData
}

# print(detectionProbability)

for key, val in detectionProbability.items():
    print(f'{key}: {val}')

# print(f"[Sexual Activity]: {jsonData['sexual_activity']} ")
# print(f"[Sexual Display]: {jsonData['sexual_display']} ")
# print(f"[Erotica]: {jsonData['erotica']} ")
