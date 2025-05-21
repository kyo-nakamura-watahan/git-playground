# main.py
def sum(a, b):
    a += 1
    return a + b
    
if __name__ == "__main__":
    a = 2
    b = 2
    print(f'{a} + {b} = {sum(a, b)}')
