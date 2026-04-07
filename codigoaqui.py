# Gabriel Zambrano Herazo 2250944 - Mario Moreno Ramirez 2250941
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def peso(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)

    def orden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is not None:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecho, resultado)

    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, nodo):
        if nodo is None:
            return -1
        altura_izq = self._calcular_altura(nodo.izquierdo)
        altura_der = self._calcular_altura(nodo.derecho)
        return 1 + max(altura_izq, altura_der)

    def mostrar_en_orden(self):
        valores = self.orden()
        print("Árbol en orden:", valores)


def main():
    arbol = ArbolBinario()
    print("=== Creación del Árbol Binario ===")
    print("Ingrese valores numéricos (ingrese 'fin' para terminar):")
    
    while True:
        entrada = input("Valor: ")
        if entrada.lower() == 'fin':
            break
        try:
            valor = int(entrada)
            arbol.insertar(valor)
            print(f"  -> Insertado {valor}")
        except ValueError:
            print("  -> Entrada inválida. Ingrese un número o 'fin'")
    
    print("\n=== Información del Árbol ===")
    print(f"a) Peso del árbol (número de nodos): {arbol.peso()}")
    orden_valores = arbol.orden()
    print(f"b) Orden del árbol (recorrido inorden): {orden_valores}")
    print(f"c) Altura del árbol: {arbol.altura()}")
    arbol.mostrar_en_orden()


if __name__ == "__main__":
    main()
