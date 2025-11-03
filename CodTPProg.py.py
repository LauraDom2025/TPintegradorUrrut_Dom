"""
TRABAJO PRÁCTICO INTEGRADOR - GESTIÓN DE DATOS DE PAÍSES
Sistema para gestionar información de países con filtros, ordenamientos y estadísticas
"""

import csv
import os

# ==============================
# ESTRUCTURAS DE DATOS Y FUNCIONES
# ==============================

def cargar_datos_desde_csv(nombre_archivo):
    """
    Carga los datos de países desde un archivo CSV
    Retorna una lista de diccionarios con la información
    """
    paises = []
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                # Validar que todos los campos estén presentes
                if all(campo in fila for campo in ['nombre', 'poblacion', 'superficie', 'continente']):
                    pais = {
                        'nombre': fila['nombre'],
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente']
                    }
                    paises.append(pais)
        
        print(f"✅ Datos cargados correctamente. {len(paises)} países encontrados.")
        return paises
    
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")
        return []
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return []

def guardar_datos_en_csv(paises, nombre_archivo):
    """
    Guarda los datos de países en un archivo CSV
    """
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        
        print(f"✅ Datos guardados correctamente en '{nombre_archivo}'")
    
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

def validar_entero(mensaje):
    """
    Valida que la entrada sea un número entero positivo
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("❌ El valor debe ser positivo.")
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")

def validar_texto(mensaje):
    """
    Valida que la entrada no esté vacía
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("❌ Este campo no puede estar vacío.")

# ==============================
# FUNCIONALIDADES DEL SISTEMA
# ==============================

def agregar_pais(paises):
    """
    Agrega un nuevo país a la lista
    """
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    nombre = validar_texto("Nombre del país: ")
    
    # Verificar si el país ya existe
    for pais in paises:
        if pais['nombre'].lower() == nombre.lower():
            print("❌ Este país ya existe en la base de datos.")
            return paises
    
    poblacion = validar_entero("Población: ")
    superficie = validar_entero("Superficie en km²: ")
    continente = validar_texto("Continente: ")
    
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    
    paises.append(nuevo_pais)
    print(f"✅ País '{nombre}' agregado correctamente.")
    return paises

def actualizar_pais(paises):
    """
    Actualiza los datos de población y superficie de un país
    """
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return paises
    
    nombre_buscar = validar_texto("Nombre del país a actualizar: ")
    
    for pais in paises:
        if pais['nombre'].lower() == nombre_buscar.lower():
            print(f"País encontrado: {pais}")
            
            print("\nNuevos datos:")
            pais['poblacion'] = validar_entero("Nueva población: ")
            pais['superficie'] = validar_entero("Nueva superficie en km²: ")
            
            print(f"✅ País '{nombre_buscar}' actualizado correctamente.")
            return paises
    
    print("❌ País no encontrado.")
    return paises

