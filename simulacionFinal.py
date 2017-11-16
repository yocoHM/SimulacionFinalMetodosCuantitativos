import numpy as np

class Reservacion:
  diasDeHospedaje = 0
  tipoDeCuarto = 0
  diaLlegada = 0
  horaLlegada = 0
  numeroDeReservacion = 0
  cantidadDePersonas = 0
  atendido = 0
  hizoReservacion = 0
  tiempoDeEspera = 0
  
  def __init__(self,numeroDeReserva,dias,cuarto,hora,fecha,personas,atendido,reserva,tiempo):
    self.numeroDeReservacion = numeroDeReserva
    self.diasDeHospedaje = dias
    self.tipoDeCuarto = cuarto
    self.horaLlegada = hora
    self.diaLlegada = fecha
    self.cantidadDePersonas = personas
    self.atendido = atendido
    self.hizoReservacion = reserva
    self.tiempoDeEspera = tiempo

class Cuarto:
  numeroDeCuarto = 0
  tipoDeCuarto = 0
  Ocupante = Reservacion(0,0,0,0,0,0,0,0,0)
  #booleano
  apartado = 0
  
  def __init__(self,numero,tipo,aparta,huesped):
    self.numeroDeCuarto = numero
    self.tipoDeCuarto = tipo
    self.apartado = aparta
    self.Ocupante = huesped

class clienteEnSpa:
  idServicio = 0
  tipoDeTratamiento = 0
  duracionTratamiento = 0
  tiempoDeEspera = 0
  atendido = 0

class prendaLavanderia:
  idLavanderia = 0
  tipoDePrenda = 0
  tipoDeServicio = 0
  atendido = 0

class clienteEnGym:
  tipoDeEntrenamiento = 0
  duracionEntrenamiento = 0
  tiempoDeEspera = 0
  ejercitado = 0

class mesaComedor:
  idMesa = 0
  capacidad = 0
  ocupacion = 0
  tiempoComida = 0
  atendido = 0
  tiempoDeEspera = 0

# variables para simulación
diasSimulados = 365
horasDeServicio = 12
totalDeHabitaciones = 100
habitacionesDisponibles = totalDeHabitaciones
habitacionesIndividualesTotales = 60
habitacionesDoblesTotales = 30
habitacionesSuiteTotales = 10
idReservacion = 0
totalDeHuespedes = 0
#lista de reservaciones
colaCheckIn = []
#lista de reservaciones
reservacionesFuturas = []
#lista de cuartos
habitaciones = []
#lista de clienteEnSpa
colaSpa = []
#lista de clienteEnSpa
servicioDeSpa = []
idSpa = 0
#lista de prendaLavanderia
colaLavanderia = []
idLavado = 0
#lista de clienteEnGym
colaGym = []
#lista de clienteEnGym
servicioDeGym = []
#lista de mesaComedor
mesasRestaurant = []
#lista de mesaComedor
colaRestaurant = []
personasEnColaYRestaurante = 0

#variables para costos
costoPorNocheIndividual = 1000
costoPorNocheDoble = 2000
costoPorNocheSuite = 3000
clientesQueAbandondanCheckIn = 0
gananciasDelDiaPorCheckIn = 0
gananciasTotalesPorCheckIn = 0
gananciasPerdidasDelDiaPorCheckIn = 0
gananciasPerdidasTotalesPorCheckIn = 0

costoTratamientoSpa = 100
gananciasDelDiaSpa = 0
gananciasPerdidasDelDiaPorSpa = 0
gananciasTotalesSpa = 0
gananciasPerdidasTotalesSpa = 0

gananciasDelDiaLavanderia = 0
gananciasTotalesLavanderia = 0

gananciasDiaRestaurante = 0
gananciasPerdidasDiaRestaurante = 0
gananciasTotalesRestaurante = 0
gananciasPerdidasTotalesRestaurante = 0
costoComidaPersona = 80

gananciasTotales = 0
gananciasPerdidasTotales = 0
balanceFinal = 0
#variables para costos

#funcion para sacar a las personas cuando termina su estancia en el hotel
def no_mas_dias (reservacion):
  return reservacion.diasDeHospedaje <= 0

#funcion para sacar a las personas de la cola cuando son atendidas
def fue_atendido (reservacion):
  return reservacion.atendido == 1

#funcion para sacar a las personas de la cola cuando pasa demasiado tiemmpo
def demasiada_espera (reservacion):
  generarPerdida(reservacion)
  return reservacion.tiempoDeEspera >= 4

def recibido_en_spa (cliente):
  return cliente.atendido == 1

def espera_spa (cliente):
  perdidasSpa(cliente)
  return cliente.tiempoDeEspera > 2

def recibido_lavanderia (prenda):
  return prenda.atendido == 1

def recibido_en_gym(cliente):
  return cliente.ejercitado == 1

def espera_restaurante(mesa):
  generarPerdidaComida(mesa)
  return mesa.tiempoDeEspera >= 2

def recibido_en_restaurante(mesa):
  return mesa.atendido == 1

#Llegada y servicio de Valet Parking del Hotel
def simulacionValet (colaAutosValet, llegadaMomentoValet, servicioMomentoValet):
  autosNoServidosValet = 0
  autosServidosValet = 0
  autosNoServidosValet = llegadaMomentoValet - servicioMomentoValet
  autosServidosValet = servicioMomentoValet - llegadaMomentoValet

  if (autosServidosValet < 0):
    autosServidosValet = servicioMomentoValet
  else:
    autosServidosValet = llegadaMomentoValet

  if (autosNoServidosValet >= 0):
    colaAutosValet += autosNoServidosValet
  else:
    while(colaAutosValet > 0 and autosNoServidosValet < 0):
      colaAutosValet -= 1
      autosNoServidosValet += 1
      autosServidosValet += 1

  resultado = (autosServidosValet, colaAutosValet)

  return resultado

