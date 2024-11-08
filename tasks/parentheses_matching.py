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

# Input: 
# s: A string containing only the characters (, ), {, }, [, and ].

# Output:
# Return True if the string is valid (i.e., all parentheses are properly 
# matched and nested).
# Return False if the string is not valid.

# We encourage candidates to refrain from using large language models (LLMs) 
# like ChatGPT when coding their solutions, as we would prefer to assess their
# individual coding skills directly.