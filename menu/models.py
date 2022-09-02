from django.db import models

# Create your models here.

class Dish(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    pic=models.ImageField(upload_to='menu/Dish')
    con=models.TextField()

    def __str__(self):
        return f"{self.name}__{self.price}"
    
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/No_image.png"

class Drink(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    pic=models.ImageField(upload_to='menu/Drink')
    con=models.TextField()

    def __str__(self):
        return f"{self.name}__{self.price}"
    
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/No_image.png"

class Pasta(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    pic=models.ImageField(upload_to='menu/Pasta')
    con=models.TextField()

    def __str__(self):
        return f"{self.name}__{self.price}"
    
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/No_image.png"

class Risotto(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    pic=models.ImageField(upload_to='menu/Risotto')
    con=models.TextField()

    def __str__(self):
        return f"{self.name}__{self.price}"
    
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/No_image.png"
