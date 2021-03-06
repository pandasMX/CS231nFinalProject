import numpy as np
from keras.models import model_from_json

from common.Enums import DistanceMetrics
from common.computeAccuracy import computeAccuracy

MODEL_PATH = './model_DistanceMetrics.L1_sigmoid_sgd_20180602-143655.json'
WEIGHTS_PATH = './model_DistanceMetrics.L1_sigmoid_sgd_20180602-143655.h5'

json_file = open(MODEL_PATH, 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights(WEIGHTS_PATH)
print("Loaded model from disk")

DATA_DIR = './img_npy_final_features_only/DRESSES/Skirt/'

consumer_features = np.load(DATA_DIR + 'consumer_ResNet50_features.npy')
consumer_labels = np.load(DATA_DIR + 'consumer_labels.npy')
shop_features = np.load(DATA_DIR + 'shop_ResNet50_features.npy')
shop_labels = np.load(DATA_DIR + 'shop_labels.npy')

print (consumer_features.shape)
print (consumer_labels.shape)
print (shop_features.shape)
print (shop_labels.shape)

metrics = [DistanceMetrics.L1] #, DistanceMetrics.L2
top_k = [3,10,20,30,40,50]

for metric in metrics:
		print ("Metric: {}".format(metric))


		accuracies = computeAccuracy(consumer_features,
												   shop_features,
												   consumer_labels,
												   shop_labels,
												   metric = metric,
												   model = model,
												   k = top_k)

		print(accuracies)
