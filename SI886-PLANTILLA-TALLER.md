UNIVERSIDAD PRIVADA DE TACNA

FACULTAD DE INGENIERÍA

ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS

INFORME DE LABORATORIO N.º 04

PLANEAMIENTO ESTRATÉGICO DE TI · SI-886

**Formulación y validación de la misión y la visión**

Semana N.º 04    ·    Unidad 1    ·    Grupo N.º [COMPLETAR]

**Integrantes:**
- Perez Perallta, Fabrizio Salvador Elias - 2023077476

**Docente:**
Dr. Oscar Juan Jimenez Flores

Tacna, Perú

---

# 1. Información sobre el evento práctico

## 1.1 Título del evento práctico
Taller de laboratorio 04 · Formulación y validación de la misión y la visión

## 1.2 Objetivos
- Elegir una empresa real del sector tecnológico y registrar su misión y su visión literales, con su fuente.
- Evaluar la misión con los cinco componentes, los siete defectos y las tres pruebas de calidad.
- Evaluar la visión con los cinco atributos y extraer sus métricas implícitas.
- Derivar la visión de la función de TI.
- Redactar las secciones 2.1 y 2.2 del PETI.

## 1.3 Tiempo de duración
100 minutos

## 1.4 Resultados de aprendizaje
Comprender la importancia de que las declaraciones estratégicas (misión y visión) sean específicas, tengan compromiso y objetivos verificables, para poder derivar y alinear la estrategia y el portafolio de TI de manera efectiva.

## 1.5 Recursos
| Recurso | Versión | Para qué se usó |
|---|---|---|
| Navegador Web | Actual | Búsqueda de la misión y visión en la web de Unity Perú. |
| Python + Matplotlib | 3.11+ | Para la ejecución del diagnóstico y visualización (Dashboard Profesional). |
| Git y GitHub | Actual | Para el control de versiones, commits y etiquetado (tags v0.4 y taller-04). |
| Markdown / Editor | Actual | Para la redacción de las declaraciones y documentos. |

