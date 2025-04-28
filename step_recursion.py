# I created this as an example assignment for students

def my_recursion(max_limit: int = 500):
    """
    A 'magical' recursive function that performs step-incrementation
    """
    result = 1 # Step = 1, Start = 1

    if not result == max_limit:
        # As long as result has not reached the max_limit        
        result += my_recursion(max_limit - result)

    print(result) # Print every iteration
    return result

my_recursion()
