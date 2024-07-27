from db.queries import insert_db_purchase_lotto_numbers, insert_db_lotto_numbers
#이 로또 크롤링 파일이 로또 크롤링 파일을 불러만 와도 크롤링 하게 되어있어서 클래스 또는 함수로 묶어줘야함
from services.check_winning_status import CheckWinningStatus


def insert_lotto_data() -> None:
    """
    로또 당청번호를 크롤링하여 데이터베이스에 추가합니다.
    이 함수는 한 번만 실행이 가능합니다. (추가로 실행시 오류)
    :return: None
    """
    insert_db_lotto_numbers()


def insert_lotto_purchase_data() -> None:
    """
    구매한 로또 번호를 입력하여 데이터베이스에 추가합니다.
    :return: None
    """
    insert_db_purchase_lotto_numbers()


def check_lotto() -> None:
    """
    구매한 로또 번호를 몇등인지 확인합니다.
    :return: None
    """
    CheckWinningStatus.check_winning_status()


if __name__ == '__main__':
    insert_lotto_data()
    insert_lotto_purchase_data()
    check_lotto()