import numpy as np


class clienteEnSpa:
	idServicio = 0
	tipoDeTratamiento = 0
	duracionTratamiento = 0
	tiempoDeEspera = 0
	atendido = 0

class prendaLavanderia
  idLavanderia = 0
  tipoDePrenda = 0
  tipoDeServicio = 0
  atendido = 0

class clienteEnGym
  tipoDeEntrenamiento = 0
  duracionEntrenamiento = 0
  tiempoDeEspera = 0
  ejercitado = 0

class mesaComedor
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
# variables para simulación

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
  perdidasSpa(cliente);
  
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
      colaAutosValet = colaAutosValet - 1
      autosNoServidosValet = autosNoServidosValet + 1
      autosServidosValet = autosServidosValet + 1

  resultado = (autosServidosValet, colaAutosValet)

  return resultado
}

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
  return np.random.uniform(1,4)

def seleccionHabitacion():
  return np.random.exponential(3.5)

#Simulación de la llegada al checkin, servicio del checkin, y asignación de habitaciones, dias de hospedaje (uniforme)
def simulacionCheckin (tamanioColaCheckIn, llegadasCheckIn, servicioMomentoCheckIn, horaEntrada, diaEntrada):
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
    tiempoDeEstancia = estanciaHotel();
    tipoDeCuarto = evaluarTipoHabitacion(seleccionHabitacion())
    numeroDePersonas = personasPorReservacion(tipoDeCuarto)
    #IMPORTANTE PARA RESERVACION
    #Reservacion nuevoReservacion = Reservacion(0,tiempoDeEstancia,tipoDeCuarto,horaEntrada,diaEntrada,numeroDePersonas,0,0,0);
    #colaCheckIn.append(nuevoReservacion);
    llegadasCheckIn2 = llegadasCheckIn2 - 1
  }

  std::list<Reservacion>::iterator it = colaCheckIn.begin()
  it = 0
  while (habitacionesDisponibles > 0 and clientesServidosCheckIn > 0 and (not colaCheckIn) and it != (len(colaCheckIn) - 1)):
    #INCREMENTAR it
    nuevoReservacion = colaCheckIn[it]
    if (nuevoReservacion.tipoDeCuarto == 1):
      int i = 0
      #BOOLEANO
      saved = 0
      #SE USA VARIABLE GLOBAL habitacionesIndividualesTotales
      while ((not saved) and i < habitacionesIndividualesTotales):
        #SE USA VARIABLE GLOBAL habitaciones
        if(habitaciones[i].Ocupante.tipoDeCuarto == 0):
          idReservacion = idReservacion + 1
          nuevoReservacion.numeroDeReservacion = idReservacion
          nuevoReservacion.atendido = 1
          # (*it).atendido = 1
          habitaciones[i].Ocupante = nuevoReservacion
          totalDeHuespedes = totalDeHuespedes + nuevoReservacion.cantidadDePersonas
          habitacionesDisponibles = habitacionesDisponibles - 1
          #SE USAN VARIABLES GLOBALES
          gananciasDelDiaPorCheckIn = gananciasDelDiaPorCheckIn + nuevoReservacion.diasDeHospedaje * costoPorNocheIndividual
          saved = 1
        else:
          i = i + 1

      if (saved == 0):
        print("No hay lugar habitaciones individuales")

    elif (nuevoReservacion.tipoDeCuarto == 2):
      i = habitacionesIndividualesTotales
      saved = 0
      #SE USAN VARIABLES GLOBALES
      while ((not saved) and i < habitacionesIndividualesTotales + habitacionesDoblesTotales):
        if(habitaciones[i].Ocupante.tipoDeCuarto == 0):
          idReservacion = idReservacion + 1
          nuevoReservacion.numeroDeReservacion = idReservacion
          nuevoReservacion.atendido = 1
          #(*it).atendido = 1;
          habitaciones[i].Ocupante = nuevoReservacion
          totalDeHuespedes = totalDeHuespedes + nuevoReservacion.cantidadDePersonas
          habitacionesDisponibles = habitacionesDisponibles - 1
          #SE USAN VARIABLES GLOBALES
          gananciasDelDiaPorCheckIn = gananciasDelDiaPorCheckIn + nuevoReservacion.diasDeHospedaje * costoPorNocheDoble
          saved = true
        else:
          i = i + 1

      if (saved == 0):
        print("No hay habitaciones dobles")

    elif (nuevoReservacion.tipoDeCuarto == 3):
      #SE USAN VARIABLES GLOBALES
      i = habitacionesIndividualesTotales + habitacionesDoblesTotales
      saved = 0
      #SE USAN VARIABLES GLOBALES
      while ((not saved) and i < habitacionesIndividualesTotales + habitacionesDoblesTotales + habitacionesSuiteTotales):
        if (habitaciones[i].Ocupante.tipoDeCuarto == 0):
          idReservacion = idReservacion + 1
          nuevoReservacion.numeroDeReservacion = idReservacion
          nuevoReservacion.atendido = 1
          #(*it).atendido = 1;
          habitaciones[i].Ocupante = nuevoReservacion
          totalDeHuespedes = totalDeHuespedes + nuevoReservacion.cantidadDePersonas
          habitacionesDisponibles = habitacionesDisponibles - 1
          gananciasDelDiaPorCheckIn = gananciasDelDiaPorCheckIn + nuevoReservacion.diasDeHospedaje * costoPorNocheSuite
          saved = 1
        else:
          i = i + 1

      if (saved == 0):
        print("No hay lugar suites")

    clientesServidosCheckIn = clientesServidosCheckIn - 1
    it = it + 1

  global colaCheckin
  colaCheckIn = [elem for elem in colaCheckin if not fue_atendido(elem)]

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
  return np.random.uniform(1,5)

