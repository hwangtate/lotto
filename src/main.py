from db.queries import insert_db_purchase_lotto_numbers, insert_db_lotto_numbers
from db.queries import truncate_db_lotto_numbers, truncate_db_purchase_numbers
from services.check_winning_status import CheckWinningStatus

if __name__ == '__main__':
    insert_db_lotto_numbers()  # 로또 번호를 크롤링 하여 데이터에베이스에 저장합니다(중복 X)
    insert_db_purchase_lotto_numbers()  # 구매한 로또 번호를 입력하여 데이터베이스에 저장합니다(중복 O)

    c = CheckWinningStatus()  # 인스턴스화
    c.check_winning_status()  # 몇등에 당첨이 됐는지 확인합니다.

    truncate_db_purchase_numbers()  # 데이터베이스의 구매한 로또 번호를 전체 삭제합니다.
    truncate_db_lotto_numbers()  # 데이터베이스의 크롤링한 로또 번호를 전체 삭제합니다.
