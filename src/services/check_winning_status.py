from src.db.connection import cursor
from src.utils.lotto_rules import LottoRule


class CheckWinningStatus:
    """
    쿼리 문으로 데이터를 가져와서 비교헐때 같은 회차의 로또 번호만 가져오기
    """
    def __init__(self):
        self.draw_number = int(input("확인하실 회차 번호를 입력해주세요. : "))

    def get_purchase_numbers(self) -> list:
        cursor.execute(
            """
            SELECT number_1, number_2, number_3, number_4, number_5, number_6 FROM purchase_numbers WHERE draw_number = %s;
            """
        , self.draw_number)
        purchase_numbers = list(cursor.fetchone())
        return purchase_numbers

    def get_winning_numbers(self) -> list:
        cursor.execute(
            """
            SELECT number_1, number_2, number_3, number_4, number_5, number_6 FROM winning_numbers WHERE draw_number = %s;
            """
        , self.draw_number)
        winning_numbers = list(cursor.fetchone())
        return winning_numbers

    def get_bonus_numbers(self) -> int:
        cursor.execute(
            """
            SELECT bonus_number FROM winning_numbers WHERE draw_number = %s;
            """
        , self.draw_number)
        bonus_number = cursor.fetchone()
        return bonus_number

    def check_winning_status (self) :
        p = self.get_purchase_numbers()
        w = self.get_winning_numbers()
        b = self.get_bonus_numbers()

        lotto_check = LottoRule(w[0], w[1], w[2], w[3], w[4], w[5], p[0], p[1], p[2], p[3], p[4], p[5], b)

        if lotto_check.first_place():
            print(lotto_check.first_place())
        elif lotto_check.second_place():
            print(lotto_check.second_place())
        elif lotto_check.third_place():
            print(lotto_check.third_place())
        elif lotto_check.fourth_place():
            print(lotto_check.fourth_place())
        elif lotto_check.fifth_place():
            print(lotto_check.fifth_place())
        else:
            print("꽝입니다!")
