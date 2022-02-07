from difflib import restore
import json
import requests
from rest_framework import response ,status 


def check_car_exist(make, model) -> bool:
	if not make:
		return  response.Response({'detail': 'Missing Make name'},status=status.HTTP_403_FORBIDDEN)
	if not model:
		return response.Response({'detail': 'Missing Model name'},status=status.HTTP_403_FORBIDDEN)
	try:

		call_response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/%s?format=json' % (make))
		data = json.loads(call_response.content)
		count = data['Count']
		results = data['Results']
		models = [str(value['Model_Name']).upper() for value in results]

		if count and model in models:
			return True
		else:
			return False

	except Exception as e:
		raise e
