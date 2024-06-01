import pandas as pd
import numpy as np
from Levenshtein import distance as levenshtein_distance

class SimpleChatBot:
    # 챗봇 객체 초기화
    # filepath: 학습 데이터 파일의 경로
    def __init__(self, filepath):
        # 학습 데이터 로드
        self.questions, self.answers = self.load_data(filepath)

    # CSV 파일로부터 질문과 답변 로드
    # filepath: CSV 파일 경로
    def load_data(self, filepath):
        data = pd.read_csv(filepath)  # CSV 파일을 DataFrame으로 읽기
        questions = data['Q'].tolist()  # 질문 열을 리스트로 변환
        answers = data['A'].tolist()  # 답변 열을 리스트로 변환
        return questions, answers  # 질문과 답변 리스트 반환

    # 레벤슈타인 거리 계산
    # str1, str2: 비교할 두 문자열
    def calculate_levenshtein_distance(self, str1, str2):
        return levenshtein_distance(str1, str2)  # Levenshtein 거리 계산 후 반환

    # 입력 문장에 가장 유사한 답변 찾기
    # input_sentence: 사용자가 입력한 문장
    def find_best_answer(self, input_sentence):
        # 입력 문장과 학습 데이터의 모든 질문 간의 레벤슈타인 거리 계산
        distances = [self.calculate_levenshtein_distance(input_sentence, question) for question in self.questions]
        # 가장 작은 레벤슈타인 거리를 가진 질문의 인덱스 찾기
        best_match_index = np.argmin(distances)
        # 해당 인덱스의 답변 반환
        return self.answers[best_match_index]

# 데이터 파일 경로
filepath = 'ChatbotData.csv'

# 챗봇 객체 생성
chatbot = SimpleChatBot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프 실행
while True:
    input_sentence = input('You: ')  # 사용자 입력 받기
    if input_sentence.lower() == '종료':  # '종료' 입력 시 루프 종료
        break
    response = chatbot.find_best_answer(input_sentence)  # 입력 문장에 대한 응답 생성
    print('Chatbot:', response)  # 챗봇 응답 출력
