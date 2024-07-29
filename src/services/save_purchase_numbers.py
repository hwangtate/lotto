from datetime import datetime


class SavePurchaseNumbersService:
    """
    서비스 폴더에 들어가야 적당한지 잘 모르겠음
    db 폴더도 나쁘지 않을 것 같긴 하지만 직접 사용자가 구매번호를 입력하는 거라
    서비스에 더 가까워 보임

    함수를 안 쓰고 스태틱 메소드를 사용한 이유는 좀 더 명확하게 구분을 짓기 위해 스태틱 메서드를 사용함
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

