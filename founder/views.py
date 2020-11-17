from django.shortcuts import render
from guardian.models import *
from core import recognize_faces_image
import os
from core import encode_faces
import boto3
import smtplib

# Create your views here.
def get_upload_found_person_image_form(request):
	return render(request, 'upload_found_person_image_form.html')


def upload_found_person_image_form(request):
	images = request.FILES.getlist('images')
	addhar_card_number = request.POST['addhar_card_number']
	try:
		os.mkdir("media/images/founder/" + str(addhar_card_number))
	except FileExistsError:
		pass

	files=[]
	file_num=0
	for image in images:
		extension=str(image).split(".")[-1]
		file_not_created=True
		while file_not_created:
			try:
				file_name = str(file_num)+"."+extension
				file_loc = "media/images/founder/"+str(addhar_card_number)+"/"+file_name
				with open(file_loc, 'wb+') as destination:
					destination.write(image.read())
				file_not_created=False
				files.append(file_name)
				file_num+=1
			except FileExistsError:
				file_num+=1
	# print(files)
	args= {'image' : "media/images/founder/" + str(addhar_card_number) + "/" +file_name}
	addhar_num,img_path=recognize_faces_image.recognize_person(args)
	# import pdb;pdb.set_trace()
	if addhar_num!="Unknown":
		missing_obj=MissingPerson.objects.get(addhar_card_number=addhar_num)
		person_name=missing_obj.name
		file=open("core/lost_and_found_db","a")
		
		# aadhar_number/place_of_last_appearence/latest_appearence
		file.write(addhar_num+"/"+missing_obj.last_appearence_place+"/"+request.POST['appearence_place']+"\n")
		file.close()
		message = "Lost person "+person_name+"("+addhar_num+") has been found at "+request.POST['appearence_place']
		
		# # Sending Text Message
		try:
			client = boto3.client('sns',region_name='us-east-1')
			status=client.publish(
				PhoneNumber="+917727906300",
				Message=message
			)
			print("Successfully sent message")
		except:
			print("Error: unable to send message")
		# print(status)

		# # Sending Email Notification
		
		try:
			sender = 'kaushal.bhansali6@gmail.com'
			receiver = 'kaushal.bhansali2@gmail.com'
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.login(sender,os.getenv("mail_key"))
			message = """Subject: Missing person found!


			Lost person Named :{} with Aadhar Number :({}) has been found at {}
			""".format(person_name,addhar_num,request.POST['appearence_place'])
			server.sendmail(sender,receiver,message)
			print("Successfully sent email")
		except:
			print("Error: unable to send email")


		status="Found"
		msg="Nearest Police Station Has Been Notified!"
	else:
		person_name="Unknown"
		status="Not Found!"
		msg=""
	return render(request, 'base.html',{'name': person_name,'status' : status,'img_path' : img_path, 'msg': msg})