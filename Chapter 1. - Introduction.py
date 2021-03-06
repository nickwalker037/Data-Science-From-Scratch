users = [
  { "id": 0, "name": "Hero" },
  { "id": 1, "name": "Dunn" },
  { "id": 2, "name": "Sue" },
  { "id": 3, "name": "Chi" },
  { "id": 4, "name": "Thor" },
  { "id": 5, "name": "Clive" },
  { "id": 6, "name": "Hicks" }, 
  { "id": 7, "name": "Devin" },
  { "id": 8, "name": "Kate" },
  { "id": 9, "name": "Klein" },
  ]
  
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# Adding a list of friends to each user

for user in users:
  user["friends"] = []

# Then populate the lists using the friendships data:

for i, j in friendships:
    # this works b/c users[i] is the user whose id is "i"
    users[i]["friends"].append(users[j])                # add i as a friend of j
    users[j]["friends"].append(users[i])                # add j as a friend of i

# So to ask "What's the average number of connections?" we...
# 1. find the total number of connections, by summing up the lengths of all the friends lists:

def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"])                         # length of friend_ids list

total_connections = sum(number_of_friends(user)
                        for user in users)              # 24

# 2. then we just divide by the number of users

num_users = len(users)                                  # length of the users list
avg_connections = total_connections / num_users         # 2.4

print("Average number of connections:", avg_connections)# confirmed 2.4

# sorting users from "most friends" to "least friends"

# create a list (user_id_, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

#sorted(num_friends_by_id,                               # get it sorted
#       key=lambda (user_id, num_friends): num_friends,  # by num_friends ------- syntax error on this line, so it is commented out for now
#       reverse=True)                                    # largest to smallest

print("Number of Friends by ID:", num_friends_by_id)


# ------ "Data Scientists You May Know!" ----- #


def friends_of_friends_ids_bad(user):                   
  return[foaf["id"]                                     # note: foaf is short for "friend of a friend"
         for friend in user["friends"]                  # for each of user's friends
         for foaf in friend["friends"]]                 # for each of _their_ friends

print (friend["id"] for friend in users[0]["friends"])  # need to check code on this line as well 

#code in the book started not behaving so I skipped ahead to the next chapta


