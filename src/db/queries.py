from src.db.connection import cursor, connection
from src.crawlers.lotto_crawler import Crawler, draw
from src.services.save_purchase_numbers import SavePurchaseNumbersService


def insert_db_lotto_numbers() -> None:
    """
    Insert lotto numbers into database
    :return: None
    """
    c = Crawler()


    cursor.execute(
        """
        INSERT INTO winning_numbers(draw_date, draw_number, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (c.d[1], c.d[0], c.winning_numbers()[0], c.winning_numbers()[1], c.winning_numbers()[2], c.winning_numbers()[3],
         c.winning_numbers()[4], c.winning_numbers()[5], c.bonus_number())
    )

    connection.commit()


def insert_db_purchase_lotto_numbers() -> None:
    """
    Insert purchase lotto numbers into database
    :return: None
    """
    s = SavePurchaseNumbersService()
    spd = SavePurchaseNumbersService().purchase_draw_number()
    sp = SavePurchaseNumbersService().purchase_lotto_number()

    cursor.execute(
        """
        INSERT INTO purchase_numbers(purchase_date, draw_number, number_1, number_2, number_3, number_4, number_5, number_6)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (s.purchase_date(), spd,
         sp[0], sp[1],
         sp[2], sp[3],
         sp[4], sp[5])
    )

    connection.commit()


def truncate_db_lotto_numbers() -> None:
    """
    Insert lotto numbers into database
    :return: None
    """
    cursor.execute(
        """
        TRUNCATE TABLE winning_numbers
        """
    )
    print("크롤링 하신 로또 번호 데이터를 삭제합니다.")
    connection.commit()


def truncate_db_purchase_numbers() -> None:
    """
    Insert lotto numbers into database
    :return: None
    """
    cursor.execute(
        """
        TRUNCATE TABLE purchase_numbers
        """
    )
    print("구매하신 로또 번호 데이터를 삭제합니다.")
    connection.commit()