#Evaluación de la variable aleatoria exponencial para obtener el servicio de valet
def evaluarServicioValet (valorExponencial):
  servicio = 0

  if(valorExponencial >= 0.0 and valorExponencial < 0.25):
    servicio = 10
  elif (valorExponencial >= 0.25 and valorExponencial < 0.5):
    servicio = 20
  elif (valorExponencial >= 0.5 and valorExponencial < 0.75):
    servicio = 30
  else:
    servicio = 40

  return servicio

def estanciaHotel():
  return int(np.random.uniform(1,4))

def seleccionHabitacion():
  return np.random.exponential(3.5)

#Simulación de la llegada al checkin, servicio del checkin, y asignación de habitaciones, dias de hospedaje (uniforme)
def simulacionCheckin (tamanioColaCheckIn, llegadasCheckIn, servicioMomentoCheckIn, horaEntrada, diaEntrada):
  #DECLARACION DE VARIABLES GLOBALES PARA SU USO
  global habitacionesDisponibles
  global habitacionesIndividualesTotales
  global habitacionesDoblesTotales
  global habitacionesSuiteTotales
  global habitaciones
  global colaCheckIn
  global idReservacion
  global totalDeHuespedes
  global gananciasDelDiaPorCheckIn
  global costoPorNocheIndividual
  global costoPorNocheDoble
  global costoPorNocheSuite

  clientesNoServidosCheckIn = 0
  clientesServidosCheckIn = 0
  clientesNoServidosCheckIn = llegadasCheckIn - servicioMomentoCheckIn
  clientesServidosCheckIn = servicioMomentoCheckIn - llegadasCheckIn

  if (clientesServidosCheckIn < 0):
    clientesServidosCheckIn = servicioMomentoCheckIn
  else:
    clientesServidosCheckIn = llegadasCheckIn

  llegadasCheckIn2 = llegadasCheckIn

  while(llegadasCheckIn2 > 0):
    tiempoDeEstancia = estanciaHotel()
    tipoDeCuarto = evaluarTipoHabitacion(seleccionHabitacion())
    numeroDePersonas = personasPorReservacion(tipoDeCuarto)
    nuevoReservacion = Reservacion(0,tiempoDeEstancia,tipoDeCuarto,horaEntrada,diaEntrada,numeroDePersonas,0,0,0)
    colaCheckIn.append(nuevoReservacion)
    llegadasCheckIn2 -= 1

  it = 0
  while (habitacionesDisponibles > 0 and clientesServidosCheckIn > 0 and (not(not colaCheckIn)) and it != (len(colaCheckIn) - 1)):
    if (colaCheckIn[it].tipoDeCuarto == 1):
      i = 0
      #BOOLEANO
      saved = 0
      #SE USA VARIABLE GLOBAL habitacionesIndividualesTotales
      while ((not saved) and i < habitacionesIndividualesTotales):
        #SE USA VARIABLE GLOBAL habitaciones
        if(habitaciones[i].Ocupante.tipoDeCuarto == 0):
          idReservacion += 1
          colaCheckIn[it].numeroDeReservacion = idReservacion
          colaCheckIn[it].atendido = 1
          habitaciones[i].Ocupante = colaCheckIn[it]
          totalDeHuespedes += colaCheckIn[it].cantidadDePersonas
          habitacionesDisponibles -= 1
          #SE USAN VARIABLES GLOBALES
          gananciasDelDiaPorCheckIn += colaCheckIn[it].diasDeHospedaje * costoPorNocheIndividual
          saved = 1
        else:
          i += 1
      if (saved == 0):
        print("No hay lugar habitaciones individuales")

    elif (colaCheckIn[it].tipoDeCuarto == 2):
      i = habitacionesIndividualesTotales
      saved = 0
      #SE USAN VARIABLES GLOBALES
      while ((not saved) and i < habitacionesIndividualesTotales + habitacionesDoblesTotales):
        if(habitaciones[i].Ocupante.tipoDeCuarto == 0):
          idReservacion += 1
          colaCheckIn[it].numeroDeReservacion = idReservacion
          colaCheckIn[it].atendido = 1
          habitaciones[i].Ocupante = colaCheckIn[it]
          totalDeHuespedes += colaCheckIn[it].cantidadDePersonas
          habitacionesDisponibles -= 1
          #SE USAN VARIABLES GLOBALES
          gananciasDelDiaPorCheckIn += colaCheckIn[it].diasDeHospedaje * costoPorNocheDoble
          saved = 1
        else:
          i += 1
      if (saved == 0):
        print("No hay habitaciones dobles")

    elif (colaCheckIn[it].tipoDeCuarto == 3):
      #SE USAN VARIABLES GLOBALES
      i = habitacionesIndividualesTotales + habitacionesDoblesTotales
      saved = 0
      #SE USAN VARIABLES GLOBALES
      while ((not saved) and i < habitacionesIndividualesTotales + habitacionesDoblesTotales + habitacionesSuiteTotales):
        if (habitaciones[i].Ocupante.tipoDeCuarto == 0):
          idReservacion += 1
          colaCheckIn[it].numeroDeReservacion = idReservacion
          colaCheckIn[it].atendido = 1
          habitaciones[i].Ocupante = colaCheckIn[it]
          totalDeHuespedes += colaCheckIn[it].cantidadDePersonas
          habitacionesDisponibles -= 1
          gananciasDelDiaPorCheckIn += colaCheckIn[it].diasDeHospedaje * costoPorNocheSuite
          saved = 1
        else:
          i += 1
      if (saved == 0):
        print("No hay lugar suites")

    clientesServidosCheckIn -= 1
    it += 1

  colaCheckIn = [colaCheckIn[i] for i in range(len(colaCheckIn)) if not fue_atendido(colaCheckIn[i])]

  return

