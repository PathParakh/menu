from django.db import models

class dish(models.Model):
    id = models.AutoField(primary_key=True)      
    dish_id = models.IntegerField(null=True)
    dish_name = models.CharField(max_length=255, blank=True, null=True)
    dish_category = models.CharField(max_length=255, blank=True, null=True)
    dish_size_large = models.CharField(max_length=255)
    dish_size_large_price = models.CharField(max_length=255, blank=True, null=True)
    dish_size_regular = models.CharField(max_length=255)
    dish_size_regular_price = models.CharField(max_length=255, blank=True, null=True)
    dish_size_small = models.CharField(max_length=255)
    dish_size_small_price = models.CharField(max_length=255, blank=True, null=True)
    dish_image = models.ImageField(upload_to='media')
    dish_description = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.dish_name

class owner(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class group(models.Model):
    id = models.AutoField
    dish_category = models.CharField(max_length=255)

    def __str__(self):
        return self.dish_category