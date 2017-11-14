import numpy as np


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

int main()
{
  //For para llenar la lista de habitaciones y generar la cantidad de habitaciones señaladas en la variables
  for (int i=0; i < totalDeHabitaciones; i++)
  {
    if (i >= 0 && i < habitacionesIndividualesTotales)
    {
      Reservacion nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0);
      Cuarto nuevoCuarto = Cuarto(i+1,1,false,nuevoReservacion);
      habitaciones.push_back(nuevoCuarto);
    }
    else if (i >= habitacionesIndividualesTotales && i < habitacionesIndividualesTotales+habitacionesDoblesTotales)
    {
      Reservacion nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0);
      Cuarto nuevoCuarto = Cuarto(i+1,2,false,nuevoReservacion);
      habitaciones.push_back(nuevoCuarto);
    }
    else if (i >= habitacionesIndividualesTotales+habitacionesDoblesTotales && i < habitacionesIndividualesTotales+habitacionesDoblesTotales+habitacionesSuiteTotales )
    {
      Reservacion nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0);
      Cuarto nuevoCuarto = Cuarto(i+1,3,false,nuevoReservacion);
      habitaciones.push_back(nuevoCuarto);
    }
  }

  clienteEnSpa ejemplo;
  ejemplo.tipoDeTratamiento = 0;
  ejemplo.duracionTratamiento = 0;
  ejemplo.tiempoDeEspera = 0;
  ejemplo.atendido = 0;
  ejemplo.idServicio = 0;

  for (int i=0; i<5; i++)
  {
    servicioDeSpa.push_back(ejemplo);
  }

  clienteEnGym clientazo;
  clientazo.tipoDeEntrenamiento = 0;
  clientazo.duracionEntrenamiento = 0;
  clientazo.tiempoDeEspera = 0;
  clientazo.ejercitado = 0;

  for(int i=0; i<5; i++)
  {
    servicioDeGym.push_back(clientazo);
  }

  for (int i=0; i<30;i++)
  {
    if (i>0 && i<20)
    {
      mesaComedor nuevaMesa;
      nuevaMesa.idMesa = i;
      nuevaMesa.capacidad = 2;
      nuevaMesa.ocupacion = 0;
      nuevaMesa.atendido = 0;
      nuevaMesa.tiempoDeEspera = 0;
      nuevaMesa.tiempoComida = 0;
      mesasRestaurant.push_back(nuevaMesa);
    }
    else if (i >=20 && i <= 29)
    {
      mesaComedor nuevaMesa;
      nuevaMesa.idMesa = i;
      nuevaMesa.capacidad = 4;
      nuevaMesa.ocupacion = 0;
      nuevaMesa.atendido = 0;
      nuevaMesa.tiempoDeEspera = 0;
      nuevaMesa.tiempoComida = 0;
      mesasRestaurant.push_back(nuevaMesa);
    }
  }

  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  std::default_random_engine generator(seed);

  // Inicio de elementos de la simulacion del servicio del valet parking
  std::poisson_distribution<int> llegadaValet(10);
  std::exponential_distribution<float> servicioValet(4);
  int llegadaMomentoValet = 0;
  int servicioMomentoValet = 0;
  std::pair<int,int> serviciosValetcolaValet (0,0);
  // Final de elementos de la simulacion del servico del valet parking

  // Inicio de elementos de la simulacion del check-in del Hotel
  int clientesEntrantes = 0;
  std::exponential_distribution<float> servicioCheckIn(4);
  int servicioMomentoCheckIn = 0;
  int cuartosDisponibles = totalDeHabitaciones;
  // Final de elementos de la simulacion del check-in del Hotel

  //logFinanciero.open("logFinanciero.txt");

  //For para simular cada día
  for (int j=0; j <= diasSimulados; j++)
  {
    //Inicia sección para generar los logs
    /*std::string nombreArchivo = "logsHabitaciones" + std::to_string(j) +".txt";
    std::string nombreArchivo2 = "logsColaCheckIn" + std::to_string(j) +".txt";
    std::string nombreArchivo3 = "logsReservaciones" + std::to_string(j) +".txt";
    std::string nombreArchivo4 = "logsSinReservaciones" + std::to_string(j) +".txt";
    std::string nombreArchivo5 = "logSpa" + std::to_string(j) + ".txt";
    std::string nombreArchivo6 = "logLavanderia" + std::to_string(j) + ".txt";
    std::string nombreArchivo7 = "logGym" + std::to_string(j) + ".txt";
    std::string nombreArchivo8 = "logRestaurante" + std::to_string(j) + ".txt";
    logsHabitaciones.open(nombreArchivo);
    logsColaCheckIn.open(nombreArchivo2);
    logsReservaciones.open(nombreArchivo3);
    logsSinReservacion.open(nombreArchivo4);
    logSpa.open(nombreArchivo5);
    logLavanderia.open(nombreArchivo6);
    logGym.open(nombreArchivo7);
    logRestaurante.open(nombreArchivo8);*/
    //Termina sección para generar los logs

    std::cout << "Día: " << j+1 << std::endl;

    //Funcion para generar un numero aleatorio de reservaciones futuras diarias
    simulacionReservaciones(j);

    //Se anota en el log las revervaciones futuras que se han generado hasta ese día
    /*logsReservaciones << "Reservaciones al día: " << j << "\n" << std::endl;
    for (std::list<Reservacion>::iterator it = reservacionesFuturas.begin(); it != reservacionesFuturas.end(); it++)
    {
      logsReservaciones << "Reservacion: Dia " << (*it).diaLlegada << "--- Hora " << (*it).horaLLegada << "\n--Tipo de habitacion: " << (*it).tipoDeCuarto << "\n--Tiempo de Estancia: " << (*it).diasDeHospedaje << "\n--Personas: " << (*it).cantidadDePersonas << "\n--Reservo Lugar: " << (*it).hizoReservacion << "\n" << std::endl;
    }
    logsReservaciones << "-----------------------------------------------------------------------------" << std::endl;
    logsReservaciones.close();*/

    //For para simular cada hora
    for (int i=0; i <= 23; i++)
    {
      if(i >= 6 && i <= 11)
      {
        simulacionRestaurante(j,i);
      }
      if (i >= 13 && i <= 18)
      {
        simulacionRestaurante(j,i);
      }
      if (i >=19 && i <= 23)
      {
        simulacionRestaurante(j,i);
      }
      if (i >= 10 && i <= 17)
      {
        simulacionLavanderia(j,i);
      }
      if (i==11)
      {
        //Se anota en el log como se encuentran las habitaciones antes del checkout para saber si alguien ya se tiene que ir
        /*logsHabitaciones << "Habitaciones al iniciar el Check-Out en el dia: " << j << "\n" << std::endl;
        for(std::vector<Cuarto>::iterator it = habitaciones.begin(); it != habitaciones.end(); it++)
        {
          logsHabitaciones << "Habitacion: " << (*it).numeroDeCuarto << "\n--Tipo de habitacion: " << (*it).tipoDeCuarto << "\n--Ocupante: " << (*it).Ocupante.numeroDeReservacion << "\n--Personas: " << (*it).Ocupante.cantidadDePersonas <<"\n--Tiempo de Estancia Restante: " << (*it).Ocupante.diasDeHospedaje << "\n--Reservo Lugar: " << (*it).Ocupante.hizoReservacion << "\n" << std::endl;
        }
        logsHabitaciones << "-----------------------------------------------------------------------------" << std::endl;*/

        int clientesCheckout = 0;

        //For para revisa si el cliente hospedado ya debe irse y dejar al habitación disponible
        for(std::vector<Cuarto>::iterator it = habitaciones.begin(); it != habitaciones.end(); it++)
        {
          if ((*it).Ocupante.diasDeHospedaje <= 0 && (*it).Ocupante.numeroDeReservacion != 0)
          {
            //std::string cuarto = ((*it).tipoDeCuarto);
            int cuarto = ((*it).Ocupante.tipoDeCuarto);
            totalDeHuespedes -= (*it).Ocupante.cantidadDePersonas;
            Reservacion nuevoReservacion = Reservacion(0,0,0,0,0,0,0,0,0);
            (*it).Ocupante = nuevoReservacion;
            //clientesHospedados.erase(it);
            clientesCheckout++;
            habitacionesDisponibles++;
          }
        }

        //Se anota en el log de habitaicones como queda al finalizar el checkout e iniciar el checkin para revisar que se hayan ido todos
        /*logsHabitaciones << "Habitaciones al finalizar el Check-Out e iniciar el CheckIn en el dia: " << j << "\n" << std::endl;
        for(std::vector<Cuarto>::iterator it = habitaciones.begin(); it != habitaciones.end(); it++)
        {
          logsHabitaciones << "Habitacion: " << (*it).numeroDeCuarto << "\n--Tipo de habitacion: " << (*it).tipoDeCuarto << "\n--Ocupante: " << (*it).Ocupante.numeroDeReservacion << "\n--Personas: " << (*it).Ocupante.cantidadDePersonas << "\n--Tiempo de Estancia Restante: " << (*it).Ocupante.diasDeHospedaje << "\n--Reservo Lugar: " << (*it).Ocupante.hizoReservacion << "\n" << std::endl;
        }
        logsHabitaciones << "-----------------------------------------------------------------------------" << std::endl;

        logsColaCheckIn << "Cola del CheckIn al finalizar el Check-Out e iniciar el CheckIn: " << j << "\n" << std::endl;
        for (std::list<Reservacion>::iterator it = colaCheckIn.begin(); it != colaCheckIn.end(); it++)
        {
          logsColaCheckIn << "Reservacion: Dia " << (*it).diaLlegada << "--- Hora " << (*it).horaLLegada << "\n--Tipo de habitacion: " << (*it).tipoDeCuarto << "\n--Personas: " << (*it).cantidadDePersonas << "\n--Reservo Lugar: " << (*it).hizoReservacion << "\n" << std::endl;
        }
        logsColaCheckIn << "-----------------------------------------------------------------------------" << std::endl;*/

        //std::cout << "Hora del Checkout, abandonan el hotel: " << clientesCheckout << " personas" << std::endl;
      }
      if (i >= 12)
      {
        if (i <= 18)
        {
          simulacionSpa(j,i);
        }
        std::cout << "Hora: " << i <<":00" << std::endl;

        //Se consigue el numero de reservaciones que llegan ese momento para restarse después al servicio ya que tienen prioridad
        int reservacionesAsignadas = asignarReservaciones(j,i);

        //Inicio Servicio de Valet
        llegadaMomentoValet = llegadaValet(generator); // Variable aleatoria para generar clientes llegan al valet
        servicioMomentoValet = evaluarServicioValet(servicioValet(generator)); // Variable aleatoria para generar cuantos servidores hay en el valet
        serviciosValetcolaValet = simulacionValet(serviciosValetcolaValet.second,llegadaMomentoValet,servicioMomentoValet);
        //Fin Servicio de Valet

        //Clientes que entran al hotel
        clientesEntrantes = serviciosValetcolaValet.first;

        //Se restan las reservaciones a los clientes entrantes par adarles prioridad a estso y después atender a los que no tienen reservación
        clientesEntrantes = clientesEntrantes - reservacionesAsignadas;

        //Inicio Servicio de CheckIn
        servicioMomentoCheckIn = evaluarServicioCheckIn(servicioCheckIn(generator)); // Variable aleatoria para generar cuantos servidores hay en el checkin
        simulacionCheckin(colaCheckIn.size(),clientesEntrantes,servicioMomentoCheckIn,i,j);
        //Fin Servicio de CheckIn
      }
      for (std::list<Reservacion>::iterator it = colaCheckIn.begin(); it != colaCheckIn.end(); it++)
      {
        (*it).tiempoDeEspera++;
      }
      colaCheckIn.remove_if(demasiada_espera);
    }

    //Se anota en los logs de habitaciones como quedan al finalizar el checkin del día
    /*logsHabitaciones << "Habitaciones al finalizar el Check-In en el dia: " << j << "\n" << std::endl;
    for(std::vector<Cuarto>::iterator it = habitaciones.begin(); it != habitaciones.end(); it++)
    {
      logsHabitaciones << "Habitacion: " << (*it).numeroDeCuarto << "\n--Tipo de habitacion: " << (*it).tipoDeCuarto << "\n--Ocupante: " << (*it).Ocupante.numeroDeReservacion << "\n--Tiempo de Estancia Restante: " << (*it).Ocupante.diasDeHospedaje << "\n--Personas: " << (*it).Ocupante.cantidadDePersonas << "\n--Reservo Lugar: " << (*it).Ocupante.hizoReservacion << "\n" << std::endl;
    }
    logsHabitaciones << "-----------------------------------------------------------------------------" << std::endl;
    logsHabitaciones.close();

    //Clientes que tienen una última oportunidad de entrar al hotel
    logsColaCheckIn << "Cola del CheckIn justo antes de finalizar el Check-In en el día: " << j << "\n" << std::endl;
    for (std::list<Reservacion>::iterator it = colaCheckIn.begin(); it != colaCheckIn.end(); it++)
    {
      logsColaCheckIn << "Reservacion: Dia " << (*it).diaLlegada << "--- Hora " << (*it).horaLLegada << "\n--Tipo de habitacion: " << (*it).tipoDeCuarto << "\n--Personas: " << (*it).cantidadDePersonas << "\n--Reservo Lugar: " << (*it).hizoReservacion << "\n--Espera: " << (*it).tiempoDeEspera << "\n" << std::endl;
    }
    logsColaCheckIn << "-----------------------------------------------------------------------------" << std::endl;*/

    //Última oportunidad de registrar a los clientes
    if(!colaCheckIn.empty())
    {
      for (std::list<Reservacion>::iterator it = colaCheckIn.begin(); it != colaCheckIn.end(); it++)
      {
        Reservacion nuevoReservacion = (*it);
        if (nuevoReservacion.tipoDeCuarto == 1)
        {
          int i = 0;
          bool saved = false;
          while (!saved && i < habitacionesIndividualesTotales)
          {
            if(habitaciones[i].Ocupante.tipoDeCuarto == 0)
            {
              idReservacion++;
              nuevoReservacion.numeroDeReservacion = idReservacion;
              nuevoReservacion.atendido = 1;
              (*it).atendido = 1;
              habitaciones[i].Ocupante = nuevoReservacion;
              totalDeHuespedes += nuevoReservacion.cantidadDePersonas;
              habitacionesDisponibles--;
              gananciasDelDiaPorCheckIn += nuevoReservacion.diasDeHospedaje * costoPorNocheIndividual;
              saved = true;
            }
            else
            {
              i++;
            }
          }
          if (saved == false)
          {
            std::cout << "No hay habitaciones individuales" << std::endl;
          }
        }
        else if (nuevoReservacion.tipoDeCuarto == 2)
        {
          int i = habitacionesIndividualesTotales;
          bool saved = false;
          while (!saved && i < habitacionesIndividualesTotales+habitacionesDoblesTotales)
          {
            if(habitaciones[i].Ocupante.tipoDeCuarto == 0)
            {
              idReservacion++;
              nuevoReservacion.numeroDeReservacion = idReservacion;
              nuevoReservacion.atendido = 1;
              (*it).atendido = 1;
              habitaciones[i].Ocupante = nuevoReservacion;
              totalDeHuespedes += nuevoReservacion.cantidadDePersonas;
              habitacionesDisponibles--;
              gananciasDelDiaPorCheckIn += nuevoReservacion.diasDeHospedaje * costoPorNocheDoble;
              saved = true;
            }
            else
            {
              i++;
            }
          }
          if (saved == false)
          {
            std::cout << "No hay habitaicones dobles" << std::endl;
          }
        }
        else if (nuevoReservacion.tipoDeCuarto == 3)
        {
          int i = habitacionesIndividualesTotales+habitacionesDoblesTotales;
          bool saved = false;
          while (!saved && i < habitacionesIndividualesTotales+habitacionesDoblesTotales+habitacionesSuiteTotales)
          {
            if(habitaciones[i].Ocupante.tipoDeCuarto == 0)
            {
              idReservacion++;
              nuevoReservacion.numeroDeReservacion = idReservacion;
              nuevoReservacion.atendido = 1;
              (*it).atendido = 1;
              habitaciones[i].Ocupante = nuevoReservacion;
              totalDeHuespedes += nuevoReservacion.cantidadDePersonas;
              habitacionesDisponibles--;
              gananciasDelDiaPorCheckIn += nuevoReservacion.diasDeHospedaje * costoPorNocheSuite;
              saved = true;
            }
            else
            {
              i++;
            }
          }
          if (saved == false)
          {
            std::cout << "No hay suites" << std::endl;
          }
        }
      }
    }

    colaCheckIn.remove_if(fue_atendido);

    //Se guarda en el log los clientes que se perdieron por llegar tarde
    /*logsColaCheckIn << "Cola del CheckIn al finalizar el Check-In en el día (Clientes de media noche): " << j << "\n" << std::endl;
    for (std::list<Reservacion>::iterator it = colaCheckIn.begin(); it != colaCheckIn.end(); it++)
    {
      logsColaCheckIn << "Reservacion: Dia " << (*it).diaLlegada << "--- Hora " << (*it).horaLLegada << "\n--Tipo de habitacion: " << (*it).tipoDeCuarto << "\n--Personas: " << (*it).cantidadDePersonas << "\n--Reservo Lugar: " << (*it).hizoReservacion << "\n--Espera: " << (*it).tiempoDeEspera << "\n" << std::endl;
    }
    logsColaCheckIn << "-----------------------------------------------------------------------------" << std::endl;
    logsColaCheckIn.close();*/

    //Se vacía la cola al finalizar el día porque no se pueden quedar ahí nada más los clientes
    colaCheckIn.clear();

    //Se le resta la noche a los clientes al terminar el día para que después se revise en el checkout
    for(std::vector<Cuarto>::iterator it = habitaciones.begin(); it != habitaciones.end(); it++)
    {
      (*it).Ocupante.diasDeHospedaje--;
    }

    //Escritura en Logs
    /*logFinanciero << "Finanzas del Día: " << j << std::endl;
    logFinanciero << "Ganancias del Día Por CheckIn: " << gananciasDelDiaPorCheckIn << std::endl;
    gananciasTotalesPorCheckIn += gananciasDelDiaPorCheckIn;
    gananciasDelDiaPorCheckIn = 0;
    logFinanciero << "Ganancias Perdidas del Día Por CheckIn: " << gananciasPerdidasDelDiaPorCheckIn << std::endl;
    gananciasPerdidasTotalesPorCheckIn += gananciasPerdidasDelDiaPorCheckIn;
    gananciasPerdidasDelDiaPorCheckIn = 0;
    logFinanciero << "Ganancias del Día por Spa: " << gananciasDelDiaSpa << std::endl;
    gananciasTotalesSpa += gananciasDelDiaSpa;
    gananciasDelDiaSpa = 0;
    logFinanciero << "Ganancias Perdidas del Día por Spa: " << gananciasPerdidasDelDiaPorSpa << std::endl;
    gananciasPerdidasTotalesSpa += gananciasPerdidasDelDiaPorSpa;
    gananciasPerdidasDelDiaPorSpa = 0;
    logFinanciero << "Ganancias del Día por Lavanderia: " << gananciasDelDiaLavanderia << std::endl;
    gananciasTotalesLavanderia += gananciasDelDiaLavanderia;
    gananciasDelDiaLavanderia = 0;
    logFinanciero << "Ganancias del Día por Restaurante: " << gananciasDiaRestaurante << std::endl;
    gananciasTotalesRestaurante += gananciasDiaRestaurante;
    gananciasDiaRestaurante = 0;
    logFinanciero << "Ganancias Perdidas del Día por Restaurante: " << gananciasPerdidasDiaRestaurante << std::endl;
    gananciasPerdidasTotalesRestaurante += gananciasPerdidasDiaRestaurante;
    gananciasPerdidasDiaRestaurante = 0;
    logFinanciero << "-----------------------------------------------------------------------------" << std::endl;
    logSpa.close();
    logLavanderia.close();
    logGym.close();
    logRestaurante.close();*/

    //Escritura en pantalla
    std::cout << "Finanzas del Día: " << j << std::endl;
    std::cout << "Ganancias del Día Por CheckIn: " << gananciasDelDiaPorCheckIn << std::endl;
    gananciasTotalesPorCheckIn += gananciasDelDiaPorCheckIn;
    gananciasDelDiaPorCheckIn = 0;
    std::cout << "Ganancias Perdidas del Día Por CheckIn: " << gananciasPerdidasDelDiaPorCheckIn << std::endl;
    gananciasPerdidasTotalesPorCheckIn += gananciasPerdidasDelDiaPorCheckIn;
    gananciasPerdidasDelDiaPorCheckIn = 0;
    std::cout << "Ganancias del Día por Spa: " << gananciasDelDiaSpa << std::endl;
    gananciasTotalesSpa += gananciasDelDiaSpa;
    gananciasDelDiaSpa = 0;
    std::cout << "Ganancias Perdidas del Día por Spa: " << gananciasPerdidasDelDiaPorSpa << std::endl;
    gananciasPerdidasTotalesSpa += gananciasPerdidasDelDiaPorSpa;
    gananciasPerdidasDelDiaPorSpa = 0;
    std::cout << "Ganancias del Día por Lavanderia: " << gananciasDelDiaLavanderia << std::endl;
    gananciasTotalesLavanderia += gananciasDelDiaLavanderia;
    gananciasDelDiaLavanderia = 0;
    std::cout << "Ganancias del Día por Restaurante: " << gananciasDiaRestaurante << std::endl;
    gananciasTotalesRestaurante += gananciasDiaRestaurante;
    gananciasDiaRestaurante = 0;
    std::cout << "Ganancias Perdidas del Día por Restaurante: " << gananciasPerdidasDiaRestaurante << std::endl;
    gananciasPerdidasTotalesRestaurante += gananciasPerdidasDiaRestaurante;
    gananciasPerdidasDiaRestaurante = 0;
    std::cout << "-----------------------------------------------------------------------------" << std::endl;

  }
  gananciasTotales = gananciasTotalesPorCheckIn + gananciasTotalesSpa + gananciasTotalesLavanderia + gananciasTotalesRestaurante;
  gananciasPerdidasTotales = gananciasPerdidasTotalesPorCheckIn + gananciasPerdidasTotalesSpa + gananciasPerdidasTotalesRestaurante;

  //Escritura en Logs
  /*logFinanciero << "-----------------------------------------------------------------------------" << std::endl;
  logFinanciero << "Ganancias Totales por CheckIn: " << gananciasTotalesPorCheckIn << std::endl;
  logFinanciero << "Ganancias Perdidas Totales por CheckIn: " << gananciasPerdidasTotalesPorCheckIn << std::endl;
  logFinanciero << "Ganancias Totales por Spa: " << gananciasTotalesSpa << std::endl;
  logFinanciero << "Ganancias Perdidas Totales por Spa: " << gananciasPerdidasTotalesSpa << std::endl;
  logFinanciero << "Ganancias Totales por Lavanderia: " << gananciasTotalesLavanderia << std::endl;
  logFinanciero << "Ganancias Totales por Restaurante: " << gananciasTotalesRestaurante << std::endl;
  logFinanciero << "Ganancias Perdidas Totales por Restaurante: " << gananciasPerdidasTotalesRestaurante << std::endl;
  logFinanciero << "-----------------------------------------------------------------------------" << std::endl;
  logFinanciero << "Ganancias Totales: " << gananciasTotales << std::endl;
  logFinanciero << "Ganancias Perdidas Totales: " << gananciasPerdidasTotales << std::endl;
  std::cout << totalDeHuespedes << '\n';
  logFinanciero.close();*/

  //Escritura en pantalla
  std::cout << "-----------------------------------------------------------------------------" << std::endl;
  std::cout << "Ganancias Totales por CheckIn: " << gananciasTotalesPorCheckIn << std::endl;
  std::cout << "Ganancias Perdidas Totales por CheckIn: " << gananciasPerdidasTotalesPorCheckIn << std::endl;
  std::cout << "Ganancias Totales por Spa: " << gananciasTotalesSpa << std::endl;
  std::cout << "Ganancias Perdidas Totales por Spa: " << gananciasPerdidasTotalesSpa << std::endl;
  std::cout << "Ganancias Totales por Lavanderia: " << gananciasTotalesLavanderia << std::endl;
  std::cout << "Ganancias Totales por Restaurante: " << gananciasTotalesRestaurante << std::endl;
  std::cout << "Ganancias Perdidas Totales por Restaurante: " << gananciasPerdidasTotalesRestaurante << std::endl;
  std::cout << "-----------------------------------------------------------------------------" << std::endl;
  std::cout << "Ganancias Totales: " << gananciasTotales << std::endl;
  std::cout << "Ganancias Perdidas Totales: " << gananciasPerdidasTotales << std::endl;
  std::cout << totalDeHuespedes << '\n';
}

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

  #CAMBIAR ESTO
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
  return np.random.poisson(3)

