#LISTAS, DICCIONARIOS (BASES DE DATOS)
usuariosR = ["207700341"]
contrasenasR = ["Candy123"]

clientes = {"207700341": ["Wendy Zepeda Zeledon, F , 70639974, wenzepeda97@gmail.com"]}


#ESTA CLASE ES PARA MANTENIMIENTO DE UN CLIENTE
class Cliente(object):
    def __init__(self, cedula, nombre, telefono, correo, sexo,deuda,mascota):
        """

        :param cedula: Identificador de la persona
        :param nombre: Nombre de la persona
        :param teléfono: Nùmero de celular
        :param correo: Correo electrónico
        :param sexo: Sexo de la persona (Femenino o Masculino)
        :param deuda: Monto adeudado
        :param mascota: Mascota del cliente

        """
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.sexo = sexo
        self.deuda = deuda
        self.mascota = mascota

    def __str__(self):
        return ("Cédula: {0}, Nombre: {1},\n"
                "Teléfono: {2}, Email: {3},\n"
                "Género: {4}, Deuda: {5},\n"
                "Mascota: {6}\n").format(self.cedula,
                                                   self.nombre,
                                                   self.telefono,
                                                   self.correo,
                                                   self.sexo,
                                                self.deuda,
                                     self.mascota)

cliente1 = Cliente("207830110", " María Fernanda Arce Castro","63317476",
                   "mariafarce23@gmail.com","Femenino","0"," Molly")

cliente2 = Cliente("207700341", "Wendy Zepeda Zeledón","70639974",
                   "wenzepeda97@gmail.com","Femenino","30000","Lazy")
print(cliente2)

#ESTA CLASE ES PARA LAS MASCOTAS

class Mascota(object):
    def __init__(self, codigo, dueno, nombre ,fingreso ,fnacimiento ,sexo ,tipo ,raza ,color ,peso , direccion, telefono, email ,observaciones):
        """

        :param codigo: Identificador el codigo de la mascota
        :param dueño: Dueño de la mascota
        :param nombre: Nombre de la mascota
        :param fingreso: Indica fecha de ingreso de la mascota
        :param fnacimiento: Indica la fecha de nacimiento de la mascota
        :param sexo: Indica sexo de la mascota(hembra o macho)
        :param tipo: Indica el tipo de animail que es(gato,perro,perico)
        :param raza: Raza de la mascota
        :param color: Color de la mascota
        :param peso: Peso en kilogramos de la mascota
        :param direccion: Dirección de residencia de la mascota
        :param teléfono: Nùmero de celular
        :param email: Correo electrónico
        :param observaciones: observaciones que cada mascota

        """
        self.codigo = codigo
        self.dueno = dueno
        self.nombre = nombre
        self.fingreso = fingreso
        self.fnacimiento = fnacimiento
        self.sexo = sexo
        self.tipo = tipo
        self.raza = raza
        self.color = color
        self.peso = peso
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.observaciones = observaciones

    def __str__(self):
        return ("Código: {0}, Dueño: {1}, Nombre: {2},\n"
                "Fecha de ingreso: {3}, Fecha de nacimiento: {4},\n"
                "Sexo: {5}, Tipo: {6},\n"
                "Raza: {7}, Color: {8}, Peso: {9},\n"
                "Dirección: {10}, Telfono: {11},\n"
                "Email: {12}, Observaciones: {13},\n").format(self.codigo,
                                                          self.dueno,
                                                          self.nombre,
                                                          self.fingreso,
                                                          self.fnacimiento,
                                                          self.sexo,
                                                          self.tipo,
                                                          self.raza,
                                                          self.color,
                                                          self.peso,
                                                          self.direccion,
                                                          self.telefono,
                                                          self.email,
                                                          self.observaciones)


