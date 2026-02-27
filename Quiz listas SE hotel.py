class huesped:
    def __init__(self, nombre, cedula, nhab):
      self.nombre = nombre
      self.cedula = cedula
      self.nhab = nhab

class habitacion:
    def __init__(self, numero):
        self.numero = numero
        self.disponible = True
        self.huesped_actual = None
        self.siguiente = None

class hotel:
    def __init__(self, total_habitaciones):
        self.primera_habitacion = None

        for i in range(1, total_habitaciones+1):
            nueva = habitacion(i)
            nueva.siguiente = self.primera_habitacion
            self.primera_habitacion = nueva    
        
        self.total_llegadas = 0


    def vacio(self):
        actual = self.primera_habitacion
        while actual != None:
            if actual.disponible == False:
                print("El hotel no está vacío")
                return 
            actual = actual.siguiente
        print("El hotel está vacío")
    
    def buscarHabitacion(self, num_buscar):
        actual = self.primera_habitacion
        while actual != None:
            if actual.numero == num_buscar:
                return actual
            actual = actual.siguiente
        return None


    def entrada(self, nombre, cedula, nhab):
        print(f"Registrando a {nombre}")
        habitacion = self.buscarHabitacion(nhab)
        if habitacion == None:
            print(f"La habitacion {nhab} no existe")
            return
        
        if habitacion.disponible == False:
            print(f"La habitacion {nhab} no está disponible")
            return
        
        nuevo = huesped(nombre, cedula, nhab)
        habitacion.huesped_actual = nuevo
        habitacion.disponible = False

        self.total_llegadas = self.total_llegadas + 1

        print(f"El huesped {nombre} ha sido registrado exitosamente en la habitacion {nhab}")

    def salida(self, cedula):
        print(f"Buscando al huesped identificado con {cedula}")
        actual = self.primera_habitacion
        while actual != None:
            if actual.huesped_actual != None and actual.huesped_actual.cedula == cedula:
                nombre = actual.huesped_actual.nombre
                num_hab = actual.numero
                actual.huesped_actual = None
                actual.disponible = True
                print(f"{nombre} salió de la habitación {num_hab}")
                return
            actual = actual.siguiente
        print(f"No se encontró ningun huesped con cédula {cedula}")

    def habitacionesDisponibles (self):
        print("Habitaciones disponibles:")
        actual = self.primera_habitacion
        while actual != None:
            if actual.disponible == True:
                print(f"Habitación {actual.numero}")
            actual = actual.siguiente
    
    def habitacionesOcupadas(self):
        print("Habitaciones ocupadas:")
        actual = self.primera_habitacion
        while actual != None:
            if actual.disponible == False:
                print(f"Habitación {actual.numero} ocupada por {actual.huesped_actual.nombre}")
            actual = actual.siguiente
    
    def consultaIndividual(self, cedula):
        print(f"Consulta individual de la cédula: {cedula}")
        actual = self.primera_habitacion
        encontrado = False

        while actual != None:
            if actual.huesped_actual != None and actual.huesped_actual.cedula == cedula:
                h = actual.huesped_actual
                print(f"Huesped con cédula {cedula} encontrado:")
                print(f"Nombre: {h.nombre}")
                print(f"Cédula: {h.cedula}")
                print(f"Número de habitación: {h.nhab}")
                encontrado = True
            actual = actual.siguiente
        if encontrado == False:
            print("No hay huesped identificado con cédula {cedula}")
    
    def consultaTotalPorCedula(self):
        print("\nConsulta total por cedula")
        huespedes = []
        actual = self.primera_habitacion
        while actual != None:
            if actual.huesped_actual != None:
                huespedes.append(actual.huesped_actual)
            actual = actual.siguiente
        
        if len(huespedes) == 0:
            print("No hay huespedes en el hotel")
            return

        print(f"Total de huespedes: {len(huespedes)}")
        for h in huespedes:
            print(f"Cédula: {h.cedula}")
            print(f"Nombre: {h.nombre}")
            print(f"Habitación: {h.nhab}")
    
    def consultaTotalPorLlegada(self):
        print("Consulta total por orden de llegada")
        huespedes = []
        actual = self.primera_habitacion
        while actual != None:
            if actual.huesped_actual != None:
                huespedes.append(actual.huesped_actual)
            actual = actual.siguiente
        
        if len(huespedes) == 0:
            print("No hay huespedes en el hotel")
            return
        
        contador = 1
        for i in range(len(huespedes)-1, -1, -1):
            h = huespedes[i]
            print(f"#{contador} - orden de llegada")
            print(f"Nombre: {h.nombre}")
            print(f"Cédula: {h.cedula}")
            print(f"Habitación: {h.nhab}")
            contador = contador + 1
        

print("CREACIÓN DEL HOTEL")
total_hab = int(input("¿Cuántas habitaciones tiene el hotel?: "))
mi_hotel = hotel(total_hab)
print(f"Hotel creado con {total_hab} habitaciones")

#Menú
while True:
    print("SISTEMA DE ADMINISTRACIÓN DE HOTEL")
    print("1. Registrar entrada de huésped")
    print("2. Registrar salida de huésped")
    print("\n--- CONSULTAS DE HUÉSPEDES ---")
    print("3. Consulta individual (por cédula)")
    print("4. Consulta total por cédula")
    print("5. Consulta total por orden de llegada")
    print("\n--- CONSULTAS DE HABITACIONES ---")
    print("6. Ver habitaciones disponibles")
    print("7. Ver habitaciones ocupadas")
    print("\n0. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
        case 1:
            print("\n--- REGISTRAR ENTRADA ---")
            cedula = input("Cédula del huésped: ")
            nombre = input("Nombre del huésped: ")
            nhab = int(input("Número de habitación: "))
            mi_hotel.entrada(cedula, nombre, nhab)
        
        case 2:
            print("\n--- REGISTRAR SALIDA ---")
            cedula = input("Cédula del huésped que se retira: ")
            mi_hotel.salida(cedula)
        
        case 3:
            print("\n--- CONSULTA INDIVIDUAL ---")
            cedula = input("Ingrese la cédula a buscar: ")
            mi_hotel.consultaIndividual(cedula)
        
        case 4:
            mi_hotel.consultaTotalPorCedula()
        
        case 5:
            mi_hotel.consultaTotalPorLlegada()
        
        case 6:
            mi_hotel.habitacionesDisponibles()
        
        case 7:
            mi_hotel.habitacionesOcupadas()
        
        case 0:
            print("\nGracias por usar el sistema, hasta luego.")
            break
        
        case _:
            print("\nOpción inválida. Intente de nuevo.")