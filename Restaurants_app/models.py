from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    cuisine_type = models.CharField(max_length=100)
    average_rating= models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def update_avg_rating(self):
        # Calculate average rating from reviews
        reviews = self.review_set.all()
        if reviews.exists():
            self.average_rating = sum(review.rating for review in reviews) / reviews.count()
        else:
            self.average_rating = 0
        self.save()

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menus', on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.dish_name} - {self.restaurant.name}"
    
class User(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField(max_length=100)

    def __str__(self):
        return self.username

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])   #Rating from 1 to 5
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.restaurant.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        self.restaurant.update_avg_rating() #update the restaurant's avg rating after each review


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reservations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.restaurant.name} on {self.reservation_date}"