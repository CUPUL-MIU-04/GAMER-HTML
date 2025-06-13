import os

# Configuración del código AdSense (personaliza con tus datos)
adsense_script_head = '''
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3869365676003245" crossorigin="anonymous"></script>
'''

adsense_ad_unit = '''
<!-- Bloque de anuncio AdSense -->
<div style="margin: 20px auto; text-align: center;">
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-3869365676003245"
         data-ad-slot="1234567890"
         data-ad-format="auto"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
'''

# Busca todos los archivos HTML en el repositorio
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            print(f"Procesando: {file_path}")
            
            # Leer el contenido del archivo
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Insertar script en el <head>
            if adsense_script_head not in content:
                content = content.replace('<head>', f'<head>\n{adsense_script_head}')
            
            # Insertar bloque de anuncio después del <body> o antes del </body>
            if adsense_ad_unit not in content:
                if '<body>' in content:
                    content = content.replace('<body>', f'<body>\n{adsense_ad_unit}')
                elif '</body>' in content:
                    content = content.replace('</body>', f'{adsense_ad_unit}\n</body>')
            
            # Guardar cambios
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

print("¡Proceso completado! Revisa los archivos modificados.")