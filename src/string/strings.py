class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """Verifica si una cadena es un palíndromo."""
        texto = ''.join(texto.lower().split())  # Convertir a minúsculas y eliminar espacios
        return texto == texto[::-1]

    def invertir_cadena(self, texto):
        """Invierte una cadena de texto sin usar slicing ni reversed()."""
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida

    def contar_vocales(self, texto):
        """Cuenta el número de vocales en una cadena."""
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char in vocales)

    def contar_consonantes(self, texto):
        """Cuenta el número de consonantes en una cadena."""
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for char in texto if char in consonantes)

    def es_anagrama(self, texto1, texto2):
        """Verifica si dos cadenas son anagramas."""
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())

    def contar_palabras(self, texto):
        """Cuenta el número de palabras en una cadena."""
        return len(texto.split())

    def palabras_mayus(self, texto):
        """Pone en mayúscula la primera letra de cada palabra en una cadena."""
        return texto.title()

    def eliminar_espacios_duplicados(self, texto):
        """Elimina espacios duplicados en una cadena."""
        return ' '.join(texto.split())

    def es_numero_entero(self, texto):
        """Verifica si una cadena representa un número entero sin usar isdigit()."""
        if not texto:
            return False
        if texto[0] in ('-', '+'):
            texto = texto[1:]
        return texto.isnumeric()

    def cifrar_cesar(self, texto, desplazamiento):
        """Aplica el cifrado César a una cadena de texto."""
        resultado = ""
        for char in texto:
            if char.isalpha():
                inicio = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - inicio + desplazamiento) % 26 + inicio)
            else:
                resultado += char
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        """Descifra una cadena cifrada con el método César."""
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        """Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index()."""
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