mascota1 = Mascota("001"," Wendy Zepeda Zeledón", "lazy",
                   " 04-08-2018", " 10-01-2017", "Hembra",
                   " Perro", "labrador", "Blanco con Cafè", "18.6 kg",
                   "Venecia", " 70639974", "wenzepeda97@gmail.com",
                   "desparacitaciòn y vacunas")

mascota2 = Mascota("002", "Maria Fernanda Arce Castro", "Molly",
                   "05-08-2018", "12-12-2015", "Hembra",
                   "Perro", "Sharpei", "Cafè y negro", "15 kg",
                   "La Vega", "63317476", "mariafarce23@gmail.com",
                   "Castraciòn y vacunas")
print(mascota1)

#ESTA CLASE ES PARA MANTENIMIENTO DE VACUNAS

class Vacuna(object):
    def __init__(self, codigo, descripcion, precio):
        """

        :param codigo: Identificador de vacuna
        :param descripcion: Descripcion de la vacuna
        :param precio: Costo de la vacuna


        """
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio


    def __str__(self):
        return ("codigo: {0} descripcion: {1}"
                "precio: {2}").format(self.codigo,
                                        self.descripcion,
                                        self.precio)


# ESTA CLASE ES PARA MANTENIMIENTO DE TRATAMIENTOS
class Tratamiento(object):
    def __init__(self, codigo, descripcion, precio):
        """

        :param codigo: Identificador de tratamiento
        :param descripcion: Descripcion del tratamiento
        :param precio: Costo del tratamiento


        """
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return ("codigo: {0} descripcion: {1}"
                "precio: {2}").format(self.codigo,
                                      self.descripcion,
                                      self.precio)




# ESTA CLASE ES PARA MANTENIMIENTO DE TRATAMIENTOS
class Servicios(object):
    def init(self, codigo_del_servicio, descripcion, precio):
        """
        :param codigo_del_servicio: Identificador del servicio
        :param descripcion: Descipción del servicio (baño, corte de cabello)
        :param precio: Costo del tratamiento

        """
        self.codigo_del_servicio = codigo_del_servicio
        self.descripcion = descripcion
        self.precio = precio

def __str__(self):
    return ("codigo_del_servicio: {0} descripcion: {1}"
            "precio: {2}").format(self.codigo_del_servicio,
                                  self.descripcion,
                                  self.precio)

serv1 = Servicios()


#MAIN PRINCIPAL
print(  "+++++++++++++++++++++++++++++++++++\n"
        "** V E T E R I N A R I A   W Y F **\n"
        "+++++++++++++++++++++++++++++++++++\n"
        "           INICIAR SESIÓN          ")

#MENU PRINCIPAL
menu = (("++++++++++++++++++++++++++++++++++\n"
        "** V E T E R I N A R I A   W Y F **\n"
        "+++++++++++++++++++++++++++++++++++\n"
        "1. Registrar nuevo usuario\n"
        "2. Mantenimiento de Clientes\n"
        "3. Mantenimiento de mascotas\n"
        "4. Control de vacunas\n"
        "5. Historial Clínico\n"
        "6. Servicios\n"
        "7. Pago\n"
        "8. Cerrar sesión\n"
        "++++++++++++++++++++++++++++++\n"
        "Seleccione una de las opciones: "))


#MENU DE OPCIONES PARA MANTENIMIENTO DE CLIENTES
opciones2 = (("++++++++++++++++++++++++++++++++++\n"
             "** V E T E R I N A R I A   W Y F **\n"
             "+++++++++++++++++++++++++++++++++++\n"
             "1. Insertar nuevo cliente\n"
             "2. Eliminar cliente\n"
             "3. Actualizar datos de cliente\n"
             "4. Consulta dato de cliente\n"
             "5. Volver al Menú Principal\n"
             "++++++++++++++++++++++++++++++\n"
             "Seleccione una de las opciones: "))

