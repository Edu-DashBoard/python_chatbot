from django.db import models
 
# Create your models here.
 
class Company(models.Model):
    code = models.CharField(max_length=20, primary_key= True)
    company = models.CharField(max_length=40)
    last_update = models.DateField()
 
    def __str__(self):
        return self.company

class QnA(models.Model):
    question = models.CharField(max_length=20, primary_key= True)
    
    def save_user_input(user_input):
        new_qna = QnA(question=user_input)
        new_qna.save()


    
