from django.db import models

class Menu(models.Model):
	name = models.CharField(max_length=200) 
	price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True, null=False)
	inventory = models.IntegerField()
	menu_item_description = models.TextField(max_length=1000, default='')

	# Change the table's name
	# class Meta:
	# 	db_table = 'Menu'

	def __str__(self):
		return f'{self.name} : {str(self.price)}'

class Booking(models.Model):
	name = models.CharField(max_length=200)
	guests_number = models.SmallIntegerField(default=1)
	reservation_date = models.DateField()

	# Change the table's name
	# class Meta:
	# 	db_table = 'Booking'

	def __str__(self) -> str:
		return self.name
