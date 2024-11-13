from player import Player
from computer import Computer
from janken_judge import judge

i = {1: "グー", 2: "チョキ", 3: "パー"}
hand = tuple(i.keys())

player = Player()
computer = Computer()

player_wins = 0
computer_wins = 0

for game_count in range(3):

    player_hand = player.pon(hand, game_count + 1)  
    computer_hand = computer.pon(hand)

    print(f"あなたの手: {i[player_hand]}")
    print(f"コンピュータの手: {i[computer_hand]}")

    result = judge(player_hand, computer_hand)
    print(result)
    
    if result == "あなたの勝ちです！":
        player_wins += 1
    elif result == "コンピューターの勝ちです！":
        computer_wins += 1

print("\n【最終結果】")
print(f"あなた: {player_wins}勝")
print(f"コンピュータ: {computer_wins}勝")

if player_wins > computer_wins:
    print("あなたの総合勝利です！")
elif computer_wins > player_wins:
    print("コンピュータの総合勝利です！")
else:
    print("引き分けです！")