# Programa para mostrar advertencias mediante condiciones

velAst = 49

if velAst < 25:
    print("No hay ningun riesgo del colisión del asteoride")
    if velAst >=20 and velAst <=24:
        print("Probabilidad de destello de luz en la atmósfera")
    else: 
        print("No hay ninguna probabilidad de destello de luz")
elif velAst >= 25:
    print("!Busquen el asteroide en el cielo!")
else:
    print("¡ADVERTENCIA! Riesgo de colisión")