
#########################
# 2- Testing Endpoints  #
##################################
# 2-a- Testing /create-candidate #
##################################
# Response with 201 code


# Handle invalid values (candidate_ref must be a unique sequence of 8 digits and alphabets) respond with status code(400)Bad request


# Handle duplicate values (check if candidate_ref already exist) respond with status code (409)conflict


###############################
# 2-b- Testing /create-score  #
###############################
# Respond with status code (201)


# It should write a single score to the dB.


# Score should be float (0 - 100) inclusive.


# Score must be pushed and stored into a list.


################################################
# 2-c- Testing /get-candidate/{candidate_ref}  #
################################################
# Respond with status code (200).


# Response should be a dict. formatted as : {'candidate_ref':'8u9i7y6t', 'name':'Test', 'score':[34,56,....]}.


# If (candidate_ref) doesn't exist respond with a msg 'Candidate not registered' and a status code(404).
