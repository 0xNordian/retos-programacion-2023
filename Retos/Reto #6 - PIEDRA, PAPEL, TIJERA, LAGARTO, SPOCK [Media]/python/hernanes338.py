# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */

def game_winner(rounds_list: list):
    
    emojis_dict = {"🗿":"rock", "📄":"paper", "✂️":"scissors", "🦎":"lizard", "🖖":"spock"}
    
    player_1_choices_list: list = []
    player_2_choices_list: list = []

    for round in rounds_list:
        player_1_choices_list.append(round[0])
        player_2_choices_list.append(round[1])
    
    winner = ''
    player_1_score: int = 0
    player_2_score: int = 0
    
    if len(player_1_choices_list) == len(player_2_choices_list):
    
        for i in range(len(player_1_choices_list)):
            player_1_choice = emojis_dict[player_1_choices_list[i]]
            player_2_choice = emojis_dict[player_2_choices_list[i]]
            
            if player_1_choice == player_2_choice:
                continue
            elif player_1_choice == "scissors" and player_2_choice == "paper" or "lizard":
                player_1_score += 1
    
    if player_1_score > player_2_score:
        winner = 'Player 1'
    elif player_1_score < player_2_score:
        winner = 'Player 2'
    else:
        winner = 'Tie'
    
    return winner
    
print(game_winner([("🗿","🗿")]))
    


# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
