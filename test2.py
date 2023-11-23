import re
import json

# Ejemplo de JSON
json_data = '''
[
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "555-1234"
    },
    {
        "name": "John Doe",
        "email": "line.doe@example.com",
        "phone": "555-1234"
    },
    {
        "name": "John Doe",
        "email": "donna.doe@example.com",
        "phone": "555-1234"
    }
]
'''

# Utilizar expresión regular para encontrar correos electrónicos después de "email":
pattern = re.compile(r'"email":\s*"(.*?)"')

# Buscar coincidencias en el JSON
matches = pattern.findall(json_data)

# Imprimir los correos electrónicos encontrados
for match in matches:
    print(match)