def diaLlegadaHotel(diaActual,diasSimulados):
  return np.random.uniform(diaActual,diasSimulados)

def horaLlegadaHotel():
  return np.random.uniform(12,23)

def reservacionesDiarias():
  return np.random.poisson(5)

def simulacionReservaciones (diaActual):
  reservacionesGeneradas = reservacionesDiarias()
  tiempoEstancia = 0
  llegada = 0
  tipoDeCuarto = 0
  horaLLegada = 0

  for i in range(reservacionesGeneradas):
    tiempoEstancia = estanciaHotel2();
    #SE USA VARIABLE GLOBAL diasSimulados
    llegada = diaLlegadaHotel(diaActual,diasSimulados);
    tipoDeCuarto = evaluarTipoHabitacion(seleccionHabitacion())
    horaLLegada = horaLLegadaHotel()
    numeroDePersonas = personasPorReservacion(tipoDeCuarto)
    #IMPORTANTE PARA RESERVACION
    # nuevaReservacion = Reservacion(0,tiempoEstancia,tipoDeCuarto,horaLLegada,llegada,numeroDePersonas,0,1,0)
    # reservacionesFuturas.append(nuevaReservacion)

  return 

def asignarReservaciones (diaActual,horaActual):
  reservacionesAsignadas = 0

  #SE USA VARIABLE GLOBAL reservacionesFuturas
  for it in reservacionesFuturas:
    if (it.diaLlegada == diaActual and it.horaLLegada == horaActual):
      #SE USA VARIABLE GLOBAL colaCheckIn
      colaCheckIn.insert(0,it)
    reservacionesAsignadas = reservacionesAsignadas + 1

  return reservacionesAsignadas

def personasPorReservacion(tipoDeCuarto):
  personas = 0

  if (tipoDeCuarto == 1): 
    personas = np.random.uniform(1,2)
  elif (tipoDeCuarto == 2):
    personas = np.random.uniform(2,4)
  else:
    personas = np.random.uniform(1,4)

  return personas

def generarPerdida(reservacion):
  if (reservacion.tiempoDeEspera >= 4):
    #SE USA VARIABLE GLOBAL gananciasPerdidasDelDiaPorCheckIn
    if(reservacion.tipoDeCuarto == 1):
      gananciasPerdidasDelDiaPorCheckIn = gananciasPerdidasDelDiaPorCheckIn + reservacion.diasDeHospedaje * costoPorNocheIndividual
    elif(reservacion.tipoDeCuarto == 2):
      gananciasPerdidasDelDiaPorCheckIn = gananciasPerdidasDelDiaPorCheckIn + reservacion.diasDeHospedaje * costoPorNocheDoble
    elif(reservacion.tipoDeCuarto == 3):
      gananciasPerdidasDelDiaPorCheckIn = gananciasPerdidasDelDiaPorCheckIn + reservacion.diasDeHospedaje * costoPorNocheSuite

    #SE USA VARIABLE GLOBAL clientesQueAbandondanCheckIn
    clientesQueAbandondanCheckIn = clientesQueAbandondanCheckIn + 1

  return

def llegadaSpa():
  return np.random.poisson(3)

