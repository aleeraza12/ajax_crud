from django.db import models

# Create your models here.
class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)




class Product(models.Model):
    product_name = models.CharField(max_length=30, blank=True)
    price = models.IntegerField(blank=True)
    category = models.CharField(max_length=30,blank=True, null=True)


class Tasks(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Books(models.Model):
    title = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    pdf = models.FileField(upload_to='upload_pdf/pdf/')
    cover_image = models.FileField(upload_to='upload_pdf/cover_image/',null=True, blank=True)

    def __str_(self):
        return self.title
