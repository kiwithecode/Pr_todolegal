
# Flask Project

Este es un proyecto básico de Flask. Flask es un microframework para Python que te permite desarrollar aplicaciones web rápidamente.

## Instalación y Configuración

1. **Crear un entorno virtual**:
    ```
    python3 -m venv venv
    ```

2. **Activar el entorno virtual**:
    - **Linux/Mac**:
        ```
        source venv/bin/activate
        ```
    - **Windows**:
        ```
        .\venv\Scripts\activate
        ```

3. **Instalar las dependencias**:
    ```
    pip install Flask
    ```

## Ejecución

Para iniciar el servidor de Flask:

```
flask run

python src/app.py
```

Por defecto, tu aplicación estará disponible en `http://127.0.0.1:5000/`.

## Desarrollo

Flask tiene soporte para la recarga automática mientras desarrollas. Asegúrate de establecer la variable de entorno `FLASK_ENV` a `development` para activar este modo:

```
export FLASK_ENV=development
```

Después de esto, cualquier cambio que realices en tu aplicación se reflejará automáticamente sin tener que reiniciar el servidor.

## Despliegue

Flask por sí solo no está diseñado para ser usado en producción. Considera usar un servidor como Gunicorn y un reverse proxy como Nginx para desplegar tu aplicación en un entorno de producción.
