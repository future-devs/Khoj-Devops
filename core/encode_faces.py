# USAGE
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

def update_pickle(args):
	try:
		args["detection_method"]
	except KeyError:
		args["detection_method"]="cnn"

	try:
		args["encodings"]
	except KeyError:
		args["encodings"]="encodings.pickle"

	# grab the paths to the input images in our dataset
	print("[INFO] quantifying faces...")
	imagePaths = list(paths.list_images(args["dataset"]))
	result=dict()
	# initialize the list of known encodings and known names
	#loop over the image paths
	# print(imagePaths)
	for (i, imagePath) in enumerate(imagePaths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
		key = imagePath.split(os.path.sep)[-2]

		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb,model=args["detection_method"])
		person_count=len(boxes)
		if person_count!=1:
			if person_count>1:
				print("More than one faces detected!")
			elif person_count==0:
				print("No face detected!")
			
			try:
				result[key].append(False)
			except KeyError:
				result[key]=[False]
				
		else:
			# compute the facial embedding for the face
			encodings = face_recognition.face_encodings(rgb, boxes)
			try:
				result[key].append(encodings)
			except KeyError:
				result[key]=[encodings]
			# print(name,encoding)
	# print(result)
	return result
	# #dump the facial encodings + names to disk
	# try:
	# 	current_encoded_pickle = open(args["encodings"] , "rb")
	# 	data = pickle.loads(current_encoded_pickle.read())
	# except FileNotFoundError:
	# 	data = {"encodings": [], "names": []}
	# print("[INFO] serializing encodings...")

	# data["encodings"]+=knownEncodings
	# data["names"]+=knownNames
	# f = open(args["encodings"], "wb")
	# f.write(pickle.dumps(data))
	# f.close()

if __name__=='__main__':
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--dataset", required=True,help="path to input directory of faces + images")
	ap.add_argument("-e", "--encodings", type=str, default="encodings.pickle",help="path to serialized db of facial encodings")
	ap.add_argument("-d", "--detection-method", type=str, default="cnn",help="face detection model to use: either `hog` or `cnn`")
	args = vars(ap.parse_args())
	update_pickle(args)