# Algorytm i parametry

Zaimplementowałem algorytm w wersji epsilon-zachłannej, jednak prawdopodobieństwo wyboru akcji jest zmieniane z każdym epizodem.
Na początku wybierane są z większym prawdopodobieństwem losowe akcje, jednak sytuacja zmienia się wraz z kolejnymi epizodami.
Taka wersja daje dużo lepsze wyniki w porównaniu ze stałym epsilonem. Wyniki w wersji ze stałym epsilonem nie przekraczały 1%.

Po przeprowadzonych testach najlepszymi parametrami okazały się:

- maksymalna liczba kroków w epizodzie: 400

- learning_rate (beta): 0.8

- gamma (dyskonto): 0.9

- epsilon: od 1 do 0.001 zmniejszany wykładniczo

- decay_rate: 0.00005

# Testowanie i wyniki

Testuję algorytm w zależności od ilości epizodów podczas uczenia się oraz funkcji nagrody.
Po nauczeniu się algorytmu badam średni procent dojścia do celu w 1000 epizodów i 200 kroków na epizod w 10 próbach.

## Algorytm ze zmiennym epsilonem

### Domyślna funkcja nagrody

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 2.160000%                                 |
| 10000   | 8.350000%                                 |
| 50000   | 18.940000%                                |
| 250000  | 59.170000%                                |


### Funkcja nagrody 1 - jeśli wpadniemy w dziurę -1 punkt, 1 punkt za dojście do celu

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 10.240000%                                |
| 10000   | 14.650000%                                |
| 50000   | 40.100000%                                |
| 250000  | 64.790000%                                |

### Funkcja nagrody 2 - przy wpadnięciu do dziury -10 punktów, 5 punktów za dojście do celu, -1 punkt za stanięcie na bezpieczną część (ale nie cel)

| epizody | średni procent dojść do celu              |
| ------- | ----------------------------------------- |
| 1000    | 2.500000%                                 |
| 10000   | 3.880000%                                 |
| 50000   | 20.960000%                                |
| 250000  | 61.120000%                                |

# Wnioski

Przy planszy 8x8 potrzeba dużej ilości epizodów aby osiągnąć optymalne rozwiązanie.
Jeśli chodzi o funkcję nagrody najlepsza okazała się pierwsza.
