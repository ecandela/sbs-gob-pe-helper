from seleniumbase import SB

from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", headless=False) as sb:
    # URL de la página
    url = "https://www.sbs.gob.pe/app/pu/ccid/paginas/vp_rentafija.aspx"
    
    # Abrir la URL con desconexión controlada
    sb.uc_open_with_disconnect(url, 2.2)
    
    # Simular presionar la tecla Tab y luego Espacio    
    sb.uc_gui_press_key("\t")
    sb.uc_gui_press_key(" ")
    
    # Reconectar después de una pausa
    sb.reconnect(2.2)
    
    # Obtener el código HTML de la página
    html_content = sb.get_page_source()
    
    # Imprimir el código HTML
    print(html_content)
