'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        answer = 'friends'
    elif to_member in social_graph[from_member]['following']:
        answer = 'follower'
    elif from_member in social_graph[to_member]['following']:
        answer = 'followed by'
    else:
        answer = 'no relationship'
    
    return answer


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)

    for i in range(size):
        row = board[i]
        column = [board[j][i] for j in range(size)]
        if len(set(row)) == 1 and row[0] != '':
            return row[0]
        if len(set(column)) == 1 and column[0] != '':
            return column[0]

    diagonal1 = [board[i][i] for i in range(size)]
    diagonal2 = [board[i][size - i - 1] for i in range(size)]
    if len(set(diagonal1)) == 1 and diagonal1[0] != '':
        return diagonal1[0]
    if len(set(diagonal2)) == 1 and diagonal2[0] != '':
        return diagonal2[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    list_of_keys = list(route_map.keys())
    first_keys = [item[0] for item in list_of_keys]
    second_keys = [item[1] for item in list_of_keys]
    new_time = list(route_map.values())
    answer = []
    final = []
    
    first_position = first_keys.index(first_stop)
    second_position = second_keys.index(second_stop)
        
    for x in range(len(new_time)):
            answer = answer + list(new_time[x].values())
    
    if first_stop == second_stop:
        return sum(answer)
    elif first_position == second_position:
        return answer[first_position]
    elif first_position < second_position:
        final = answer[first_position : second_position + 1]
        return sum(final)
    elif first_position > second_position:
        final = answer[first_position:] + answer[:second_position + 1]
        return sum(final)
