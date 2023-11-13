from django.shortcuts import render
#edit
from .models import Company
from .models import QnA, Question_Answer
from django.http import HttpResponse
from django.template import loader
from main.API import palm_api_ko ,palm_api_en
# 네이버 papago_api 번역
from main.papago_translate import *


user_input= ""
palm_answer=""
user_output2=""
def index(request):
    #edit

    print("첫페이지")
    return render(request, 'main/project.html')


def questions_ko(user_input):
    # bard_answer =  API.bard_api_qeustion(user_input)
    print()
    palm_answer = palm_api_ko(user_input)

    return palm_answer  #, bard_answer



def save_user_input(request):
    
    global user_input   # user_input 초기화
    global palm_answer
    global user_output2

    print("두번째페이지")
    
    print("API완료")
    if request.method == 'POST':
        user_input = request.POST.get('user_input')  # POST 요청에서 user_input 데이터 가져오기
        if user_input:

            print('유저 입력값:',user_input)
            # user_output = bard_api(user_input)
            user_output2='바드답안'
            palm_answer = palm_api_en(user_input)
            
            # print('출력값:',palm_answer)
            if palm_answer==None:
                print("답 없음!")
                palm_answer='답할 수 있는 범위를 벗어났어요.'

            return render(request, 'main/index.html', {'user_input': user_input,'user_output':palm_answer,'user_output2':user_output2})  # 사용자 입력을 context에 추가
    return render(request, 'main/index.html', { 'user_input': user_input, 'user_output':palm_answer,'user_output2':user_output2})  # POST 요청이 아닌 경우 또는 user_input이 없는 경우에 대한 응답
 
def save_user_output(request):

    global user_input
    global palm_answer
    global user_output2
    
    if request.method == 'POST':
        which=request.POST.get('answer')
        if which=='left':
            answer=palm_answer
        else:
            answer=user_output2
        if user_input:
            print("DB에 입력되었습니다. Q:",user_input,"\nA:",answer)
            # user_input을 데이터베이스에 저장하거나 다른 작업을 수행
            QA = Question_Answer(Question=user_input,Answer=answer)
            QA.save()
            
            
            return render(request, 'main/index2.html',{'user_input': user_input, 'user_output':answer})  # 사용자 입력을 context에 추가
    return render(request, 'main/index2.html', {'user_input': user_input,'user_output':answer})  # POST 요청이 아닌 경우 또는 user_input이 없는 경우에 대한 응답 


# 한국어 질문과 답변 (네이버 papago_api를 이용해 한국어 질문을 영어로 번역 후 palm에게 보내고 palm의 영어 답변을 한국어로 다시 번역)
