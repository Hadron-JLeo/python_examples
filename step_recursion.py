# Interesting takes on step-incrementation-recursion



# Counts up by using a counter variable: current
def count_up(max_limit: int, current: int = 1) -> None:
    if current > max_limit:
        return
    print(current)
    count_up(max_limit, current + 1)


# Counts up using nested, helper function
def count_up_helper(max_limit: int) -> None:
    def helper(current: int) -> None:
        if current > max_limit:
            return
        print(current)
        helper(current + 1)

    helper(1)  # Start from 1

# 'Magical' (=not proper) recursion by subtracting backwards and adding the to the result, only works if the result is a number that divides the max_limit cleanly!
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
