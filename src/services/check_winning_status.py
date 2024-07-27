from src.db.connection import cursor, connection
from src.utils.lotto_rules import LottoRule


class CheckWinningStatus:

    @staticmethod
    def get_purchase_numbers() -> list:
        cursor.execute(
            """
            SELECT number_1, number_2, number_3, number_4, number_5, number_6 FROM purchase_numbers 
            """
        )
        purchase_numbers = list(cursor.fetchone())
        return purchase_numbers

    @staticmethod
    def get_winning_numbers() -> list:
        cursor.execute(
            """
            SELECT number_1, number_2, number_3, number_4, number_5, number_6 FROM winning_numbers
            """
        )
        winning_numbers = list(cursor.fetchone())
        return winning_numbers

    @staticmethod
    def get_bonus_numbers() -> int:
        cursor.execute(
            """
            SELECT bonus_number FROM winning_numbers
            """
        )
        bonus_number = cursor.fetchone()
        return bonus_number

    @classmethod
    def check_winning_status (cls) :
        p = cls.get_purchase_numbers()
        w = cls.get_winning_numbers()
        b = cls.get_bonus_numbers()

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

