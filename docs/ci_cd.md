# Flujo General CI/CD

Este workflow se ejecuta en cada Pull Request a las ramas:

- `main`
- `develop`
- `feature/*`
- `release/*`
- `hotfix/*`

Realiza:

- Checkout del código
- Configuración del entorno Python 3.10
- Instalación de dependencias
- Ejecución de tests con reporte de cobertura
- Subida de reportes como artefactos
- Anotación automática de errores en el PR
- Comentarios de cobertura de código en el PR
- Escaneo de calidad con SonarQube
