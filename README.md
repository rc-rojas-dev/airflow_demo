# Apache Airflow 3.2.2 - Entorno de Desarrollo

Este proyecto configura un entorno local de Apache Airflow 3.2.2 utilizando Docker Compose y PostgreSQL como base de datos de metadatos.

## Requisitos Previos

### Linux

Instalar:

* Docker Engine 28+
* Docker Compose v2+
* Git

---

## Estructura del Proyecto

```text
.
├── dags/
├── src/
├── plugins/
├── logs/
├── config/
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
└── .env
```

### Descripción

| Carpeta             | Descripción                     |
| ------------------- | ------------------------------- |
| dags                | DAGs de Airflow                 |
| src                 | Código Python del proyecto      |
| plugins             | Plugins personalizados          |
| logs                | Logs de Airflow                 |
| config              | Configuración adicional         |
| requirements.txt    | Dependencias Python             |
| Dockerfile          | Imagen personalizada de Airflow |
| docker-compose.yaml | Definición de servicios         |

---

## Crear Directorios

```bash
mkdir -p dags logs plugins config src
```

---

## Configuración del Usuario

Crear archivo `.env`:

```bash
echo "AIRFLOW_UID=$(id -u)" > .env
echo "AIRFLOW_API_AUTH_JWT_SECRET = Tu-token-123456789"
```
Verificar:

```bash
cat .env
```
---
## Fast install
```bash
docker compose build
docker compose up airflow-init
docker compose up -d
```
---

## Construir la Imagen

Construir imagen personalizada:

```bash
docker compose build
```

Reconstrucción completa:

```bash
docker compose build --no-cache
```

---

## Inicializar la Base de Datos

Ejecutar migraciones:

```bash
docker compose run --rm airflow-init
o
docker compose up airflow-init
```
---

## Levantar Servicios

Iniciar todos los servicios:

```bash
docker compose up -d
```

Verificar:

```bash
docker compose ps
```

Salida esperada:

```text
airflow-postgres
airflow-apiserver
airflow-scheduler
airflow-dag-processor
airflow-triggerer
```

Todos deben aparecer como:

```text
running
healthy
```
---
Verificar logs:

```bash
docker compose logs airflow-init
```

## Acceder a Airflow

Abrir navegador:

```text
http://localhost:8080
```

---

## Verificar la Instalación

Ingresar al scheduler:

```bash
docker exec -it airflow-scheduler bash
```

Verificar versión:

```bash
airflow version
```
Listar DAGs:

```bash
airflow dags list
```
---

## Crear un DAG de Prueba

Crear archivo:

```text
dags/hello_world.py
```

Contenido:

```python
from airflow.sdk import DAG, task
from datetime import datetime

with DAG(
    dag_id="hello_world",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
):

    @task
    def hello():
        print("Hola Airflow 3.2.2")

    hello()
```

Verificar:

```bash
docker exec -it airflow-scheduler airflow dags list
```

---

## Logs

Ver logs del scheduler:

```bash
docker compose logs -f airflow-scheduler
```

Ver logs del API Server:

```bash
docker compose logs -f airflow-apiserver
```

Ver logs del DAG Processor:

```bash
docker compose logs -f airflow-dag-processor
```

---

## Comandos Útiles

### Detener servicios

```bash
docker compose stop
```

### Iniciar servicios

```bash
docker compose start
```

### Reiniciar servicios

```bash
docker compose restart
```

### Eliminar contenedores

```bash
docker compose down
```

### Eliminar contenedores y volúmenes

```bash
docker compose down -v
```

---

## Actualizar Dependencias

Modificar:

```text
requirements.txt
```

Reconstruir:

```bash
docker compose build --no-cache
docker compose up -d
```

---

## Verificar Salud de Servicios

```bash
docker compose ps
```

Todos los servicios deben aparecer como:

```text
healthy
```

---

## Solución de Problemas

### Error: Permission denied

Verificar:

```bash
cat .env
```

y que exista:

```text
AIRFLOW_UID=<tu_uid>
```

---

### Error: Database migration failed

Ejecutar nuevamente:

```bash
docker compose run --rm airflow-init
```

---

### Error: DAG no aparece

Verificar:

```bash
docker exec -it airflow-scheduler airflow dags list
```

Comprobar sintaxis:

```bash
python dags/mi_dag.py
```

---

## Arquitectura

```text
PostgreSQL
     ^
     |
     |
Airflow Scheduler
     |
     v
DAG Processor

API Server

Triggerer
```

### Componentes

* PostgreSQL: Base de datos de metadatos.
* Scheduler: Programa ejecuciones.
* DAG Processor: Analiza DAGs.
* API Server: UI y API REST.
* Triggerer: Manejo de tareas diferidas.

---

## Versión

```text
Apache Airflow 3.2.2
Python 3.12
PostgreSQL 17
Docker Compose v2
```
