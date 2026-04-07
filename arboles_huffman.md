# Árboles de Huffman

## ¿Qué son los Árboles de Huffman?

Los **Árboles de Huffman** son estructuras de datos arbóreas utilizadas en ciencias de la computación para implementar la **codificación de Huffman**, un algoritmo de compresión de datos sin pérdida muy eficiente.

## Características Principales

- **Estructura de árbol binario**: Cada nodo tiene como máximo dos hijos
- **Árbol con peso**: Cada nodo hoja contiene un símbolo y su frecuencia de aparición
- **Árbol óptimo**: Minimiza la longitud promedio del código resultante
- **Construcción de abajo hacia arriba**: Se construye comenzando por los símbolos menos frecuentes

## ¿Cómo funciona?

### Algoritmo de Construcción

1. **Crear nodos hoja**: Se crea un nodo para cada símbolo con su frecuencia
2. **Construir el árbol**: Se combinan repetidamente los dos nodos con menor frecuencia
3. **Asignar códigos**: Se recorre el árbol asignando 0 para la rama izquierda y 1 para la derecha
4. **Generar tabla de códigos**: Cada símbolo obtiene un código único de longitud variable

### Ejemplo Simple

Supongamos que tenemos el texto: "AAABBC"

**Frecuencias:**
- A: 3 veces
- B: 2 veces
- C: 1 vez

**Árbol resultante:**
```
        (6)
       /   \
     (3)   (3)
     / \   / \
    A   (2)  (2)
       / \   / \
      B   C
```

**Códigos generados:**
- A: `0` (1 bit)
- B: `10` (2 bits)
- C: `11` (2 bits)

## Ventajas

**Compresión eficiente**: Reduce significativamente el tamaño de archivos  
**Óptimo**: Genera códigos de longitud mínima  
**Rápido**: O(n log n) en tiempo de construcción  
 **Sin pérdida**: Permite recuperar los datos originales perfectamente  

## Desventajas

 Requiere conocer las frecuencias previas de los símbolos  
 Debe transmitir el árbol junto con los datos comprimidos  
 No es óptimo para todos los tipos de datos  

## Aplicaciones Prácticas

- **Compresión de archivos**: ZIP, GZIP, DEFLATE
- **Transmisión de datos**: Comunicaciones comprimidas
- **Códigos de barras y QR**: Almacenamiento eficiente
- **Redes y telecomunicaciones**: Reducción de ancho de banda
- **Formatos multimedia**: JPEG, MP3, y otros estándares

## Comparación con Otros Métodos

| Método | Ventaja | Desventaja |
|--------|---------|-----------|
| **Huffman** | Muy eficiente y rápido | Requiere tabla de frecuencias |
| **LZ77/LZ78** | Adaptativo | Menos óptimo que Huffman |
| **Aritmética** | Mejor compresión | Más complejo computacionalmente |

## Complejidad Computacional

- **Tiempo de construcción**: O(n log n)
- **Tiempo de codificación**: O(m) donde m es el número de símbolos
- **Espacio requerido**: O(n) para el árbol y tabla de códigos

## Ejemplo en Pseudocódigo

```
función construirArbolHuffman(frecuencias):
    crear cola de prioridad con nodos hoja
    
    mientras cola tenga más de un nodo:
        nodo1 = extraer nodo con menor frecuencia
        nodo2 = extraer nodo con menor frecuencia
        
        padre = nuevo nodo
        padre.frecuencia = nodo1.frecuencia + nodo2.frecuencia
        padre.izquierda = nodo1
        padre.derecha = nodo2
        
        insertar padre en cola
    
    retornar último nodo (raíz del árbol)
```

## Conclusión

Los Árboles de Huffman son una herramienta fundamental en la compresión de datos, ofreciendo un equilibrio excelente entre simplicidad y eficiencia. Su algoritmo greedy garantiza una solución óptima para la codificación de longitud variable, lo que los hace indispensables en muchas aplicaciones modernas de procesamiento de información.
