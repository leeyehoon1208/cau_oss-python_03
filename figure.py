# %% 
import math

class line:
    """선의 길이를 저장하는 클래스입니다. 외부에서 접근 가능한 __length 변수와 해당 변수를 수정할 수 있는 set_length와 get_length 메소드를 제공합니다."""


    __width = 0
    __height = 0
    def __init__(self, width, height):
        """
        초기 width 와 height 길이 값을 받습니다.
        Args:
            width: 생성된 초기 선의 가로 길이 값입니다.
            height: 생성된 초기 선의 세로 길이 값입니다.
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """
        선의 길이를 수정합니다.
        Args:
            width: 수정하고자 하는 선의 가로 길이 값입니다.
            height: 수정하고자 하는 선의 세로 길이 값입니다.
        """
        self.__width = width
        self.__height = height

    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이 값을 반환합니다.
        Returns:
            저장하고 있는 선의 길이 값입니다.
        """
        return self.__width, self.__height

def area_rectangle(width, height):
    
    if width <= 0 or height <= 0: raise ValueError
    return width * height

def area_ellipse(width, height):
   
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi

def area_regular_triangle(width, height):
    
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2

# %%
