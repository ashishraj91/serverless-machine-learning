import boto3
import os
import uuid
import ctypes
import pickle
import sklearn
from sklearn.externals import joblib
import json
s3_client = boto3.client('s3')

def lambda_handler(event, context):
	s_desc=event['token']
	X_test1=[]
	X_test1.append(s_desc)
	bucket = 'syed-snow-bucket'
	key = 'model.pkl'
	download_path = '/tmp/{}{}'.format(uuid.uuid4(),key)
	s3_client.download_file(bucket, key, download_path)
	f = open(download_path, 'rb')
	loaded_model = pickle.load(f)
	class_predicted = loaded_model.predict(X_test1)
	val1=str(class_predicted[0])
	data={}
	data['predicted']=val1
	json_outcome=json.dumps(data) 
	f.close() 