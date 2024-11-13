class Player:
    def pon(self, hand, round_number):
        while True:
            try:
                print(f"----- ラウンド {round_number} -----")
                player_hand = int(input("1.グー 2.チョキ 3.パー\nあなたの手を選択してください。> "))
                if player_hand in hand:
                    return player_hand
                else:
                    print("グー、チョキ、パーのいずれかを入力してください")
            except ValueError:
                print("グー、チョキ、パーのいずれかを入力してください")