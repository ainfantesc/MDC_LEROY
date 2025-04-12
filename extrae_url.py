import xml.etree.ElementTree as ET
import pandas as pd

# Ruta del archivo XML
archivo_xml = r'xml_page.xml'

# Parsear el XML
tree = ET.parse(archivo_xml)
root = tree.getroot()

# Namespace (muy importante)
ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Lista para guardar las URLs filtradas
urls = []

# Iterar sobre cada url
for url in root.findall('ns:url', ns):
    loc = url.find('ns:loc', ns)
    if loc is not None and loc.text.startswith('https://www.leroymerlin.es/productos/iluminacion'):
        urls.append(loc.text)

# Convertir a DataFrame
df = pd.DataFrame(urls, columns=['URL'])

# Guardar a CSV o imprimir
df.to_csv('urls_iluminacion.csv', index=False, encoding='utf-8')
print(df)
