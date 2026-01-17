# Portal Analítico - Prueba Técnica

Este proyecto es una aplicación web básica construida con Django y Docker, diseñada para visualizar métricas de negocio simuladas. Incluye una arquitectura de contenedores para la aplicación y una base de datos PostgreSQL, junto con la resolución de ejercicios analíticos en SQL.

## Requisitos Previos

Asegúrate de tener instalados los siguientes componentes en tu sistema:

- Docker
- Docker Compose

## Instalación y Despliegue

Sigue estos pasos para levantar el entorno localmente:

1. **Clonar o descargar el repositorio**

2. **Construir y levantar los contenedores**
   
   Desde la raíz del proyecto, ejecuta:
   
   ```bash
   docker-compose up --build
   ```

3. **Acceder a la aplicación**
   
   Una vez que los contenedores estén corriendo, abre tu navegador en:
   
   ```
   http://localhost:8000
   ```

## Estructura del Proyecto

```
.
├── app/                      # Código fuente de Django (analytics_portal)
│   └── dashboard/           # Aplicación del portal y visualización
├── docker-compose.yml       # Definición de servicios (Web y Base de Datos)
└── sql_queries.sql          # Solución al Bloque 2 (Consultas BigQuery)
```

## Descripción de Componentes

- **`/app`**: Contiene el código fuente de Django (`analytics_portal`)
- **`/app/dashboard`**: Aplicación encargada de la lógica del portal y la visualización
- **`docker-compose.yml`**: Definición de los servicios (Web y Base de Datos)
- **`sql_queries.sql`**: Solución al Bloque 2 (Consultas BigQuery)

## Servicios Docker

El proyecto utiliza los siguientes servicios:

- **Web**: Aplicación Django
- **Database**: PostgreSQL

## Tecnologías Utilizadas

- Django
- PostgreSQL
- Docker
- Docker Compose

---

Desarrollado como prueba técnica