datos = {
    "codigo": ["001", "002", "003", "004", "005"],
    "nombre": ["Juan", "Ana", "Facundo", "Jesus", "Fiorella"],
}
listadatos = []
respuesta = "si"
while respuesta == "si":
    codigodato = input("Ingresar el codigo del alumno: ")
    curso = input("Ingrese el curso: ")
    nota1 = int(input("Ingresar nota 1 : "))
    nota2 = int(input("Ingresar nota 2 : "))
    nota3 = int(input("Ingresar nota 3 : "))
    x = 0
    for i in datos["codigo"]:
        if i == codigodato:
            codigodato = i
            nombredato = datos["nombre"][x]
            promedio = nota1 + nota2 + nota3
            promediototal = promedio / 3
            registro = codigodato, '\t', nombredato, '\t', curso, '\t',  nota1, '\t', nota2, '\t', nota3
            listadatos.append(registro)
        x += 1
    respuesta = input("Desea seguir ingresando los datos?: si o no ")

print("Codigo", '\t', "Nombre", '\t', "Curso", '\t', "Nota1", '\t', "Nota2", '\t', "Nota3")
for x in listadatos:
    print(*x, end="\n")

print("El promedio total es: ", promediototal)