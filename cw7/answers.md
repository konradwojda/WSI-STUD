# Reprezentacja grafu

Klasa Node odpowiada za jeden z węzłów i posiada nazwę, listę nazw węzłów, od których jest zależna
oraz słownik z prawdopodobieństwami.

- jeśli węzeł nie zależy od innych, wtedy słownik ma jeden element - prawdopodobieństwo "True"

- jeśli węzeł zależy od innych wtedy słownik zawiera krotki z wartościami węzłów, od których zależy np. (True, False) podanych w kolejności podania węzłów na liście
    - w przypadku gdy węzeł zależy od jednego węzła również jest to krotka np. (True,)

Lepiej możemy to zobaczyć w pliku `nodes_structure.json`

Wszystkie prawdopodobieństwa podane są dla prawdopodobieństw zdarzenia "True", ponieważ przeciwne możemy obliczyć.

# Generowanie próbki

Gdy mamy stworzoną strukturę węzłów generowanie próbki jest dosyć proste:

- w przypadku braku zależności od innych węzłów - losujemy liczbę od 0 do 1 i sprawdzamy czy jest mniejsza od podanego prawdopodobieństwa

- w przypadku gdy węzeł zależy od innych - sprawdzam ich wartości, losuję liczbę od 0 do 1 i sprawdzam czy jest mniejsza od prawdopodobieństwa zadeklarowanego dla odpowiednich wartości węzłów, od których zależy

W taki sposób otrzymujemy słownik reprezentujący próbkę.

# Ładowanie danych z pliku

Zdecydowałem się na użycie pliku JSON, tak aby można było wykorzystać słowniki do tworzenia węzłów.

Ważne jest, aby podawać węzły w takiej kolejności, w jakiej są w grafie.

# Wyniki z wykorzystaniem klasyfikatora ID3

Wykonano klasyfikację dla 5000 próbek.

## Macierz pomyłek

| Predykcja / Klasa rzeczywista | Pozytywna | Negatywna |
| ----------------------------- | --------- | --------- |
| Pozytywna                     | 247       | 87        |
| Negatywna                     | 145       | 1571      |

Dokładność: **86%**

# Wnioski

Generowanie danych okazało się być dosyć proste, jednak najważniejsze było wymyślenie odpowiedniej struktury reprezentowania grafu oraz wczytywania go z pliku.