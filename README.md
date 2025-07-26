# 🌉 BRIDGE SaaS
## Plataforma para Despachantes de Aduana - Bolivia

[![License](https://img.shields.io/badge/License-Private-red.svg)](LICENSE)
[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://djangoproject.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3.13-yellow.svg)](https://python.org/)

> **Sistema integral que moderniza y automatiza los procesos de despacho aduanero en Bolivia, conectando despachantes, agencias y operadores de comercio exterior.**

---

## 🎯 **RESUMEN EJECUTIVO**

**BRIDGE SaaS** es una plataforma de última generación que digitaliza completamente las operaciones de comercio exterior en Bolivia. Combina una arquitectura moderna con funcionalidades específicas del sector aduanero boliviano.

### **🔑 Características Principales:**
- 🚢 **Gestión completa de despachos** (DIM, DAM, liquidaciones)
- 📄 **Centro documental inteligente** con OCR y validación automática
- 📊 **Dashboard ejecutivo** con métricas en tiempo real
- 🔗 **Integraciones nativas** con SIDUNEA y sistemas gubernamentales
- 💰 **Módulo financiero** con facturación y conciliación automática
- 🎯 **CRM especializado** para el sector aduanero

---

## 📁 **ESTRUCTURA DEL PROYECTO**

```
bridge-saas-private/
├── 📋 DOCUMENTACIÓN
│   ├── README.md                    # 📖 Este archivo - Guía principal
│   ├── docs/                        # 📚 Documentación técnica completa
│   │   ├── bridge_credentials.txt   # 🔐 Credenciales de acceso al sistema
│   │   └── BRIDGE SaaS PLANO GENERAL.txt # 🗺️ Arquitectura completa
│   └── docker-compose.yml           # 🐳 Configuración Docker
│
├── 🔧 BACKEND (API + Base de Datos)
│   └── backend/                     # 🐍 Aplicación Django REST API
│       ├── manage.py                # ⚡ Comando principal Django
│       ├── requirements.txt         # 📦 Dependencias Python
│       ├── bridge_core/             # ⚙️ Configuración principal
│       │   ├── settings.py          # 🔧 Configuraciones Django
│       │   ├── urls.py              # 🌐 URLs principales
│       │   └── wsgi.py              # 🚀 Servidor WSGI
│       └── apps/                    # 📱 Módulos de negocio
│           ├── authentication/      # 🔐 Sistema de usuarios y roles
│           ├── clients/             # 🏢 Gestión de clientes
│           ├── customs/             # 🚢 Despachos aduaneros
│           ├── documents/           # 📄 Gestión documental
│           ├── dashboard/           # 📊 Panel de control
│           ├── reports/             # 📈 Reportes y análisis
│           └── audit/               # 🔍 Auditoría y trazabilidad
│
├── 🌐 FRONTEND (Interfaz de Usuario)
│   └── frontend/                    # ⚛️ Aplicación Next.js + TypeScript
│       ├── package.json             # 📦 Dependencias Node.js
│       ├── next.config.js           # ⚙️ Configuración Next.js
│       ├── tailwind.config.js       # 🎨 Configuración Tailwind CSS
│       └── src/                     # 💻 Código fuente
│           ├── components/          # 🧩 Componentes React reutilizables
│           │   └── Dashboard.tsx    # 📊 Dashboard principal (9.8KB)
│           ├── pages/               # 📄 Páginas de la aplicación
│           │   ├── _app.tsx         # ⚙️ Configuración global + Tailwind
│           │   └── index.tsx        # 🏠 Página principal
│           └── styles/              # 🎨 Estilos globales
│               └── globals.css      # 🌐 CSS global
│
├── 🔧 DEVOPS & UTILIDADES
│   ├── docker/                      # 🐳 Configuraciones Docker
│   │   └── postgres/                # 🗄️ Setup PostgreSQL
│   └── scripts/                     # 🛠️ Scripts de automatización
│       ├── setup.sh                 # 🚀 Instalación completa
│       ├── setup_fixed.sh           # 🔧 Setup corregido
│       └── dev.sh                   # 🎯 Desarrollo rápido
│
└── 📊 DATOS & LOGS
    ├── logs/                        # 📝 Logs de aplicación
    └── media/                       # 🖼️ Archivos multimedia
```

---

## 🏗️ **ARQUITECTURA TÉCNICA**

### **🔧 Backend: Django REST Framework**
```python
# Stack Robusto y Escalable
Framework: Django 4.2 LTS + Django REST Framework
Lenguaje: Python 3.13
Base de Datos: PostgreSQL 14
Cache: Redis 6.x
API: RESTful con documentación OpenAPI
Autenticación: JWT + OAuth 2.0
```

### **🌐 Frontend: Next.js + TypeScript**
```typescript
// Interfaz Moderna y Responsiva
Framework: Next.js 14 con TypeScript
UI: Tailwind CSS + Componentes personalizados
Estado: React Hooks + Context API
Gráficos: Chart.js para dashboards interactivos
Performance: SSR + SSG optimizado
```

### **🗄️ Base de Datos: PostgreSQL**
```sql
-- Estructura Optimizada para Comercio Exterior
- Clientes y proveedores
- Despachos aduaneros (DIM, DAM, liquidaciones)
- Documentos con versionado
- Auditoría completa de operaciones
- Métricas y reportes en tiempo real
```

---

## 🎯 **MÓDULOS PRINCIPALES**

### **🔐 Authentication** - Sistema de Usuarios
- **Propósito**: Gestión completa de usuarios, roles y permisos
- **Funcionalidades**: Login/logout, JWT tokens, roles granulares
- **Estado**: ✅ **Completamente funcional** (2,861 bytes de código)

### **🏢 Clients** - Gestión de Clientes
- **Propósito**: CRM especializado para importadores/exportadores
- **Funcionalidades**: Registro, evaluación, historial de operaciones
- **Estado**: 🔄 **En desarrollo** (254 bytes - estructura básica)

### **🚢 Customs** - Despachos Aduaneros
- **Propósito**: Core del sistema - gestión completa de despachos
- **Funcionalidades**: DIM, DAM, liquidaciones, seguimiento SIDUNEA
- **Estado**: 🔄 **En desarrollo** (254 bytes - estructura básica)

### **📄 Documents** - Centro Documental
- **Propósito**: Gestión inteligente de documentos aduaneros
- **Funcionalidades**: OCR, validación automática, archivo digital
- **Estado**: 🔄 **En desarrollo** (254 bytes - estructura básica)

### **📊 Dashboard** - Panel de Control
- **Propósito**: Métricas ejecutivas y operativas en tiempo real
- **Funcionalidades**: KPIs, gráficos interactivos, alertas
- **Estado**: 🔄 **En desarrollo** (254 bytes backend, frontend completo)

### **📈 Reports** - Reportes y Análisis
- **Propósito**: Business Intelligence para comercio exterior
- **Funcionalidades**: Reportes automáticos, exportación, análisis
- **Estado**: 🔄 **En desarrollo** (254 bytes - estructura básica)

### **🔍 Audit** - Auditoría y Trazabilidad
- **Propósito**: Cumplimiento normativo y trazabilidad completa
- **Funcionalidades**: Logs, audit trail, cumplimiento regulatorio
- **Estado**: 🔄 **En desarrollo** (254 bytes - estructura básica)

---

## 🚀 **INSTALACIÓN Y SETUP**

### **📋 Requisitos Previos**
```bash
# Verificar instalaciones
python3 --version  # Python 3.13+
node --version      # Node.js 18+
git --version       # Git 2.40+
```

### **⚡ Instalación Rápida**
```bash
# 1. Clonar repositorio
git clone https://github.com/wydiego/bridge-saas-private.git
cd bridge-saas-private

# 2. Setup automático
chmod +x scripts/setup.sh
./scripts/setup.sh

# 3. Iniciar servicios
chmod +x scripts/dev.sh
./scripts/dev.sh
```

### **🔧 Instalación Manual**

#### **Backend Setup:**
```bash
cd backend

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

#### **Frontend Setup:**
```bash
cd frontend

# Instalar dependencias
npm install

# Iniciar desarrollo
npm run dev
```

### **🐳 Docker Setup (Alternativo)**
```bash
# Levantar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f
```

---

## 🌐 **URLs DE ACCESO**

### **🔧 Backend Django**
- **API Root**: http://127.0.0.1:8000/api/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **API Docs**: http://127.0.0.1:8000/api/schema/swagger-ui/
- **Redoc**: http://127.0.0.1:8000/api/schema/redoc/

### **🌐 Frontend Next.js**
- **Aplicación**: http://localhost:3000/
- **Dashboard**: http://localhost:3000/ (página principal)

### **🔐 Credenciales de Acceso**
```
Usuario: lewis
Email: lewis@bridge.bo
Contraseña: LewisAdmin2024!
```

---

## 📊 **ESTADO ACTUAL DEL DESARROLLO**

### **✅ COMPLETAMENTE FUNCIONAL**
- ✅ **Estructura base** del proyecto completa
- ✅ **Backend Django** configurado con 7 apps modulares
- ✅ **Frontend Next.js** funcionando con dashboard visual
- ✅ **Autenticación** completa y funcional
- ✅ **Base de datos** PostgreSQL configurada
- ✅ **Dashboard UI** moderno y responsivo (9,843 bytes)

### **🔄 EN DESARROLLO (Pendientes)**
- 🔄 **Modelos Django** - Expandir desde estructura básica (254 bytes) a modelos completos
- 🔄 **APIs REST** - Solo authentication funciona, falta CRUD completo
- 🔄 **Conectividad** - Frontend desconectado del backend
- 🔄 **Datos reales** - Dashboard muestra datos simulados
- 🔄 **Funcionalidades específicas** - Despachos, documentos, reportes

### **📈 MÉTRICAS DE CÓDIGO**
```
Total archivos: 97
Líneas de código: ~4,411
Backend Django: ~2,500 líneas
Frontend Next.js: ~1,911 líneas
Documentación: Completa y actualizada
```

---

## 🎯 **PRÓXIMOS PASOS PRIORITARIOS**

### **🔥 CRÍTICO (Esta semana)**
1. **Desarrollar modelos Django completos**
   - Cliente (NIT, razón social, clasificación)
   - Despacho (DIM, DAM, valores, estados)
   - Documento (OCR, validación, versionado)

2. **Crear APIs REST funcionales**
   - Dashboard endpoints (stats, activities, charts)
   - CRUD completo para cada módulo
   - Autenticación JWT integrada

3. **Conectar frontend con backend**
   - Servicios API con axios
   - Manejo de estados y loading
   - Formularios CRUD funcionales

### **🎨 IMPORTANTE (Próximas 2 semanas)**
1. **Modernizar interfaces NEXUS**
   - Rediseñar pantallas del manual
   - Componentes React reutilizables
   - UX intuitiva y moderna

2. **Implementar funcionalidades core**
   - Workflow de despachos aduaneros
   - Sistema de documentos con upload
   - Reportes dinámicos

### **🚀 FUTURO (Próximo mes)**
1. **Integraciones externas**
   - SIDUNEA (simulado)
   - APIs bancarias (simulado)
   - WhatsApp Business

2. **Características avanzadas**
   - OCR inteligente
   - IA para clasificación arancelaria
   - Mobile PWA

---

## 🛠️ **COMANDOS ÚTILES**

### **🔧 Backend (Django)**
```bash
# Desde /backend con venv activado
python manage.py runserver          # Iniciar servidor
python manage.py makemigrations     # Crear migraciones
python manage.py migrate            # Aplicar migraciones
python manage.py createsuperuser    # Crear admin
python manage.py shell              # Shell Django
python manage.py collectstatic      # Archivos estáticos
```

### **🌐 Frontend (Next.js)**
```bash
# Desde /frontend
npm run dev          # Desarrollo
npm run build        # Build producción
npm run start        # Servidor producción
npm run lint         # Linting
```

### **🐳 Docker**
```bash
docker-compose up -d              # Levantar servicios
docker-compose logs -f backend    # Ver logs backend
docker-compose exec backend bash  # Shell en container
docker-compose down               # Bajar servicios
```

---

## 📚 **DOCUMENTACIÓN ADICIONAL**

### **📖 Archivos Clave para Revisar**
- **`docs/bridge_credentials.txt`** - Todas las credenciales del sistema
- **`docs/BRIDGE SaaS PLANO GENERAL.txt`** - Arquitectura detallada
- **`backend/bridge_core/settings.py`** - Configuración Django
- **`frontend/src/components/Dashboard.tsx`** - Dashboard principal

### **🔗 Enlaces Útiles**
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com/)
- [PostgreSQL](https://www.postgresql.org/)

---

## 🤝 **CONTRIBUIR AL PROYECTO**

### **👥 Para Colaboradores**
1. **Clonar** el repositorio privado
2. **Seguir** las instrucciones de instalación
3. **Crear** branch para features: `git checkout -b feature/nueva-funcionalidad`
4. **Hacer** commits descriptivos
5. **Crear** Pull Request para revisión

### **🔍 Para Testing**
1. **Instalar** siguiendo la guía de setup
2. **Probar** todas las funcionalidades actuales
3. **Reportar** bugs en Issues de GitHub
4. **Sugerir** mejoras y nuevas características

---

## 📞 **CONTACTO Y SOPORTE**

**Desarrollador Principal**: Diego Lewensztain (@wydiego)  
**Email**: diegolewensztain@gmail.com  
**Proyecto**: BRIDGE SaaS - Despachantes de Aduana Bolivia

---

## 📄 **LICENCIA**

Este proyecto es **privado** y está protegido por derechos de autor. El acceso está restringido a colaboradores autorizados.

---

<div align="center">

**🌉 BRIDGE SaaS - Conectando el comercio internacional con la era digital**

*Desarrollado con ❤️ para modernizar el comercio exterior boliviano*

</div>
