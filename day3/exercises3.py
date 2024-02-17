
#Día 3: 30 días programando en python

#Primer punto, declaración de variables 

age = 26
height = 70.0
complex_num = 1+3j

#Cuarto punto, Pedirle al usuario la base y la altura de un triangulo para calcular su area

base = int(input("Ingrese la base del triangulo: "))
height = int(input("Ingrese la altura del triangulo: "))

print("El area del trianculo es ", int(0.5 * base * height))

#Quinto punto, pedirle al usuarilo los valores de 3 variables para encontrar el perimetro de un triangulo

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

print("El perimetro del triangulo es ", int(a + b + c))

#Sexto, calculara el area y el perimetro de un rectangulo, con los datos dados por el usuario 

length_Rec = int(input("Ingrece la longitud del rectangulo: "))
width_Rec = int(input("Ingrese el ancho del rectangulo :"))

print("El area del rectangulo es: ", length_Rec*width_Rec)
print("El perimetro del rectangulo es: ", (2*(length_Rec + width_Rec)))

#Septimo, calcular el area y la circunferencia de un circulo

pi = 3.14
radio = int(input("Ingrese el radio del circulo: "))

print("El area del circulo es: ", (pi*radio*radio))
print("La circunferencia del circulo es: ", (2*pi*radio))

#Octavo, calcular la pendiente de y = 2x - 2

x1, y1 = 0, -2      #Valores para sacar los puntos de intercepcion cuando x sea 0
x2, y2 = 1, 0       #Valores para sacar los puntos de intercepcion cuando y sea 0

m_1 = (y2 - y1) / (x2 - x1)

print(f"Pendiente (m): {m_1}")
print(f"Y-intercepcion (b): {2*(x1)-2}")    #La intercepcion de X es el valor de y cuando x vale 0
print(f"X-intercepcion (b): {x2}")          #La intercepcion de X es el valor de x cuando y vale 0

#Noveno, Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point 
#(2, 2) and point (6,10)

x1, y1 = 2, 2     
x2, y2 = 6, 10  

m_2 = (y2 - y1) / (x2 - x1)
dis_eucli = pow((((x2-x1)**2+(y2-y1)**2)),0.5)

print(f"Pendiente (m): {m_2}")
print(f"La distancia euclidiana es: {dis_eucli}")

#Decimo, comparar pendientes entre 8 y 9
 
print("la pendiente del punto 8 es mayor con respecto al punto nueve:", m_1 > m_2)
print("la pendiente del punto 8 es menor con respecto al punto nueve:", m_1 < m_2)
print("la pendiente del punto 8 son iguales con respecto al punto nueve:", m_1 == m_2)

#Onceavo, Calculate the value of y (y = x^2 + 6x + 9). 
#Try to use different x values and figure out at what x value y is going to be 0.

#y = (x + 3)^2 , si x= -3, y es 0 

x1 = -3

y1 = x1**2 + 6*x1 + 9

print("Sé encontro el valor de x cuando y es 0: ", y1 == 0, f"\nEl numero es {x1}")

#Doceavo, encuentra el tamaño de 'python' y 'dragon' y haz una falsa comparación

cadena_1 = 'Python'
cadena_2 = 'Dragon'

print("La longitud de 'Python' es mayor que la de 'Dragon': ",len(cadena_1)>len(cadena_2) )

#Treceavo, Usar 'and' y ver si 'on' se encuentra en 'python' o 'dragon'

print("En ambas cadenas anteriores se encuentra 'on' : ", 'on' in cadena_1 and 'on' in cadena_2 )
# usamos in para consultar si en una lista contiene cierto item

#14. Usar in para verificar si en la siguiente cadena se encuentra 'jargon'

cadena_1 = 'I hope this course is not full of jargon.'

print(f"En la siguiente oracion :\n '{cadena_1}' \nse ecuentra la palabra 'jargon' : {'jargon' in cadena_1}")

#15. usar 'is no' para verificar si no esta en las cadenas de 'dragon' y 'python'

cadena_1 = 'Python'
on_esta_1 = 'on' in cadena_1        #Verifica si 'on' se encuentra dentro de la cadena 1
on_esta_2 = 'on' in cadena_2        #Verifica si 'on' se encuentra dentro de la cadena 1
print("No esta 'on' en las cadenas 'python' y 'dragon':", on_esta_1 is not on_esta_2 )

#16. Encontrar el tamaño de 'python' y pasar su valor a flotante y despues a string

tam_cadena = len(cadena_1)
print(f"El tamaño de la cadena 'python' es: {tam_cadena} y es {type(tam_cadena)} ")
print(f"Ahora su tipo paso a ser : {type(float(tam_cadena))} ")
print(f"Ahora su tipo paso a ser : {type(str(tam_cadena))} ")

#17. comprobar que el numero ingresado es par

num_par = int(input("Ingrese un numero para comprobar si es par o no: "))
print("El numero ingresado es par: ", (num_par%2) == 0)

#18. comprobar que la division de piso de 7/3 sea igual a 2.7 convertido en entero 

division_piso = 7//3
num = 2.7

print("El resultado de la division de piso de 7 entre 3 y la parte entera de 2.7 son la misma : ", division_piso == int(num))

#19. ver si '10' y 10 tienen el mismo tipo de dato 

tipo_1 = '10'
tipo_2 = 10 

print("Son el mismo tipo de dato: ", type(tipo_1) == type(tipo_2))

#20. Ver si el entero de 9.8 es igual a 10

num_1 = float('9.8')
num_2 = 10

print("9.8 es igual a 10: ", int(num_1) == num_2)

#21. 

hora = int(input("Ingrese el numero de horas :"))
por_hora = int(input("Ingrese cuanto gana por hora :"))

print("Usted gana por hora: ", hora* por_hora)

#22. Calcular cuanto a vivido una persona en segundos
min = 60
hora = min * 60
dia = hora *24
año = dia * 365
edad = int(input("Ingrese cuantos años tiene: "))

print(f"Usted ha vivido por {edad * año} segundos ")

#23.
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")