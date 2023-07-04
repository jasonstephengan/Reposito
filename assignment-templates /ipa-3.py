#!/usr/bin/env python
# coding: utf-8

# In[60]:


from_member = input("username: ")
to_member = input("username: ")
social_graph = {
    "@JLuuuu":{"first_name":"Joshua",
                  "last_name":"Lu",
                  "following":["@the.james.ang,", "@jasongan"
                  ]
    },
    "@the.james.ang":  {"first_name":"James",
                  "last_name":"Ang",
                  "following":[
                      "@jasongan","@JLuuuu", "@eugene_B", "@willeh"
                  ]
    },
    "@jasongan" : {"first_name":"Jason",
                "last_name":"Gan",
                "following":[
                    "@JLuuuu","@eugene_B"
                ]
    },
    "@eugene_B" : {"first_name":"Eugene",
                "last_name":"Briones",
                "following":[
                    "@the.james.ang", "@willeh"
                ]
                 },

   "@willeh" : {"first_name":"Willie",
                "last_name":"Yu",
                "following":[
                    
                ]
               },
                        
}
def relationship_status(from_member, to_member, social_graph):
#follower test
    if from_member in social_graph:
        value = social_graph[from_member]
        follow_list = value["following"]
        if to_member in follow_list:

        #friends test
            if to_member in social_graph:
                value2 = social_graph[to_member]
                follow_list2 = value2["following"]
                if from_member in follow_list2:
                    return "friends"
                else:
                    return "follower"
    
                
#followed by test
        elif to_member in social_graph:
            value2 = social_graph[to_member]
            follow_list2 = value2["following"]
            if from_member in follow_list2:
                return "followed by"
        
#no relation
            else:
                return "no relationship"

#print outcomes        
result = relationship_status(from_member, to_member, social_graph)

if result == "friends":
    print(from_member, "and", to_member,"are friends")

elif result == "follower":
    print(from_member, "is a follower of", to_member)

elif result == "followed by":
    print(from_member, "is followed by", to_member)

elif result == "no relationship":
    print("There is no relationship between", from_member, "and", to_member)

    
    


# In[7]:


board = [
['X', 'O', 'X', 'O', 'O'],
['O', 'X', 'O', 'O', 'X'],
['X', 'X', 'X', 'O', 'O'],
['X', 'O', 'X', 'X', 'O'],
['O', 'X', 'O', 'O', 'X'], 
        ]


def tic_tac_toe(board):
#horizontal win
    for a in range(len(board)):
        row = []
        for b in range(len(board)):
            row.append(board[a][b])
        if row.count('O') == len(row):
            return "O"
        elif row.count('X') == len(row):
            return "X"

#vertical win
    for c in range(len(board)):
        column = []
        for d in range(len(board)):
            column.append(board[d][c])
        if column.count('O') == len(column):
            return "O"
        elif column.count('X') == len(column):
            return "X"

#left diagonal win 
    diagonal = []
    for e in range(len(board)):
        diagonal.append(board[e][e])
    if diagonal.count('O') == len(diagonal):
        return "O Win"
    elif diagonal.count('X') == len(diagonal):
            return "X"

#right diagonal win 
    diagonal2 = []
    for f in range(len(board)):
        diagonal2.append(board[f][-f-1])
    if diagonal2.count('O') == len(diagonal2):
        return "O"
    elif diagonal2.count('X') == len(diagonal2):
        return "X"
    else:
        return "NO WINNER"

            
winner = tic_tac_toe(board)

if winner == "X":
    print("X")

elif winner == "O":
    print("O")
    
elif winner == "NO WINNER":
    print("NO WINNER")


# In[126]:


route_map = {
    ("Place A", "Place B"): {
        "travel_time_mins": 10
    },
    ("Place B", "Place C"): {
        "travel_time_mins": 35
    },
    ("Place C", "Place D"): {
        "travel_time_mins": 55
    }, 
    ("Place D", "Place A"): {
        "travel_time_mins": 15
    }
}
first_stop = "Place D"
last_stop = "Place B"

def eta(first_stop, second_stop, route_map):
    traveltime = 0
    x = 0
    mylist = list(route_map.items())
    from_stop = mylist[x][0][0]

# Identify the first stop
    while first_stop != from_stop:
        x += 1
        from_stop = mylist[x][0][0]
#second stop
    to_stop = mylist[x][0][1]

#add distances then loop the stops
    while True:
        traveltime += route_map[(from_stop, to_stop)]["travel_time_mins"]
        if to_stop == last_stop:
            break
        else:
            x += 1
            if x >= len(mylist):
                x = 0
            from_stop = to_stop
            to_stop = mylist[x][0][1]
    return traveltime

traveltime = eta(first_stop, second_stop, route_map)
print(traveltime)