#MENU DE OPCIONES PARA MANTENIMIENTO DE MASCOTAS
opciones3 = (("++++++++++++++++++++++++++++++++++\n"
              "** V E T E R I N A R I A  W Y F **\n"
              "+++++++++++++++++++++++++++++++++++\n"
              "1. Insertar nueva mascota\n"
              "2. Eliminar mascota\n"
              "3. Actualizar datos de mascota\n"
              "4. Consulta dato de mascota\n"
              "5. Volver al Menú Principal\n"
              "++++++++++++++++++++++++++++++\n"
              "Seleccione una de las opciones: "))

#MENU DE OPCIONES PARA MANTENIMIENTO DE VACUNAS
opciones4 = (("+++++++++++++++++++++++++++++++++++\n"
              "** V E T E R I N A R I A   W Y F **\n"
              "+++++++++++++++++++++++++++++++++++\n"
              "1. Insertar vacuna\n"
              "2. Eliminar vacuna\n"
              "3. Volver al Menú principal\n"
              "+++++++++++++++++++++++++++++++++++\n"
              "Selecione una de las opciones: "))

opciones5 = (("+++++++++++++++++++++++++++++++++++\n"
              "** V E T E R I N A R I A   W Y F **\n"
              "+++++++++++++++++++++++++++++++++++\n"
              "1. Insertar nuevo historial de mascota\n"
              "2. Consultar historial de mascota\n"
              "3. Eliminar historial de mascota\n"
              "4. Volver al Menú principal\n"
              "+++++++++++++++++++++++++++++++++++\n"
              "Selecione una de las opciones: "))


#FUNCION PARA REGISTRO DE USUARIO
def registrar(ced, cont):
    if ced in usuariosR:
        print("Número de ususario existente en el sistema. Intente nuevamente\n")
    else:
        usuariosR.append(ced)
        contrasenasR.append(cont)
        print("Se ha creado un nuevo usuario en el sistema.\n")
        print(usuariosR)

#main principal
while 1:
    usuario = input('User: ')
    if usuario in usuariosR:
        passw = input('Password: ')
        if passw in contrasenasR:
            print("Ingreso de datos correcto.")
        else:
            print("Contraseña incorrecta. Por favor intente nuevamente")
    else:
        print("Nombre usuario inválido por favor intente nuevamente.\n"
              "Sí aún no esta registrado, contacte a su administrador.")
        break
    while 1:
        op = int(input(menu))
        if op == 1:
            ced = input("Número de cédula: ")
            cont = input("Ingrese una contraseña de al menos 8 caracteres: ")
            registrar(ced,cont)

        elif op == 2:
            while 1:
                menu2 = int(input(opciones2))
                if menu2 == 1:
                    pass
                elif menu2 == 2:
                    pass
                elif menu2 == 3:
                    pass
                elif menu2 == 4:
                    pass
                elif menu2 == 5:
                    break
                else:
                    print("Opción inválida. Intente nuevamente")

        elif op == 3:
            while 1:
                menu3 = int(input(opciones3))
                if menu3 == 1:
                    pass
                elif menu3 == 2:
                    pass
                elif menu3 == 3:
                    pass
                elif menu3 == 4:
                    pass
                elif menu3 == 5:
                    break
                else:
                    print("Opción inválida. Intente nuevamente")


        elif op == 4:
            while 1:
                menu4 = int(input(opciones4))
                if menu4 == 1:
                    pass
                elif menu4 == 2:
                    pass
                elif menu4 == 3:
                    pass
                elif menu4 == 4:
                    pass
                elif menu4 == 5:
                    break
                else:
                    print("Opción inválida. Intente nuevamente")

        elif op == 5:
            while 1:
                menu5 = int(input(opciones4))
                if menu5 == 1:
                    pass
                elif menu5 == 2:
                    pass
                elif menu5 == 3:
                    pass
                elif menu5 == 4:
                    pass
                elif menu5 == 5:
                    break
                else:
                    print("Opción inválida. Intente nuevamente")

        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            break
        else:
            print("Opción inválida. Por favor intente nuevamente.")
