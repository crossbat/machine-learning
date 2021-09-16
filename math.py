import matplotlib.pyplot as plt
import math as math

def Graph_maker(start, end, func, raise_point = 0.01):
    x_data = []
    y_data = []

    x = start
    
    if func == 'linear':
        print('input your function :')
        f = input('')

        erase = ['y', 'Y', 'X', '=', ' ']
        f = ''.join(x for x in f if x not in erase)
        if f.count('^') != 0:
            for i in range(f.count('^')):
                f = f.replace('^', '**')
        print(f)
        while x < end:
            x_data.append(x)
            y_data.append(eval(f))
            x += raise_point

    else:
        while x < end:
            x_data.append(x)

            if func == 'sin':
                y_data.append(math.sin(x))
                
            elif func == 'cos':
                y_data.append(math.cos(x))
                
            elif func == 'tan':
                y_data.append(math.tan(x))
            
            else:
                print('잘못된 입력')
                break

            x += raise_point
    
    plt.figure(figsize = (50, 50))
    plt.plot(x_data, y_data, '-')
    plt.xlabel("X")
    plt.ylabel('Y')
    plt.title('f = ' + func)
    plt.legend()

    return plt.show()

Graph_maker(start = -25, end = 25, func = 'linear', raise_point= 0.001)


