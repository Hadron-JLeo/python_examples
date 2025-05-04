  
class Maths(): 

    _count:int = 0

    

    """ 
    We use a staticmethod when we know the function is semantically related to the class, 
    but does not need any information from the class or an instance
    """
    @staticmethod 
    def add_numbers(num1:float, num2:float):
        return num1 + num2

    @classmethod
    def 

# Driver's code 
if __name__ == "__main__": 
      
    # Calling method of class 
    # without creating instance 
    res = Maths.add_numbers(1, 2) 
    print("The result is", res) 
