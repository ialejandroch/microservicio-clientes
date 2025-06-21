
# 🧩 Microservicio de Gestión de Clientes

Este proyecto es un microservicio desarrollado con **FastAPI** para la gestión básica de clientes (crear, consultar, actualizar y eliminar). Está diseñado para ejecutarse como contenedor Docker y desplegarse automáticamente en un clúster de Kubernetes utilizando **Helm** y **ArgoCD** como parte de una arquitectura GitOps.

---

## 🚀 Tecnologías Utilizadas

- **FastAPI**: Framework web para construir APIs rápidas y eficientes en Python.
- **Docker**: Empaquetamiento del microservicio en una imagen liviana.
- **Kubernetes + Minikube**: Entorno de orquestación local para contenedores.
- **Helm**: Gestión de despliegue con charts y valores personalizables.
- **ArgoCD**: Automatización del despliegue GitOps desde el repositorio.
- **GitHub**: Repositorio fuente conectado directamente con ArgoCD.

---

## 🧱 Estructura del Proyecto

```
microservicio-clientes/
│
├── app/
│   ├── main.py
│   ├── models.py
│   └── crud.py
│
├── Dockerfile
├── requirements.txt
│
├── helm/
│   └── microservicio/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           └── service.yaml
│
└── README.md
```

---

## ⚙️ Endpoints del microservicio

Una vez desplegado, accede a la documentación interactiva de la API en:

```
http://localhost:<puerto>/docs
```

Endpoints disponibles:

- `POST /clientes/` - Crear cliente
- `GET /clientes/` - Listar todos los clientes
- `GET /clientes/{cliente_id}` - Consultar cliente por ID
- `PUT /clientes/{cliente_id}` - Actualizar cliente
- `DELETE /clientes/{cliente_id}` - Eliminar cliente

---

## 🐳 Construcción y ejecución con Docker

```bash
# Construir imagen
docker build -t microservicio-clientes .

# Ejecutar localmente
docker run -p 8000:80 microservicio-clientes
```

---

## ☸️ Despliegue en Kubernetes con Helm

```bash
# Desde la raíz del proyecto
cd helm/microservicio

# Instalar el chart
helm install microservicio .

# Si ya existe, usar upgrade
helm upgrade microservicio .
```

---

## 🔄 Automatización con ArgoCD

Este proyecto está conectado con ArgoCD para automatizar el despliegue cada vez que se realiza un **push al repositorio**.

Pasos realizados:

1. Instalación de ArgoCD en el clúster.
2. Creación de `Application` apuntando a este repositorio.
3. Configuración de sincronización automática.
4. Acceso a UI: http://localhost:8080 (con `port-forward` a `svc/argocd-server`)
5. Autenticación inicial con:
   ```bash
   kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 --decode
   ```

---

## 📦 Helm values por defecto

```yaml
replicaCount: 1

image:
  repository: henrychca/microservicio-clientes
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80
```

---

## ✍️ Autor

Henry Alejandro Chicuazuque Castiblanco
Diego Borja
Baney Giomar Acosta Melo
Jorge Enrique Avendaño Ortega
Maira Alejandra Pérez Mondragón 
Weimar Alfredo Avendaño Barragán

[GitHub](https://github.com/ialejandroch)

---


