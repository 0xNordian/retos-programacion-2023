# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

# Scissors cuts paper
# Scissors decapitates lizard
# Paper covers rock
# Paper disproves Spock
# Rock crushes lizard
# Rock crushes scissors
# Lizard poisons Spock
# Lizard eats paper
# Spock smashes scissors
# Spock vaporizes rock

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
                
            elif player_1_choice == "scissors" and (player_2_choice == "paper" or player_2_choice == "lizard"):
                player_1_score += 1
            elif player_1_choice == "paper" and (player_2_choice == "rock" or player_2_choice == "spock"):
                player_1_score += 1
            elif player_1_choice == "rock" and (player_2_choice == "lizard" or player_2_choice == "scissors"):
                player_1_score += 1
            elif player_1_choice == "lizard" and (player_2_choice == "spock" or player_2_choice == "paper"):
                player_1_score += 1
            elif player_1_choice == "spock" and (player_2_choice == "scissors" or player_2_choice == "rock"):
                player_1_score += 1
            else:
                player_2_score += 1
    
    if player_1_score > player_2_score:
        winner = 'Player 1'
    elif player_1_score < player_2_score:
        winner = 'Player 2'
    else:
        winner = 'Tie'
    
    return winner
    
print(game_winner([("🗿","📄"), ("✂️","🗿"), ("🖖","✂️")]))
