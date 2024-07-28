from datetime import datetime


class SavePurchaseNumbersService:
    """
    Service to save winning numbers
    """
    @staticmethod
    def purchase_date() -> str:
        """
        구매 날짜 리턴
        :return: str
        """
        return str(datetime.now().date())

    @staticmethod
    def purchase_draw_number() -> int:
        """
        구매 회차 리턴
        :return: int
        """
        return int(input("구매하실 로또의 회차를 입력해주세요. : "))

    @staticmethod
    def purchase_lotto_number() -> list:
        """
        구매한 로또 리턴
        :return: list
        """
        return list(map(int, input("구매할 로또 번호를 입력해주세요. : ").split()))

