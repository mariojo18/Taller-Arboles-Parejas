# Gabriel Zambrano Herazo 220944 - Mario Moreno Ramirez 2250941
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, padre):
        nuevo_nodo = Nodo(valor)
        
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        
        nodo_padre = self.buscar(self.raiz, padre)
        if nodo_padre:
            nodo_padre.hijos.append(nuevo_nodo)

    def buscar(self, nodo_actual, valor_buscado):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == valor_buscado:
            return nodo_actual
        for cada_hijo in nodo_actual.hijos:
            resultado = self.buscar(cada_hijo, valor_buscado)
            if resultado:
                return resultado
        return None

    def peso(self):
        return self.contar(self.raiz)

    def contar(self, nodo_actual):
        if nodo_actual is None:
            return 0
        total_nodos = 1
        for cada_hijo in nodo_actual.hijos:
            total_nodos = total_nodos + self.contar(cada_hijo)
        return total_nodos

    def orden(self):
        return self.max_hijos(self.raiz)

    def max_hijos(self, nodo_actual):
        if nodo_actual is None:
            return 0
        mayor_cantidad = len(nodo_actual.hijos)
        for cada_hijo in nodo_actual.hijos:
            cantidad_hijo = self.max_hijos(cada_hijo)
            if cantidad_hijo > mayor_cantidad:
                mayor_cantidad = cantidad_hijo
        return mayor_cantidad

    def altura(self):
        return self.calc_altura(self.raiz)

    def calc_altura(self, nodo_actual):
        if nodo_actual is None:
            return -1
        if len(nodo_actual.hijos) == 0:
            return 0
        mayor_altura = 0
        for cada_hijo in nodo_actual.hijos:
            altura_hijo = self.calc_altura(cada_hijo)
            if altura_hijo > mayor_altura:
                mayor_altura = altura_hijo
        return 1 + mayor_altura

# PROGRAMA
mi_arbol = Arbol()

print("Crear raiz:")
while True:
    valor_ingresado = input("Valor: ")
    es_numero = True
    for caracter in valor_ingresado:
        if caracter not in "0123456789-":
            es_numero = False
            break
    if es_numero:
        mi_arbol.insertar(int(valor_ingresado), None)
        break
    print("Error: numero")

print("\nAgregar nodos (formato: valor,padre)")
print("Ejemplo: 5,2   Escriba 'fin' para terminar")

while True:
    entrada_usuario = input("> ")
    if entrada_usuario == "fin":
        break
    
    partes = entrada_usuario.split(",")
    if len(partes) != 2:
        print("Error: use valor,padre")
        continue
    
    texto_valor = partes[0]
    texto_padre = partes[1]
    
    valor_es_numero = True
    for caracter in texto_valor:
        if caracter not in "0123456789-":
            valor_es_numero = False
    padre_es_numero = True
    for caracter in texto_padre:
        if caracter not in "0123456789-":
            padre_es_numero = False
    
    if valor_es_numero and padre_es_numero:
        mi_arbol.insertar(int(texto_valor), int(texto_padre))
    else:
        print("Error: numeros")

print("\nResultados:")
print("a) Peso:", mi_arbol.peso())
print("b) Orden:", mi_arbol.orden())
print("c) Altura:", mi_arbol.altura())
