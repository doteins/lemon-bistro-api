from django.db import models

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True, null=False)
   inventory = models.IntegerField()
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name

class Booking(models.Model):
    name = models.CharField(max_length=200)
    guests_number = model.SmallIntegerField(default=1)
    reservation_date = models.DateField()
    # reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return f'{self.title} : {str(self.price)}'
