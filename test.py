import numpy as np
from easyemb.fundcls import SpinType, Dict4Data, get_standard_repr, WARN_CHAR

DEFAULT_CONST = 2.0
something = np.array([1, 2, 3])

class MyError(Exception):
    """"""

f = lambda x: x + 1

class MyClass:
    rf"""
    This is a test class to debug the color theme.
    $\hat H | \Psi \rangle = | \Psi \rangle $

    {DEFAULT_CONST:.2f}
    """
    def __init__(self, spin_type:SpinType) -> None:
        """
        This is a test of the docstring.
        https://code.visualstudio.com/api/extension-guides/color-theme
        """
        # This is a test of the inline comment.
        self.spin_type = spin_type
        self.a = 3
        assert isinstance(2, int), "Test of string."
        print(
            (
                (1, 2), (
                    (3, 4), (5, 6)
                )
            )
        )
        return

    def get_repr(self) -> str:
        return get_standard_repr(self.spin_type)

if __name__ == "__main__":
    my_instance = MyClass(SpinType.SZ)
    print(my_instance.get_repr())  # Should print the standard representation for SpinType.SZ
