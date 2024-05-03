# Importaciones necesarias para el funcionamiento del codigo
import pandas as pd
import matplotlib.pyplot as plt

# Array con el que se van a extraer los datos para el trabajo
ventas_mensuales = [
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},
{"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
{"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
{"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
{"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
{"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]

# DataFrame con todos los datos de ventas_mensuales
df0 = pd.DataFrame(ventas_mensuales)

# Division por trimestres, lo tuve que hacer asi porque no conocia otra manera
Trimestre1=[
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023}]
df1 = pd.DataFrame(Trimestre1)

Trimestre2 = [
    {"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
]
df2 = pd.DataFrame(Trimestre2)

Trimestre3 = [
    {"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023}
]
df3 = pd.DataFrame(Trimestre3)

Trimestre4 = [
    {"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023}
]
df4 = pd.DataFrame(Trimestre4)

Trimestre5 = [
    {"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024}
]
df5 = pd.DataFrame(Trimestre5)

Trimestre6= [
    {"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024}
]
df6 = pd.DataFrame(Trimestre6)

Trimestre7 = [
    {"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024}
]
df7 = pd.DataFrame(Trimestre7)

Trimestre8 = [
    {"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]
df8 = pd.DataFrame(Trimestre8)

# Usando el primer DataFrame, se retornan todos los meses y total de ventas donde estos superen 20000
ventas_mayores_2000 = df0[df0['total_ventas'] > 20000]

# Se imprime el total de ventas que hubo en todos los trimestres
print("El total de las ventas del primer trimestre es de: ", df1['total_ventas'].sum())

print("El total de las ventas del segundo trimestre es de: ", df2['total_ventas'].sum())

print("El total de las ventas del tercer trimestre es de: ", df3['total_ventas'].sum())

print("El total de las ventas del cuarto trimestre es de: ", df4['total_ventas'].sum())

print("El total de las ventas del quinto trimestre es de: ", df5['total_ventas'].sum())

print("El total de las ventas del sexto trimestre es de: ", df6['total_ventas'].sum())

print("El total de las ventas del septimo trimestre es de: ", df7['total_ventas'].sum())

print("El total de las ventas del octavo trimestre es de: ", df8['total_ventas'].sum())


# Se imprime por consola que meses superaron las 20000 ventas
print ("Los meses donde hubo ventas mayores a 20000 fueron: ")
# Lo hice con 2 prints asi quedaba mas legible en la consola
print(ventas_mayores_2000)


# Se imprime por consola el mes con mas ventas y cuales fueron
print('El mes con mayor ventas es diciembre2 con un total de: ', df0["total_ventas"].max())

#Se imprime por consola el promedio de ventas mensuales
print('El promedio de ventas mensuales es de: ',df0['total_ventas'].mean())

#Se realiza el dataframe unicamente con los meses y su total de ventas
df0.drop('año', axis=1, inplace=True)

# Con los meses y ventas, se le asignan valores X e Y para poder realizar los graficos
x = df0['mes']
y = df0['total_ventas']

# Se le pasan los valores a la libreria para poder realizar el grafico
plt.plot(x, y)
# Titulo para el grafico
plt.title('Grafico de ventas por mes')

# Nombre para el valor X
plt.xlabel('Meses')
# Nombre para el valor Y
plt.ylabel('Ventas por mes')

# Demostracion del grafico
plt.show()