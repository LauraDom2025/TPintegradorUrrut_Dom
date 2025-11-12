"""
Sistema de Gestión de Países
Maneja información de países con persistencia en CSV
"""

import csv
import os

# Constantes
ARCHIVO_CSV = "paises.csv"
COLUMNAS_CSV = ["nombre", "poblacion", "superficie", "continente"]

"""Funciones auxiliares"""

def limpiar_consola():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def normalizar_texto(texto):
    """Normaliza texto eliminando espacios extras y convirtiendo a minúsculas."""
    return " ".join(texto.split()).lower()

def cargar_paises():
    """
    Carga la lista de países desde el archivo CSV.
    Retorna lista vacía si el archivo no existe.
    """
    paises = []
    
    if not os.path.exists(ARCHIVO_CSV):
        return paises
    
    with open(ARCHIVO_CSV, mode='r', encoding='utf-8', newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["poblacion"].isdigit() and fila["superficie"].isdigit():
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
    
    return paises

def guardar_paises(paises):
    """Guarda la lista de países en el archivo CSV."""
    with open(ARCHIVO_CSV, mode='w', encoding='utf-8', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS_CSV)
        escritor.writeheader()
        escritor.writerows(paises)

def buscar_pais_por_nombre(paises, nombre):
    """
    Busca un país por coincidencia exacta de nombre.
    Retorna índice o None.
    """
    nombre_norm = normalizar_texto(nombre)
    for i in range(len(paises)):
        if normalizar_texto(paises[i]["nombre"]) == nombre_norm:
            return i
    return None

def validar_entero_positivo(mensaje, permitir_cero=False):
    """
    Solicita un número entero positivo con validación.
    Permite cancelar operación.
    """
    while True:
        entrada = input(mensaje).strip()
        
        if entrada.isdigit():
            numero = int(entrada)
            if permitir_cero and numero >= 0:
                return numero
            elif not permitir_cero and numero > 0:
                return numero
            else:
                limpiar_consola()
                print("\nError: Debe ingresar un número mayor que 0.")
                print("\nSí desea intentar nuevamente, presione S")
                if input().strip().lower() != 's':
                    return None
                limpiar_consola()
        else:
            limpiar_consola()
            print("\nError: Debe ingresar un número entero válido.")
            print("\nSí desea intentar nuevamente, presione S")
            if input().strip().lower() != 's':
                return None
            limpiar_consola()

def validar_texto_no_vacio(mensaje):
    """Solicita texto no vacío. Permite cancelar."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("\nError: El campo no puede estar vacío.")
            print("\nSí desea intentar nuevamente, presione S")
            if input().strip().lower() != 's':
                return None

"""Funciones del menú principal"""

def agregar_pais(paises):
    """Agrega un nuevo país con validación completa."""
    limpiar_consola()
    
    print("=" * 63)
    print("--- AGREGAR NUEVO PAÍS ---")
    print("=" * 63)
    
    nombre = validar_texto_no_vacio("\nIngrese el nombre del país: ")
    if nombre is None:
        print("\nOperación cancelada.")
        return
    
    if buscar_pais_por_nombre(paises, nombre) is not None:
        print(f"\nError: El país '{nombre}' ya existe.")
        return
    
    poblacion = validar_entero_positivo("Ingrese la población: ", permitir_cero=False)
    if poblacion is None:
        print("\nOperación cancelada.")
        return
    
    superficie = validar_entero_positivo("Ingrese la superficie (km²): ", permitir_cero=False)
    if superficie is None:
        print("\nOperación cancelada.")
        return
    
    continente = validar_texto_no_vacio("Ingrese el continente: ")
    if continente is None:
        print("\nOperación cancelada.")
        return
    
    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    
    guardar_paises(paises)
    limpiar_consola()
    print(f"\n País '{nombre}' agregado exitosamente.")

def actualizar_pais(paises):
    """Actualiza población y/o superficie de un país."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        return
    
    print("=" * 63)
    print("--- ACTUALIZAR DATOS DE PAÍS ---")
    print("=" * 63)
    mostrar_listado_paises(paises)
    
    nombre = validar_texto_no_vacio("\nIngrese el nombre del país a actualizar: ")
    if nombre is None:
        print("\nOperación cancelada.")
        return
    
    indice = buscar_pais_por_nombre(paises, nombre)
    if indice is None:
        limpiar_consola()
        print(f"\nError: El país '{nombre}' no existe.")
        return
    
    limpiar_consola()
    print(f"\nPaís seleccionado: {paises[indice]['nombre']}")
    print(f"Población actual: {paises[indice]['poblacion']:,}")
    print(f"Superficie actual: {paises[indice]['superficie']:,} km²")
    
    print("\n1. Actualizar población")
    print("2. Actualizar superficie")
    print("3. Actualizar ambos")
    
    opcion = input("\nSeleccione una opción (1-3): ").strip()
    
    if opcion in ["1", "3"]:
        poblacion = validar_entero_positivo("\nNueva población: ", permitir_cero=False)
        if poblacion is None:
            print("\nOperación cancelada.")
            return
        paises[indice]["poblacion"] = poblacion
    
    if opcion in ["2", "3"]:
        superficie = validar_entero_positivo("\nNueva superficie (km²): ", permitir_cero=False)
        if superficie is None:
            print("\nOperación cancelada.")
            return
        paises[indice]["superficie"] = superficie
    
    if opcion in ["1", "2", "3"]:
        guardar_paises(paises)
        limpiar_consola()
        print(f"\n País '{paises[indice]['nombre']}' actualizado exitosamente.")
    else:
        print("\nOpción inválida.")

def buscar_pais(paises):
    """Busca país por coincidencia parcial o exacta en el nombre."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        return
    
    print("=" * 63)
    print("--- BUSCAR PAÍS ---")
    print("=" * 63)
    
    termino = validar_texto_no_vacio("\nIngrese el nombre (total o parcial): ")
    if termino is None:
        print("\nOperación cancelada.")
        return
    
    termino_norm = normalizar_texto(termino)
    resultados = [p for p in paises if termino_norm in normalizar_texto(p["nombre"])]
    
    limpiar_consola()
    if not resultados:
        print(f"\nNo se encontraron países con '{termino}'.")
    else:
        print(f"\n--- RESULTADOS DE BÚSQUEDA: '{termino}' ---")
        print("-" * 90)
        print(f"{'País':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<20}")
        print("-" * 90)
        for p in resultados:
            print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<20}")
        print(f"\nTotal encontrados: {len(resultados)}")

def filtrar_por_continente(paises):
    """Filtra países por continente."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        return
    
    print("=" * 63)
    print("--- FILTRAR POR CONTINENTE ---")
    print("=" * 63)
    
    continente = validar_texto_no_vacio("\nIngrese el continente: ")
    if continente is None:
        print("\nOperación cancelada.")
        return
    
    continente_norm = normalizar_texto(continente)
    resultados = [p for p in paises if normalizar_texto(p["continente"]) == continente_norm]
    
    limpiar_consola()
    if not resultados:
        print(f"\nNo hay países en '{continente}'.")
    else:
        print(f"\n--- PAÍSES EN {continente.upper()} ---")
        print("-" * 90)
        print(f"{'País':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<20}")
        print("-" * 90)
        for p in resultados:
            print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<20}")
        print(f"\nTotal: {len(resultados)} países")

