#!/bin/bash
# 🚀 BRIDGE SaaS - Setup Corregido (Fixed Pillow Error)
# Ubicación: ~/Documents/n8n/Bridge

set -e  # Salir si hay errores

echo "🌉 BRIDGE SaaS - Setup Corregido para Lewis"
echo "=============================================="
echo ""

# Verificar ubicación
BRIDGE_PATH="$HOME/Documents/n8n/Bridge"
if [ ! -d "$BRIDGE_PATH" ]; then
    echo "❌ Directorio BRIDGE no encontrado en $BRIDGE_PATH"
    echo "Por favor ejecuta primero el script de creación del proyecto"
    exit 1
fi

cd "$BRIDGE_PATH"

# Crear directorio backend si no existe
if [ ! -d "backend" ]; then
    echo "❌ Directorio backend no encontrado. Ejecuta primero el script de setup inicial."
    exit 1
fi

cd backend

echo "🐍 Iniciando setup corregido de Python..."

# Verificar si Python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado. Instalando..."
    
    # Detectar el sistema operativo
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux - Ubuntu/Debian
        sudo apt update
        sudo apt install -y python3 python3-pip python3-venv python3-dev
        # Instalar dependencias del sistema para Pillow
        sudo apt install -y libjpeg-dev zlib1g-dev libpng-dev libfreetype6-dev
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install python@3.11
            # Instalar dependencias para Pillow en macOS
            brew install jpeg libpng freetype
        else
            echo "❌ Homebrew no está instalado. Por favor instala Python3 manualmente."
            exit 1
        fi
    else
        echo "❌ Sistema operativo no soportado para instalación automática"
        echo "Por favor instala Python3 manualmente"
        exit 1
    fi
fi

echo "✅ Python3 detectado: $(python3 --version)"

# Limpiar entorno virtual anterior si existe
if [ -d "venv" ]; then
    echo "🔄 Limpiando entorno virtual anterior..."
    rm -rf venv
fi

# Crear entorno virtual
echo "🐍 Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
echo "⚡ Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip a la última versión
echo "📦 Actualizando pip..."
pip install --upgrade pip

# Crear requirements.txt corregido (sin Pillow problemático)
echo "📝 Creando requirements.txt corregido..."

cat > requirements.txt << 'EOF'
# Django Core
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1

# Database & Cache
psycopg2-binary==2.9.7
redis==4.6.0
django-redis==5.4.0

# Authentication
djangorestframework-simplejwt==5.3.0
cryptography==41.0.7

# API Documentation
drf-spectacular==0.26.5

# Environment
python-decouple==3.8

# Utils
requests==2.31.0
python-dateutil==2.8.2

# Production
gunicorn==21.2.0
whitenoise==6.6.0

# Development
django-debug-toolbar==4.2.0
django-extensions==3.2.3
EOF

echo "📦 Instalando dependencias Python (sin Pillow por ahora)..."
pip install -r requirements.txt

# Intentar instalar Pillow por separado con mejor manejo de errores
echo "🖼️  Instalando Pillow..."
if pip install Pillow==10.0.1; then
    echo "✅ Pillow instalado correctamente"
else
    echo "⚠️  Pillow falló, intentando con versión más estable..."
    if pip install Pillow==9.5.0; then
        echo "✅ Pillow 9.5.0 instalado correctamente"
    else
        echo "⚠️  Pillow falló nuevamente, instalando sin especificar versión..."
        if pip install Pillow; then
            echo "✅ Pillow instalado con versión automática"
        else
            echo "❌ No se pudo instalar Pillow. El sistema funcionará sin manejo de imágenes."
            echo "Para usar funcionalidades de imágenes, instala las dependencias del sistema:"
            echo "Ubuntu/Debian: sudo apt install libjpeg-dev zlib1g-dev libpng-dev"
            echo "macOS: brew install jpeg libpng freetype"
        fi
    fi
fi

echo "✅ Setup completado!"
echo ""
echo "🚀 Para continuar:"
echo "1. cd $BRIDGE_PATH/backend"
echo "2. source venv/bin/activate"
echo "3. python manage.py migrate"
echo "4. python manage.py create_lewis_admin"
echo "5. python manage.py runserver"
echo ""
echo "🌐 URLs importantes:"
echo "   Backend API: http://localhost:8000"
echo "   Admin Panel: http://localhost:8000/admin"
echo "   API Docs: http://localhost:8000/api/docs/"
echo ""
echo "🔐 Credenciales de Lewis:"
echo "   Usuario: lewis"
echo "   Email: lewis@bridge.bo"
echo "   Password: LewisAdmin2024!"