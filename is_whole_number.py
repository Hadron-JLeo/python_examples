# Interesting typing exercise

from typing import Union
# Alternatively from Python 3.10 we can use int | float for our use-case


def is_whole_number(num: Union[int, float]) -> bool:
    """
    Check if a number is a whole number (integer value).
    Args:
        num: An INTEGER or FLOAT argument.

    Returns:
        bool: True if the number is a whole number (i.e., an integer or a float with no decimal part), 
              otherwise False.
              
    Raises:
        ValueError: If the provided input is neither an int nor a float.
      
    """
    if not isinstance(num, (int, float)):
        raise ValueError(f"Input must be int or float, got {type(num).__name__}")

    if isinstance(num, float):
        return num.is_integer()
    return True
