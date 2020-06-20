from django.db import models
# Create your models here.
class Shoes(models.Model):
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	price1 = models.CharField(max_length=20)
	status =models.BooleanField(default=False)
	category=models.CharField(max_length=50)
	def __str__(self):
		return self.name
	

class SingleShoes(models.Model):
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	img2 = models.ImageField(upload_to='pics')
	img3= models.ImageField(upload_to='pics')
	price1 = models.CharField(max_length=20)
	sole=models.CharField(max_length=20)
	closure=models.CharField(max_length=20)
	materialtype=models.CharField(max_length=20)
	lifestyle=models.CharField(max_length=20)

	def __str__(self):
		return self.name
	
class Orders(models.Model):
		item_json=models.CharField(max_length=5000)
		username=models.CharField(max_length=100)
		password=models.CharField(max_length=100)
		address1=models.CharField(max_length=100)
		address2=models.CharField(max_length=100)
		city=models.CharField(max_length=30)
		state=models.CharField(max_length=30)
		zipcode=models.CharField(max_length=30)
		phone=models.CharField(max_length=15)

class OrderUpdate(models.Model):
	order_id =models.IntegerField(default="")
	update_desc=models.CharField(max_length=5000)
	timestamp=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.update_desc[0:8]+"..."
	
