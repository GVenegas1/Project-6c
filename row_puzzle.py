
#Author:Gabriel Venegas
#Github:GVenegas1
# Feb 11, 2026
#Description:Tries to find a path to the zero at the end of the list.
#We move by jumping the exact number written on our current square.

def explore_path(game_squares, current_spot, path_history):
    """game_squares: the list of numbers we are playing on
    current_spot: the index where the token is currently sitting
    path_history: a set that remembers everywhere we have already stepped"""

    #Check if Won. You win if the index is the very last one on list.
    if current_spot == len(game_squares) - 1:
        return True

    #Check: If the jump landed at a negative index or past the end of the list.
    if current_spot < 0 or current_spot >= len(game_squares):
        return False

    # Check: If we have already stood on this square in this path and stop!
    if current_spot in path_history:
        return False

    # Moves: Record that we are visiting this spot right now
    path_history.add(current_spot)

    #Get the jump distance from the current square
    jump_value = game_squares[current_spot]

    #Jumping forward (Right) and adding jump_value to current index
    if explore_path(game_squares, current_spot + jump_value, path_history):
        return True

    #Jumping backward (Left) and subtract jump_value from our current index
    if explore_path(game_squares, current_spot - jump_value, path_history):
        return True

    #If neither jump led to a win,We remove it from our history so
    #other path attempts aren't blocked by it.
    path_history.remove(current_spot)

    return False


def row_puzzle(row_list):
    """This is the main function that starts the game.
    It kicks off the recursion at the first square (index 0)"""

    #Create an empty set to keep track of our 'path_history'
    visited_set = set()

    #Return the result
    return explore_path(row_list, 0, visited_set)


