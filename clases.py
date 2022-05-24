class Bicicletas:
    def __init__(self,marca,rodado,precio):
        self.marca=marca
        self.rodado=rodado
        self.precio=precio
#DATOS YA CARGADOS EN LA CONCESIONARIA.
biciorbea="Orbea"
rodadoorbea=29
precioorbea=150000
orbea=Bicicletas(biciorbea,rodadoorbea,precioorbea)
########       print(orbea.marca,orbea.rodado,orbea.precio)
bicivenzo="Venzo"
rodadovenzo=26
preciovenzo=85000
venzo=Bicicletas(bicivenzo,rodadovenzo,preciovenzo)
########       print(venzo.marca,venzo.rodado,venzo.precio)



class Motos:
    def __init__(self,marca,modelo,precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
#DATOS YA CARGADOS EN LA CONCESIONARIA.
motohonda="Honda Wave"
modelohonda=2014
preciohonda=90000
honda=Motos(motohonda,modelohonda,preciohonda)
########      print(honda.marca,honda.modelo,honda.precio)
motomotomel="Motomel"
modelomotomel=2017
preciomotomel=110000
motomel=Motos(motomotomel,modelomotomel,preciomotomel)
########     print(motomel.marca,motomel.modelo,motomel.precio)





class Auto:
    def __init__(self,marca,modelo,precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
#DATOS YA CARGADOS EN LA CONCESIONARIA.
autovw="volkswagen Nivus"
modelovw=2020
preciovw=2100000
vw=Auto(autovw,modelovw,preciovw)
#######          print(vw.marca, vw.modelo, vw.precio)
autoford="Ford Focus"
modeloford=2015
precioford=4500000
ford=Auto(autoford,modeloford,precioford)
#######          print(ford.marca,ford.modelo,ford.precio)