def filtrar_por_poblacion(paises):
    """Filtra países por rango de población."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        return
    
    print("=" * 63)
    print("--- FILTRAR POR RANGO DE POBLACIÓN ---")
    print("=" * 63)
    
    minimo = validar_entero_positivo("\nPoblación mínima: ", permitir_cero=True)
    if minimo is None:
        print("\nOperación cancelada.")
        return
    
    maximo = validar_entero_positivo("Población máxima: ", permitir_cero=True)
    if maximo is None:
        print("\nOperación cancelada.")
        return
    
    if minimo > maximo:
        print("\nError: El mínimo no puede ser mayor que el máximo.")
        return
    
    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    
    limpiar_consola()
    if not resultados:
        print(f"\nNo hay países con población entre {minimo:,} y {maximo:,}.")
    else:
        print(f"\n--- PAÍSES CON POBLACIÓN ENTRE {minimo:,} Y {maximo:,} ---")
        print("-" * 90)
        print(f"{'País':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<20}")
        print("-" * 90)
        for p in resultados:
            print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<20}")
        print(f"\nTotal: {len(resultados)} países")

def filtrar_por_superficie(paises):
    """Filtra países por rango de superficie."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        return
    
    print("=" * 63)
    print("--- FILTRAR POR RANGO DE SUPERFICIE ---")
    print("=" * 63)
    
    minimo = validar_entero_positivo("\nSuperficie mínima (km²): ", permitir_cero=True)
    if minimo is None:
        print("\nOperación cancelada.")
        return
    
    maximo = validar_entero_positivo("Superficie máxima (km²): ", permitir_cero=True)
    if maximo is None:
        print("\nOperación cancelada.")
        return
    
    if minimo > maximo:
        print("\nError: El mínimo no puede ser mayor que el máximo.")
        return
    
    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
    
    limpiar_consola()
    if not resultados:
        print(f"\nNo hay países con superficie entre {minimo:,} y {maximo:,} km².")
    else:
        print(f"\n--- PAÍSES CON SUPERFICIE ENTRE {minimo:,} Y {maximo:,} KM² ---")
        print("-" * 90)
        print(f"{'País':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<20}")
        print("-" * 90)
        for p in resultados:
            print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<20}")
        print(f"\nTotal: {len(resultados)} países")

