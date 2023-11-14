# bard
from bardapi import Bard
import os
import bardapi
import openai

# palm
import pprint
import google.generativeai as palm

# 네이버 papago_api 번역
import main.papago_translate as pt

OPENAI_API_KEY = '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'
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
    response = palm.chat(messages = question)
    
    print("'palm'의 답변\n")
    print(response.last)
    
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
    
    # 한국어 질문을 영어로 번역
    aaa=pt.translate_ko2en(question)
    if aaa == 0:
        return 'text 응답없음'
    print('aaa',aaa)
    response = palm.chat(messages = aaa)
    
    print("'palm'의 답변\n", response)
    # 영어 답변을 한국어로 번역
    print(pt.translate_en2ko(response.last))
    
    return pt.translate_en2ko(response.last)


def chat_gpt_answer(question : str):
    """
    Input
        1) question (str) :
            질문
    Print
        1) OpenAI의 답변
    Output
        1) answer :
            OpenAI의 답변
    """
    # OpenAI API 키 설정
    
    openai.api_key = ""
    
    # OpenAI API에 요청 보내기
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150 # 최대 답변 글자수
    )
    
    # API 응답에서 답변 추출
    answer = response['choices'][0]['text'].strip()
    
    print("'OpenAI'의 답변\n")
    print(answer)
    