# bard
from bardapi import Bard
import os
import bardapi

# palm
import pprint
import google.generativeai as palm

# 네이버 papago_api 번역
import main.papago_translate as pt


palm_api = 'AIzaSyAcRMOWVEDSxMqZwgc3nTzgDbDSCAG4Ap8'
bard_api = 'dAh_C6Op_pXCblErPTSBldRe5-9hEHFvzASbpp9xNcflZnUJ5N_o_Vd7k28zCf0cNQSQBg.'

def bard_api_qeustion(question : str):
    """
    Input
        1) question (str) :
            질문
    Print
        1) bard의 답변 중에 1번쨰 답변
    Output
        1) response['content'] :
            bard의 답변 중에 1번쨰 답변
    """
    os.environ['_BARD_API_KEY'] = bard_api
    bard = Bard()
    response = bard.get_answer(question)
    
    print("'bard'의 답변\n")
    print(response['content'])
    
    # return response['content']


def palm_api_en(question : str):
    """
    Input
        1) question (str) :
            영어 질문
    Print
        1) palm의 영어 답변
    Output
        1) response.last :
            palm의 영어 답변
    """
    palm.configure(api_key = palm_api)
    print('palm key == ok')
    response = palm.chat(messages = question)
    
    print("'palm'의 답변\n", response.last)
    
    return response.last


def palm_api_ko(question : str):
    """
    Input
        1) question (str) :
            한국어 질문
    Print
        1) palm의 영어 답변을 한국어로 번역한 답변
    Output
        1) response.last :
            palm의 영어 답변을 한국어로 번역한 답변
    """
    palm.configure(api_key = palm_api)
    print('palm key == ok \n question:',question)
    
    # 한국어 질문을 영어로 번역
    en_question=pt.translate_ko2en(question)
    if en_question == 0:
        return 'text 응답없음'
    print('english question:',en_question)
    response = palm.chat(messages = en_question)
    
    print("'palm'의 답변\n", response)
    # 영어 답변을 한국어로 번역
    ko_answer=pt.translate_en2ko(response.last)
    
    return ko_answer
