# BlogFinal - Proyecto Django

Este es un proyecto final de Django para crear una aplicación de blog con funcionalidades como administración, perfiles de usuario y más.

## Pasos para Configurar el Proyecto

### 1. Clonar el Repositorio
Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/BlogFinal.git
```

### 2. Instalar Dependencias
Instala todas las dependencias necesarias para el proyecto ejecutando:

```bash
pip install -r requirements.txt
```

### 3. Aplicar Migraciones
Aplica las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```

### 4. Crear un Superusuario (Opcional)
Si deseas acceder al panel de administración de Django, crea un superusuario:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones que aparecerán en la terminal.

### 5. Ejecutar el Servidor
Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Ahora podrás acceder al blog en [http://127.0.0.1:8000/](http://127.0.0.1:8000/) desde tu navegador.

### 6. Subir Cambios a GitHub
Si realizas cambios en el proyecto y deseas subirlos a GitHub, sigue estos pasos:

1. Agrega todos los archivos al repositorio:

   ```bash
   git add .
   ```

2. Realiza un commit con un mensaje:

   ```bash
   git commit -m "Descripción de los cambios"
   ```

3. Sube los cambios al repositorio remoto:

   ```bash
   git push origin main
   ```

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
BlogFinal/
│
├── blog/                  # Aplicación principal del blog
├── main/                  # Aplicación para el panel de administración
├── manage.py              # Archivo para gestionar el proyecto
├── requirements.txt       # Dependencias del proyecto
└── BlogFinal/             # Configuración principal del proyecto
```

#







