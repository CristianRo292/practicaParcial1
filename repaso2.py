# Resolver ecuación cuadrática: ax^2 + bx + c = 0
# Solve quadratic equation: ax^2 + bx + c = 0
a = 1
b = 2
c = -15
p = 0
m = 0
r = 0
ra = 0.0
den = 0.0
x1 = 0.0
x2 = 0.0

# Calcular el discriminante (b² - 4ac)
# Calculate the discriminant (b² - 4ac)
p = b ** 2  # b al cuadrado / b squared
m = 4 * a * c  # 4 veces a por c / 4 times a times c
r = p - m  # Discriminante / Discriminant

# Verificar si el discriminante es positivo (raíces reales)
# Check if discriminant is positive (real roots)
if r > 0 :
    print("Si se puede")  # Se pueden calcular raíces reales / Real roots can be calculated
    ra = r ** (1/2)  # Calcular raíz cuadrada del discriminante / Calculate square root of discriminant
    den = 2 * a  # Calcular denominador común / Calculate common denominator
    x1 = (-b + ra) / den  # Primera raíz / First root
    x2 = (-b - ra) / den  # Segunda raíz / Second root
    # Mostrar resultados con 2 decimales / Show results with 2 decimals
    print (f"El valor de X1 = {x1:.2f}, y de X2: {x2:.2f}")
else:
    print("No se puede")  # No hay raíces reales / No real roots