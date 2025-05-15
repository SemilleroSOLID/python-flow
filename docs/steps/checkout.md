# Checkout del Código

En este paso se utiliza la acción oficial de GitHub para obtener el código del repositorio en la máquina donde corre la acción.

```yaml
- name: Checkout del código
  uses: actions/checkout@v4


---

### `docs/steps/setup_python.md`

```markdown
# Configurar Python

Configura el entorno para usar Python 3.10 con esta acción oficial:

```yaml
- name: Configurar Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.10'


---

### `docs/steps/install_deps.md`

```markdown
# Instalar Dependencias

Aquí se actualiza pip e instalan las dependencias listadas en `requirements.txt`:

```yaml
- name: Instalar dependencias
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt


---

### `docs/steps/run_tests.md`

```markdown
# Ejecutar Tests con Cobertura

Se ejecutan las pruebas unitarias y se genera el reporte de cobertura:

```yaml
- name: Ejecutar tests con cobertura
  run: |
    mkdir -p test-results
    coverage run --source=app -m xmlrunner discover -s tests -o test-results || true
    coverage xml -o coverage.xml || true
    coverage html -d coverage_html || true


---

### `docs/steps/upload_reports.md`

```markdown
# Subir Reportes como Artefacto

Se suben los resultados de pruebas y cobertura como artefactos para descargar en GitHub Actions:

```yaml
- name: Subir reportes como artefacto
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: reportes
    path: |
      test-results
      coverage_html


---

### `docs/steps/upload_reports.md`

```markdown
# Subir Reportes como Artefacto

Se suben los resultados de pruebas y cobertura como artefactos para descargar en GitHub Actions:

```yaml
- name: Subir reportes como artefacto
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: reportes
    path: |
      test-results
      coverage_html


---

### `docs/steps/annotate_pr.md`

```markdown
# Anotar Errores de Tests en el PR

Se usan los reportes JUnit para mostrar errores directamente en los archivos del PR:

```yaml
- name: Anotar errores de tests en el PR
  uses: mikepenz/action-junit-report@v4
  if: always()
  with:
    report_paths: 'test-results/*.xml'


---

### `docs/steps/comment_coverage.md`

```markdown
# Comentar Cobertura en el PR

Se usa la acción `orgoro/coverage` para comentar la cobertura del código en el PR:

```yaml
- name: Comentar cobertura en el PR
  uses: orgoro/coverage@v3.2
  if: always()
  with:
    coverageFile: coverage.xml
    token: ${{ secrets.GITHUB_TOKEN }}
    thresholdAll: 0.8
    thresholdNew: 0.9
    thresholdModified: 0.5


---

### `docs/steps/sonarqube.md`

```markdown
# Escaneo con SonarQube

Al final del workflow se ejecuta el análisis estático de código con SonarQube:

```yaml
- name: Run SonarQube scan
  uses: SonarSource/sonarqube-scan-action@v4
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
  with:
    args: >
      -Dsonar.organization=semillerosolid
      -Dsonar.projectKey=SemilleroSOLID_python-flow


