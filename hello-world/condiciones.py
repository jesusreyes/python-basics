resultado = 10

if resultado > 10:
    print('La variable cumple con la condición')
else:
    print('La condición no se cumple')

calificacion = 8

if calificacion == 10:
    print('Felicidades, aprobaste la materia con una calificación perfecta.')
elif calificacion == 9 or calificacion == 8:
    print('Felicidades, aprobaste la materia.')
elif calificacion == 6 or calificacion == 7:
    print('Aprobaste la materia.')
else:
    print('Reprobaste la materia')

# Ternario
calificacion = 10
color = None

color = 'Verde' if calificacion >= 7 else 'Rojo'

print(calificacion, color)

