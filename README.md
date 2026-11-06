# <img src="https://media.tenor.com/GvP5WfH4AKgAAAAj/bee-minecraft.gif" width="40" style="vertical-align: middle;" alt="Abeja"> Ejercicio 2: Ejecución con Concurrencia - Recolección en Enjambre <img src="https://media.tenor.com/GvP5WfH4AKgAAAAj/bee-minecraft.gif" width="40" style="vertical-align: middle;" alt="Abeja">



## Descripción
Este proyecto demuestra la **ejecución concurrente con hilos (`threading`)** en Python simulando el trabajo simultáneo de un enjambre de abejas.

Se despliegan tres abejas obreras (`t1`, `t2`, `t3`) al mismo tiempo hacia distintas flores (Rosa, Girasol y Tulipán). Gracias a la concurrencia, todas recolectan néctar en paralelo, reduciendo el tiempo total de ejecución de 6 segundos a **3.00 segundos**.

## Requisitos
- Docker y Docker Compose instalados.

## Ejecución con Docker Compose

1. Clonar el repositorio y acceder al directorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ejercicio2-concurrencia
  
2. Iniciar el contenedor:
   ```
   docker compose up

3. Detener y eliminar el contenedor al finalizar:
   ```
   docker compose down

## Salida esperada en el contenedor:

```
Iniciando la recolección en enjambre de néctar...
Abeja Obrera #1 está recolectando néctar de la Rosa.
Abeja Obrera #2 está recolectando néctar de la Girasol.
Abeja Obrera #3 está recolectando néctar de la Tulipán.
Abeja Obrera #3 ha terminado de recolectar néctar de la Tulipán.
Abeja Obrera #1 ha terminado de recolectar néctar de la Rosa.
Abeja Obrera #2 ha terminado de recolectar néctar de la Girasol.
Tiempo total de recolección: 3.00 segundos.
