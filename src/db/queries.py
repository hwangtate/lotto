from connection import cursor, connection
from src.crawlers.lotto_crawler import draw_date, winning_numbers, bonus_number, draw_number
from src.services.save_winning_numbers import SaveWinningNumbersService

def insert_db_lotto_numbers() -> None:
    """
    Insert lotto numbers into database
    :return: None
    """
    cursor.execute(
        """
        INSERT INTO winning_numbers(draw_date, draw_number, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (draw_date, draw_number, winning_numbers[0], winning_numbers[1], winning_numbers[2], winning_numbers[3],
         winning_numbers[4], winning_numbers[5], bonus_number)
    )
    connection.commit()


def insert_db_purchase_lotto_numbers() -> None:
    """
    Insert purchase lotto numbers into database
    :return: None
    """
    cursor.execute(
        """
        INSERT INTO purchase_numbers(purchase_date, draw_number, number_1, number_2, number_3, number_4, number_5, number_6)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (SaveWinningNumbersService.purchase_date(), SaveWinningNumbersService.purchase_draw_number(),
         SaveWinningNumbersService.purchase_lotto_number()[0], SaveWinningNumbersService.purchase_lotto_number()[1],
         SaveWinningNumbersService.purchase_lotto_number()[2], SaveWinningNumbersService.purchase_lotto_number()[3],
         SaveWinningNumbersService.purchase_lotto_number()[4], SaveWinningNumbersService.purchase_lotto_number()[5])
    )
    connection.commit()
