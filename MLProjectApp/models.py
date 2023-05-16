from django.db import models
from django import forms

# Steps after creating models ->
# 1. Run migrations
# 2. Do migrate

# makemigrations - create changes and store in a file
# migrate - apply the pending changes by makemigrations -> write the changes in the DB

# Model defines your database
TYPE_CHOICES= (
    ('Feedback', 'Feedback'),
    ('Query', 'Query')
)

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    type_choice = models.CharField(max_length=10, choices=TYPE_CHOICES)
    # type_choice = forms.CharField(label='Type of Message', widget=forms.RadioSelect(choices=TYPE_CHOICES))
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

# python manage.py makemigrations -> Creates a file of whatever the changes that is made in the models.py file.
# To reflect the changes two things need to do ->
# 1. Register the model in 'admin.py'
# 2. Register the app / appname from 'apps.py' in home to 'settings.py' in project
# 3. Then run the migrations

# Note: No table has been created in the Django database after running the migration command. To create the tables in the Django database we need to run the migrate command.