def evaluarServicioCheckIn (valorExponencial):
  servicio = 0

  if (valorExponencial >= 0.0 and valorExponencial < 0.25):
    servicio = 20
  elif (valorExponencial >= 0.25 and valorExponencial < 0.5):
    servicio = 30
  elif (valorExponencial >= 0.5 and valorExponencial < 0.75):
    servicio = 40
  else:
    servicio = 60

  return servicio

def evaluarTipoHabitacion (valorExponencial):
  habitacion = 0

  if (valorExponencial > 0 and valorExponencial <= 0.33):
    habitacion = 1
  elif (valorExponencial > 0.33 and valorExponencial <= 0.66):
    habitacion = 2
  else:
    habitacion = 3

  return habitacion

def estanciaHotel2():
  return int(np.random.uniform(1,5))

def diaLlegadaHotel(diaActual,diasSimulados):
  return int(np.random.uniform(diaActual,diasSimulados))

def horaLlegadaHotel():
  return int(np.random.uniform(12,23))

def reservacionesDiarias():
  return int(np.random.poisson(5))

def simulacionReservaciones (diaActual):
  global reservacionesFuturas
  global diasSimulados

  reservacionesGeneradas = reservacionesDiarias()
  tiempoEstancia = 0
  llegada = 0
  tipoDeCuarto = 0
  horaLlegada = 0

  for i in range(reservacionesGeneradas):
    tiempoEstancia = estanciaHotel2()
    #VARIABLE GLOBAL diasSimulados
    llegada = diaLlegadaHotel(diaActual,diasSimulados)
    tipoDeCuarto = evaluarTipoHabitacion(seleccionHabitacion())
    horaLlegada = horaLlegadaHotel()
    numeroDePersonas = personasPorReservacion(tipoDeCuarto)
    nuevaReservacion = Reservacion(0,tiempoEstancia,tipoDeCuarto,horaLlegada,llegada,numeroDePersonas,0,1,0)
    reservacionesFuturas.append(nuevaReservacion)

  return 

def asignarReservaciones (diaActual,horaActual):
  global colCheckIn
  global reservacionesFuturas
  reservacionesAsignadas = 0

  #VARIABLE GLOBAL reservacionesFuturas
  for i in range(len(reservacionesFuturas)):
    if (reservacionesFuturas[i].diaLlegada == diaActual and reservacionesFuturas[i].horaLlegada == horaActual):
      #VARIABLE GLOBAL colaCheckIn
      colaCheckIn.insert(0,reservacionesFuturas[i])
    reservacionesAsignadas += 1

  return reservacionesAsignadas

def personasPorReservacion(tipoDeCuarto):
  personas = 0

  if (tipoDeCuarto == 1): 
    personas = int(np.random.uniform(1,2))
  elif (tipoDeCuarto == 2):
    personas = int(np.random.uniform(2,4))
  else:
    personas = int(np.random.uniform(1,4))

  return personas

def generarPerdida(reservacion):
  #DECLARACION DE VARIABLES GLOBALES PARA SU USO
  global gananciasPerdidasDelDiaPorCheckIn
  global clientesQueAbandondanCheckIn

  if (reservacion.tiempoDeEspera >= 4):
    if(reservacion.tipoDeCuarto == 1):
      gananciasPerdidasDelDiaPorCheckIn += reservacion.diasDeHospedaje * costoPorNocheIndividual
    elif(reservacion.tipoDeCuarto == 2):
      gananciasPerdidasDelDiaPorCheckIn += reservacion.diasDeHospedaje * costoPorNocheDoble
    elif(reservacion.tipoDeCuarto == 3):
      gananciasPerdidasDelDiaPorCheckIn += reservacion.diasDeHospedaje * costoPorNocheSuite

    clientesQueAbandondanCheckIn += 1

  # print("perdidas = ",gananciasPerdidasDelDiaPorCheckIn)

  return

def llegadaSpa():
  return int(np.random.poisson(3))

def tipoDeServicioSpa():
  return np.random.exponential(3.5)

def servicioSpa():
  return np.random.exponential(4)

def simulacionSpa(diaActual, horaActual):
  #DECLARACION DE VARIABLES GLOBALES PARA SU USO
  global colaSpa
  global idSpa
  global gananciasDelDiaSpa

  llegadasSpa = llegadaSpa()
  servidoresSpa = evaluarSpa(servicioSpa())

  for i in range(len(servicioDeSpa)): 
    if (servicioDeSpa[i].duracionTratamiento <= 0):
      servicioDeSpa[i] = clienteEnSpa()

  for i in range(llegadasSpa):
    #TUPLA
    tipoDeTratamiento = evaluarServicioSpa(tipoDeServicioSpa())
    nuevoCliente = clienteEnSpa()
    nuevoCliente.tipoDeTratamiento = tipoDeTratamiento[0]
    nuevoCliente.duracionTratamiento = tipoDeTratamiento[1]
    nuevoCliente.tiempoDeEspera = 0
    nuevoCliente.atendido = 0
    nuevoCliente.idServicio = 0
    colaSpa.append(nuevoCliente)

  clientesServidosSpa = servidoresSpa

  it = 0
  while (clientesServidosSpa > 0 and (not(not colaSpa)) and it != (len(colaSpa) - 1)):
    it2 = 0
    servido = 0
    while (it2 != (len(servicioDeSpa) - 1) and servido == 0):
      if(servicioDeSpa[it2].duracionTratamiento == 0):
        idSpa += 1
        servicioDeSpa[it2] = colaSpa[it]
        servicioDeSpa[it2].idServicio = idSpa
        colaSpa[it].atendido = 1
        gananciasDelDiaSpa += servicioDeSpa[it2].duracionTratamiento * costoTratamientoSpa
        servido = 1
      else:
        it2 += 1

    it += 1
    clientesServidosSpa += 1

  colaSpa = [colaSpa[i] for i in range(len(colaSpa)) if not recibido_en_spa(colaSpa[i])]

  for i in range(len(colaSpa)):
    colaSpa[i].tiempoDeEspera += 1

  colaSpa = [colaSpa[i] for i in range(len(colaSpa)) if not espera_spa(colaSpa[i])]

  for i in range(len(servicioDeSpa)):
    servicioDeSpa[i].duracionTratamiento -= 1

  return