def tipoDeServicioGym():
  return np.random.exponential(3.5)

def servicioGym():
  return np.random.exponential(4)

def simulacionGym(diaActual,horaActual):
  int llegadasGym = llegadaGym()
  int servidoresGym = evaluarGym(servicioGym())

  for it in servicioGym:
    if (it.duracionEntrenamiento <= 0):
      clientazo = clienteGym()
      clientazo.tipoDeEntrenamiento = 0
      clientazo.duracionEntrenamiento = 0
      clientazo.tiempoDeEspera = 0
      clientazo.ejercitado = 0
      #CHECAR DEEP COPY
      it = clientazo

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
  cliente = colaGym[0]

  while (clientesServidosGym > 0 and (not colaGym) and i != (len(colaGym) - 1)):
    #CHECAR DEEP COPY
    nuevoCliente = colaGym[i]
    cliente2 = servicioDeGym[0]
    i2 = 0
    servido = 0

    while (i2 != (len(servicioDeGym) - 1) and servido == 0):
      if (cliente2.duracionEntrenamiento == 0):
        #CHECAR DEEP COPY
        cliente2 = cliente
        cliente.ejercitado = 1
        servido = 1
      else:
        i2 += 1
    i += 1
    clientesServidosGym += 1

  global colaGym
  colaGym = [elem for elem in colaGym if not recibido_en_gym(elem)]

  for cliente in colaGym:
    cliente.tiempoDeEspera += 1

  for cliente in servicioDeGym:
    cliente.duracionEntrenamiento -= 1

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
  return np.random.poisson(30)

