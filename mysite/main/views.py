from django.shortcuts import render
#edit
from .models import Company
from .models import QnA, Question_Answer
from django.http import HttpResponse
from django.template import loader
from API import *

user_input= ""
def index(request):
    #edit
    company_list = Company.objects.all()		# Company 모델에 있는 정보를 전부 가져온다.
    context = {'company_list': company_list}	# company_list의 정보를 context에 담는다.
 
    return render(request, 'main/project.html', context)

def save_user_input(request):
    company_list = Company.objects.all()  # Company 모델에 있는 정보를 전부 가져옵니다.
    context = {'company_list': company_list}
    global user_input   # user_input 초기화
    user_output = bard_api(user_input)
    user_output2 = palm_api_ko(user_input)
    if request.method == 'POST':
        user_input = request.POST.get('user_input')  # POST 요청에서 user_input 데이터 가져오기
        if user_input:
            
            return render(request, 'main/index.html', {'context': context, 'user_input': user_input,'user_output':user_output,'user_output2':user_output2})  # 사용자 입력을 context에 추가
    return render(request, 'main/index.html', {'context': context, 'user_input': user_input, 'user_output':user_output,'user_output2':user_output2})  # POST 요청이 아닌 경우 또는 user_input이 없는 경우에 대한 응답
 
def save_user_output(request):
    company_list = Company.objects.all()  # Company 모델에 있는 정보를 전부 가져옵니다.
    context = {'company_list': company_list}
    global user_input
   

    if request.method == 'POST':
        
        if user_input:
            # user_input을 데이터베이스에 저장하거나 다른 작업을 수행
            QA = Question_Answer(Question=user_input)
            QA.save()
            return render(request, 'main/index2.html', context={'context': context, 'user_input': user_input})  # 사용자 입력을 context에 추가
    return render(request, 'main/index2.html', {'context': context, 'user_input': user_input})  # POST 요청이 아닌 경우 또는 user_input이 없는 경우에 대한 응답 

def load_data(request,context):
    print(context['user_input'])
    qa = Question_Answer.objects.filter(Question=context['user_input']) # 검색
    print(qa)
    template = loader.get_template('main/index.html')
    context["qa"] = qa # 화면에 보여줄 요소 추가
    return HttpResponse(template.render(context,request))# 화면상에 보인다.

