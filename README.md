# 🚀 BRIDGE SaaS - Sistema de Gestión para Despachantes de Aduana

<div align="center">
  <img src="https://img.shields.io/badge/version-0.1.0-blue.svg" />
  <img src="https://img.shields.io/badge/status-en%20desarrollo-yellow.svg" />
  <img src="https://img.shields.io/badge/python-3.13-blue.svg" />
  <img src="https://img.shields.io/badge/django-4.2.7-green.svg" />
</div>

## 📝 Descripción

BRIDGE es una plataforma SaaS moderna diseñada específicamente para despachantes de aduana en Bolivia. El sistema digitaliza y automatiza los procesos de despacho aduanero, gestión de clientes, control documental y generación de reportes, cumpliendo con las regulaciones de la Aduana Nacional de Bolivia.

## 🎯 Características Principales

- **🔐 Sistema de Autenticación JWT** con roles y permisos
- **📦 Gestión de Despachos Aduaneros** con flujo completo desde borrador hasta archivo
- **👥 Gestión de Clientes** con categorización y evaluaciones
- **📄 Control Documental** con versionado y trazabilidad
- **📊 Dashboard** con estadísticas en tiempo real
- **📈 Reportes** personalizados y exportables
- **🔍 Auditoría** completa de todas las operaciones

## 🛠️ Stack Tecnológico

### Backend
- **Framework:** Django 4.2.7 + Django REST Framework
- **Base de Datos:** PostgreSQL
- **Cache:** Redis
- **Autenticación:** JWT (djangorestframework-simplejwt)
- **Documentación API:** drf-spectacular (Swagger/Redoc)

### Frontend (En desarrollo)
- **Framework:** Next.js con TypeScript
- **UI:** Tailwind CSS
- **Componentes:** Lucide Icons

## 📁 Estructura del Proyecto

```
bridge-saas/
├── backend/
│   ├── apps/
│   │   ├── authentication/    # ✅ Sistema de usuarios y autenticación
│   │   ├── clients/          # ⚠️  Gestión de clientes (falta API)
│   │   ├── customs/          # ✅ Despachos aduaneros
│   │   ├── documents/        # ⚠️  Gestión documental (falta API)
│   │   ├── dashboard/        # ❌ Panel de control
│   │   ├── reports/          # ❌ Generación de reportes
│   │   └── audit/            # ❌ Auditoría y logs
│   ├── bridge_core/          # Configuración principal Django
│   ├── logs/                 # Archivos de log
│   ├── media/                # Archivos subidos
│   └── static/               # Archivos estáticos
├── frontend/                 # Aplicación Next.js
└── docs/                     # Documentación
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.13+
- PostgreSQL 14+
- Redis (opcional para cache)
- Node.js 18+ (para frontend)

### Backend

1. **Clonar el repositorio:**
```bash
git clone https://github.com/wydiego/bridge-saas-private.git
cd bridge-saas-private/backend
```

2. **Crear entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Variables de entorno requeridas:**
```env
# Django
SECRET_KEY=tu-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=bridge_db
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432

# Redis (opcional)
REDIS_URL=redis://localhost:6379/1

# JWT
JWT_SECRET_KEY=tu-jwt-secret
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000

# Admin
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@bridge.bo
ADMIN_PASSWORD=AdminPassword123!
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=Bridge
```

6. **Ejecutar migraciones:**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Crear superusuario:**
```bash
python manage.py createsuperuser
```

8. **Ejecutar servidor:**
```bash
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📌 API Endpoints

### Autenticación
- `POST /api/auth/login/` - Iniciar sesión
- `GET /api/auth/profile/` - Perfil del usuario
- `POST /api/auth/refresh/` - Refrescar token

### Despachos Aduaneros
- `GET /api/customs/despachos/` - Listar despachos
- `POST /api/customs/despachos/` - Crear despacho
- `GET /api/customs/despachos/{id}/` - Detalle despacho
- `PUT /api/customs/despachos/{id}/` - Actualizar despacho
- `DELETE /api/customs/despachos/{id}/` - Eliminar despacho
- `GET /api/customs/despachos/dashboard_stats/` - Estadísticas

### Documentación API
- `http://127.0.0.1:8000/api/schema/swagger-ui/` - Swagger UI
- `http://127.0.0.1:8000/api/schema/redoc/` - Redoc

## 🔄 Estado del Proyecto

### ✅ Completado
- Sistema de autenticación con JWT
- Modelos de datos principales
- API de despachos aduaneros
- Configuración de infraestructura

### 🚧 En Desarrollo
- APIs de clientes y documentos
- Frontend completo
- Sistema de reportes
- Módulo de auditoría

### 📋 Próximos Pasos
1. Completar serializers y vistas para módulo de clientes
2. Implementar API completa para gestión documental
3. Desarrollar dashboard con estadísticas reales
4. Crear sistema de reportes exportables
5. Implementar auditoría completa
6. Integración con SIDUNEA (Aduana Nacional)

## 📊 Estado de Desarrollo por Módulo

```
Authentication: ████████████████████ 100%
Customs:       ██████████████░░░░░░ 70%
Clients:       ████████░░░░░░░░░░░░ 40%
Documents:     ██████░░░░░░░░░░░░░░ 30%
Dashboard:     ░░░░░░░░░░░░░░░░░░░░ 0%
Reports:       ░░░░░░░░░░░░░░░░░░░░ 0%
Audit:         ░░░░░░░░░░░░░░░░░░░░ 0%
```

## 👥 Contribución

Este es un proyecto privado. Para contribuir, contacta al equipo de desarrollo.

## 📄 Licencia

Proyecto privado - Todos los derechos reservados.

## 📞 Contacto

Para más información sobre BRIDGE SaaS, contacta a:
- Email: info@bridge.bo
- GitHub: [@wydiego](https://github.com/wydiego)

---

*BRIDGE - Conectando el comercio internacional con el futuro digital*
