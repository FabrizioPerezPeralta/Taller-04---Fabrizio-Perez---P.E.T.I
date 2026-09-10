import sys
import matplotlib.pyplot as plt

def show_visual_diagnostic():
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.canvas.manager.set_window_title('Diagnóstico Visual - Unity Perú')
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.95, "Diagnóstico de Declaraciones Estratégicas\nUnity Perú", 
            fontsize=16, weight='bold', ha='center', va='top', color='navy')
            
    # Mision
    ax.text(0.05, 0.85, "MISIÓN", fontsize=14, weight='bold', color='darkred')
    mision_text = "«Proporcionar soluciones tecnológicas integrales y avanzadas que optimicen la\ninfraestructura crítica de sus clientes, garantizando la seguridad y la continuidad operativa»"
    ax.text(0.05, 0.77, mision_text, fontsize=10, style='italic', bbox=dict(facecolor='#f0f0f0', edgecolor='gray', boxstyle='round,pad=0.5'))
    
    # Componentes Misión
    ax.text(0.05, 0.70, "1. Componentes:", fontsize=12, weight='bold')
    comp_text = (
        "[ ✔ ] Qué hacemos\n"
        "[ ✔ ] Para quién\n"
        "[ ✖ ] Cómo nos distingue\n"
        "[ ✔ ] Para qué\n"
        "[ ✖ ] Con qué compromiso"
    )
    ax.text(0.05, 0.53, comp_text, fontsize=11, family='monospace', color='black')

    # Defectos Misión
    ax.text(0.40, 0.70, "2. Defectos Hallados:", fontsize=12, weight='bold')
    def_text = (
        "• Ausencia de compromiso\n"
        "• Falsa distinción (genérica)"
    )
    ax.text(0.40, 0.62, def_text, fontsize=11, color='darkred')
    
    # Pruebas Misión
    ax.text(0.05, 0.45, "3. Pruebas de Calidad:", fontsize=12, weight='bold')
    pruebas_text = (
        "✖ Prueba de sustitución (Falla con Sonda, IBM, etc.)\n"
        "✖ Prueba de la decisión (Falla por ser muy amplia)\n"
        "✖ Prueba del reconocimiento (Falla)"
    )
    ax.text(0.05, 0.33, pruebas_text, fontsize=11, color='black')

    ax.text(0.05, 0.25, "VEREDICTO MISIÓN: REFORMULAR", fontsize=12, weight='bold', color='white', bbox=dict(facecolor='#cc0000', edgecolor='darkred', boxstyle='round,pad=0.5'))

    # Vision
    ax.text(0.55, 0.45, "VISIÓN", fontsize=14, weight='bold', color='darkblue')
    vis_text = (
        "«Consolidarse como una empresa líder en soluciones de\n"
        "infraestructura tecnológica en la región, marcando nuevos\n"
        "estándares de calidad e innovación...»"
    )
    ax.text(0.55, 0.33, vis_text, fontsize=9, style='italic', bbox=dict(facecolor='#f0f8ff', edgecolor='blue', boxstyle='round,pad=0.5'))

    # Atributos
    ax.text(0.55, 0.25, "Atributos:", fontsize=12, weight='bold')
    attr_text = (
        "[ ✖ ] Temporalmente acotada\n"
        "[ ✖ ] Verificable\n"
        "[ ✔ ] Ambiciosa pero alcanzable\n"
        "[ ✔ ] Específica del negocio\n"
        "[ ✔ ] Movilizadora"
    )
    ax.text(0.55, 0.08, attr_text, fontsize=11, family='monospace')

    ax.text(0.55, 0.02, "VEREDICTO VISIÓN: AJUSTAR", fontsize=12, weight='bold', color='black', bbox=dict(facecolor='#ffcc00', edgecolor='darkorange', boxstyle='round,pad=0.5'))

    plt.tight_layout()
    
    # Guardar en anexos como pide la guia
    import os
    os.makedirs("docs/evidencias/S04", exist_ok=True)
    plt.savefig("docs/evidencias/S04/anexo_C_grafico_diagnostico.png", dpi=150)
    
    # Mostrar la ventana
    plt.show()

def main():
    print("==========================================================")
    print("DIAGNÓSTICO DE DECLARACIONES ESTRATÉGICAS")
    print("==========================================================\n")
    print("EMPRESA: Unity Perú\n")
    print("MISION:")
    print("«Proporcionar soluciones tecnológicas integrales y avanzadas que optimicen la infraestructura crítica de sus clientes, garantizando la seguridad y la continuidad operativa»\n")
    
    print("--- COMPONENTES DE LA MISION ---")
    print("[X] Qué hacemos (Actividad esencial): «Proporcionar soluciones tecnológicas integrales y avanzadas»")
    print("[X] Para quién (Destinatario): «sus clientes»")
    print("[ ] Cómo nos distingue: [Ausente - No especifica un diferenciador único en el método]")
    print("[X] Para qué (Valor que genera): «que optimicen la infraestructura crítica... garantizando la seguridad y la continuidad operativa»")
    print("[ ] Con qué compromiso (Principios): [Ausente]\n")
    
    print("--- DEFECTOS (Solo se listan los presentes) ---")
    print("- Ausencia de compromiso: No declara un principio rector en la misión.")
    print("- Falsa distinción: Carece de un componente que los diferencie de otros proveedores de infraestructura.\n")
    
    print("--- PRUEBAS DE CALIDAD ---")
    print("1. Prueba de sustitución con tres competidores (Cisco, IBM, Sonda): FALLA.")
    print("2. Prueba de la decisión: FALLA.")
    print("3. Prueba del reconocimiento: FALLA.\n")
    
    print("VEREDICTO MISION: REFORMULAR.\n")
    
    print("==========================================================\n")
    print("VISION:")
    print("«Consolidarse como una empresa líder en soluciones de infraestructura tecnológica en la región, marcando nuevos estándares de calidad e innovación, y siendo un pilar en el avance del desarrollo tecnológico sostenible en el Perú»\n")
    
    print("--- ATRIBUTOS DE LA VISION ---")
    print("- Temporalmente acotada: No cumple")
    print("- Verificable: No cumple")
    print("- Ambiciosa pero alcanzable: Cumple")
    print("- Específica del negocio: Cumple")
    print("- Movilizadora: Cumple\n")
    
    print("VEREDICTO VISION: AJUSTAR.")
    print("==========================================================")
    
    # Llamar a la ventana gráfica al final
    try:
        show_visual_diagnostic()
    except Exception as e:
        print("No se pudo mostrar la ventana visual:", e)

if __name__ == '__main__':
    main()