def buscar_pais(paises):
    """
    Busca países por nombre (coincidencia parcial)
    """
    print("\n--- BUSCAR PAÍS ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    nombre_buscar = validar_texto("Nombre a buscar: ").lower()
    resultados = []
    
    for pais in paises:
        if nombre_buscar in pais['nombre'].lower():
            resultados.append(pais)
    
    if resultados:
        print(f"\n🔍 {len(resultados)} país(es) encontrado(s):")
        mostrar_paises(resultados)
    else:
        print("❌ No se encontraron países con ese nombre.")

def filtrar_por_continente(paises):
    """
    Filtra países por continente
    """
    print("\n--- FILTRAR POR CONTINENTE ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    continentes = list(set(pais['continente'] for pais in paises))
    print("Continentes disponibles:", ", ".join(continentes))
    
    continente_filtrar = validar_texto("Continente a filtrar: ")
    resultados = []
    
    for pais in paises:
        if pais['continente'].lower() == continente_filtrar.lower():
            resultados.append(pais)
    
    if resultados:
        print(f"\n🌍 {len(resultados)} país(es) encontrado(s) en {continente_filtrar}:")
        mostrar_paises(resultados)
    else:
        print("❌ No se encontraron países en ese continente.")

def filtrar_por_rango_poblacion(paises):
    """
    Filtra países por rango de población
    """
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    print("Ingrese el rango de población:")
    min_poblacion = validar_entero("Población mínima: ")
    max_poblacion = validar_entero("Población máxima: ")
    
    if min_poblacion > max_poblacion:
        print("❌ Error: La población mínima no puede ser mayor que la máxima.")
        return
    
    resultados = []
    for pais in paises:
        if min_poblacion <= pais['poblacion'] <= max_poblacion:
            resultados.append(pais)
    
    if resultados:
        print(f"\n👥 {len(resultados)} país(es) encontrado(s) en el rango:")
        mostrar_paises(resultados)
    else:
        print("❌ No se encontraron países en ese rango de población.")

def filtrar_por_rango_superficie(paises):
    """
    Filtra países por rango de superficie
    """
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    print("Ingrese el rango de superficie:")
    min_superficie = validar_entero("Superficie mínima (km²): ")
    max_superficie = validar_entero("Superficie máxima (km²): ")
    
    if min_superficie > max_superficie:
        print("❌ Error: La superficie mínima no puede ser mayor que la máxima.")
        return
    
    resultados = []
    for pais in paises:
        if min_superficie <= pais['superficie'] <= max_superficie:
            resultados.append(pais)
    
    if resultados:
        print(f"\n🗺️ {len(resultados)} país(es) encontrado(s) en el rango:")
        mostrar_paises(resultados)
    else:
        print("❌ No se encontraron países en ese rango de superficie.")

def ordenar_paises(paises):
    """
    Ordena países por diferentes criterios
    """
    print("\n--- ORDENAR PAÍSES ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    print("1. Ordenar por nombre (A-Z)")
    print("2. Ordenar por nombre (Z-A)")
    print("3. Ordenar por población (ascendente)")
    print("4. Ordenar por población (descendente)")
    print("5. Ordenar por superficie (ascendente)")
    print("6. Ordenar por superficie (descendente)")
    
    opcion = input("Seleccione una opción (1-6): ")
    
    paises_ordenados = paises.copy()
    
    if opcion == '1':
        paises_ordenados.sort(key=lambda x: x['nombre'])
        print("\n✅ Países ordenados por nombre (A-Z):")
    elif opcion == '2':
        paises_ordenados.sort(key=lambda x: x['nombre'], reverse=True)
        print("\n✅ Países ordenados por nombre (Z-A):")
    elif opcion == '3':
        paises_ordenados.sort(key=lambda x: x['poblacion'])
        print("\n✅ Países ordenados por población (ascendente):")
    elif opcion == '4':
        paises_ordenados.sort(key=lambda x: x['poblacion'], reverse=True)
        print("\n✅ Países ordenados por población (descendente):")
    elif opcion == '5':
        paises_ordenados.sort(key=lambda x: x['superficie'])
        print("\n✅ Países ordenados por superficie (ascendente):")
    elif opcion == '6':
        paises_ordenados.sort(key=lambda x: x['superficie'], reverse=True)
        print("\n✅ Países ordenados por superficie (descendente):")
    else:
        print("❌ Opción inválida.")
        return
    
    mostrar_paises(paises_ordenados)

def mostrar_estadisticas(paises):
    """
    Muestra estadísticas de los países
    """
    print("\n--- ESTADÍSTICAS ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    # País con mayor y menor población
    pais_max_poblacion = max(paises, key=lambda x: x['poblacion'])
    pais_min_poblacion = min(paises, key=lambda x: x['poblacion'])
    
    # País con mayor y menor superficie
    pais_max_superficie = max(paises, key=lambda x: x['superficie'])
    pais_min_superficie = min(paises, key=lambda x: x['superficie'])
    
    # Promedios
    total_poblacion = sum(pais['poblacion'] for pais in paises)
    total_superficie = sum(pais['superficie'] for pais in paises)
    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)
    
    # Cantidad por continente
    continentes = {}
    for pais in paises:
        continente = pais['continente']
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1
    
    print(f"📊 Total de países: {len(paises)}")
    print(f"👥 Población total: {total_poblacion:,}")
    print(f"🗺️ Superficie total: {total_superficie:,} km²")
    print(f"📈 Promedio de población: {promedio_poblacion:,.0f}")
    print(f"📐 Promedio de superficie: {promedio_superficie:,.0f} km²")
    
    print(f"\n🏆 País con mayor población: {pais_max_poblacion['nombre']} ({pais_max_poblacion['poblacion']:,})")
    print(f"📉 País con menor población: {pais_min_poblacion['nombre']} ({pais_min_poblacion['poblacion']:,})")
    print(f"🏞️ País con mayor superficie: {pais_max_superficie['nombre']} ({pais_max_superficie['superficie']:,} km²)")
    print(f"📏 País con menor superficie: {pais_min_superficie['nombre']} ({pais_min_superficie['superficie']:,} km²)")
    
    print(f"\n🌍 Cantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"   {continente}: {cantidad} país(es)")

def mostrar_paises(paises):
    """
    Muestra la lista de países formateada
    """
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print("\n" + "="*80)
    print(f"{'NOMBRE':<20} {'POBLACIÓN':<15} {'SUPERFICIE':<15} {'CONTINENTE':<15}")
    print("="*80)
    
    for pais in paises:
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<15,} {pais['continente']:<15}")
    
    print("="*80)

def mostrar_todos_los_paises(paises):
    """
    Muestra todos los países de la base de datos
    """
    print("\n--- TODOS LOS PAÍSES ---")
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    mostrar_paises(paises)

# ==============================
# FUNCIÓN PRINCIPAL - MENÚ
# ==============================

def menu_principal():
    """
    Función principal que muestra el menú y gestiona las opciones
    """
    ARCHIVO_CSV = "paises.csv"
    paises = cargar_datos_desde_csv(ARCHIVO_CSV)
    
    while True:
        print("\n" + "="*50)
        print("      SISTEMA DE GESTIÓN DE PAÍSES")
        print("="*50)
        print("1. Agregar país")
        print("2. Actualizar datos de país")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Mostrar todos los países")
        print("8. Guardar datos")
        print("9. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-9): ")
        
        if opcion == '1':
            paises = agregar_pais(paises)
        elif opcion == '2':
            paises = actualizar_pais(paises)
        elif opcion == '3':
            buscar_pais(paises)
        elif opcion == '4':
            menu_filtrar(paises)
        elif opcion == '5':
            ordenar_paises(paises)
        elif opcion == '6':
            mostrar_estadisticas(paises)
        elif opcion == '7':
            mostrar_todos_los_paises(paises)
        elif opcion == '8':
            guardar_datos_en_csv(paises, ARCHIVO_CSV)
        elif opcion == '9':
            guardar_datos_en_csv(paises, ARCHIVO_CSV)
            print("¡Gracias por usar el sistema! 👋")
            break
        else:
            print("❌ Opción inválida. Por favor, seleccione 1-9.")

def menu_filtrar(paises):
    """
    Submenú para las opciones de filtrado
    """
    while True:
        print("\n--- FILTRAR PAÍSES ---")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            filtrar_por_continente(paises)
        elif opcion == '2':
            filtrar_por_rango_poblacion(paises)
        elif opcion == '3':
            filtrar_por_rango_superficie(paises)
        elif opcion == '4':
            break
        else:
            print("❌ Opción inválida.")

# ==============================
# EJECUCIÓN DEL PROGRAMA
# ==============================

if __name__ == "__main__":
    print("🚀 Iniciando Sistema de Gestión de Países...")
    menu_principal()