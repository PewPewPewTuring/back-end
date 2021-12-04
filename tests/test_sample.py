def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

# anything with _test or test_ will get run w/ pytest
# don't assert the same line in two tests within the same class
# when making a test class, preface it with Test or pytest will not see it

a = 5
b = 6
def addition(a, b):
    c = a + b
    return c

def test_addition():
    assert addition(a, b) == 11

class TestClass:

    def test_1(self):
        x = "string"
        assert "t" in x

    # def test_2(self):
    #     x = "hello"
    #     assert hasattr(x, "check")
