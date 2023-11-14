import os
from openai import OpenAI

def initialize_openai_client(api_key):
    os.environ["OPENAI_API_KEY"] = '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'
    return openai.OpenAI()

def chat_gpt_answer(api_key, initial_messages=[]):
    client = initialize_openai_client(api_key)
    messages = initial_messages

    while True:
        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})

        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=messages,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        assistant_response = completion["choices"][0]["message"]["content"]
        print(f'ChatGPT: {assistant_response}')

        messages.append({"role": "assistant", "content": assistant_response})

        return assistant_response

if __name__ == "__main__":
    # 터미널에서 실행되는 코드
    chat_gpt_answer()