def tamanioMesa():
  return np.random.exponential(3.5)

def tamanioOcupado():
  return np.random.exponential(3.5)

def simulacionRestaurante(diaActual,horaActual):
  noLoHagas = 0

  if (diaActual == 0 and horaActual < 13):
    noLoHagas = 1
  if (horaActual == 11 or horaActual == 18 or horaActual == 23):
    #eliminar los elementos de colaRestaurant
    del colaRestaurant[:]

    for mesa in mesasRestaurant:
      mesa.ocupacion = 0;
      mesa.atendido = 0;
      mesa.tiempoDeEspera = 0;
      mesa.tiempoComida = 0;
    
    global personasEnColaYRestaurante
    personasEnColaYRestaurante = 0
  elif (not noLoHagas):

    for mesa in mesasRestaurant:
      if (mesa.tiempoComida == 0):
        global personasEnColaYRestaurante
        personasEnColaYRestaurante -= mesa.ocupacion

        mesa.ocupacion = 0;
        mesa.atendido = 0;
        mesa.tiempoDeEspera = 0;
        mesa.tiempoComida = 0;

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
    while ((not colaRestaurant) and i != (len(colaRestaurant) - 1)):
      if (colaRestaurant[i].ocupacion <= 2):
        ingresa = 0
        i2 = 0

        while(i2 != (len(mesasRestaurant) - 1) and ingresa == 0):
          if(mesasRestaurant[i2].ocupacion == 0 and mesasRestaurant[i2].capacidad == 2):
            #VARIABLE GLOBAL mesasRestaurant
            mesasRestaurant[i2].ocupacion = colaRestaurant[i].ocupacion
            mesasRestaurant[i2].tiempoDeEspera = 0
            mesasRestaurant[i2].tiempoComida = colaRestaurant[i].tiempoComida
            colaRestaurant[i].atendido = 1;

            global personasEnColaYRestaurante
            personasEnColaYRestaurante += mesasRestaurant[i2].ocupacion
            gananciasDiaRestaurante += costoComidaPersona * mesasRestaurant[i2].ocupacion
            ingresa = 1
          else:
            i2 += 1
      else
        ingresa = 0
        i2 = 0
        while(i2 != (len(mesasRestaurant) - 1) and ingresa == 0):
          if (mesasRestaurant[i2].ocupacion == 0 and mesasRestaurant[i2].capacidad == 4):
            mesasRestaurant[i2].ocupacion = colaRestaurant[i].ocupacion
            mesasRestaurant[i2].tiempoDeEspera = 0
            mesasRestaurant[i2].tiempoComida = colaRestaurant[i].tiempoComida
            colaRestaurant[i].atendido = 1

            global personasEnColaYRestaurante
            personasEnColaYRestaurante += mesasRestaurant[i2].ocupacion
            global gananciasDiaRestaurante
            gananciasDiaRestaurante += costoComidaPersona * mesasRestaurant[i2].ocupacion
            ingresa = 1
          else:
            i2 += 1
      i+= 1

    global colaRestaurant
    colaRestaurant = [elem for elem in colaRestaurant if not recibido_en_restaurante(elem)]

    for mesa in colaRestaurant:
      mesa.tiempoDeEspera += 1

    global colaRestaurant
    colaRestaurant = [elem for elem in colaRestaurant if not espera_restaurante(elem)]

    for mesa in mesasRestaurant:
      mesa.tiempoComida -= 1

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

#CHECAR ESTO PORQUE SE PASA UN PARAMETRO CONST
def generarPerdidaComida(mesaComedor):

  if (mesaComedor.tiempoDeEspera >= 2):
    global personasEnColaYRestaurante
    personasEnColaYRestaurante -= mesaComedor.ocupacion

    global gananciasPerdidasDiaRestaurante
    gananciasPerdidasDiaRestaurante += mesaComedor.ocupacion * costoComidaPersona

  return