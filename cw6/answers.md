# Algorytm i parametry

Zaimplementowałem algorytm w wersji epsilon-zachłannej, jednak prawdopodobieństwo wyboru akcji jest zmieniane z każdym epizodem.
Na początku wybierane są z większym prawdopodobieństwem losowe akcje, jednak sytuacja zmienia się wraz z kolejnymi epizodami.
Ta wersja daje dużo lepsze wyniki w porównaniu ze stałym epsilonem.

Po przeprowadzonych testach najlepszymi parametrami okazały się:

- maksymalna liczba kroków w epizodzie: 400

- learning_rate (beta): 0.8

- gamma (dyskonto): 0.9

- epsilon: od 1 do 0.001 zmniejszany wykładniczo

- decay_rate: 0.00005

# Testowanie i wyniki

Testuję algorytm w zależności od ilości epizodów podczas uczenia się oraz funkcji nagrody.
Po nauczeniu się algorytmu badam średni procent dojścia do celu w 1000 epizodów i 200 kroków na epizod w 10 próbach.
Dodatkowo zamieszczam porównanie skuteczności algorytmu dla zmiennego i stałego epsilona.

## Algorytm ze stałym epsilonem i domyślną funkcją nagrody

| epizody | średni procent dojść do celu w 10 próbach |
| ------- | ----------------------------------------- |
| 1000    | 0.620000%                                 |
| 5000    | 0.700000%                                 |
| 10000   | 0.800000%                                 |
| 50000   | 06.540000%                                |
| 100000  | 03.420000%                                |
| 250000  | 03.280000%                                |

## Algorytm ze zmiennym epsilonem

### Domyślna funkcja nagrody

| epizody | średni procent dojść do celu w 10 próbach |
| ------- | ----------------------------------------- |
| 1000    | 1.620000%                                 |
| 5000    | 3.700000%                                 |
| 10000   | 6.800000%                                 |
| 50000   | 26.540000%                                |
| 100000  | 43.420000%                                |
| 250000  | 63.280000%                                |


### Funkcja nagrody 1

| epizody | średni procent dojść do celu w 10 próbach |
| ------- | ----------------------------------------- |
| 1000    | 0.620000%                                 |
| 5000    | 0.700000%                                 |
| 10000   | 0.800000%                                 |
| 50000   | 06.540000%                                |
| 100000  | 03.420000%                                |
| 250000  | 03.280000%                                |

### Funkcja nagrody 2

| epizody | średni procent dojść do celu w 10 próbach |
| ------- | ----------------------------------------- |
| 1000    | 0.620000%                                 |
| 5000    | 0.700000%                                 |
| 10000   | 0.800000%                                 |
| 50000   | 06.540000%                                |
| 100000  | 03.420000%                                |
| 250000  | 03.280000%                                |

# Wnioski