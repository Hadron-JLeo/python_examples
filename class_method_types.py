""" Script to showcase the different types of methods a class can have """  

class Maths(): 

    _count:int = 0

    """ 
    We use a staticmethod when we know the function is semantically related to the class, 
    but does not need any information from the class or an instance
    """
    def __init__(self, favorite_number:int)->None:
        self.favorite_number = favorite_number
        Maths._count += 1 

  
    @staticmethod 
    def add_numbers(num1:float, num2:float)->float:
        return num1 + num2

  
    @classmethod
    def get_count(cls)->int:
        return cls._count

  
    def get_fav_num(self)->int:
        return self.favorite_number
      

if __name__ == "__main__": 

    res = Maths.add_numbers(1, 2) 
    my_math = Maths(13)
    print(Maths.get_count())
    print("The result is", res) 
