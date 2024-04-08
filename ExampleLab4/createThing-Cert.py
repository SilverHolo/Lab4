################################################### Connecting to AWS
import boto3

import json
################################################### Create random name for things
import random
import string
import os 

###### added code 
total_thing_count = 5
device_id =5 
thingGroupName ="ThingGroup1DN"
thingGroupArn = "arn:aws:iot:us-east-2:851725370370:thinggroup/ThingGroup1DN"
################################################### Parameters for Thing
thingArn = ''
thingId = ''
thingName = f'TestCarDN5'
defaultPolicyName = 'DNMainPolicy'
#######################################################

def createThing():
	global thingClient
	thingResponse = thingClient.create_thing(
		thingName = thingName
	)
	data = json.loads(json.dumps(thingResponse, sort_keys=False, indent=4))
	for element in data: 
		if element == 'thingArn':
			thingArn = data['thingArn']
		elif element == 'thingId':
			thingId = data['thingId']
			createCertificate()

def createCertificate():
	global thingClient
	certResponse = thingClient.create_keys_and_certificate(
			setAsActive = True
	)
	data = json.loads(json.dumps(certResponse, sort_keys=False, indent=4))
	for element in data: 
			if element == 'certificateArn':
					certificateArn = data['certificateArn']
			elif element == 'keyPair':
					PublicKey = data['keyPair']['PublicKey']
					PrivateKey = data['keyPair']['PrivateKey']
			elif element == 'certificatePem':
					certificatePem = data['certificatePem']
			elif element == 'certificateId':
					certificateId = data['certificateId']
							
	with open('public.key', 'w') as outfile:
			outfile.write(PublicKey)
	with open('private.key', 'w') as outfile:
			outfile.write(PrivateKey)
	with open('cert.pem', 'w') as outfile:
			outfile.write(certificatePem)

	response = thingClient.attach_policy(
			policyName = defaultPolicyName,
			target = certificateArn
	)
	response = thingClient.attach_thing_principal(
			thingName = thingName,
			principal = certificateArn
	)

thingClient = boto3.client('iot')
createThing()