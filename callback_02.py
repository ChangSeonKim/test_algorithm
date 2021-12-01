def fun_callback(input):
    print('fun_callback sum:', input)
    return

def fun_call(one, two, fun_callback):
    result = one + two
    fun_callback(result) 
    return

first = 10
second = 20
fun_call(first, second,fun_callback)