def tipoServicioSpa():
  return np.random.exponential(3.5)

def servicioSpa():
  return np.random.exponential(4)

def simulacionSpa(diaActual, horaActual):
  llegadasSpa = llegadaSpa()
  servidoresSpa = evaluarSpa(servicioSpa())

  for cliente in servicioDeSpa: 
    if (cliente.duracionTratamiento <= 0):
      ejemplo = clienteEnSpa()
      ejemplo.tipoDeTratamiento = 0
      ejemplo.duracionTratamiento = 0
      ejemplo.tiempoDeEspera = 0
      ejemplo.atendido = 0
      ejemplo.idServicio = 0
      cliente = ejemplo;

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

  i = 0
  clientesServidosSpa = servidoresSpa

  it = 0
  while (clientesServidosSpa > 0 and (not colaSpa) and it != (len(colaSpa) - 1)):
    # nuevoCliente = colaSpa[it]
    it2 = 0
    servido = 0
    while (it2 != (len(servicioDeSpa) - 1) and servido == 0):
      if(servicioDeSpa[it2].duracionTratamiento == 0):
        idSpa = idSpa + 1
        servicioDeSpa[it2] = colaSpa[it]
        servicioDeSpa[it2].idServicio = idSpa
        colaSpa[it].atendido = 1
        gananciasDelDiaSpa = gananciasDelDiaSpa + servicioDeSpa[it2].duracionTratamiento * costoTratamientoSpa
        servido = 1
      else:
        it2 = it2 + 1

    it = it + 1
    clientesServidosSpa = clientesServidosSpa + 1

  global colaSpa
  colaSpa = [elem for elem in colaCheckin if not recibido_en_spa(elem)]

  for cliente in colaSpa:
    cliente.tiempoDeEspera = cliente.tiempoDeEspera + 1

  global colaSpa
  colaSpa = [elem for elem in colaCheckin if not espera_spa(elem)]

  for cliente in servicioDeSpa:
    cliente.duracionTratamiento = cliente.duracionTratamiento - 1

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
  if (cliente.tiempoDeEspera >= 2)
    gananciasPerdidasDelDiaPorSpa = gananciasPerdidasDelDiaPorSpa + cliente.duracionTratamiento * costoTratamientoSpa

  return

def llegadaLavanderia():
  return np.random.poisson(4)

def tipoPrenda():
  return np.random.exponential(3.5)

def lavadoOTinto():
  return np.random.exponential(3.5)

def servicioLavanderia():
  return np.random.exponential(4)

def simulacionLavanderia(diaActual, horaActual):
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

  i = 0

  it = 0
  # colaLavanderia
  while (cantidadServicio > 0 and (not colaLavanderia) and it != (len(colaLavanderia) - 1)):
    idLavado = idLavado + 1
    colaLavanderia[it].idLavanderia = idLavado
    colaLavanderia[it].atendido = 1
    if (colaLavanderia[it].tipoDePrenda == 1):
      if (colaLavanderia[it].tipoDeServicio == 1):
        gananciasDelDiaLavanderia = gananciasDelDiaLavanderia + 50
      elif (colaLavanderia[it].tipoDeServicio == 2):
        gananciasDelDiaLavanderia = gananciasDelDiaLavanderia + 20
    elif (colaLavanderia[it].tipoDePrenda == 2):
      if (colaLavanderia[it].tipoDeServicio == 1):
        gananciasDelDiaLavanderia = gananciasDelDiaLavanderia + 100
      elif (colaLavanderia[it].tipoDeServicio == 2):
        gananciasDelDiaLavanderia = gananciasDelDiaLavanderia + 60
    elif (colaLavanderia[it].tipoDePrenda == 3):
      if (colaLavanderia[it].tipoDeServicio == 1):
        gananciasDelDiaLavanderia = gananciasDelDiaLavanderia + 200
      elif ((*it).tipoDeServicio == 2):
        gananciasDelDiaLavanderia = gananciasDelDiaLavanderia + 150

    cantidadServicio = cantidadServicio - 1
    it = it + 1
  colaLavanderia.remove_if(recibido_lavanderia);

  return

def evaluarTipoPrenda (valorExponencial):
  prenda = 0

  if (valorExponencial > 0 && valorExponencial <= 0.3333):
    prenda = 1
  elif (valorExponencial > 0.3333 && valorExponencial <= 0.6666):
    prenda = 2
  else:
    prenda = 3

  return prenda


