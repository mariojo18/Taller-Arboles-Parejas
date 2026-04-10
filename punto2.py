
from bigtree import print_tree, list_to_tree

caminos = [
    "Cuerpo/Cabeza/Ojos",
    "Cuerpo/Cabeza/Nariz",
    "Cuerpo/Cabeza/Boca",
    "Cuerpo/Tronco/Pecho",
    "Cuerpo/Tronco/Espalda",
]

root = list_to_tree(caminos)
print_tree(root)
