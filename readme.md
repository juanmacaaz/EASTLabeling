# Dependencias

    pip install opencv-python

# Instrucciones de uso

## Iniciar

1. Cargar en la carpeta "input" las imagenes en formato "jpg"
2. Ejecutar el programa desde la terminal, python main.py

## Uso

    [Clic izquierdo del raton] ->> colocar un punto.
    [d]                        ->> pasar a la siguiente imagen (Si esta colocado los 4 puntos realizara una copia en la carpeta output en el formato EAST https://github.com/argman/EAST/tree/master/training_samples).
    [a]                         ->> Vuelve hacia la imagen acterior.
    [s]                         ->> Sale de la aplicacion.
    [r]                         ->> Limpia los puntos de la imagen para poder ponerlos otra vez.

## Cosas importantes

1. Colocar los puntos en orden:
    1. Arriba izquierda
    2. Arriba derecha
    3. Abajo derecha
    4. Abajo izquierda

2. En el codigo fuente hay una variable SCALE, cambiar en caso de que la imagen sea muy grande o pequena.
   El valor por defecto es 1, es decir que no aumentara.
   Es un factor multiplicativo. 0,5 la mas pequena, 2 el doble mas grande.