def ordenar_paises(paises):
    """Ordena países por criterio seleccionado."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        return
    
    print("=" * 63)
    print("--- ORDENAR PAÍSES ---")
    print("=" * 63)
    print("\n1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    
    criterio = input("\nSeleccione criterio (1-3): ").strip()
    
    if criterio not in ["1", "2", "3"]:
        print("\nOpción inválida.")
        return
    
    direccion = input("¿Orden ascendente (A) o descendente (D)?: ").strip().upper()
    if direccion not in ["A", "D"]:
        print("\nOpción inválida.")
        return
    
    reverso = (direccion == "D")
    
    # Ordenamiento manual 
    if criterio == "1":
        paises_ordenados = []
        for p in paises:
            paises_ordenados.append(p)
        
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                cond = normalizar_texto(paises_ordenados[i]["nombre"]) > normalizar_texto(paises_ordenados[j]["nombre"])
                if (cond and not reverso) or (not cond and reverso):
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        titulo = "NOMBRE"
    
    elif criterio == "2":
        paises_ordenados = []
        for p in paises:
            paises_ordenados.append(p)
        
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                cond = paises_ordenados[i]["poblacion"] > paises_ordenados[j]["poblacion"]
                if (cond and not reverso) or (not cond and reverso):
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        titulo = "POBLACIÓN"
    
    else:
        paises_ordenados = []
        for p in paises:
            paises_ordenados.append(p)
        
        for i in range(len(paises_ordenados)):
            for j in range(i + 1, len(paises_ordenados)):
                cond = paises_ordenados[i]["superficie"] > paises_ordenados[j]["superficie"]
                if (cond and not reverso) or (not cond and reverso):
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        titulo = "SUPERFICIE"
    
    limpiar_consola()
    orden_texto = "DESCENDENTE" if reverso else "ASCENDENTE"
    print(f"\n--- PAÍSES ORDENADOS POR {titulo} ({orden_texto}) ---")
    print("-" * 90)
    print(f"{'País':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<20}")
    print("-" * 90)
    for p in paises_ordenados:
        print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<20}")

def mostrar_estadisticas(paises):
    """Muestra estadísticas generales del dataset."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        return
    
    print("=" * 63)
    print("--- ESTADÍSTICAS GENERALES ---")
    print("=" * 63)
    
    # País con mayor y menor población 
    pais_mayor_pob = paises[0]
    pais_menor_pob = paises[0]
    
    for p in paises:
        if p["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = p
        if p["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = p
    
    # Promedios
    total_pob = 0
    total_sup = 0
    for p in paises:
        total_pob += p["poblacion"]
        total_sup += p["superficie"]
    
    promedio_pob = total_pob // len(paises)
    promedio_sup = total_sup // len(paises)
    
    print(f"\n Mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,})")
    print(f" Menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,})")
    print(f" Promedio de población: {promedio_pob:,}")
    print(f" Promedio de superficie: {promedio_sup:,} km²")
    
    # Cantidad por continente
    continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1
    
    print("\n Cantidad de países por continente:")
    cont_lista = []
    for cont in continentes:
        cont_lista.append((cont, continentes[cont]))
    
    # Ordenar continentes alfabéticamente
    for i in range(len(cont_lista)):
        for j in range(i + 1, len(cont_lista)):
            if cont_lista[i][0] > cont_lista[j][0]:
                cont_lista[i], cont_lista[j] = cont_lista[j], cont_lista[i]
    
    for cont, cantidad in cont_lista:
        print(f" {cont}: {cantidad} país(es)")
    
    print(f"\n Total de países registrados: {len(paises)}")

def mostrar_listado_paises(paises):
    """Muestra tabla completa de países."""
    if not paises:
        return
    
    print("\n--- LISTADO DE PAÍSES ---")
    print("-" * 90)
    print(f"{'País':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<20}")
    print("-" * 90)
    for p in paises:
        print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<20}")
    print(f"\nTotal: {len(paises)} países")

def mostrar_todos_los_paises(paises):
    """Opción del menú para mostrar todos los países."""
    limpiar_consola()
    
    if not paises:
        print("\nNo hay países registrados.")
        print("=" * 63)
        return
    
    print("=" * 63)
    print("--- TODOS LOS PAÍSES ---")
    print("=" * 63)
    mostrar_listado_paises(paises)
    print("=" * 63)

"""Menú principal"""

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 63)
    print(" SISTEMA DE GESTIÓN DE PAÍSES ".center(63))
    print("=" * 63)
    print("1. Agregar país")
    print("2. Actualizar datos de país")
    print("3. Buscar país por nombre")
    print("4. Filtrar por continente")
    print("5. Filtrar por rango de población")
    print("6. Filtrar por rango de superficie")
    print("7. Ordenar países")
    print("8. Mostrar estadísticas")
    print("9. Mostrar todos los países")
    print("10. Salir")
    print("=" * 63)

