#from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
#fs = FileSystemStorage(location='/media/pdf/')
class Book(models.Model):
	b_id=models.AutoField
	book_name = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	category=models.CharField(max_length=50, default="")
	pdf = models.FileField(upload_to="books/pdf", default="")
	date =  models.DateField()
	image=models.ImageField(upload_to="books/images",default="")

	def __str__(self):
		return self.book_name
