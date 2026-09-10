import sys

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
    print("1. Prueba de sustitución con tres competidores (Cisco, IBM, Sonda): FALLA. Al reemplazar el nombre, la declaración sigue aplicando a cualquiera de estos competidores de TI.")
    print("2. Prueba de la decisión: FALLA. Es demasiado amplia y no permite descartar líneas de negocio tecnológicas.")
    print("3. Prueba del reconocimiento: FALLA. Al leerla, no se identifica unívocamente a Unity Perú.\n")
    
    print("VEREDICTO MISION: REFORMULAR. (Sobrevive a la sustitución y faltan componentes clave)\n")
    
    print("==========================================================\n")
    print("VISION:")
    print("«Consolidarse como una empresa líder en soluciones de infraestructura tecnológica en la región, marcando nuevos estándares de calidad e innovación, y siendo un pilar en el avance del desarrollo tecnológico sostenible en el Perú»\n")
    
    print("--- ATRIBUTOS DE LA VISION ---")
    print("- Temporalmente acotada: No cumple (No indica un año o plazo límite)")
    print("- Verificable: No cumple (El término 'líder' sin métrica no es verificable directamente)")
    print("- Ambiciosa pero alcanzable: Cumple (Expande su alcance a nivel regional siendo pilar en Perú)")
    print("- Específica del negocio: Cumple (Soluciones de infraestructura tecnológica)")
    print("- Movilizadora: Cumple (Inspira a marcar nuevos estándares e impulsar la sostenibilidad)\n")
    
    print("VEREDICTO VISION: AJUSTAR. (Carece de plazo y métrica objetiva verificable)")
    print("==========================================================")

if __name__ == '__main__':
    main()
