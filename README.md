# Proyecto de Investigación en Optimización

## Descripción del Proyecto

Este proyecto implementa y compara dos métodos de optimización numérica para minimizar la siguiente función objetivo:

$$f(x,y) = 10(y - x^2)^2 + \frac{(x-1)^2}{2} + (y-1)^2$$

### Métodos Implementados

1. **Newton-CG (Conjugate Gradient)**: Método de Newton que utiliza gradiente conjugado para resolver el sistema lineal en cada iteración
2. **Quasi-Newton BFGS**: Método quasi-Newton que aproxima la matriz Hessiana mediante actualizaciones sucesivas

## Estructura del Proyecto

```
OptimProj/
├── README.md                           # Este archivo
├── Informe.md                          # Análisis teórico extendido (español)
├── Implementation/
│   ├── Methods_Implementation.ipynb    # Implementación en Jupyter Notebook
│   ├── Experiments/
│   │   ├── exp1.json                   # Configuración experimento 1
│   │   └── exp2.json                   # Configuración experimento 2
│   └── Results/
│       ├── results_exp1.json           # Resultados experimento 1
│       └── results_exp2.json           # Resultados experimento 2
```

## Requisitos del Sistema

### Software Necesario

- **Python**: Versión 3.7 o superior
- **Jupyter**: Para ejecutar notebooks interactivos

### Librerías de Python

```
numpy>=1.19.0
scipy>=1.5.0
matplotlib>=3.3.0
jupyter>=1.0.0
```

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd OptimProj
```

### 2. Crear entorno virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install numpy scipy matplotlib jupyter
```

O usando un archivo de requisitos:

```bash
pip install -r requirements.txt
```

## Uso del Proyecto

### Opción 1: Ejecutar Jupyter Notebook (Recomendado)

1. Iniciar Jupyter Notebook:
```bash
cd Implementation
jupyter notebook
```

2. Abrir `Methods_Implementation.ipynb` en el navegador

3. Ejecutar las celdas secuencialmente:
   - **Celdas 1-2**: Importar librerías y definir funciones
   - **Celdas 3-4**: Definir métodos de optimización y framework
   - **Celda 5**: Ejecutar experimentos (genera resultados JSON)
   - **Celdas 6-8**: Visualizar gráficas
   - **Celda 9**: Ver resumen de resultados

### Opción 2: Ejecutar desde Python

```python
import sys
sys.path.append('Implementation')

# Importar y ejecutar
from Methods_Implementation import MakeExperiments
MakeExperiments()
```

## Cómo Ejecutar Experimentos

### Configuración de Experimentos

Los experimentos se configuran mediante archivos JSON en `Implementation/Experiments/`:

**Formato del archivo JSON:**
```json
[
  {
    "learning_rate": 0.01,
    "tol": 1e-6,
    "max_iter": 1000,
    "x0": [0.0, 0.0]
  }
]
```

**Parámetros:**
- `learning_rate`: Tasa de aprendizaje (no se usa directamente en SciPy, pero se guarda para referencia)
- `tol`: Tolerancia de convergencia
- `max_iter`: Número máximo de iteraciones
- `x0`: Punto inicial `[x, y]`

### Ejecutar Experimentos

**Método 1 - Desde Notebook:**
```python
MakeExperiments()
```

**Método 2 - Crear nuevos experimentos:**

1. Crear archivo `Implementation/Experiments/exp3.json`
2. Ejecutar `MakeExperiments()` nuevamente
3. Los resultados se guardarán automáticamente en `Implementation/Results/results_exp3.json`

### Interpretar Resultados

Los resultados JSON contienen:

```json
{
  "config": { ... },
  "newton_cg": {
    "x_optimal": [1.0, 1.0],
    "f_optimal": 0.0,
    "iterations": 10,
    "function_evaluations": 50,
    "gradient_evaluations": 30,
    "execution_time": 0.001234,
    "distance_to_optimum": 1.5e-10,
    "success": true
  },
  "bfgs": { ... }
}
```

## Análisis Teórico

El documento `Informe.md` contiene:

1. **Definición de la función**: Dominio, signo y propiedades
2. **Análisis matemático**: Continuidad, diferenciabilidad
3. **Cálculo del gradiente**: Derivadas parciales
4. **Matriz Hessiana**: Segundas derivadas
5. **Análisis de convexidad**: Determinación de convexidad
6. **Mínimo teórico**: Punto crítico en (1, 1) con f(1,1) = 0
7. **Descripción de algoritmos**: Newton-CG y BFGS
8. **Comparación de métodos**: Criterios y resultados esperados

**Resultado teórico principal:**
- **Mínimo global único**: $(x^*, y^*) = (1, 1)$
- **Valor mínimo**: $f(1, 1) = 0$

## Visualizaciones Incluidas

### 1. Superficie 3D
Representación tridimensional de la función objetivo con el mínimo marcado.

### 2. Curvas de Nivel con Trayectorias
Contornos de la función mostrando las rutas de convergencia desde diferentes puntos iniciales.

### 3. Comparación de Convergencia
Gráficas comparativas de iteraciones y tiempo de ejecución entre métodos.

## Resultados Esperados

### Newton-CG
- ✓ Convergencia rápida (5-15 iteraciones típicamente)
- ✓ Alta precisión final (distancia < 1e-10)
- ✓ Requiere cálculo/aproximación de Hessiana

### BFGS
- ✓ Convergencia robusta (10-30 iteraciones típicamente)
- ✓ Buena precisión final
- ✓ Solo requiere gradiente

## Comparación de Métodos

| Criterio | Newton-CG | BFGS |
|----------|-----------|------|
| Velocidad de convergencia | Cuadrática | Superlineal |
| Información requerida | Gradiente + Hessiana | Solo gradiente |
| Iteraciones típicas | Menos | Más |
| Tiempo por iteración | Mayor | Menor |
| Robustez | Alta | Muy alta |

## Solución de Problemas

### Error: "Module not found"
```bash
pip install numpy scipy matplotlib jupyter
```

### Error: "Experiments directory not found"
Asegúrate de estar en el directorio correcto:
```bash
cd Implementation
```

### Los gráficos no se muestran
En Jupyter Notebook, añade al inicio:
```python
%matplotlib inline
```

## Contribuciones y Desarrollo

Para modificar o extender el proyecto:

1. **Añadir nuevos experimentos**: Crear archivos JSON en `Experiments/`
2. **Modificar la función**: Editar `f(x)` y `grad_f(x)` en el notebook
3. **Añadir métodos**: Implementar nuevas funciones `optimize_<method>`
4. **Nuevas visualizaciones**: Extender la sección de gráficas

## Autores y Reconocimientos

Proyecto de investigación en optimización numérica.

### Referencias

- Nocedal, J., & Wright, S. J. (2006). *Numerical Optimization* (2nd ed.). Springer.
- SciPy Documentation: https://docs.scipy.org/doc/scipy/reference/optimize.html

## Licencia

Este proyecto es de uso académico y educativo.

---

**Fecha de creación**: Noviembre 2025  
**Versión**: 1.0
