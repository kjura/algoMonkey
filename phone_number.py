def my_func(line):
    
    if len(line) < 4:
        return line
    else:
        rev = line[::-1]
        output = []
        for pos, ch in enumerate(rev):
            if pos == 0:
                output.append(ch)
            elif pos % 3 != 0:
                output.append(ch)
            else:
                output.append('.')
                output.append(ch) 
    return ''.join(output[::-1])


print(my_func('123'))
print(my_func('1567442346'))
print(my_func('126765856876234'))
print(my_func('12312343534'))
print(my_func('12309854098347987234798347'))


assert my_func('1') == '1'
assert my_func('123') == '123'
assert my_func('1234') == '1.234'
assert my_func('12345') == '12.345'
assert my_func('12345678') == '12.345.678'
