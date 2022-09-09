from django.db import models

# Create your models here.
priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
]


class Todo(models.Model):
 
    title=models.CharField(max_length=30)
    description=models.TextField()
    isDone=models.BooleanField(default=False)
    Priority=models.CharField(max_length=2,choices=priority_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title