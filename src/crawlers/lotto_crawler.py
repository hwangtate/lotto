from selenium import webdriver
from selenium.webdriver.common.by import By

class Crawler():

    @staticmethod
    def draw_number() -> int:
        """
        로또 회차 리턴
        :return: int
        """
        return 1129

    @staticmethod
    def draw_date() -> str:
        """
        로또 번호 크롤링 날짜 리턴
        :return:
        """
        return 2024


draw_number = 1129
draw_date = '2024-07-27'

browser = webdriver.Chrome()
browser.get(f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={draw_number}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8')

winning_numbers = browser.find_elements(By.CLASS_NAME, "ball")
winning_numbers = [int(winning_number.text) for winning_number in winning_numbers]
winning_numbers = winning_numbers[:-1]

bonus_number = int(browser.find_element(By.CLASS_NAME, "bonus_number").text)
