from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from src.utils.webdriver import *

def draw():
    draw_number = int(input("크롤링 하실 회차 번호를 입력해주세요. : "))
    draw_date = datetime.now().date()
    return draw_number, draw_date

class Crawler:

    def __init__(self):
        self.d = draw()
        self.browser = browser = webdriver.Chrome()
        self.browser.get(
            f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={self.d[0]}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')

    def winning_numbers(self) -> list:
        """
        로또 당첨 번호 리턴
        :return: list
        """
        winning_numbers = self.browser.find_elements(By.CLASS_NAME, "ball")
        winning_numbers = [int(winning_number.text) for winning_number in winning_numbers]
        winning_numbers = winning_numbers[:-1]

        return winning_numbers

    def bonus_number(self) -> int:
        """
        보너스 번호 리턴
        :return: int
        """
        bonus_number = int(self.browser.find_element(By.CLASS_NAME, "bonus_number").text)

        return bonus_number