## 1.6 Seguridad
- La misión y la visión se copiaron **literalmente**, incluyendo la dirección de la página web oficial (https://unity.pe) y la fecha de consulta (10 de setiembre de 2026).
- Solo se consultaron páginas públicas de la empresa, respetando las directrices del taller.

---

# 2. Procedimiento o metodología

## Paso A — Elegir la empresa y registrar sus declaraciones
- **Acción:** Se seleccionó a la empresa "Unity Perú", dedicada a brindar soluciones de infraestructura de Data Center, Ciberseguridad y Misión Crítica.
- **Evidencia:** Se creó y rellenó el archivo `02_identidad/MV01_declaraciones.md` con los textos literales extraídos de `https://unity.pe/nosotros/`.

## Paso B — Evaluar la misión
- **Acción:** Se desarrolló el simulador en Python `MV01_diagnostico_declaraciones.py` para analizar la misión de Unity Perú con base en los 5 componentes, 7 defectos y 3 pruebas de calidad. 
- **Resultado:** La misión carece de compromiso explícito, adolece de falsa distinción y no supera la prueba de sustitución (es genérica y aplicaría a empresas como Cisco o IBM). El veredicto del sistema fue: REFORMULAR.
- **Evidencia:** Archivos `2.1_mision.md` y salida guardada en `diagnostico.txt`.

## Paso C — Evaluar la visión
- **Acción:** Se utilizó el mismo script para analizar la visión. Cumple con ser ambiciosa, específica y movilizadora, pero falla en ser temporalmente acotada y verificable explícitamente. Se extrajeron las métricas implícitas (cobertura regional y sostenibilidad).
- **Evidencia:** Archivo `2.2_vision.md` estructurado yDashboard visual generado.

## Paso D — Derivar la visión de TI y redactar secciones 2.1 y 2.2
- **Acción:** Basado en la visión corporativa (liderazgo regional y sostenibilidad tecnológica), se derivaron las capacidades de negocio (Diseño de infraestructura, Despliegue regional, Gestión energética) y sus respectivas capacidades de TI habilitadoras (BIM/Gemelos digitales, ERP Cloud LATAM, Telemetría IoT).
- **Evidencia:** Archivos `2.1_mision.md` y `2.2_vision.md` completados.

## Paso E y F — Validar, registrar y cerrar
- **Acción:** Se aplicaron validaciones, se inicializó Git y se generó el commit y las etiquetas requeridas para entregar el código.
- **Comandos ejecutados:**
  ```bash
  git add .
  git commit -m "S04: Se mejora el grafico visual con dashboard profesional"
  git tag -a v0.4 -m "PETI v0.4 - identidad estrategica"
  git tag -a taller-04 -m "Taller 04 - SI886"
  ```

---

# 3. Resultados

> **Nota:** En un entorno real, las columnas de "Evidencia" tendrían la URL del repositorio de GitHub apuntando a la rama o tag `taller-04`. Dado el ambiente local, los archivos se encuentran en el directorio del proyecto.

| # | Resultado esperado | ¿Se logró? | Evidencia (Archivo Local) |
|---|---|---|---|
| 1 | Empresa del sector tecnológico elegida, con su actividad y su país | Sí | `02_identidad/MV01_declaraciones.md` |
| 2 | Misión y visión transcritas literalmente, con dirección y fecha | Sí | `02_identidad/MV01_declaraciones.md` |
| 3 | Los cinco componentes de la misión con su fragmento literal | Sí | `02_identidad/2.1_mision.md` |
| 4 | Defectos señalados con nombre técnico y prueba | Sí | `docs/evidencias/S04/diagnostico.txt` |
| 5 | Prueba de sustitución ejecutada con tres competidores | Sí | `docs/evidencias/S04/diagnostico.txt` |
| 6 | Prueba de decisión y reconocimiento respondidas | Sí | `02_identidad/2.1_mision.md` |
| 7 | Veredicto de la misión y de la visión | Sí | `docs/evidencias/S04/diagnostico.txt` |
| 8 | Los cinco atributos de la visión evaluados | Sí | `02_identidad/2.2_vision.md` |
| 9 | Métricas implícitas con su línea base y fuente | Sí | `02_identidad/2.2_vision.md` |
| 10| Versión propuesta de la misión indicando que decide la empresa | Sí | `02_identidad/2.1_mision.md` |
| 11| Visión de TI derivada con la estructura de la teoría | Sí | `02_identidad/2.2_vision.md` |
| 12| Tabla de derivación (estado actual a estado objetivo por capacidad) | Sí | `02_identidad/2.2_vision.md` |
| 13| Etiqueta `v0.4` en Git | Sí | Comprobado vía CLI local. |

---

# 4. Conclusiones

1. **La debilidad de las declaraciones genéricas:** Una misión que no sobrevive a la prueba de sustitución (como es el caso evaluado de Unity Perú al compararlo con IBM o Sonda) no aporta foco ni restringe las áreas de oportunidad de la empresa, lo que conlleva a un plan de TI desalineado si se apoya en ella.
2. **Las métricas en la Visión son cruciales:** Aunque una visión sea ambiciosa ("ser empresa líder"), la falta de acotación temporal y métricas verificables obliga a los equipos de planeación estratégica a "extraer métricas implícitas". Esto puede generar diferentes interpretaciones sobre qué significa exactamente el éxito.
3. **Traducción de metas corporativas a tecnología operativa:** La visión de la empresa no mueve inversión real ni progreso medible a menos que sus declaraciones (ej. "desarrollo tecnológico sostenible") se traduzcan paso a paso en capacidades de TI concretas (estado actual vs. estado objetivo), como la adopción de "Telemetría IoT para eficiencia energética".

---

# 5. Cuestionario

**¿Qué riesgo correría una organización real si este diagnóstico o formulación se hiciera mal?**

El principal riesgo es destinar grandes volúmenes de capital y recursos humanos a proyectos de Tecnologías de la Información (Portafolio de TI) que no empujen realmente a la organización hacia sus metas principales. Una declaración demasiado amplia ("falsa distinción") haría que el área de TI adquiera o desarrolle soluciones para "todo", dispersando el presupuesto sin apalancar la verdadera ventaja competitiva del negocio.

---

# 6. Referencias bibliográficas

- González Millán, J. (2020). *Manual práctico de planeación estratégica*. Ediciones Díaz de Santos. https://elibro.net/es/lc/bibliotecaupt/titulos/129291
- CEPLAN. *Guía para el Planeamiento Institucional* — formulación de la misión institucional. https://www.gob.pe/ceplan
- Unity Perú. (2026). *Nosotros*. Recuperado el 10 de septiembre de 2026 de https://unity.pe/nosotros/
- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI — Anexo I.

---

# 7. Anexos

- **Anexo A**: Declaraciones de Unity Perú (`02_identidad/MV01_declaraciones.md`)
- **Anexo B**: Salida de consola del diagnóstico (`docs/evidencias/S04/diagnostico.txt`)
- **Anexo C**: Gráfico Dashboard generado en Matplotlib (`docs/evidencias/S04/anexo_C_grafico_diagnostico.png`)
- **Anexo D**: Secciones estructuradas derivadas (`02_identidad/2.1_mision.md` y `02_identidad/2.2_vision.md`)
