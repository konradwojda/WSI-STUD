# Algorytm i parametry

Zaimplementowałem algorytm w wersji epsilon-zachłannej, jednak prawdopodobieństwo wyboru akcji jest zmieniane z każdym epizodem.
Na początku wybierane są z większym prawdopodobieństwem losowe akcje, jednak sytuacja zmienia się wraz z kolejnymi epizodami.
Taka wersja daje lepsze wyniki w porównaniu ze stałym epsilonem.

Po przeprowadzonych testach najlepszymi parametrami okazały się:

- maksymalna liczba kroków w epizodzie: 400

- learning_rate (beta): 0.1

- gamma (dyskonto): 0.9

- epsilon: od 1 do 0.001 zmniejszany wykładniczo

- decay_rate: 0.00005

# Testowanie i wyniki

Testuję algorytm w zależności od ilości epizodów podczas uczenia się oraz funkcji nagrody.
Po nauczeniu się algorytmu badam średni procent dojścia do celu w 1000 epizodów i 200 kroków na epizod w 10 próbach.

## Algorytm ze stałym epsilonem = 0.85

### Domyślna funkcja nagrody

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 0.220000%                                 |
| 5000    | 24.760000%                                |
| 10000   | 31.960000%                                |
| 50000   | 42.520000%                                |


### Funkcja nagrody 1 - jeśli wpadniemy w dziurę -1 punkt, 1 punkt za dojście do celu

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 18.72000%                                 |
| 5000    | 70.340000%                                |
| 10000   | 72.020000%                                |
| 50000   | 77.360000%                                |

### Funkcja nagrody 2 - przy wpadnięciu do dziury -10 punktów, 10 punktów za dojście do celu, -1 punkt za stanięcie na bezpieczną część (ale nie cel)

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 8.960000%                                 |
| 5000    | 15.340000%                                |
| 10000   | 25.450000%                                |
| 50000   | 47.230000%                                |

## Algorytm ze zmiennym epsilonem

### Domyślna funkcja nagrody

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 3.440000%                                 |
| 5000    | 35.560000%                                |
| 10000   | 38.840000%                                |
| 50000   | 47.240000%                                |


### Funkcja nagrody 1 - jeśli wpadniemy w dziurę -1 punkt, 1 punkt za dojście do celu

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 25.30000%                                 |
| 5000    | 72.640000%                                |
| 10000   | 76.560000%                                |
| 50000   | 82.820000%                                |

### Funkcja nagrody 2 - przy wpadnięciu do dziury -10 punktów, 10 punktów za dojście do celu, -1 punkt za stanięcie na bezpieczną część (ale nie cel)

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 9.960000%                                 |
| 5000    | 16.680000%                                |
| 10000   | 27.700000%                                |
| 50000   | 57.520000%                                |

# Wnioski

Najlepsza funkcja nagrody okazała się odejmująca 1pkt za wpadnięcie w dziurę i dająca 1pkt za dojście do celu.
Metoda ze zmniejszaniem epsilon okazała się być lepsza, niż ta ze stałym.
