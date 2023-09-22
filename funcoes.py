def f(x):
    return eval(f_expressao)

def g(x):
    return eval(g_expressao)

def compose(f, g, x):
    return f(g(x))

f_expressao = input("Digite a expressão para f(x): ")
g_expressao = input("Digite a expressão para g(x): ")


x_value = float(input("Digite o valor de x: "))

g_of_f = compose(g, f, x_value)
g_of_g = compose(g, g, x_value)
f_of_f = compose(f, f, x_value)
f_of_g = compose(f, g, x_value)

print("(g ° f)(x) =", g_of_f)
print("(g ° g)(x) =", g_of_g)
print("(f ° f)(x) =", f_of_f)
print("(f ° g)(x) =", f_of_g)
