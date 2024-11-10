
# Proyecto de Ejemplo con Prolog en Python

Este proyecto demuestra cómo interactuar con hechos y reglas definidas en Prolog desde Python utilizando la biblioteca `pyswip`. 
Se define un conjunto de reglas y hechos sobre colores y mascotas en distintas casas, y se realizan consultas para verificar relaciones entre ellas.

## Requisitos

Este proyecto utiliza `pyswip`, que está especificado en el archivo `requirements.txt`. 

## Configuración e instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Crear un entorno virtual**:
    Es recomendable crear un entorno virtual para gestionar las dependencias de este proyecto. Ejecuta el siguiente comando:
    ```bash
    python3 -m venv venv
    ```

3. **Activar el entorno virtual**:
    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - En macOS y Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instalar las dependencias**:
    Con el entorno virtual activado, instala las dependencias utilizando `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución del código

Una vez configurado el entorno, puedes ejecutar el código para ver los resultados de las consultas Prolog en Python:
```bash
python Ejemplo_Prolog.py
```

## Descripción del Código

El código realiza las siguientes acciones:

1. Define una serie de hechos y reglas en Prolog sobre el color y las mascotas en cada casa.
2. Realiza consultas para obtener el color y la mascota de cada casa.
3. Verifica la regla de que la casa roja está a la izquierda de la casa verde y muestra el resultado.

