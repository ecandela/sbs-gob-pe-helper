import os
from seleniumbase import Driver

def uc_driver_instalado() -> bool:
    """Verifica si uc_driver ya está instalado en SeleniumBase."""
    driver_dir = os.path.join(os.path.dirname(__import__("seleniumbase").__file__), "drivers")
    return any("uc_driver" in file for file in os.listdir(driver_dir))

# Si uc_driver no está instalado, ejecutar Driver(uc=True) para que SeleniumBase lo instale automáticamente
if not uc_driver_instalado():
    print("⚠️ uc_driver no encontrado. SeleniumBase lo instalará automáticamente...")
    try:
        driver = Driver(uc=True)  # Esto instalará uc_driver si falta
        print("✅ uc_driver ha sido instalado correctamente.")
        driver.quit()
    except Exception as e:
        print(f"❌ Error instalando uc_driver: {e}")
else:
    print("✅ uc_driver ya está instalado.")