def main():
    """Función principal que ejecuta el menú interactivo."""
    limpiar_consola()
    
    paises = cargar_paises()
    
    print("=" * 63)
    print("\n--- Bienvenido al Sistema de Gestión de Países ---")
    if paises:
        print(f"Se cargaron {len(paises)} país(es) del archivo '{ARCHIVO_CSV}'.\n".center(63))
    else:
        print(f"No hay datos. Archivo '{ARCHIVO_CSV}' no encontrado.\n".center(63))
    print("=" * 63)
    print("\nPresione Enter para continuar...")
    input()
    limpiar_consola()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        match opcion:
            case "1":
                agregar_pais(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "2":
                actualizar_pais(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "3":
                buscar_pais(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "4":
                filtrar_por_continente(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "5":
                filtrar_por_poblacion(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "6":
                filtrar_por_superficie(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "7":
                ordenar_paises(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "8":
                mostrar_estadisticas(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "9":
                mostrar_todos_los_paises(paises)
                input("\nPresione Enter para continuar...")
                limpiar_consola()
            case "10":
                limpiar_consola()
                print("=" * 60)
                print("--- SALIENDO DEL SISTEMA ---")
                print("=" * 60)
                print("\n¡Gracias por usar el Sistema de Gestión de Países!\n")
                print("=" * 60)
                break
            case "":
                limpiar_consola()
            case _:
                limpiar_consola()
                print("\nError: Opción inválida. Seleccione una opción del 1 al 10.")
                input("\nPresione Enter para continuar...")
                limpiar_consola()

if __name__ == "__main__":
    main()
    