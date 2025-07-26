#!/bin/bash
echo "🚀 Iniciando desarrollo de BRIDGE"

# Verificar si estamos en el directorio correcto
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ No se encuentra docker-compose.yml"
    echo "Ejecuta este script desde ~/Documents/n8n/Bridge/"
    exit 1
fi

# Iniciar servicios Docker
echo "🐳 Iniciando PostgreSQL y Redis..."
docker-compose up -d postgres redis

# Esperar a que los servicios estén listos
echo "⏳ Esperando que los servicios estén listos..."
sleep 10

# Verificar que los servicios estén corriendo
if ! docker ps | grep -q "bridge_lewis_postgres"; then
    echo "❌ PostgreSQL no se inició correctamente"
    exit 1
fi

if ! docker ps | grep -q "bridge_lewis_redis"; then
    echo "❌ Redis no se inició correctamente"
    exit 1
fi

echo "✅ Servicios Docker iniciados correctamente"

# Backend
echo "🐍 Configurando backend..."
cd backend

# Verificar entorno virtual
if [ ! -d "venv" ]; then
    echo "❌ Entorno virtual no encontrado. Ejecuta ./scripts/setup.sh primero"
    exit 1
fi

# Activar entorno virtual
source venv/bin/activate

# Ejecutar migraciones
echo "🔄 Ejecutando migraciones..."
python manage.py migrate

# Crear usuario Lewis si no existe
echo "👤 Creando usuario Lewis..."
python manage.py create_lewis_admin

# Iniciar servidor Django
echo "🌐 Iniciando servidor Django en http://localhost:8000"
echo "🔗 Admin: http://localhost:8000/admin"
echo "📖 API Docs: http://localhost:8000/api/docs/"
echo ""
echo "Credenciales de Lewis:"
echo "Usuario: lewis"
echo "Email: lewis@bridge.bo"
echo "Password: LewisAdmin2024!"
echo ""

python manage.py runserver
