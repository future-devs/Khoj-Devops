from django.db import models
import pickle


# class Guardain(models.Model):
# 	name = models.CharField(max_length=100, null=True, blank=True)
# 	address = models.TextField(null=True, blank=True)
# 	contact = models.CharField(max_length=15, null=True, blank=True)
# 	email = models.EmailField(null=True, blank=True)
# 	addhar_card_number = models.CharField(max_length=12, null=True, blank=True)


class MissingPerson(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	gender = models.CharField(max_length=1, null=True, blank=True)
	lower_height_range = models.IntegerField(null=True,blank=True)
	upper_height_range = models.IntegerField(null=True,blank=True)
	body_built = models.TextField(null=True,blank=True)
	blood_group = models.TextField(null=True,blank=True)
	face_complexion = models.TextField(null=True, blank=True)
	face_shape = models.TextField(null=True, blank=True)
	addhar_card_number = models.CharField(max_length=12, primary_key=True)
	last_appearence_place = models.TextField(null=True, blank=True)


class MissingPersonImages(models.Model):
	addhar_card_number = models.ForeignKey(MissingPerson, on_delete=models.CASCADE, null=True, blank=True, name="addhar_card_number")
	image = models.FileField(null=True, blank=True)
	pickel = models.TextField(null=True, blank=True)



# category_number = models.IntegerField(null=True, blank=True)
# guardian = models.ForeignKey(Guardain, on_delete=models.CASCADE, null=True, blank=True)
