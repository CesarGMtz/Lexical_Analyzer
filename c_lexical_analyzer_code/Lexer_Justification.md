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
- En base al estándar revisado, los *identifiers* también pueden contener *UCNs*, sin embargo, no los consideramos ya que entrarían en conflicto con la futura implementación de la tokenización de estas *UCNs*, haciendo que reconozca a todas las *UCNs* como *identifiers*

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
Para este elemento se identificó que los *characters* se forman de cualquier combinación de caracteres que se encuentre entre dos comillas sencillas, incluyendo secuencias de escape y *UCNs*. Esto se logró por medio del siguiente regex:
~~~
r"L?'(\\([abfnrtv\\'\"?]|x[\dA-Fa-f]+|[0-7]{1,3}|u[\dA-Fa-f]{4}|U[\dA-Fa-f]{8})|[^\\'\n])*'"
~~~

## String Literals
Para este elemento se identificó que los *strings* se forman de cualquier combinación de caracteres que se encuentre entre dos comillas dobles, incluyendo secuencias de escape y **UCNs. Esto se logró por medio del siguiente regex:
~~~
r'L?"(\\([abfnrtv\\\'\"?]|x[\dA-Fa-f]+|[0-7]{1,3}|u[\dA-Fa-f]{4}|U[\dA-Fa-f]{8})|[^\\\"\n])*"'
~~~

## Punctuators
Para este elemento, al simplemente tratarse de un listado de puntuadores finitos, se logró implementar la tokenización de este elemento por medio del siguiente regex:
~~~
r'\[|\]|\(|\)|\{|\}|\.\.\.|\.|->|\+\+|\-\-|&&|&=|&|\*=|\*|\+=|\+|\-=|\-|~|!=|!|/=|/|%=|<%|%>|%:%:|%:|%|<<=|>>=|<<|>>|<=|>=|<:|:>|<|>|==|=|\^=|\^|\|\||\|=|\||\?|:|;|,|\#\#|\#'

~~~
Este regex solo se trata de una alternancia de todos los puntuadores disponibles en C, por lo que, si un elemento del código coincide exactamente, se le denominará como *punctuator*

## Header Names
Para este elemento, se identificó que los *headers* se forman de cualquier combinación de caracteres, excepto *\n*, que se encuentre entre los caracteres *<>*. Esto se logró por medio del siguiente regex:
~~~
r'<[^\\n>]+>'
~~~
A pesar de que este regex es útil, hay algunas puntos que valen la pena mencionar:
- A pesar de que, lexicológicamente hablando, el regex reconoce los *headers*, para hacerlo correctamente se debería de reconocer la sentencia *#include* en conjunto; sin embargo, esto no se considero ya que la identificación de elementos *#include header* complicaría mucho el código
- En base al estándar revisado, los *headers* también pueden definirse entre dos comillas dobles, sin embargo, no lo consideramos ya que entraría en conflicto con la implementación de *strings* que ya tenemos, haciendo que reconozca a todos los *headers* como *strings*

## Preprocessing Numbers (PPNs)
En base al estándar revisado, los *PPNs* tienen la misma léxica que los *integers* y los *floats*, por lo que se decidió no implementarlo pues entraría en conflicto con estas mismas, identificando incorrectamente los diferentes tokens

## Comments
Para este elemento, se identificó que los *comments* se forman de una doble barra invertida, seguida de cualquier combinación de caracteres, o de cualquier combinación de caracteres, incluyendo *\n* para la multilinea, que se encuentre entre los caracteres */\* \*/*. Esto se logró por medio del siguiente regex:
~~~
r'(//.*)|(/\*(.|\n)*?\*/)'
~~~
