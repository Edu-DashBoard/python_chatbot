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

class Question_Answer(models.Model):
    ID = models.AutoField(primary_key= True, auto_created=True) 
    user_key = models.CharField(max_length=200, null=True)
    Question = models.CharField(max_length=1000,default='질문') # 질문(필수)
    Answer = models.CharField(max_length=200,default='답변') # 답변(필수)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_accepted=models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    Keywords = models.CharField(max_length=200, null=True)
    Date = models.DateTimeField(auto_now_add=True, null=True)
    Links = models.CharField(max_length=200, null=True)
    
