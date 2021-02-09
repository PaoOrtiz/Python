from tkinter import *
class catalogo:
    pass
    def __init__(self):
        self.Nombre = input("Introduce el nombre del producto: \n")
        self.Precio = int(input("Introduce el precio del producto: \n"))
        self.Cantidad = int(input("Introduce la cantidad del producto al ingresar: \n"))
        self.Proveedor = input("Ingresa el proveedor: \n")
        self.Categoría = input("Introduzca la categoría: \n")
        

    def imprimir(self):
                return (f"Información del producto ingresado: \nNombre del producto:{self.Nombre} \nPrecio:{self.Precio}  \nProveedor:{self.Proveedor}")

    def iva (self):
        self.iva = self.Precio * float (0.13) * self.Cantidad 
        self.resultado = self.Precio* self.Cantidad
        self.final = self.iva + self.resultado
        print(f"Precio con IVA {self.final}")

    def impuesto(self):
            if self.Precio>75:                
                num= int(input("Debes pagar Impuestos, selecciona el porcentaje \n1% \n2% \n3% \n4% \n5% \n"))
             

class categorias(catalogo):
    pass
    def __init__(self):
        self.categoria =("Electrodomésticos\n Teléfonos\n Computadoras\n Zapatos \n Ropa")
        self.catego = input("Agrega una nueva categoría")
    def imprim ():
        return (categoria)
         
    


nuevo_producto = catalogo()
print (nuevo_producto.imprimir())
print(nuevo_producto.impuesto())
print(nuevo_producto.iva())



       

raiz= Tk()
raiz.title ("Catálogo")
raiz.geometry ("500x300")

BotonAgregar =Button(raiz,text= "Agregar producto", command= catalogo).pack()
BotonAgregar =Button(raiz,text= "Mostrar los productos por categoría", command=categoria).pack()
BotonAgregar =Button(raiz,text= "Mostrar todos los productos en un rango de precios ", command= categorias).pack()
BotonAgregar =Button(raiz,text= "Agregar más categorías de los productos", command= categorias).pack()

raiz.mainloop()