# import test
# print(test.f(5))

# def new_string(string, count = 3):
#     return string * count

# print(new_string(4))

def test_name(*params):
    res: str = ''
    for item in params:
        res += item
    return res

print(test_name('a', 'b', 'c', 'd'))