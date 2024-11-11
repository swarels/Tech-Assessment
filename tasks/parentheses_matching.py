# ---------------------------------------------------------------------------- #
#                   Parenthesis Matching (Balanced Brackets)                   #
# ---------------------------------------------------------------------------- #

# -------------------------------- BACKGROUND -------------------------------- #

# In many programming languages, parentheses are used to group expressions and 
# arguments, ensuring that the code is logically structured. A sequence of 
# parentheses is valid if every opening parenthesis has a corresponding closing 
# parenthesis and the parentheses are properly nested.

# You are given a string s containing only the characters (, ), {, }, [, and ]. 
# Your task is to determine if the string is valid by checking if the 
# parentheses are correctly paired and nested.

# A valid string:
# - Must contain no unmatched parentheses.
# - For every opening parenthesis (, {, or [, there must be a corresponding 
# closing parenthesis ), }, or ].
# - Parentheses must be correctly nested (i.e., ({[]}) is valid, but ({[})] is 
# not).

# -------------------------------- REQUIREMENTS ------------------------------- #

# Function Signature:
'''def is_valid_parentheses(s: str) -> bool:'''

def is_valid_parentheses(s):
    print("This is the string:")
    print(s)

    # Initial Checks
    if (len(s) % 2 or len(s) == 0):
        return(False)
    
    
    # Function to determine if two characters are corresponding opposites
    def is_opp(c1, c2):
        if (c1 == "("):
            if (c2 == ")"):
                return True
            else:
                return False
        if (c1 == "{"):
            if (c2 == "}"):
                return True
            else:
                return False
        if (c1 == "["):
            if (c2 == "]"):
                return True
            else:
                return False
        if (c1 == ")"):
            if (c2 == "("):
                return True
            else:
                return False
        if (c1 == "}"):
            if (c2 == "{"):
                return True
            else:
                return False
        if (c1 == "]"):
            if (c2 == "["):
                return True
            else:
                return False
        return("ERROR - UNKNOWN CHARACTER/CASE")


    stack = []

    for i in range(len(s)):
        print("Index:", i, " character:", s[i])
        print("Stack:", stack)
        # Push the initial character
        if (i == 0):
            stack.append(s[i])
            continue
        
        # If stack is empty, add and continue
        if (len(stack) == 0):
            stack.append(s[i])
            continue
        else:
            if (is_opp(s[i], stack[-1])):
                print("OPPOSITE")
                stack.pop()
            else:
                stack.append(s[i])
    
    print("-------------------------")
    print("Final length:", len(stack))
    if (len(stack) == 0):
        return(True)
    return(False)


print(is_valid_parentheses("([{()}])(([{]}))"))


## I am not too sure if the question explains whether or not concatenated nested parentheses are valid
## For example "()[]"
## I have taken into assumption that this IS VALID, and thus added into my code a check for this
## on line 82, checking if the stack is empty first. 
## If these sorts of strings are NOT VALID, please ignore these lines
## That check could be voided, and the string "()[]" would return FALSE instead

# Input: 
# s: A string containing only the characters (, ), {, }, [, and ].

# Output:
# Return True if the string is valid (i.e., all parentheses are properly 
# matched and nested).
# Return False if the string is not valid.

# We encourage candidates to refrain from using large language models (LLMs) 
# like ChatGPT when coding their solutions, as we would prefer to assess their
# individual coding skills directly.