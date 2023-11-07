from django.shortcuts import render
#edit
from .models import Company
from .models import QnA
from django.http import HttpResponse

def index(request):
    #edit
    company_list = Company.objects.all()		# Company 모델에 있는 정보를 전부 가져온다.
    context = {'company_list': company_list}	# company_list의 정보를 context에 담는다.
 
    return render(request, 'main/project.html', context)

def save_user_input(request):
    company_list = Company.objects.all()		# Company 모델에 있는 정보를 전부 가져온다.
    context = {'company_list': company_list}
    if request.method == 'POST':
        user_input = request.POST.get('user_input')  # POST 요청에서 user_input 데이터 가져오기
        if user_input:
            # user_input을 데이터베이스에 저장하거나 다른 작업을 수행
            new_qna = QnA(question=user_input)
            new_qna.save()
            return render(request, 'main/index.html', context) # 저장 완료 메시지 또는 다른 응답 반환

    return HttpResponse("Invalid request")  # POST 요청이 아닌 경우 또는 user_input이 없는 경우에 대한 응답 
