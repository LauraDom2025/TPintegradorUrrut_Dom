# Sistema de Gestión de Países

=====================================================================

## Descripción del Proyecto

Sistema de gestión de información sobre países desarrollado en Python que permite realizar operaciones CRUD, búsquedas, filtrados, ordenamientos y cálculos estadísticos sobre un dataset de países almacenado en formato CSV.

El sistema implementa un menú interactivo de consola que facilita la gestión completa de datos incluyendo nombre, población, superficie y continente de cada país.

=====================================================================

## Datos de la Universidad y la Cátedra

**Universidad:** [UTN San Nicolás]  
**Cátedra:** Programación 1  
**Año Académico:** [2025]  
**Carrera:** [Tecnicatura en programación]

---

## Integrantes del Equipo

- **Integrante 1:** [Dominguez Laura] - [marlauradominguez@gmail.com]
- **Integrante 2:** [Urrutia Lorenzo] - [lorenzoiurrutia@gmail.com]

---

## Datos de los Profesores

**Profesor Titular:** [Ariel Enferrel - Cinthia Rigoni]  
**Profesores Auxiliares:** [Luciano Chiroli (Comisión 11) - Ana Mutti (Comisión 4)]

=====================================================================

## Instrucciones de Ejecución y Uso 

1. ### Instalación

A. Clonar o descargar el proyecto
B. No se requieren librerías de terceros

2. ### Ejecución

A. Inicializacion de terminal 
B. ```bash
    python gestion_paises.py
    ```

3. ### Creación del Archivo CSV Inicial

En caso de que el archivo `paises.csv` no exista, el programa iniciará con un dataset vacío. 
Puede crear manualmente el archivo con el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
```

4. ### Bienvenida al sistema

El programa le da la bienvenida y le informa:
    Si comienza a trabajar desde un archivo .csv: "Vacio" 
    Si ya contiene informacion, la informara cuantos paises contiene el mismo

5. ### Acceso a las Opciones, en el Menú

### 1. Agregar País
Permite ingresar un nuevo país con todos sus datos. 

### 2. Actualizar Datos de País
Modifica población y/o superficie de un país existente.

### 3. Buscar País por Nombre
Búsqueda por coincidencia parcial o total en el nombre del país (insensible a mayúsculas/minúsculas).

### 4. Filtrar paises por Continente
Muestra todos los países pertenecientes a un continente específico.

### 5. Filtrar paises por Rango de Población
Filtra países cuya población se encuentre entre dos valores mínimo y máximo.

### 6. Filtrar paises por Rango de Superficie
Filtra países cuya superficie (en km²) se encuentre entre dos valores mínimo y máximo.

### 7. Ordenar Países
Ordena el dataset por:
- Nombre (alfabéticamente)
- Población
- Superficie

### 8. Mostrar Estadísticas
Calcula y muestra:
- País con mayor población
- País con menor población
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente
- Total de países registrados

### 9. Mostrar Todos los Países
Visualiza el listado completo en formato tabla.

### 10. Salir
Cierra el programa de forma ordenada.

=====================================================================

## Ejemplos de Uso

### Ejemplo 1: Agregar un Nuevo País

```
En el Menu, seleccione una opción: 1

Ingrese el nombre del país: Francia
Ingrese la población: 67391582
Ingrese la superficie (km²): 643801
Ingrese el continente: Europa

País 'Francia' agregado exitosamente.
```

### Ejemplo 2: Buscar País

```
En el Menu, seleccione una opción: 3

Ingrese el nombre (total o parcial): arg

--- RESULTADOS DE BÚSQUEDA: 'arg' ---
País                      Población    Superficie (km²)    Continente
----------------------------------------------------------------------
Argentina                 45,376,763           2,780,400    América

Total encontrados: 1
```

=====================================================================

### Participación de los Integrantes

#### Laura
**Funciones implementadas:**
- Sistema completo de carga y guardado de datos CSV
- Desarrollo de las funciones principales (agregar, actualizar, buscar)
- Implementación de validaciones y manejo de errores (en conjunto)
- Lógica de filtrado y ordenamiento de datos
- Cálculo de estadísticas y métricas

#### Lorenzo
**Funciones implementadas:**
- Diseño y estructura del menú principal
- Desarrollo del sistema de navegación entre opciones
- Documentación completa del código
- Pruebas, verificación de funcionalidades y manejo de errores (en conjunto)

#### Trabajo en Equipo
- **Reuniones de coordinación:** Planificación diaria de tareas
- **Revisiones de código:** Revisión mutua del trabajo implementado
- **Pruebas:** 
  - **Testing colaborativo de todas las funcionalidades:**
    - No se permiten entradas vacías, da error
    - Solo acepta enteros positivos para población y superficie
    - No permite agregar países con nombres ya existentes
    - Verificar tipos de datos al cargar desde archivo
    - Informar claramente cuando no hay coincidencias
    - El usuario puede abortar cualquier operación en curso
=====================================================================

## Links de Referencia

### Repositorio GitHub
[https://github.com/LorenzoIUrrutia/TP_Integrador_P1_Dominguez_Urrutia]

### Video Tutorial
[https://youtu.be/1unwQRMZXAw]

### Documentación Oficial Python
- Python 3.13: https://docs.python.org/3.13/
- Tutorial Python: https://docs.python.org/3.13/tutorial/
- Librería Estándar: https://docs.python.org/3.13/library/

=====================================================================