def evaluarServicioSpa (variableExponencial):
  tupla = (0,0)

  if (variableExponencial > 0 and variableExponencial <= 0.3333):
    tupla = (1,2)
  elif (variableExponencial > 0.3333 and variableExponencial <= 0.6666):
    tupla = (2,3)
  else:
    tupla = (3,4)
  
  return tupla

def evaluarSpa (variableExponencial):
  servidores = 0

  if (variableExponencial > 0 and variableExponencial <= 0.3333):
    servidores =  3
  elif (variableExponencial > 0.3333 and variableExponencial <= 0.6666):
    servidores = 4
  else:
    servidores = 5

  return servidores

def perdidasSpa(cliente):
  #DECLARACION DE VARIABLES GLOBALES PARA SU USO
  global gananciasPerdidasDelDiaPorSpa

  if (cliente.tiempoDeEspera >= 2):
    gananciasPerdidasDelDiaPorSpa = gananciasPerdidasDelDiaPorSpa + cliente.duracionTratamiento * costoTratamientoSpa
  return

def llegadaLavanderia():
  return int(np.random.poisson(4))

def tipoDePrenda():
  return np.random.exponential(3.5)

def lavadoOTinto():
  return np.random.exponential(3.5)

def servicioLavanderia():
  return np.random.exponential(4)

def simulacionLavanderia(diaActual, horaActual):
  #DECLARACION DE VARIABLES GLOBALES PARA SU USO
  global colaLavanderia
  global gananciasDelDiaLavanderia
  global idLavado

  llegadasLavanderia = llegadaLavanderia()
  cantidadServicio = evaluarServicioLavanderia(servicioLavanderia())

  for i in range(llegadasLavanderia):
    tipoPrenda = evaluarTipoPrenda(tipoDePrenda())
    tipoDeServicio = evaluarTipoDeServicio(lavadoOTinto())
    nuevoCliente = prendaLavanderia()
    nuevoCliente.tipoDePrenda = tipoPrenda
    nuevoCliente.tipoDeServicio = tipoDeServicio
    nuevoCliente.idLavanderia = 0
    colaLavanderia.append(nuevoCliente)

  it = 0
  while (cantidadServicio > 0 and (not(not colaLavanderia)) and it != (len(colaLavanderia) - 1)):
    idLavado += 1
    colaLavanderia[it].idLavanderia = idLavado
    colaLavanderia[it].atendido = 1
    if (colaLavanderia[it].tipoDePrenda == 1):
      if (colaLavanderia[it].tipoDeServicio == 1):
        gananciasDelDiaLavanderia += 50
      elif (colaLavanderia[it].tipoDeServicio == 2):
        gananciasDelDiaLavanderia += 20

    elif (colaLavanderia[it].tipoDePrenda == 2):
      if (colaLavanderia[it].tipoDeServicio == 1):
        gananciasDelDiaLavanderia += 100
      elif (colaLavanderia[it].tipoDeServicio == 2):
        gananciasDelDiaLavanderia += 60

    elif (colaLavanderia[it].tipoDePrenda == 3):
      if (colaLavanderia[it].tipoDeServicio == 1):
        gananciasDelDiaLavanderia += 200
      elif (colaLavanderia[it].tipoDeServicio == 2):
        gananciasDelDiaLavanderia += 150

    cantidadServicio -= 1
    it += 1
    
  colaLavanderia = [colaLavanderia[i] for i in range(len(colaLavanderia)) if not recibido_lavanderia(colaLavanderia[i])]

  return

def evaluarTipoPrenda (valorExponencial):
  prenda = 0

  if (valorExponencial > 0 and valorExponencial <= 0.3333):
    prenda = 1
  elif (valorExponencial > 0.3333 and valorExponencial <= 0.6666):
    prenda = 2
  else:
    prenda = 3

  return prenda

def evaluarTipoDeServicio (valorExponencial):
  servicio = 0

  if (valorExponencial > 0 and valorExponencial <= 0.5):
    servicio = 1
  elif (valorExponencial > 0.5):
    servicio = 2

  return servicio

def evaluarServicioLavanderia (valorExponencial):
  servicio = 0

  if (valorExponencial > 0 and valorExponencial <= 0.25):
    servicio = 2
  elif (valorExponencial > 0.25 and valorExponencial <= 0.5):
    servicio = 4
  elif (valorExponencial > 0.5 and valorExponencial <= 0.75):
    servicio = 6
  else:
    servicio = 8

  return servicio

def llegadaGym():
  return int(np.random.poisson(3))

