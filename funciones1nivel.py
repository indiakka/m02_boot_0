def normal(x):
    return x

def cuadrado(y):
    return y * y

def cubo(x):
    return x**3


def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
        
    return resultado

<<<<<<< HEAD:funciones1nivel.py
if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))
=======
print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))
>>>>>>> ec4a25229d86aa5b2d34b40975603959ab8e9d80:funicones1nivel.py
