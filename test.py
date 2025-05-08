import math, random, datetime, os  # unnecessary imports


class BaseClass:
    def greet(self):
        print("Hello from BaseClass")


class SubClassA(BaseClass):
    def greet(self):

        # duplicate code within a function
        print("Hello from SubClassA")
        print("Hello from SubClassA")

        # duplicate code across multiple classes
        a = 5 + 5
        b = a * 2
        c = b - 3
        d = b / 4
        e = a * 4
        f = e * e
        g = a + b
        h = 2 + e
        i = f + g
        print("A calc:", d)


class SubClassB(BaseClass):
    def greet(self):
        print("Hello from SubClassB")
        print("Hello from SubClassB")
        a = 5 + 5
        b = a * 2
        c = b - 3
        d = b / 4
        e = a * 4
        f = e * e
        g = a + b
        h = 2 + e
        i = f + g
        print("B calc:", d)


class SubClassC(BaseClass):
    def greet(self):
        print("Hello from SubClassC")
        print("Hello from SubClassC")
        
        a = 5 + 5
        b = a * 2
        c = b - 3
        d = b / 4
        e = a * 4
        f = e * e
        g = a + b
        h = 2 + e
        i = f + g

        a = 5 + 5
        b = a * 2
        c = b - 3
        d = b / 4
        e = a * 4
        f = e * e
        g = a + b
        h = 2 + e
        i = f + g

        print("C calc:", d)


def overly_complicated_function(
    a: int, b: str, c: float
):  # only 'a' and 'b' are used
    if a > 0:
        if a < 10:
            if a != 5:
                if b == "test":
                    print("test passed")
                else:
                    if b != "":
                        print("not empty")
                    else:
                        print("empty string")
            else:
                print("a is 5")
        else:
            print("a is too big")
    else:
        print("a is non-positive")


def uses_typing(x: int, y: str) -> str:
    print(y)
    return str(x)


def unused_function(z, w, u):  # only z is used
    return z + 1


def                              main()         :  # a lot of spaces
    objA = SubClassA()
    objB = SubClassB()
    objC = SubClassC()
    objA.greet()
    objB.greet()
    objC.greet()

    result1 = overly_complicated_function(3, "hello", "not used")  # c is unnecessary
    result2 = uses_typing("not an int", 42)  # type annotations ignored
    print(result2)

    math.sqrt(16)  # calculated but not used


main()
