import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_donut(ax, labels, sizes, colors, title, center_text):
    wedges, texts = ax.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(width=0.3, edgecolor='w'))
    ax.text(0, 0, center_text, ha='center', va='center', fontsize=22, weight='bold', color='#333333')
    ax.set_title(title, fontsize=14, weight='bold', color='#2c3e50', pad=15)
    ax.legend(wedges, labels, loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=1, frameon=False, fontsize=11)

def show_visual_diagnostic():
    fig = plt.figure(figsize=(14, 9))
    fig.canvas.manager.set_window_title('Diagnóstico Visual Avanzado - Unity Perú')
    fig.patch.set_facecolor('#f8f9fa')
    
    # Title
    fig.suptitle('Dashboard de Diagnóstico Estratégico: Unity Perú', fontsize=24, weight='bold', color='#1a252f', y=0.95)
    
    # Grid setup
    gs = fig.add_gridspec(2, 3, width_ratios=[1, 1.6, 0.7], height_ratios=[1, 1], wspace=0.2, hspace=0.5)
    
    # ================= ROW 1: MISSION =================
    # Donut Chart
    ax1 = fig.add_subplot(gs[0, 0])
    draw_donut(ax1, ['Presente (3)', 'Ausente (2)'], [60, 40], ['#27ae60', '#e74c3c'], 'Componentes de Misión', '60%')
    
    # Text Analysis
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis('off')
    ax2.text(0, 1, "MISIÓN - ANÁLISIS DE CALIDAD", fontsize=15, weight='bold', color='#2c3e50', va='top')
    mision_text = (
        "Declaración actual:\n«Proporcionar soluciones tecnológicas integrales y avanzadas que optimicen...»\n\n"
        "► Componentes:\n"
        "  [ ✔ ] Qué hacemos   [ ✔ ] Para quién   [ ✔ ] Para qué\n"
        "  [ ✖ ] Cómo nos distingue (Falsa distinción, carece de método único)\n"
        "  [ ✖ ] Con qué compromiso (Ausente, sin principios rectores declarados)\n\n"
        "► Pruebas de Calidad:\n"
        "  [ ✖ ] Prueba de sustitución (Podría aplicar a Sonda, IBM o Cisco)\n"
        "  [ ✖ ] Prueba de decisión (No acota suficientemente las oportunidades)\n"
        "  [ ✖ ] Prueba de reconocimiento (Imposible deducir la empresa)"
    )
    ax2.text(0, 0.85, mision_text, fontsize=12, va='top', ha='left', color='#34495e', linespacing=1.6)

    # Verdict
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.axis('off')
    rect1 = patches.FancyBboxPatch((0.0, 0.3), 1.0, 0.4, boxstyle="round,pad=0.1", facecolor="#e74c3c", edgecolor="#c0392b", linewidth=2)
    ax3.add_patch(rect1)
    ax3.text(0.5, 0.5, "VEREDICTO\nREFORMULAR", ha='center', va='center', fontsize=18, weight='bold', color='white')

    # ================= ROW 2: VISION =================
    # Donut Chart
    ax4 = fig.add_subplot(gs[1, 0])
    draw_donut(ax4, ['Cumple (3)', 'No Cumple (2)'], [60, 40], ['#2980b9', '#f39c12'], 'Atributos de Visión', '60%')
    
    # Text Analysis
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.axis('off')
    ax5.text(0, 1, "VISIÓN - ANÁLISIS DE ATRIBUTOS", fontsize=15, weight='bold', color='#2c3e50', va='top')
    vision_text = (
        "Declaración actual:\n«Consolidarse como una empresa líder en soluciones de infraestructura...»\n\n"
        "► Atributos Cumplidos:\n"
        "  [ ✔ ] Ambiciosa pero alcanzable (Expansión regional desde Perú)\n"
        "  [ ✔ ] Específica del negocio (Infraestructura tecnológica)\n"
        "  [ ✔ ] Movilizadora (Motiva a marcar estándares y ser sostenible)\n\n"
        "► Atributos Fallidos:\n"
        "  [ ✖ ] Temporalmente acotada (Carece de un año, plazo u horizonte límite)\n"
        "  [ ✖ ] Verificable (Términos como 'líder' son ambiguos sin métrica concreta)"
    )
    ax5.text(0, 0.85, vision_text, fontsize=12, va='top', ha='left', color='#34495e', linespacing=1.6)

    # Verdict
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.axis('off')
    rect2 = patches.FancyBboxPatch((0.0, 0.3), 1.0, 0.4, boxstyle="round,pad=0.1", facecolor="#f39c12", edgecolor="#d68910", linewidth=2)
    ax6.add_patch(rect2)
    ax6.text(0.5, 0.5, "VEREDICTO\nAJUSTAR", ha='center', va='center', fontsize=18, weight='bold', color='white')

    # Footer
    fig.text(0.5, 0.03, "Generado por Sistema de Análisis Estratégico (Python + Matplotlib) - Taller 04", ha='center', fontsize=11, color='#7f8c8d')

    # Save and show
    os.makedirs("docs/evidencias/S04", exist_ok=True)
    img_path = "docs/evidencias/S04/anexo_C_grafico_diagnostico.png"
    plt.savefig(img_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    
    try:
        os.startfile(os.path.abspath(img_path))
    except Exception as e:
        print("No se pudo abrir la imagen automáticamente:", e)


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
    
    try:
        show_visual_diagnostic()
    except Exception as e:
        print("No se pudo generar la salida visual:", e)

if __name__ == '__main__':
    main()
