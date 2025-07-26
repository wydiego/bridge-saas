#!/bin/bash
echo "🚀 Setup inicial de BRIDGE"

cd backend

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado"
    exit 1
fi

# Crear entorno virtual
echo "🐍 Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
echo "⚡ Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo "✅ Setup completado!"
echo ""
echo "Para continuar:"
echo "1. cd backend"
echo "2. source venv/bin/activate"
echo "3. python manage.py migrate"
echo "4. python manage.py create_lewis_admin"
echo "5. python manage.py runserver"
