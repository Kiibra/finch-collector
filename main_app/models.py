from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples 
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Add the Toy model
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toy-detail', kwargs={'pk': self.id})

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  # Add the M:M relationship
  toys = models.ManyToManyField(Toy)
  # Add the foreign key linking to a user instance
  user = models.ForeignKey(User, on_delete=models.CASCADE)

	# new code below
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('finch-detail', kwargs={'finch_id': self.id})
  # add this new method
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  
# Add new Feeding model below Finch model
class Feeding(models.Model):
  # the first optional positional argument overrides the label
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

  # Create a finch_id column in the database
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    # method for obtaining the value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']