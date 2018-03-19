# ----------------------------------------------------
# Test MSFT Azure Face API with SDK
# Refer to https://azure-recipe.kc-cloud.jp/2017/02/cognitive-services-face-sdk/
# 
# Add pictures and train the person
# ----------------------------------------------------
import cognitive_face as CF
import json
import glob
from time import sleep

# KEY = 'dbbc8957ea3f4f2f8f3641dfac48862b' # KEY 1
KEY = 'd047720aeab74e7b90776063ed8b3736' # KEY 2
CF.Key.set(KEY)

BASE_URL = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

group_id = 'test_gid'
person_id = 'aa1a1aef-08e6-4461-9dd5-6facb073bc68' # Koh in test_gid

# Input new picture for training
image_path = input("Enter new picture file path > ")
image = open(image_path, 'rb')
result = CF.person.add_face(image, group_id, person_id)
image.close()
print(json.dumps(result, indent=4))

# Train the person group
result = CF.person_group.train(group_id)
print('Checking the training status. Please wait for a minute...')
sleep(60)

# Check the training status
result = CF.person_group.get_status(group_id)
print(json.dumps(result, indent=4))
