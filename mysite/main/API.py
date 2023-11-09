# bard
from bardapi import Bard
import os
import bardapi

# palm
import pprint
import google.generativeai as palm

# 네이버 papago_api 번역
import papago_translate as pt

# api_keys
from tokens import APIS

# def questions_ko(question):
#     bard_api(question)
#     print()
#     result = palm_api_ko(question)
#     return result



# if __name__ == '__main__':
#     print(questions_ko('파이썬이 뭐야'))





def bard_api(question : str):
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
    os.environ['_BARD_API_KEY'] = APIS['bard_api']
    bard = Bard()
    response = bard.get_answer(question)
    
    # print("'bard'의 답변\n")
    # print(response['content'])
    
    return response['content']  # 바드 결과값 



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
    palm.configure(api_key = APIS['palm_api'])
    
    # 한국어 질문을 영어로 번역
    response = palm.chat(messages = pt.translate_ko2en(question))
    
    # print("'palm'의 답변\n")
     # 영어 답변을 한국어로 번역
    # print(pt.translate_en2ko(response.last))
    
    return pt.translate_en2ko(response.last)    # palm 결과값 
