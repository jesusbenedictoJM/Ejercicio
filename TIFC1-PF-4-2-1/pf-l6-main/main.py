import requests

def trivia_fetch(num):
    try:
        response = requests.get(f"http://numbersapi.com/{num}?json")
        if response.status_code == 200:
            data = response.json()
            return {
                "number": data.get("number", num),
                "fact": data.get("text", "No se encontró trivia.")
            }
        else:
            return {
                "number": num,
                "fact": "No se pudo obtener la trivia desde la API."
            }
    except Exception as e:
        return {
            "number": num,
            "fact": f"Ocurrió un error al conectarse a la API: {e}"
        }

def main():
    print(" Bienvenido al juego de Trivias Numérica ")
    print(" Ingresa un número y descubre un dato curioso sobre él.")
    
    try:
        numero = int(input(" Ingresa un número: "))
        trivia = trivia_fetch(numero)
        print(f"\n Dato sobre el número {trivia['number']}:\n {trivia['fact']}")
    except ValueError:
        print(" Entrada inválida. Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()
