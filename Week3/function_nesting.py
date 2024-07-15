# Function Nesting


def outer_function():
    words = "I am Outer Function"
    def inner_function():
        def inner_inner_funtion():
            return words
        
        print(inner_inner_funtion())
        return True
    print(inner_function())

    return "True"


print(outer_function())


name="Miracle"