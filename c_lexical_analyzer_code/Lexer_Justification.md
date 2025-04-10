# Elementos Léxicos de C

- César Guerra Martínez | A01656774
- José Luis Zago Guevara | A01736278
- Christian Flores Alberto | A01734997

## Keywords
Para este elemento, al simplemente tratarse de un listado de palabras finitas, se logró implementar la tokenización de este elemento por medio del siguiente regex:
~~~
r'[_a-zA-Z](\w)*'
~~~
Una vez se reconoce que el emento del código es una palabra, solo es cuestión de revisar si dicha palabra pertenece al listado de *keywords*

## Identifiers
Para este elemento, se identificó que los *identifiers* siguen un patrón en el que deben comenzar con guión bajo o cualquier letra del abecedario, excepto la ñ, minúscula o mayúscula; luego, pueden ser seguidas de un número no determinado de guiones bajos, letras, y/o digitos. Esto se logró por medio del siguiente regex:
~~~
r'[_a-zA-Z](\w)*'
~~~
A pesar de que este regex es útil, hay algunas puntos que valen la pena mencionar:
- Las *keywords* y los *identifiers* usan el mismo regex, siendo su único diferenciador si pertenecen o no a la lista de *keywords*
- En base al estándar revisado, dependiendo de la implementción de C, hay algunos caracteres que se implementan o no, con la intención de mantenerlo simple, se decidió no implementar en el regex estos casos especiales
- En base al estándar revisado, los identifiers también pueden contener *UCNs*, sin embargo, no los consideramos ya que entrarían en conflicto con la futura implementación de la tokenización de estas *UCNs*, haciendo que reconozca a todas las *UCNs* como *identifiers*

## Universal Character Names (UCNs)
Para este elemento, se identificó que los *UCNs* siguen un patrón en el que, si comienzan con *\u*, son seguidos de 4 dígitos, y/o letras de la *a* a la *f*, mínusculas o mayúsculas; y, si comienzan con *\U*, son seguidas de 8 elementos. Esto se logró por medio del siguiente regex:
~~~
r'\\(u[\dA-Fa-f]{4}|U[\dA-Fa-f]{8})'
~~~
A pesar de que este regex es útil, se debe mencionar que no reconoce todos los *UCNs*, pues dependiendo del compilador, la implementacón de C, etc. hay algunos que generan problemas con el lexer.

## Constants
### Integer Constants
Para este elemento, se identificó que las *integers* pueden formarse de decimales, octales o hexadecimales, los cuales pueden ser seguidos por los caracterés *l*, *ll*, y/o *u*, minúsculas o mayúsculas, de forma opcional. Esto se logró por medio del siguiente regex:
~~~
r'(0[xX][a-fA-F\d]+|[1-9]\d*|0[0-7]*)([uU](ll|LL|[lL])?|(ll|LL|[lL])[uU]?)?'
~~~
### Floating Constants
Para este elemento, se identificó que los *floats* pueden ser de tipo decimal o hexadecimal, los cuales pueden ser seguidos de un exponente con o sin signo (en el caso de los decimales), y un *floating-suffix* (en ambos casos), de forma opcional. Esto se logró por medio del siguiente regex:
~~~
r'((\d+\.\d*|\.\d+)([e|E][+-]?\d+)?|(\d*[e|E][+-]?\d+)|0[xX]([a-fA-F\d]+\.[a-fA-F\d]*|\.[a-fA-F\d]+)[pP][+-]?\d+|0[xX][a-fA-F\d]+[pP][+-]?\d+)[flFL]?'
~~~
### Enumeration Constants
En base al estándar revisado, las *enumeration constants* son lexicológicamente idénticas a los *identifiers*, siendo su único diferenciador que son declarados con el tipo *int*; debido a lo anterior, se optó por no implementar este elemento, pues la identificaión de elementos *int identifier* complicaría mucho el código
### Character Constants
    TODO

## String Literals
    TODO

## Punctuators
    TODO

## Header Names
    NO CONSIDERO HEADERS DE ""

## Preprocessing Numbers
    NO LO CONSIDERO

## Comments
    TODO
