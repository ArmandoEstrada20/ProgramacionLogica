from pyswip import Prolog

# Inicializamos Prolog
prolog = Prolog()

# Definimos hechos y reglas en Prolog
# Definimos que hay tres casas y cada una tiene un color único y una mascota única
prolog.assertz("color(casa1, rojo)")
prolog.assertz("color(casa2, azul)")
prolog.assertz("color(casa3, verde)")

# Hechos: Colocamos las pistas dadas
prolog.assertz("mascota(casa2, gato)")  # La persona en la casa azul tiene un gato
prolog.assertz("mascota(casa1, perro)") # La persona en la casa roja tiene un perro

# Regla: La casa roja está a la izquierda de la casa verde
prolog.assertz("izquierda(X, Y) :- color(X, rojo), color(Y, verde)")

# Funciones para hacer consultas y verificar resultados
def encontrar_color(casa):
    """Devuelve el color de la casa."""
    resultado = list(prolog.query(f"color({casa}, Color)"))
    return resultado[0]["Color"] if resultado else None

def encontrar_mascota(casa):
    """Devuelve la mascota en la casa especificada."""
    resultado = list(prolog.query(f"mascota({casa}, Mascota)"))
    return resultado[0]["Mascota"] if resultado else None

def verificar_izquierda():
    """Verifica que la casa roja esté a la izquierda de la casa verde."""
    resultado = list(prolog.query("izquierda(X, Y)"))
    return resultado

# Ejecución de consultas
print("Color de la casa 1:", encontrar_color("casa1"))
print("Color de la casa 2:", encontrar_color("casa2"))
print("Color de la casa 3:", encontrar_color("casa3"))

print("Mascota en la casa 1:", encontrar_mascota("casa1"))
print("Mascota en la casa 2:", encontrar_mascota("casa2"))
print("Mascota en la casa 3:", encontrar_mascota("casa3"))

# Verificamos la regla de la casa roja a la izquierda de la verde
if verificar_izquierda():
    print("La casa roja está a la izquierda de la casa verde según las reglas.")
else:
    print("La regla sobre la casa roja y verde no se cumple.")