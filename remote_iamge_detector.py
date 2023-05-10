
# this example uses requests
import requests
import json

params = {
  'url': 'https://sightengine.com/assets/img/examples/example7.jpg',
  'models': 'nudity-2.0,wad,offensive,gore,tobacco',
  'api_user': '1896820637',
  'api_secret': 'b93gb2p94aBDaEqyEayJ'
}
r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)

res = json.loads(r.text)

nudityJsonData = res["nudity"]['sexual_display']
weaponsJsonData = res['weapon']
drugsJsonData = res['weapon']
medicalDrugsJsonData = res['weapon']
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