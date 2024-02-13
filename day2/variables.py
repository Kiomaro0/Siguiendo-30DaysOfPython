import pydoc, sys

#Día 2: 30 días programando en python

#Nivel 1

first_name = "Samuel"
last_name = "Peña"
full_name = first_name + " " + last_name
country = "Colombia"
city = "Bogotá"
age = "26"
year = "2024"
is_married = False
is_true = True
is_light_on = False
numero, dato, cosa= 5, "nosé", "trompo"

#Nivel 2

#Primer punto
print("El tipo de dato de la variable first_name es: ", type(first_name))
print("El tipo de dato de la variable last_name es: ", type(last_name))
print("El tipo de dato de la variable full_name es: ", type(full_name))
print("El tipo de dato de la variable country es: ", type(country))
print("El tipo de dato de la variable city es: ", type(city))
print("El tipo de dato de la variable age es: ", type(age))
print("El tipo de dato de la variable year es: ", type(year))
print("El tipo de dato de la variable is_married es: ", type(is_married))
print("El tipo de dato de la variable is_true es: ", type(is_true))
print("El tipo de dato de la variable is_light_on es: ", type(is_light_on))
print("El tipo de dato de la variable numero es: ", type(numero))
print("El tipo de dato de la variable dato es: ", type(dato))
print("El tipo de dato de la variable cosa es: ", type(cosa))

#Segundo punto

print("la longitudad guardada en la variable first_name es: ", len(first_name))

#Tercer punto

if len(first_name) < len(last_name):
    print("La longitud del apellido es mayor que la del nombre")
else:
    print("La longitud del nombre es mayor que la del apellido")

#Cuarto punto
    
num_one = 5
num_two = 4

total= num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#Quinto punto

r = 30
area_of_circle = 3.14 * (pow(2,r))
circum_of_circle = 2*3.14*r

r_user = float(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ", 3.14*(pow(2,r_user)))

#Sexto punto

first_name = input("Ingrese un nombre: ")
last_name = input("Ingrese un apellido: ")
full_name = input("Ingrese su nombre completo: ")
country = input("Ingrese un pais: ")
city = input("Ingrese una ciudad: ")
age = input("Ingrese una edad: ")
year = input("Ingrese un año: ")
is_married = input("Ingrese si es casado: ")
is_true = input("Ingrese si es verdad: ")
is_light_on = input("Ingrese si la luz esta encendida: ")
numero, dato, cosa= input("Ingrese un numero: "),input("Ingrese un dato: "),input("Ingrese una cosa: ")

#Septimo punto 

pydoc.help("keywords")