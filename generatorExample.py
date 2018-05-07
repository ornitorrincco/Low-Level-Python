# if netx(obj) is called more of 9 times it will raise a error execturion, but is easy map his content, because is a ITERATOR

def GeneratorExample():
    for i in range (1, 10):
        if i == 3:
            # whatever return, doesn't is returned
            yield 'False'
            return
        yield i

obj =  GeneratorExample()
for k in obj:
    print(str(k))
# print(next(obj))
# print(next(obj))
# print(next(obj))
