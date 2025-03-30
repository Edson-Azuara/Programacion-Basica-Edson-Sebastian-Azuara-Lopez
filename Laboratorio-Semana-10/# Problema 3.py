# Problema 3

#Desarrolla un programa que permita gestionar contactos de la siguiente manera:
# Cada contacto debe ser almacenado como una tupla con nombre, n´umero
# y correo.

# La agenda de contactos debe almacenarse en una lista.
# Debe permitir agregar nuevos contactos.
# Buscar contactos por nombre e imprimir sus detalles.
# Listar todos los contactos en orden alfab´ etico.

def agregar_contacto(agenda, nombre, numero, correo):
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto {nombre} agregado exitosamente.")

def buscar_contacto(agenda, nombre):
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
            return
    print("Contacto no encontrado.")

def listar_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.")
        return
    agenda_ordenada = sorted(agenda, key=lambda x: x[0].lower())
    print("Lista de contactos:")
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

def menu():
    agenda = []
    while True:
        print("\nGestor de Contactos")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            numero = input("Ingrese el número: ")
            correo = input("Ingrese el correo: ")
            agregar_contacto(agenda, nombre, numero, correo)
        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_contacto(agenda, nombre)
        elif opcion == "3":
            listar_contactos(agenda)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()

