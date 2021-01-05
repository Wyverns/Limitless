async def iter_func(arg, *lambdas):
    """Simple function that iterates through a list of (true or false) lambdas and returns True if anyone of them are True and returns
        False otherwise. Useful for flags and multiple checks.
        Example:
        funcs = [lambda x: x == 0,
                 lambda x: 1 == 0]

        await iter_func(0, *funcs)"""
    for func in lambdas:
        if func(arg):
            return True
        else:
            continue
    return False
