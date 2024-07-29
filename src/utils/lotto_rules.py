class LottoRule:

    def __init__(self, win_num_1, win_num_2, win_num_3, win_num_4, win_num_5, win_num_6, pur_num_1, pur_num_2, pur_num_3, pur_num_4, pur_num_5, pur_num_6, bonus_num):
        """
        :param win_num_1 ~ win_num_6: 로또 당첨 번호
        :param pur_num_1 ~ pur_num_6: 구매 로또 번호
        """
        self.winning_number_list = [win_num_1, win_num_2, win_num_3, win_num_4, win_num_5, win_num_6]
        self.purchase_number_list = [pur_num_1, pur_num_2, pur_num_3, pur_num_4, pur_num_5, pur_num_6]
        self.bonus_num = bonus_num[0]

    def first_place(self) -> str | None:
        """
        로또 1등 당첨 기준(6개번호 맞취기)
        :return: str | None
        """
        if len(set(self.winning_number_list) & set(self.purchase_number_list)) == 6:
            return "1등입니다!"

    def second_place(self) -> str:
        """
        로또 2등 당첨 기준
        :return: str
        """

        if len(set(self.winning_number_list) & set(self.purchase_number_list)) == 5:
            for i in self.purchase_number_list:
                if i == self.bonus_num:
                    return "2등입니다!"
                else:
                    continue

    def third_place(self) -> str:
        """
        로또 3등 당첨 기준
        :return: str
        """

        if len(set(self.winning_number_list) & set(self.purchase_number_list)) == 5:
            return "3등입니다!!!!!!!!"


    def fourth_place(self) -> str:
        """
        로똥 4등 당첨 기준
        :return: str
        """
        if len(set(self.winning_number_list) & set(self.purchase_number_list)) == 4:
            return "4등입니다!"

    def fifth_place(self) -> str:
        """
        로또 5등 당첨 기준
        :return: str
        """
        if len(set(self.winning_number_list) & set(self.purchase_number_list)) == 3:
            return "5등입니다!"
