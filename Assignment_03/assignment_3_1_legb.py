x = "Global X"


def outer():
    x = "Enclosing X"

    def inner():
        x = "Local X"
        print("Inner x:", x)

    inner()
    print("Outer x:", x)


outer()
print("Main x:", x)