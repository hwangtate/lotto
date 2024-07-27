from selenium import webdriver
from selenium.webdriver.common.by import By

draw_number = 1129
draw_date = '2024-07-27'

browser = webdriver.Chrome()
browser.get(f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={draw_number}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')

winning_numbers = browser.find_elements(By.CLASS_NAME, "ball")
winning_numbers = [int(winning_number.text) for winning_number in winning_numbers]
winning_numbers = winning_numbers[:-1]

bonus_number = int(browser.find_element(By.CLASS_NAME, "bonus_number").text)

# 이 크롤링 파일을 클래스로 만들어서 사용하고 싶어요 알려주세요. 많이 시도해보다가 잘 안됐어요
# class Crawler():
#
#     def __init__(self):
#         self.browser = browser = webdriver.Chrome()
#         self.browser.get(
#             f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={draw_number}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')
#
#     @staticmethod
#     def draw_number() -> int:
#         """
#         로또 회차 리턴
#         :return: int
#         """
#         return 1129
#
#     @staticmethod
#     def draw_date() -> str:
#         """
#         로또 번호 크롤링 날짜 리턴
#         :return: str
#         """
#         return '2024-07-27'
#
#     def winning_numbers(self) -> list:
#         """
#         로또 당첨 번호 리턴
#         :return: list
#         """
#         winning_numbers = self.browser.find_elements(By.CLASS_NAME, "ball")
#         winning_numbers = [int(winning_number.text) for winning_number in winning_numbers]
#         winning_numbers = winning_numbers[:-1]
#
#         return winning_numbers
#
#     @staticmethod
#     def bonus_number() -> int:
#         """
#         보너스 번호 리턴
#         """
#         bonus_number = int(browser.find_element(By.CLASS_NAME, "bonus_number").text)
#
#         return bonus_number