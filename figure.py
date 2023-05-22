# %% 
"""
figure 모듈은 함수 및 클래스를 제공하는 모듈이다.
그리고 정사각형, 원, 그리고 정삼각형의 넓이를 구하고 반환한다. 
"""
import math

class line:
    """선의 길이를 저장하는 클래스입니다. 외부에서 접근 가능한 __length 변수와 해당 변수를 수정할 수 있는 set_length와 get_length 메소드를 제공합니다."""

    def __init__(self, length):
        """
        초기 길이 값을 받습니다.
        Args:
            length: 생성된 초기 선의 길이 값입니다.
        """
        self.__length = length

    def set_length(self, length):
        """
        선의 길이를 수정합니다.
        Args:
            length: 수정하고자 하는 선의 길이입니다.
        """
        self.__length = length

    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이 값을 반환합니다.
        Returns:
            저장하고 있는 선의 길이 값입니다.
        """
        return self.__length

def area_square(length):
    """주어진 길이의 정사각형의 넓이를 계산하여 반환합니다."""
    return length * length

def area_circle(length):
    """주어진 길이를 반지름으로 하는 원의 넓이를 계산하여 반환합니다."""
    return length * length * math.pi

def area_regular_triangle(length):
    """주어진 길이를 한 변으로 하는 정삼각형의 넓이를 계산하여 반환합니다."""
    return length * length * math.sqrt(3) / 4

# %%
