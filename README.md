# Juego del Ahorcado en Python

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de un juego del ahorcado utilizando Python y ejecutado desde la consola.

El objetivo es que el jugador descubra una palabra oculta, seleccionada aleatoriamente desde un archivo de texto, ingresando una letra por vez. Para lograrlo, dispone de un máximo de seis intentos incorrectos.

El proyecto permite aplicar conceptos fundamentales de programación, como modularización, programación orientada a objetos, estructuras de datos, funciones y manejo de archivos.

## 2. Objetivo y funcionamiento del juego

Al iniciar una partida, el programa selecciona una palabra al azar del archivo `wordlist.txt` y presenta al jugador una serie de guiones que representan sus letras.

El jugador debe ingresar una letra por vez. Si la letra pertenece a la palabra, se revela su posición correspondiente. Si no pertenece, se registra un error y se actualiza la representación gráfica del ahorcado.

La partida finaliza cuando el jugador descubre todas las letras de la palabra o alcanza los seis errores permitidos. Al terminar, puede elegir si desea jugar nuevamente o salir del programa.

## 3. Funcionalidades principales

- Selección aleatoria de palabras desde un archivo externo.
- Validación de las entradas del usuario: se acepta una sola letra por vez.
- Conversión de las entradas a minúsculas.
- Detección de letras repetidas.
- Visualización del progreso de la palabra.
- Representación gráfica del ahorcado mediante caracteres ASCII.
- Actualización de los intentos restantes.
- Detección de las condiciones de victoria y derrota.
- Opción de iniciar una nueva partida.

## 4. Organización y componentes del proyecto

El proyecto se encuentra organizado en los siguientes archivos:

- **`main.py`**: constituye el punto de entrada del programa. Gestiona la interacción con el usuario, solicita las letras, controla el desarrollo de la partida y permite volver a jugar.

- **`game.py`**: contiene la clase `HangmanGame`, responsable de administrar el estado de cada partida. Incluye métodos para procesar las letras ingresadas, mostrar el progreso y comprobar las condiciones de victoria y derrota.

- **`utils.py`**: contiene funciones auxiliares. Su función principal es obtener una palabra aleatoria a partir del archivo de palabras.

- **`wordlist.txt`**: almacena las palabras disponibles para el juego. Actualmente contiene 20 palabras.

- **`README.md`**: contiene la documentación del proyecto.

## 5. Decisiones técnicas

Durante el desarrollo se adoptaron las siguientes decisiones:

- **Modularización:** se distribuyeron las responsabilidades en diferentes archivos para organizar el código y facilitar su mantenimiento.

- **Programación orientada a objetos:** se implementó la clase `HangmanGame` para representar una partida y centralizar la información relacionada con su estado, como la palabra, las letras ingresadas y la cantidad de errores.

- **Estructuras de datos:** se utilizaron listas para almacenar las letras ingresadas por el jugador y las palabras obtenidas del archivo.

- **Manejo de archivos:** se utilizó un archivo de texto externo para almacenar las palabras, separando los datos de la lógica del programa.

- **Biblioteca estándar:** se utilizó el módulo `random` para seleccionar las palabras aleatoriamente, sin necesidad de instalar bibliotecas externas.

- **Validación de entradas:** se incorporaron controles para evitar entradas inválidas y el ingreso repetido de letras.

## 6. Requisitos

Para ejecutar el proyecto se necesita:

- Python 3 instalado.
- Una terminal o consola.
- Los archivos del proyecto.

No se requieren bibliotecas externas.

## 7. Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/WistonTravieso/Python---Ahorcado.git
```

Ingresar a la carpeta del proyecto:

```bash
cd Python---Ahorcado/hangman_project
```

Ejecutar el programa:

```bash
python3 main.py
```

**Importante:** ejecutar el programa desde la carpeta `hangman_project`, ya que allí se encuentra el archivo `wordlist.txt` que utiliza el juego.

## 8. Integrantes

Wiston Travieso
Gabriela Rodriguez
