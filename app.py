import os
import shodan
import sys

def main():
    # REQUISITO: Uso de variables de entorno
    api_key = os.environ.get('SHODAN_API_KEY')
    target_ip = '8.8.8.8' 

    if not api_key:
        print("ERROR: SHODAN_API_KEY no configurada.")
        sys.exit(1)

    api = shodan.Shodan(api_key)

    try:
        print(f"--- Consultando IP: {target_ip} ---")
        results = api.host(target_ip)
        # REQUISITO: Procesar >= 3 campos
        print(f"Organización: {results.get('org', 'N/A')}")
        print(f"País: {results.get('country_name', 'N/A')}")
        print(f"Puertos: {results.get('ports', 'N/A')}")

    # REQUISITO: Manejo de >= 4 tipos de errores
    except shodan.APIError as e:
        print(f"Error de API: {e}")
    except ConnectionError:
        print("Error: Fallo de red.")
    except TimeoutError:
        print("Error: Tiempo de espera agotado.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
