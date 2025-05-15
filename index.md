# 🐍 Python Unittest + Coverage + GitHub Actions

Bienvenido a la documentación del proyecto **Python Flow**.  
Este repositorio implementa una estructura básica para proyectos Python con pruebas automáticas, integración continua, cobertura de código y buenas prácticas de GitFlow.

---

## 🚀 Características principales

- ✅ Pruebas unitarias con `unittest`
- ✅ Reportes de cobertura con `coverage.py`
- ✅ Reportes en formato JUnit para GitHub
- ✅ Comentarios automáticos en Pull Requests con cobertura
- ✅ Integración con SonarQube
- ✅ Workflow con ramas `feature/`, `release/`, `hotfix/`, `develop`, y `main`

---

## 🧪 Estructura del Proyecto

```bash
.
├── app/
│   ├── main.py          # Funciones principales
│   └── nueva_func.py    # (opcional) Más funcionalidades
│
├── tests/
│   ├── test_calc.py     # Pruebas para main.py
│   └── test_nueva.py    # Pruebas para nueva_func.py
│
├── requirements.txt     # Dependencias
├── .github/workflows/   # CI/CD en GitHub Actions
