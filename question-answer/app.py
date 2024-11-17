from transformers import pipeline
import os

def question_answer(context, question):
    # 로컬 모델 경로
    local_model_path = os.path.expanduser("/app/model")
    
    # QA 파이프라인 초기화
    qa_pipeline = pipeline("question-answering", model=local_model_path, tokenizer=local_model_path, device_map="cpu")
    
    # 질문에 답변 생성
    answer = qa_pipeline(question=question, context=context)
    
    print(answer["answer"])
    return answer["answer"]

# 컨텍스트와 질문 입력
context = """ 
The quick brown fox jumps over the lazy dog. This sentence contains all the letters in the English alphabet.
"""
question = "What does the fox jump over?"

question_answer(context, question)
