# gregorian_calendar

## Sobre los Calendarios

Los calendarios son de suma importancia, para la humanidad en muchos sentidos.
Además de permitirnos poder llevar registro de los acontecimientos, también ayuda
a predecir otros eventos tales como las estaciones.

## El Calendario Juliano

Julio César, motivado por su descontento hacia el desorden y aleatoriedad del
calendario romano, desarrolló uno que contenía 364.25 días, por lo que se definió la
duración estándar de un año en 365 días, sumando un día más (el anterior a cada
25 de febrero) al año, cada 4 años. Aún cuando este calendario era mucho más
preciso que su antecesor, la pequeña diferencia de 11 minutos con 14 segundos,
hacía que cada 128 años se acumulara 1 día completo. [1]
Las diferencias antes mencionadas, hacían acarrear pequeños errores acumulados,
que con el paso de los años, serían más notorios.

## El Calendario Gregoriano

En 1572 el vigente Papa Gregorio XIII mostró disconformidad con el calendario de
aquella época, ya que una de las fechas más importantes para la Iglesia Católica no
estaba correspondiendo con las estaciones del año. La pascua, fecha basada en el
día del equinoccio vernal (o sea, el primer día de la primavera del hemisferio norte)
se estaba celebrando en los primeros días del mes de marzo.[1] Esto era una clara
evidencia de la imprecisión del calendario juliano.
Con ayuda de astrónomos, el papa desarrolló un calendario mejorado. La solución
fue que el nuevo calendario, el “Gregoriano” seguiría teniendo 365 días con un día
adicional cada 4 años (que fue movido luego después del 28 de febrero). Aún así,
no habría años bisiestos en los años terminados en 00, a menos que estos años
fueran divisibles por 400. Por tanto, 1700, 1800, 1900, 2100 no serían años
bisiestos, pero 1600, 2000, 2400 sí serían años bisiestos.[1]
Esto llevó, a que por indicaciones del papa, el día 4 de octubre de 1582, iba a ser
seguido por el 15 de octubre de 1582, para compensar la diferencia entre el
calendario juliano y el calendario gregoriano, la cual era de 10 días para ese
entonces.[1]

## Algunos Datos Curiosos

Dos personajes muy famosos de la historia, Miguel de Cervantes y William
Shakespeare, vivieron durante el cambio del calendario juliano al gregoriano.
Considerando que el cambio de calendario se hizo efectivo en 1582, tanto Miguel deCervantes que se asume nació en el año 1547 [5], y Shakespeare nacido en 1564
[4], vivieron varios años durante la vigencia del calendario juliano. La muerte de
estos personajes, fue un 22 de abril de 1616 [5], y 23 de abril de 1616 [6]. Es decir,
Cervantes murió el día antes de la muerte de Shakespeare.

## Sobre las funciones implementadas

R0:
● Una entrada válida se define como una tupla de la forma
( x, y , z ) donde x, y , z ∈ {1, 2 , 3 , . ..}
● Dada una entrada que cumpla con la condición anterior, la salida debe ser
True.
● Dada una entrada que NO cumpla la condición anterior, la salida debe ser
False.
R1:
● Indicará para una entrada dada, la cual representa un año, si este coincide
con un año bisiesto según el calendario gregoriano.
● El valor de los años de entrada deberá ser mayor o igual a 1582, dado que
este es el año en que se pone en vigencia el calendario gregoriano. En caso
contrario, el valor de retorno será False.
● Para las entradas que coincidan con valores mayores a 1582, deberá
evaluarse si este es bisiesto, dadas las siguientes condiciones.
○ Si es divisible entre 4:
■ Si es divisible entre 100
● Si es divisible entre 100, y además es divisible entre 400
debe retornar True.
● Si es divisible entre 100, pero no es divisible entre 400
debe retornar False
■ Si no es divisible entre 100 debe retornar True
○ Si no es divisible entre 4 deberá retornar False.
○ En cualquier caso no contemplado, debe retornar False.
R2:
● Dada una entrada válida (condicionada por R0), determinar si esta coincide
con una fecha válida según el calendario gregoriano.● Debe considerar que la fecha mínima aceptable es el 15 de octubre de 1582,
que sería equivalente a la tupla (1582,10,15). Cualquier valor inferior a este
deberá retornar False.
● Debe considerar los casos en que la fecha pertenece a un mes de 28, 30, 31
ó 29 (bisiesto) días. En cualquier combinación de año, mes, día que se
incumplan las restricciones de los requerimientos R0 o R1, el valor de retorno
deberá ser False.
● Cualquier fecha que exista dentro del calendario gregoriano, deberá retornar
True.
R3:
● El valor de entrada, debe ser una entrada válida, aceptada en los
requerimientos R0, R2 y R1 en caso de requerirse.
● En caso de que la fecha de entrada exista en el calendario gregoriano, debe
indicarse la fecha siguiente a dicho día, retornando una tupla que de igual
forma cumpla con las restricciones de fecha válida para el calendario
gregoriano.
R4:
● El valor de entrada debe validarse, para que satisfaga las condiciones
indicadas en el calendario gregoriano. Cualquier valor no válido en la entrada,
retornará un -1.
● El valor de retorno, deberá ser la cantidad de días que han transcurrido en el
año indicado, a partir del primero de enero. Es importante considerar que
entre el primero de enero, y el primero de enero de un mismo año, han
transcurrido 0 días.
● Se deberá considerar el año para determinar si este se trata de un año
bisiesto o no.
R5:
● Deberá validarse que el valor de entrada sea una fecha válida según lo
indicado en el requerimiento R3. En caso de que esto no sea así, el valor de
retorno deberá ser -1.
● Este requerimiento deberá indicar el día de la semana, al que corresponde
una fecha dada.
● Se utiliza la siguiente nomenclatura para identificar los días de la semana:
○ Domingo : 0
○ Lunes : 1
○ Martes : 2
○ Miércoles : 3
○ Jueves : 4
○ Viernes : 5
○ Sábado : 6
○ Error : -1

