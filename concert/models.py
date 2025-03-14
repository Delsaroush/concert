from django.db import models

class Concert(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=150)
    available_tickets = models.IntegerField(default=0)  # Add a default value here

    def __str__(self):
        return self.name
class Ticket(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    purchaser_name = models.CharField(max_length=100)
    purchased_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.purchaser_name} - {self.concert.name}"