def tipoDeServicioGym():
  return np.random.exponential(3.5)

def servicioGym():
  return np.random.exponential(4)

def simulacionGym(diaActual,horaActual):
  global colaGym
  global servicioDeGym

  llegadasGym = llegadaGym()
  servidoresGym = evaluarGym(servicioGym())

  for it in range(len(servicioDeGym)):
    if (servicioDeGym[it].duracionEntrenamiento <= 0):
      servicioDeGym[it] = clienteEnGym()

  for i in range(llegadasGym):
    #TUPLA
    tipoDeEntrenamiento = evaluarServicioGym(tipoDeServicioGym())
    nuevoCliente = clienteEnGym()
    nuevoCliente.tipoDeEntrenamiento = tipoDeEntrenamiento[0]
    nuevoCliente.duracionEntrenamiento = tipoDeEntrenamiento[1]
    nuevoCliente.tiempoDeEspera = 0
    nuevoCliente.ejercitado = 0
    colaGym.append(nuevoCliente)

  i = 0
  clientesServidosGym = servidoresGym
  while (clientesServidosGym > 0 and (not(not colaGym)) and i != (len(colaGym) - 1)):
    i2 = 0
    servido = 0

    while (i2 != (len(servicioDeGym) - 1) and servido == 0):
      if (servicioDeGym[0].duracionEntrenamiento == 0):
        servicioDeGym[0] = colaGym[i]
        colaGym[i].ejercitado = 1
        servido = 1
      else:
        i2 += 1
    i += 1
    clientesServidosGym += 1

  colaGym = [colaGym[i] for i in range(len(colaGym)) if not recibido_en_gym(colaGym[i])]

  for i in range(len(colaGym)):
    colaGym[i].tiempoDeEspera += 1

  for i in range(len(servicioDeGym)):
    servicioDeGym[i].duracionEntrenamiento -= 1

  return

def evaluarServicioGym (variableExponencial):
  tupla = (0,0)

  if (variableExponencial > 0 and variableExponencial <= 0.3333):
    tupla = (1,2)
  elif (variableExponencial > 0.3333 and variableExponencial <= 0.6666):
    tupla = (2,3)
  else:
    tupla = (3,4)

  return tupla

def evaluarGym (variableExponencial):
  servidores = 0

  if (variableExponencial > 0 and variableExponencial <= 0.3333):
    servidores = 2
  elif (variableExponencial > 0.3333 and variableExponencial <= 0.6666):
    servidores = 3
  else:
    servidores = 5

  return servidores

def llegadaRestaurante():
  return int(np.random.poisson(30))

def tamanioMesa():
  return np.random.exponential(3.5)

def tiempoOcupado():
  return np.random.exponential(3.5)

def simulacionRestaurante(diaActual,horaActual):
  #DECLARACION DE VARIABLES GLOBALES PARA SU USO
  global colaRestaurant
  global personasEnColaYRestaurante
  global mesasRestaurant
  global gananciasDiaRestaurante
  global costoComidaPersona

  noLoHagas = 0

  if (diaActual == 0 and horaActual < 13):
    noLoHagas = 1
  if (horaActual == 11 or horaActual == 18 or horaActual == 23):
    #eliminar los elementos de colaRestaurant
    del colaRestaurant[:]

    for i in range(len(mesasRestaurant)):
      mesasRestaurant[i].ocupacion = 0
      mesasRestaurant[i].atendido = 0
      mesasRestaurant[i].tiempoDeEspera = 0
      mesasRestaurant[i].tiempoComida = 0
    
    personasEnColaYRestaurante = 0
  elif (not noLoHagas):
    for i in range(len(mesasRestaurant)):
      if (mesasRestaurant[i].tiempoComida == 0):
        #VARIABLE GLOBAL personasEnColaYRestaurante
        personasEnColaYRestaurante -= mesasRestaurant[i].ocupacion

        mesasRestaurant[i].ocupacion = 0
        mesasRestaurant[i].atendido = 0
        mesasRestaurant[i].tiempoDeEspera = 0
        mesasRestaurant[i].tiempoComida = 0

    gruposQueLlegan = llegadaRestaurante()

    for i in range(gruposQueLlegan):
      numeroDeComensales = validarComensales(tamanioMesa())
      estanciaMesa = validarEstanciaMesa(tiempoOcupado())
      nuevaMesa = mesaComedor()
      nuevaMesa.idMesa = 0
      nuevaMesa.ocupacion = numeroDeComensales
      nuevaMesa.atendido = 0
      nuevaMesa.tiempoDeEspera = 0
      nuevaMesa.tiempoComida = estanciaMesa

      #VARIABLE GLOBAL colaRestaurant
      colaRestaurant.append(nuevaMesa)

    i = 0
    while ((not(not colaRestaurant)) and i != (len(colaRestaurant) - 1)):
      if (colaRestaurant[i].ocupacion <= 2):
        ingresa = 0
        i2 = 0

        while(i2 != (len(mesasRestaurant) - 1) and ingresa == 0):
          if(mesasRestaurant[i2].ocupacion == 0 and mesasRestaurant[i2].capacidad == 2):
            #VARIABLE GLOBAL mesasRestaurant
            mesasRestaurant[i2].ocupacion = colaRestaurant[i].ocupacion
            mesasRestaurant[i2].tiempoDeEspera = 0
            mesasRestaurant[i2].tiempoComida = colaRestaurant[i].tiempoComida
            colaRestaurant[i].atendido = 1

            #VARIABLE GLOBAL personasEnColaYRestaurante
            personasEnColaYRestaurante += mesasRestaurant[i2].ocupacion
            gananciasDiaRestaurante += costoComidaPersona * mesasRestaurant[i2].ocupacion
            ingresa = 1
          else:
            i2 += 1
      else:
        ingresa = 0
        i2 = 0
        while(i2 != (len(mesasRestaurant) - 1) and ingresa == 0):
          if (mesasRestaurant[i2].ocupacion == 0 and mesasRestaurant[i2].capacidad == 4):
            mesasRestaurant[i2].ocupacion = colaRestaurant[i].ocupacion
            mesasRestaurant[i2].tiempoDeEspera = 0
            mesasRestaurant[i2].tiempoComida = colaRestaurant[i].tiempoComida
            colaRestaurant[i].atendido = 1

            #VARIABLE GLOBAL personasEnColaYRestaurante
            personasEnColaYRestaurante += mesasRestaurant[i2].ocupacion
            #VARIABLE GLOBAL gananciasDiaRestaurante
            gananciasDiaRestaurante += costoComidaPersona * mesasRestaurant[i2].ocupacion
            ingresa = 1
          else:
            i2 += 1
      i+= 1

    #VARIABLE GLOBAL colaRestaurant
    colaRestaurant = [colaRestaurant[i] for i in range(len(colaRestaurant)) if not recibido_en_restaurante(colaRestaurant[i])]

    for i in range(len(colaRestaurant)):
      colaRestaurant[i].tiempoDeEspera += 1

    #VARIABLE GLOBAL colaRestaurant
    colaRestaurant = [colaRestaurant[i] for i in range(len(colaRestaurant)) if not espera_restaurante(colaRestaurant[i])]

    for i in range(len(mesasRestaurant)):
      mesasRestaurant[i].tiempoComida -= 1

  return

