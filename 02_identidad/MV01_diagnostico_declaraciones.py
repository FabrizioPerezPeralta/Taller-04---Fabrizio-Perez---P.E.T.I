import sys

def main():
    print("==========================================================")
    print("DIAGNÓSTICO DE DECLARACIONES ESTRATÉGICAS")
    print("==========================================================\n")
    print("EMPRESA: HashiCorp\n")
    print("MISION:")
    print("«Proporcionar un conjunto de herramientas consistente y fiable para que las empresas puedan desplegar, asegurar, conectar y ejecutar sus aplicaciones y software en cualquier entorno (multi-cloud e híbrido)»\n")
    
    print("--- COMPONENTES DE LA MISION ---")
    print("[X] Qué hacemos (Actividad esencial): «Proporcionar un conjunto de herramientas consistente y fiable»")
    print("[X] Para quién (Destinatario): «para que las empresas»")
    print("[X] Cómo nos distingue: «en cualquier entorno (multi-cloud e híbrido)»")
    print("[X] Para qué (Valor que genera): «puedan desplegar, asegurar, conectar y ejecutar sus aplicaciones y software»")
    print("[ ] Con qué compromiso (Principios): [Ausente]\n")
    
    print("--- DEFECTOS (Solo se listan los presentes) ---")
    print("- Ausencia de compromiso: No declara un principio rector o compromiso en la misión.\n")
    
    print("--- PRUEBAS DE CALIDAD ---")
    print("1. Prueba de sustitución con tres competidores (Red Hat, VMware, AWS): FALLA. Al reemplazar el nombre de la empresa, la declaración sigue aplicando perfectamente.")
    print("2. Prueba de la decisión: FALLA. No es suficientemente restrictiva o enfocada como para guiar todas las decisiones (sigue siendo algo amplia).")
    print("3. Prueba del reconocimiento: FALLA. Podría pertenecer a cualquier proveedor de herramientas DevOps.\n")
    
    print("VEREDICTO MISION: REFORMULAR. (Sobrevive a la sustitución y le falta un componente)\n")
    
    print("==========================================================\n")
    print("VISION:")
    print("La empresa NO PUBLICA una declaración de visión literal.\n")
    
    print("--- ATRIBUTOS DE LA VISION ---")
    print("- Temporalmente acotada: No cumple (ausente)")
    print("- Verificable: No cumple (ausente)")
    print("- Ambiciosa pero alcanzable: No cumple (ausente)")
    print("- Específica del negocio: No cumple (ausente)")
    print("- Movilizadora: No cumple (ausente)\n")
    
    print("VEREDICTO VISION: AUSENTE. (Continuar con la derivación usando la misión)")
    print("==========================================================")

if __name__ == '__main__':
    main()
