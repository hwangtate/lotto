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
        return '2024-07-27'

    @staticmethod
    def purchase_draw_number() -> int:
        """
        구매 회차 리턴
        :return: int
        """
        return 1129

    @staticmethod
    def purchase_lotto_number() -> list:
        """
        구매한 로또 리턴
        :return: list
        """
        return [5, 10, 11, 17, 21, 22]