## Sobre el Diseño de las Funciones

Para el desarrollo de las funciones, dado que son relativamente sencillas, no se
requirió un diseño complejo de las mismas.
Aún así, se consideraron algunos aspectos importantes a cumplir en cada uno de
los segmentos de código, descritas a continuación:
● Documentación básica para cada función: Este aspecto considera para cada
función, incluir en un encabezado de documentación el autor de esta con su
respectivo contacto, descripción de la función, significado de los parámetros
de entrada, definición del valor de salida, y detalle de las restricciones en
caso de ser requeridas.
● Estandarización de valores de retorno: Se consideró para este caso, lo
siguiente.
○ En caso de que la salida esperada fuera entera, se retorna el valor
calculado en la función en caso de que este sea válido, y se utiliza el
valor -1 como retorno cuando se encuentra una entrada incorrecta o
un error.
○ En caso de que la salida requerida sea booleana, se retorna True para
los casos en que se cumple la serie de condiciones, y False para
aquellos casos en que no se cumple, o se genera error.

## Evidencias de Pruebas Realizadas

Dada la gran cantidad de posibles valores que podrían recibir las funciones como
entrada, se decidió realizar funciones con casos de prueba para cada una de ellas.
Para cada una, se definió una serie de casos extremos, casos promedio, propensos
a generar error (Strings, tuplas de strings, valores negativos, valores flotantes, etc),
además de un arreglo con los resultados esperados (oráculo).
De esta forma se logró realizar una serie de pruebas exhaustivas, con entradas
controladas y salidas esperadas para cada uno de los casos de prueba, para cada
una de las funciones.
Las funciones que se utilizaron para este fin, se encuentran en las últimas líneas del
código fuente, claramente señaladas con un prefijo “test_” al inicio del nombre de
cada función.
Para garantizar un funcionamiento aceptable, en los conjuntos de pruebas por
realizar, se consideraron valores de entrada que incluyen:
● Valores String.
● Tuplas de string.
● Tuplas con valores negativos.
● Tuplas con valores de punto flotante.

## Análisis de Resultados

De una ejecución a cada una de las funciones destinadas para testing, se
obtuvieron los siguientes resultados.

```
Testing fecha_es_tupla function
From 24 tests, 24 are correct, and 0 are incorrect.

Testing bisiesto function
From 27 tests, 27 are correct and 0 are incorrect.

Testing fecha_es_valida function
From 35 tests, 35 are correct, and 0 are incorrect

Testing dia_siguiente function
From 28 tests, 28 are correct, and 0 are incorrect

Testing dias_desde_primero_enero function
From 32 tests, 32 are correct, and 0 are incorrect

Testing dia_semana function
From 13 tests, 13 are correct, and 0 are incorrect

```

Tal y como se mencionó en la sección anterior, se utilizó un “oráculo” con los
valores de entrada y el valor esperado, previamente validado.
Cada uno de los resultados obtenidos en la ejecución de cada función, fue
comparado con los valores indicados en el oráculo, con el fin de determinar si la
salida de la función evaluada era correcta o no.
Del conjunto de casos evaluados, puede notarse en la figura anterior, que no se
reportaron resultados incorrectos para las ejecuciones.
Con este análisis, se puede concluir que el funcionamiento de las funciones
solicitadas, es aceptable en términos funcionales.

## Referencias

[1] Dominguez, M. (s.f). ​ La historia del calendario Gregoriano . ​ [online] VIX.
Available
at:
https://www.vix.com/es/btg/curiosidades/3523/la-historia-del-calendario-grego
riano [Accessed 15 Sep. 2019].
[2] Humanoriginproject.com. (s.f). ​ The Gregorian Calendar & the Unbelievable
Leap-Year
Paradox ​ .
[online]
Available
at:
https://humanoriginproject.com/gregorian-calendar-leap-year/ [Accessed 15
Sep. 2019].
[3]
En.wikipedia.org.
(2019)​ .
Computus . ​
[online]
Available
https://en.wikipedia.org/wiki/Computus [Accessed 15 Sep. 2019].
at:
[4] Arogundade, B. (2019). ​ BEST FACTS: Where & When Was William
Shakespeare Born? Timeline & Life . ​ [online] Arogundade.com. Available at:
http://www.arogundade.com/where-and-when-was-was-william-shakespeare-
born-timeline-and-life-facts-about-william-shakespeare.html [Accessed 15
Sep. 2019].
[5] En.wikipedia.org. (2019). ​ Miguel de Cervantes . ​ [online] Available at:
https://en.wikipedia.org/wiki/Miguel_de_Cervantes [Accessed 15 Sep. 2019].
[6]
En.wikipedia.org. (2019). ​ William Shakespeare . ​ [online] Available at:
https://en.wikipedia.org/wiki/William_Shakespeare [Accessed 15 Sep. 2019].