def validarComensales (variableExponencial):
  comensales = 0

  if (variableExponencial > 0 and variableExponencial <= 0.25):
    comensales = 1
  elif(variableExponencial > 0.25 and variableExponencial <= 0.5):
    comensales = 2
  elif(variableExponencial > 0.5 and variableExponencial <= 0.75):
    comensales = 3
  else:
    comensales = 4

  return comensales

def validarEstanciaMesa (variableExponencial):
  estanciaMesa = 0

  if (variableExponencial > 0 and variableExponencial <= 0.5):
    estanciaMesa = 1
  else:
    estanciaMesa = 2

  return estanciaMesa

def generarPerdidaComida(mesaComedor):
  #DECLARACION DE VARIABLES GLOBALES PARA SU USO
  global personasEnColaYRestaurante
  global gananciasPerdidasDiaRestaurante
  global costoComidaPersona

  if (mesaComedor.tiempoDeEspera >= 2):
    personasEnColaYRestaurante -= mesaComedor.ocupacion
    gananciasPerdidasDiaRestaurante += mesaComedor.ocupacion * costoComidaPersona

  return

def llegadaValet():
  return int(np.random.poisson(10))

def servicioValet():
  return np.random.exponential(4.0)

def servicioCheckIn():
  return np.random.exponential(4.0)


