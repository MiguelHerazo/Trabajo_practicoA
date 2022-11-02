
from Excepciones import OpcionIncorrecta
import random

from datetime import datetime,timedelta

    


class Vehiculo:
    def __init__(self,color : str,placa : str,marca : str,modelo : str,precio : int,año : str):
        self.color : str = color
        self.placa : str = placa
        self.marca : str = marca
        self.modelo : str = modelo
        self.precio : int = precio
        año : str = año
        self.estado = False #esto guarda si esta vendido o no, al inicio no se encuentra vendido el auto, por tanto es false

    def informacion_del_vehiculo(self):#metodo para imprimir la informacion de un vehiculo
        print("Color:",self.color)
        print("Placa:",self.placa)
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Precio: $",self.precio)
        if(self.estado):
            print("Estado: vendido")
        else:
            print("Estado: sin vender")
    
    def asignarDatos(self,color,placa,marca,modelo,precio): #este metodo sirve por si alguien desea editar un vehiculo se reasignan los atributos
        self.color = color
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def venderVehiculo(self):
        self.estado = True




class Moto(Vehiculo):

    def __init__(self, color: str, placa: str, marca: str, modelo: str, precio: int, año: str):
        super().__init__(color, placa, marca, modelo, precio, año)

    
    def informacion_de_la_moto(self):

        super().informacion_del_vehiculo()

    def vendermoto(self):

        super().venderVehiculo()











    


class Piezas:

    

    producto = {
    "tipo":"",
    "pieza":"",
    "precio":0,
    "unidades disponibles":0}
        
    

    

                       
class Agenadar_citas:

    def __init__(self, fecha : str, hora: str) -> None:
       
        
        self.fecha : str = fecha
        self.fecha : str = fecha
        self.hora : str = hora
        

    
class Test_drive:

    fecha = []

    def __init__(self,cedula:str,nombre:str,correo:str,numero:str,fecha):
        self.cedula : str = cedula
        self.nombre : str = nombre
        self.correo :str = correo
        self.numero:str = numero
        self.fechas = fecha

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombre} - {self.correo} - {self.numero} - {self.fecha}"
        
        

    def asignar_fecha():
        print("---------------------------------------")
        print("Agenda Tu Test Drive")
        cedula = input("Ingrese su cedula: ")
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo: ")
        numero = input("Ingrese su numero: ")



        hoy = datetime.now()
        print(hoy)

        dirve = hoy + timedelta(days= random.randint(0,31), hours=random.randint(0,24),minutes=random.randint(0,60))
        Test_drive.fecha.append(Test_drive(cedula,nombre,correo,numero,dirve))

        print(f"Hola {nombre}, su test Drive fue asignado con la fecha {dirve}")

    
                
        




class Concesionario:

    
        
    
    
    
    inventario = []
        
    


    def catalogo_de_vehiculos(concesionario_vehiculo):#metodo que recorre una lista de vehiculos e imprime la informacion de cada uno
        print("")
        for i in range(len(concesionario_vehiculo)):
            print("Vehiculo #",i+1)
            concesionario_vehiculo[i].informacion_del_vehiculo()
            print("--------------------")

    def catalogo_de_la_moto(concesionario_moto):#metodo que recorre una lista de vehiculos e imprime la informacion de cada uno
        print("")
        for i in range(len(concesionario_moto)):
            print("Moto #",i+1)
            concesionario_moto[i].informacion_de_la_moto()
            print("--------------------") 

    
    def catalogo_piezas():
        
        Concesionario.inventario.append( { "tipo":"llantas","pieza":"llantas michelin","precio" : 250000, "unidades disponibles":2 } )
        Concesionario.inventario.append( { "tipo":"frenos","pieza":"frenos racing","precio" : 3950000, "unidades disponibles":1} )
        Concesionario.inventario.append( { "tipo":"ventanas","pieza":"ventanas polarizadas","precio" : 1150000, "unidades disponibles":8} )

        for producto in Concesionario.inventario:

            print("---------------------")
            print("\t tipo:", producto["tipo"])
            print("\t pieza:", producto["pieza"])
            print("\t precio:", producto["precio"])
            print("\t unidaes disponibles:", producto["unidades disponibles"])
            

    def vender_producto():
        
        Concesionario.catalogo_piezas()

        buscar = input("ingrese el producto que quiere comprar....>")

        for producto in Concesionario.inventario:

            if buscar == producto["tipo"]:
                print("---------------------")
                print("\t tipo:", producto["tipo"])
                print("\t pieza:", producto["pieza"])
                print("\t precio:", producto["precio"])
                print("\t unidaes disponibles:", producto["unidades disponibles"])

            else:
                print("No hay un producto con ese nombre")

        print("vuelva pronto XD")
    
    
    
    


