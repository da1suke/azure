# ----------------------------------------------------
# Test MSFT Azure Face API with SDK
# Refer to https://azure-recipe.kc-cloud.jp/2017/02/cognitive-services-face-sdk/
# 
# Verify picture with person
# ----------------------------------------------------
import cognitive_face as CF
import json

# KEY = 'dbbc8957ea3f4f2f8f3641dfac48862b' # KEY 1
KEY = 'd047720aeab74e7b90776063ed8b3736' # KEY 2
CF.Key.set(KEY)

BASE_URL = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

personGroupId = 'test_gid'
personId = 'aa1a1aef-08e6-4461-9dd5-6facb073bc68' # Koh in test_gid

# Input picture and get faceId
image_path = input("Enter picture file path > ")
image = open(image_path, 'rb')
result = CF.face.detect(image)
image.close()
face_id = result[0]['faceId']
print("\n face_id = " + face_id + "\n")

# Show all persons' information
"""
result = CF.person.lists(personGroupId)
print(json.dumps(result, indent=4))
"""

# Verify
result = CF.face.verify(face_id, person_group_id=personGroupId, person_id=personId)
print(json.dumps(result, indent=4))
