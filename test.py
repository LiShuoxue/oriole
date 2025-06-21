import numpy as np
from scipy import linalg as la

DEFAULT_CONST = 2.0
print(DEFAULT_CONST)
something = np.array([1, 2, 3])
def some_function(x): return x + 1
def other_function(x): return tuple(map(lambda t: t + 1, x))


print('Here is another set of string.')


class MyClass:
    rf"""This is a test of regex docstring
    $\hat H | \Psi \rangle = | \Psi \rangle $
    {DEFAULT_CONST}
    """

    def __init__(self, param: np.ndarray) -> None:
        """
        This is a test of the docstring.
        https://code.visualstudio.com/api/extension-guides/color-theme
        """
        # This is a test of the inline comment.
        new_var = int(True)
        self.param = param + new_var
        assert isinstance(2, int), "Test of string."

    def test_function(self) -> str:
        print("sth. {:.2f}".format(la.norm(some_function(self.param))))
        print(f"sth{DEFAULT_CONST:12.2e}")
        raise ValueError("This is a test of the exception.")


if __name__ == "__main__":
    my_instance = MyClass(np.arange(16).reshape(4, 4))
    print(my_instance.test_function())