def main():
  #DECLARACION DE LAS VARIABLES GLOBALES PARA USARLAS
  global gananciasDelDiaPorCheckIn
  global gananciasTotalesPorCheckIn
  global gananciasPerdidasDelDiaPorCheckIn
  global gananciasPerdidasTotalesPorCheckIn
  global gananciasDelDiaSpa
  global gananciasTotalesSpa
  global gananciasPerdidasDelDiaPorSpa
  global gananciasPerdidasTotalesSpa
  global gananciasDelDiaLavanderia
  global gananciasTotalesLavanderia
  global gananciasDiaRestaurante
  global gananciasTotalesRestaurante
  global gananciasPerdidasDiaRestaurante
  global gananciasPerdidasTotalesRestaurante
  global colaCheckIn
  global totalDeHuespedes
  global totalDeHabitaciones
  global habitaciones
  global habitacionesDisponibles
  global servicioDeSpa
  global servicioDeGym
  global mesasRestaurant
  global diasSimulados
  global idReservacion

  #For para llenar la lista de habitaciones y generar la cantidad de habitaciones señaladas en la variables
  for i in range(totalDeHabitaciones):
    if (i >= 0 and i < habitacionesIndividualesTotales):
      nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0)
      nuevoCuarto = Cuarto(i+1,1,0,nuevoReservacion)
      habitaciones.append(nuevoCuarto)

    #USO DE VARIABLES GLOBALES
    elif (i >= habitacionesIndividualesTotales and i < habitacionesIndividualesTotales + habitacionesDoblesTotales):
      nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0)
      nuevoCuarto = Cuarto(i+1,2,0,nuevoReservacion)
      habitaciones.append(nuevoCuarto)
      
    #USO DE VARIABLES GLOBALES
    elif (i >= habitacionesIndividualesTotales + habitacionesDoblesTotales and i < habitacionesIndividualesTotales + habitacionesDoblesTotales + habitacionesSuiteTotales ):
      nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0)
      nuevoCuarto = Cuarto(i+1,3,0,nuevoReservacion)
      habitaciones.append(nuevoCuarto)

  #se crea un cliente en spa genérico
  ejemplo = clienteEnSpa()
  #se llena con 5 clientes el spa
  for i in range(5):
    #VARIABLE GLOBAL servicioDeSpa
    servicioDeSpa.append(ejemplo)

  #se crea un cliente en gym genérico
  clientazo = clienteEnGym()
  #se llena con 5 clientes el gym
  for i in range(5):
    #VARIABLE GLOBAL servicioDeGym
    servicioDeGym.append(clientazo)

  #hay 30 mesas en el restaurante
  for i in range(30):
    #las primeras 20 son de capacidad 2
    if (i >= 0 and i < 20):
      nuevaMesa = mesaComedor()
      nuevaMesa.idMesa = i
      nuevaMesa.capacidad = 2
      #VARIABLE GLOBAL mesasRestaurant
      mesasRestaurant.append(nuevaMesa)
    #las ultimas 10 son de capacidad 4
    elif (i >= 20 and i <= 29):
      nuevaMesa = mesaComedor()
      nuevaMesa.idMesa = i
      nuevaMesa.capacidad = 4
      #VARIABLE GLOBAL mesasRestaurant
      mesasRestaurant.append(nuevaMesa)

  # Inicio de elementos de la simulacion del servicio del valet parking
  llegadaMomentoValet = 0
  servicioMomentoValet = 0
  #TUPLA
  serviciosValetcolaValet = (0,0)
  #Final de elementos de la simulacion del servico del valet parking

  #Inicio de elementos de la simulacion del check-in del Hotel
  clientesEntrantes = 0
  servicioMomentoCheckIn = 0
  #USO DE VARIABLE GLOBAL totalDeHabitaciones
  cuartosDisponibles = totalDeHabitaciones
  #Final de elementos de la simulacion del check-in del Hotel

  # #For para simular cada día
  for j in range(diasSimulados):
    print("Día: ",j+1)
    #Funcion para generar un numero aleatorio de reservaciones futuras diarias
    simulacionReservaciones(j)

    #For para simular cada hora
    for i in range(24):
      if(i >= 6 and i <= 11):
        simulacionRestaurante(j,i)
      if (i >= 13 and i <= 18):
        simulacionRestaurante(j,i)
      if (i >=19 and i <= 23):
        simulacionRestaurante(j,i)
      if (i >= 10 and i <= 17):
        simulacionLavanderia(j,i)
      if (i == 11):
        clientesCheckout = 0
        #For para revisa si el cliente hospedado ya debe irse y dejar al habitación disponible
        for it in range(len(habitaciones)):
          if (habitaciones[it].Ocupante.diasDeHospedaje <= 0 and habitaciones[it].Ocupante.numeroDeReservacion != 0):
            cuarto = habitaciones[it].Ocupante.tipoDeCuarto
            totalDeHuespedes -= habitaciones[it].Ocupante.cantidadDePersonas
            nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0)
            habitaciones[it].Ocupante = nuevoReservacion
            clientesCheckout += 1
            habitacionesDisponibles += 1

      if (i >= 12):
        if (i <= 18):
          simulacionSpa(j,i)
          simulacionGym(j,i)
        print("Hora: ", i, ":00")

        #Se consigue el numero de reservaciones que llegan ese momento para restarse después al servicio ya que tienen prioridad
        reservacionesAsignadas = asignarReservaciones(j,i)

        #Inicio Servicio de Valet
        llegadaMomentoValet = llegadaValet() # Variable aleatoria para generar clientes llegan al valet
        servicioMomentoValet = evaluarServicioValet(servicioValet()) # Variable aleatoria para generar cuantos servidores hay en el valet
        serviciosValetcolaValet = simulacionValet(serviciosValetcolaValet[1],llegadaMomentoValet,servicioMomentoValet)
        #Fin Servicio de Valet

        #Clientes que entran al hotel
        clientesEntrantes = serviciosValetcolaValet[0]

        #Se restan las reservaciones a los clientes entrantes par adarles prioridad a estso y después atender a los que no tienen reservación
        clientesEntrantes = clientesEntrantes - reservacionesAsignadas

        #Inicio Servicio de CheckIn
        servicioMomentoCheckIn = evaluarServicioCheckIn(servicioCheckIn()) #Variable aleatoria para generar cuantos servidores hay en el checkin
        simulacionCheckin(len(colaCheckIn),clientesEntrantes,servicioMomentoCheckIn,i,j)
        #Fin Servicio de CheckIn
      
      for i in range(len(colaCheckIn)):
        colaCheckIn[i].tiempoDeEspera += 1
        
      colaCheckIn = [colaCheckIn[i] for i in range(len(colaCheckIn)) if not demasiada_espera(colaCheckIn[i])]

    #Última oportunidad de registrar a los clientes
    if (not(not colaCheckIn)):
      for it in range(len(colaCheckIn)):
        #nuevoReservacion = colaCheckIn[it]
        if (colaCheckIn[it].tipoDeCuarto == 1):
          i = 0
          saved = 0
          #USO DE VARIABLE GLOBAL habitacionesIndividualesTotales
          while (not saved and i < habitacionesIndividualesTotales):
            if (habitaciones[i].Ocupante.tipoDeCuarto == 0):
              idReservacion += 1
              colaCheckIn[it].numeroDeReservacion = idReservacion
              colaCheckIn[it].atendido = 1
              habitaciones[i].Ocupante = colaCheckIn[it]
              #USO DE VARIABLE GLOBAL totalDeHuespedes
              totalDeHuespedes += colaCheckIn[it].cantidadDePersonas
              #USO DE VARIABLE GLOBAL habitacionesDisponibles
              habitacionesDisponibles -= 1
              #USO DE VARIABLES GLOBALES
              gananciasDelDiaPorCheckIn += colaCheckIn[it].diasDeHospedaje * costoPorNocheIndividual
              saved = 1
            else:
              i += 1
          if (saved == 0):
            print("No hay habitaciones individuales")

        elif (colaCheckIn[it].tipoDeCuarto == 2):
          #USO DE VARIABLE GLOBAL habitacionesIndividualesTotales
          i = habitacionesIndividualesTotales
          saved = 0
          #USO DE VARIABLES GLOBALES
          while (not saved and i < habitacionesIndividualesTotales + habitacionesDoblesTotales):
            if (habitaciones[i].Ocupante.tipoDeCuarto == 0):
              idReservacion += 1
              colaCheckIn[it].numeroDeReservacion = idReservacion
              colaCheckIn[it].atendido = 1
              habitaciones[i].Ocupante = colaCheckIn[it]
              #USO DE VARIABLE GLOBAL totalDeHuespedes
              totalDeHuespedes += colaCheckIn[it].cantidadDePersonas
              #USO DE VARIABLE GLOBAL habitacionesDisponibles
              habitacionesDisponibles -= 1
              #USO DE VARIABLE GLOBAL gananciasDelDiaPorCheckIn
              gananciasDelDiaPorCheckIn += colaCheckIn[it].diasDeHospedaje * costoPorNocheDoble
              saved = 1
            else:
              i += 1
          if (saved == 0):
            print("No hay habitaciones dobles")

        elif (colaCheckIn[it].tipoDeCuarto == 3):
          #USO DE VARIABLES GLOBALES
          i = habitacionesIndividualesTotales + habitacionesDoblesTotales
          saved = 0
          while (not saved and i < habitacionesIndividualesTotales + habitacionesDoblesTotales + habitacionesSuiteTotales):
            if(habitaciones[i].Ocupante.tipoDeCuarto == 0):
              idReservacion += 1
              colaCheckIn[it].numeroDeReservacion = idReservacion
              colaCheckIn[it].atendido = 1
              habitaciones[i].Ocupante = colaCheckIn[it]
              totalDeHuespedes += colaCheckIn[it].cantidadDePersonas
              habitacionesDisponibles -= 1
              gananciasDelDiaPorCheckIn += colaCheckIn[it].diasDeHospedaje * costoPorNocheSuite
              saved = 1
            else:
              i += 1
          if (saved == 0):
            print("No hay suites")

    colaCheckIn = [colaCheckIn[i] for i in range(len(colaCheckIn)) if not fue_atendido(colaCheckIn[i])]

    #Se vacía la cola al finalizar el día porque no se pueden quedar ahí nada más los clientes
    colaCheckIn = []

    #Se le resta la noche a los clientes al terminar el día para que después se revise en el checkout
    for it in range(len(habitaciones)):
      habitaciones[it].Ocupante.diasDeHospedaje -= 1

    #Escritura en pantalla
    print("Finanzas del Día: ",j+1)
    print("Ganancias del Día Por CheckIn: ",gananciasDelDiaPorCheckIn)
    gananciasTotalesPorCheckIn += gananciasDelDiaPorCheckIn
    gananciasDelDiaPorCheckIn = 0
    # print("Ganancias Perdidas del Día Por CheckIn: ",gananciasPerdidasDelDiaPorCheckIn)
    # gananciasPerdidasTotalesPorCheckIn += gananciasPerdidasDelDiaPorCheckIn
    # gananciasPerdidasDelDiaPorCheckIn = 0
    print("Ganancias del Día por Spa: ", gananciasDelDiaSpa)
    gananciasTotalesSpa += gananciasDelDiaSpa
    gananciasDelDiaSpa = 0
    # print("Ganancias Perdidas del Día por Spa: ",gananciasPerdidasDelDiaPorSpa)
    # gananciasPerdidasTotalesSpa += gananciasPerdidasDelDiaPorSpa
    # gananciasPerdidasDelDiaPorSpa = 0
    print("Ganancias del Día por Lavanderia: ",gananciasDelDiaLavanderia)
    gananciasTotalesLavanderia += gananciasDelDiaLavanderia
    gananciasDelDiaLavanderia = 0
    print("Ganancias del Día por Restaurante: ",gananciasDiaRestaurante)
    gananciasTotalesRestaurante += gananciasDiaRestaurante
    gananciasDiaRestaurante = 0
    # print("Ganancias Perdidas del Día por Restaurante: ",gananciasPerdidasDiaRestaurante)
    # gananciasPerdidasTotalesRestaurante += gananciasPerdidasDiaRestaurante
    # gananciasPerdidasDiaRestaurante = 0
    print("-----------------------------------------------------------------------------")

  gananciasTotales = gananciasTotalesPorCheckIn + gananciasTotalesSpa + gananciasTotalesLavanderia + gananciasTotalesRestaurante
  gananciasPerdidasTotales = gananciasPerdidasTotalesPorCheckIn + gananciasPerdidasTotalesSpa + gananciasPerdidasTotalesRestaurante

  #Escritura en pantalla
  print("-----------------------------------------------------------------------------")
  print("Ganancias Totales por CheckIn: ",gananciasTotalesPorCheckIn)
  # print("Ganancias Perdidas Totales por CheckIn: ",gananciasPerdidasTotalesPorCheckIn)
  print("Ganancias Totales por Spa: ",gananciasTotalesSpa)
  # print("Ganancias Perdidas Totales por Spa: ",gananciasPerdidasTotalesSpa)
  print("Ganancias Totales por Lavanderia: ",gananciasTotalesLavanderia)
  print("Ganancias Totales por Restaurante: ",gananciasTotalesRestaurante)
  # print("Ganancias Perdidas Totales por Restaurante: ",gananciasPerdidasTotalesRestaurante)
  print("-----------------------------------------------------------------------------")
  print("Ganancias Totales: ",gananciasTotales)
  # print("Ganancias Perdidas Totales: ",gananciasPerdidasTotales)
  print("Total de huespedes: ", totalDeHuespedes)
#FIN DEL MAIN

if __name__ == "__main__":
    main()