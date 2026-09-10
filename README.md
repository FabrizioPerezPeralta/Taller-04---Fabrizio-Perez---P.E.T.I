# Taller 04 - Formulación y validación de la misión y la visión

Este repositorio contiene el desarrollo del Laboratorio 04 correspondiente a la **Semana 04** del curso **Planeamiento Estratégico de TI (SI-886)** de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna.

En este taller se ha formulado, analizado y validado la identidad estratégica (Misión y Visión) de la empresa **Unity Perú**.

**Autor:** Fabrizio Salvador Elias Perez Perallta - 2023077476

---

## 📂 Estructura y Redirección del Proyecto

Todo el trabajo se ha dividido en los siguientes archivos y carpetas, tal como lo establece el taller. Haz clic en los enlaces para ir directamente al contenido:

### 1. Documentación Estratégica (`/02_identidad`)
Esta carpeta guarda las declaraciones originales y las secciones derivadas que formarán parte del documento PETI final:
- 📄 [**`MV01_declaraciones.md`**](./02_identidad/MV01_declaraciones.md): Registro literal de la misión y visión extraídas de la página oficial de Unity Perú.
- 📄 [**`2.1_mision.md`**](./02_identidad/2.1_mision.md): Análisis componente a componente de la misión, resultados de las tres pruebas de calidad y la versión propuesta tras hallar defectos.
- 📄 [**`2.2_vision.md`**](./02_identidad/2.2_vision.md): Análisis de los atributos de la visión, extracción de métricas implícitas y derivación de las **capacidades de TI** requeridas a futuro.

### 2. Automatización y Diagnóstico
- 🐍 [**`MV01_diagnostico_declaraciones.py`**](./02_identidad/MV01_diagnostico_declaraciones.py): Script en Python que automatiza la evaluación de los componentes y atributos. **Nota:** Incluye un Dashboard Profesional usando `matplotlib`.

### 3. Evidencias y Anexos (`/docs/evidencias/S04`)
- 📝 [**`diagnostico.txt`**](./docs/evidencias/S04/diagnostico.txt): Salida en texto plano generada por el script de diagnóstico.
- 📊 [**`anexo_C_grafico_diagnostico.png`**](./docs/evidencias/S04/anexo_C_grafico_diagnostico.png): Dashboard visual generado por el script que resume el nivel de cumplimiento de las declaraciones estratégicas.

### 4. Informe Final
- 📑 [**`SI886-PLANTILLA-TALLER.md`**](./SI886-PLANTILLA-TALLER.md): Es la plantilla oficial del curso completamente **rellenada** con el procedimiento, resultados y conclusiones de este taller. Lista para ser exportada a PDF.

---

## 🚀 Cómo ejecutar el Dashboard de Diagnóstico Visual

El script evalúa la calidad de la misión y visión, guardando los resultados en formato texto y además generando automáticamente un reporte visual tipo dashboard usando gráficos de anillo (donuts).

**Prerrequisitos:** 
Tener Python 3.11+ instalado con la librería `matplotlib`.
```bash
pip install matplotlib
```

**Ejecución:**
Desde la raíz del proyecto, ejecuta el siguiente comando:
```bash
python 02_identidad/MV01_diagnostico_declaraciones.py
```
*Esto generará y abrirá automáticamente la imagen `anexo_C_grafico_diagnostico.png` en el visor de fotos predeterminado de tu sistema operativo.*

---

## 📝 Resumen de Resultados (Unity Perú)
- **Misión:** Se identificó que carece de un compromiso explícito y presenta una distinción falsa (es genérica y aplicaría a otros integradores de TI como Cisco o IBM). El veredicto del sistema fue **REFORMULAR**.
- **Visión:** Es ambiciosa y específica, movilizando a la empresa hacia el desarrollo sostenible y la expansión regional. Sin embargo, carece de plazos temporales explícitos. Veredicto: **AJUSTAR**.
- **TI:** Gracias al análisis de la visión, se descubrió que para que la empresa alcance el "liderazgo en la región" y la "sostenibilidad", el área de TI deberá implementar herramientas como **BIM / Gemelos Digitales**, **ERP Cloud LATAM** y **Telemetría IoT de eficiencia energética**.
