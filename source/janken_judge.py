def judge(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "引き分け"
    elif (player_hand == 1 and computer_hand == 2) or \
         (player_hand == 2 and computer_hand == 3) or \
         (player_hand == 3 and computer_hand == 1):
        return "あなたの勝ちです！"
    else:
        return "コンピューターの勝ちです！"