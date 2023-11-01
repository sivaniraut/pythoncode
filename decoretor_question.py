def validate_fun(func):
    def inner(*args, **kwargs):
        if all(isinstance(num, int) for num in args):
            return func(*args, **kwargs)
        else:
            return "invalid input"
    return inner

@validate_fun
def sum_num(a, b):
    return a + b
print(sum_num("5","10"))


def validated_even_num(func):
    """
    @summary- validating the even no
    :param func: function argument
    :return: the actual main function
    """

    # def inner(*args, **kwargs):
    #     if i in args