class Menu:

    def menu():
        concesionario_vehiculo = []#el concesionario es una lista de vehiculos
    
        Concesionario.concesionario_moto = []

        

        
    
        opc = 1
        while(opc != 0):
            print("------------------------------------------------")
            print()
            print("--------Bienvenido a tu Moto Sport--------")
            print()
            print("0. Salir")
            print("1. Registrar Usuario")
            print("2. Registrar vehiculo")
            print("3. catalogo vehiculos")
            print("4. Vender vehiculo")
            print("5. Editar informacion de un vehiculo")
            print("6. registrar moto")
            print("7. catalogo de motos ")
            print("8. vender moto ")
            print("9. Comprar piezas ")
            print("10. Agendar test Drive ")
            
            


            print()


            opc = int(input("Ingrese opcion: "))
            print()
            
            if(opc == 1):
                Concesionario.registrar_usuario()
                
                
                    
            
            
            elif(opc == 2):
                try:
                    color = str(input("Ingrese color: "))
                    placa = str(input("Ingrese placa: "))
                    marca = str(input("Ingrese marca: "))
                    modelo = str(input("Ingrese modelo: "))
                    precio = int(input("Ingrese precio: "))
                    año = str(input("Ingrese año: "))
                    concesionario_vehiculo.append(Vehiculo(color,placa,marca,modelo,precio,año))
                    
                
                except ValueError:
                    print("El dato que ingreso esta incorrecto")

            
            
            elif(opc == 3):
                Concesionario.catalogo_de_vehiculos(concesionario_vehiculo)
            elif(opc == 4):
                Concesionario.catalogo_de_vehiculos(concesionario_vehiculo)
                numero = int(input("Ingrese # del vehiculo que desea vender: "))
                if(numero >= 1 and numero <= len(concesionario_vehiculo)):
                    concesionario_vehiculo[numero-1].venderVehiculo()
                else:
                    print("Ingrese # de vehiculo valido!")
            elif(opc == 5):
                Concesionario.catalogo_de_vehiculos(concesionario_vehiculo)
                numero = int(input("Ingrese # del vehiculo que desea editar: "))
                color = input("Ingrese color: ")
                placa = input("Ingrese placa: ")
                marca = input("Ingrese marca: ")
                modelo = input("Ingrese modelo: ")
                precio = input("Ingrese precio: ")
                if(numero >= 1 and numero <= len(concesionario_vehiculo)):
                    concesionario_vehiculo[numero-1].asignarDatos(color,placa,marca,modelo,precio)
                else:
                    print("Ingrese # de vehiculo valido!")

            elif(opc == 6):
                color = input("Ingrese color: ")
                placa = input("Ingrese placa: ")
                marca = input("Ingrese marca: ")
                modelo = input("Ingrese modelo: ")
                precio = input("Ingrese precio: ")
                año = input("Ingrese año: ")
                Concesionario.concesionario_moto.append(Moto(color,placa,marca,modelo,precio,año))  

            elif(opc == 7):
                Concesionario.catalogo_de_la_moto(Concesionario.concesionario_moto) 

            elif(opc == 8):
                Concesionario.catalogo_de_la_moto(Concesionario.concesionario_moto)
                numero = int(input("Ingrese # de la moto que desea vender: "))
                if(numero >= 1 and numero <= len(Concesionario.concesionario_moto)):
                    Concesionario.concesionario_moto[numero-1].vendermoto()
                else:
                    print("Ingrese # de moto valido!")               

            elif(opc == 9):
                Concesionario.vender_producto()

            elif(opc == 10):
                Test_drive.asignar_fecha()
                
                

                
                

            
                
        
       
            else:
                print("Ingrese una opcion correcta y gracias")

         


            



Menu.menu()