import React from 'react';
import { 
  Users, 
  FileText, 
  TrendingUp, 
  Clock, 
  AlertCircle, 
  CheckCircle,
  BarChart3,
  DollarSign,
  Package,
  Calendar,
  Bell,
  Search,
  Menu,
  Settings,
  LogOut
} from 'lucide-react';

const Dashboard = () => {
  // Datos simulados para el dashboard
  const stats = [
    {
      title: "Despachos Activos",
      value: "24",
      change: "+12%",
      trend: "up",
      icon: Package,
      color: "text-blue-600"
    },
    {
      title: "Clientes Activos", 
      value: "156",
      change: "+8%",
      trend: "up",
      icon: Users,
      color: "text-green-600"
    },
    {
      title: "Ingresos Mensuales",
      value: "$45,200",
      change: "+15%", 
      trend: "up",
      icon: DollarSign,
      color: "text-purple-600"
    },
    {
      title: "Eficiencia",
      value: "94%",
      change: "+3%",
      trend: "up", 
      icon: TrendingUp,
      color: "text-orange-600"
    }
  ];

  const recentActivities = [
    {
      id: 1,
      type: "despacho",
      title: "DIM-2025-001 completado",
      time: "Hace 15 min",
      status: "completed"
    },
    {
      id: 2,
      type: "cliente",
      title: "Nuevo cliente registrado",
      time: "Hace 1 hora",
      status: "new"
    },
    {
      id: 3,
      type: "alerta",
      title: "Vencimiento de documento",
      time: "Hace 2 horas",
      status: "warning"
    },
    {
      id: 4,
      type: "despacho",
      title: "Inspección pendiente",
      time: "Hace 3 horas",
      status: "pending"
    }
  ];

  const quickActions = [
    { name: "Nuevo Despacho", icon: Package, color: "bg-blue-500" },
    { name: "Agregar Cliente", icon: Users, color: "bg-green-500" },
    { name: "Generar Reporte", icon: FileText, color: "bg-purple-500" },
    { name: "Ver Calendario", icon: Calendar, color: "bg-orange-500" }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="flex items-center justify-between px-6 py-4">
          <div className="flex items-center space-x-4">
            <Menu className="h-6 w-6 text-gray-600 cursor-pointer" />
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">B</span>
              </div>
              <span className="text-xl font-bold text-gray-900">BRIDGE</span>
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
              <input
                type="text"
                placeholder="Buscar..."
                className="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
            <Bell className="h-6 w-6 text-gray-600 cursor-pointer" />
            <Settings className="h-6 w-6 text-gray-600 cursor-pointer" />
            <LogOut className="h-6 w-6 text-gray-600 cursor-pointer" />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex">
        {/* Sidebar */}
        <aside className="w-64 bg-white shadow-sm min-h-screen">
          <nav className="mt-8">
            <div className="px-4 space-y-2">
              <a href="#" className="flex items-center space-x-3 text-gray-700 p-2 rounded-lg bg-blue-50 text-blue-700">
                <BarChart3 className="h-5 w-5" />
                <span className="font-medium">Dashboard</span>
              </a>
              <a href="#" className="flex items-center space-x-3 text-gray-700 p-2 rounded-lg hover:bg-gray-50">
                <Package className="h-5 w-5" />
                <span>Despachos</span>
              </a>
              <a href="#" className="flex items-center space-x-3 text-gray-700 p-2 rounded-lg hover:bg-gray-50">
                <Users className="h-5 w-5" />
                <span>Clientes</span>
              </a>
              <a href="#" className="flex items-center space-x-3 text-gray-700 p-2 rounded-lg hover:bg-gray-50">
                <FileText className="h-5 w-5" />
                <span>Documentos</span>
              </a>
              <a href="#" className="flex items-center space-x-3 text-gray-700 p-2 rounded-lg hover:bg-gray-50">
                <TrendingUp className="h-5 w-5" />
                <span>Reportes</span>
              </a>
            </div>
          </nav>
        </aside>

        {/* Main Dashboard */}
        <main className="flex-1 p-6">
          {/* Welcome Section */}
          <div className="mb-8">
            <h1 className="text-2xl font-bold text-gray-900">¡Bienvenido al Dashboard BRIDGE!</h1>
            <p className="text-gray-600 mt-1">Gestión integral de operaciones aduaneras para Bolivia</p>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            {stats.map((stat, index) => (
              <div key={index} className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-600">{stat.title}</p>
                    <p className="text-2xl font-bold text-gray-900 mt-1">{stat.value}</p>
                    <p className={`text-sm mt-1 ${stat.trend === 'up' ? 'text-green-600' : 'text-red-600'}`}>
                      {stat.change}
                    </p>
                  </div>
                  <div className={`p-3 rounded-lg ${stat.color} bg-opacity-10`}>
                    <stat.icon className={`h-6 w-6 ${stat.color}`} />
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Quick Actions */}
          <div className="mb-8">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Acciones Rápidas</h2>
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
              {quickActions.map((action, index) => (
                <button
                  key={index}
                  className="p-4 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow"
                >
                  <div className={`w-12 h-12 ${action.color} rounded-lg flex items-center justify-center mb-3 mx-auto`}>
                    <action.icon className="h-6 w-6 text-white" />
                  </div>
                  <p className="text-sm font-medium text-gray-900">{action.name}</p>
                </button>
              ))}
            </div>
          </div>

          {/* Recent Activity & Chart */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Recent Activity */}
            <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">Actividad Reciente</h3>
              <div className="space-y-4">
                {recentActivities.map((activity) => (
                  <div key={activity.id} className="flex items-center space-x-3">
                    <div className={`w-2 h-2 rounded-full ${
                      activity.status === 'completed' ? 'bg-green-500' :
                      activity.status === 'warning' ? 'bg-yellow-500' :
                      activity.status === 'new' ? 'bg-blue-500' : 'bg-gray-500'
                    }`}></div>
                    <div className="flex-1">
                      <p className="text-sm font-medium text-gray-900">{activity.title}</p>
                      <p className="text-xs text-gray-500">{activity.time}</p>
                    </div>
                    {activity.status === 'completed' && <CheckCircle className="h-4 w-4 text-green-500" />}
                    {activity.status === 'warning' && <AlertCircle className="h-4 w-4 text-yellow-500" />}
                    {activity.status === 'pending' && <Clock className="h-4 w-4 text-gray-500" />}
                  </div>
                ))}
              </div>
            </div>

            {/* Chart Placeholder */}
            <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">Despachos por Mes</h3>
              <div className="h-64 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg flex items-center justify-center">
                <div className="text-center">
                  <BarChart3 className="h-16 w-16 text-blue-500 mx-auto mb-4" />
                  <p className="text-gray-600">Gráfico de despachos</p>
                  <p className="text-sm text-gray-500">Datos en tiempo real</p>
                </div>
              </div>
            </div>
          </div>

          {/* Status Banner */}
          <div className="mt-8 bg-gradient-to-r from-blue-600 to-purple-600 text-white p-6 rounded-xl">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-lg font-semibold">Sistema BRIDGE Operativo</h3>
                <p className="text-blue-100">Todas las integraciones funcionando correctamente</p>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
                <span className="text-sm">En línea</span>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
