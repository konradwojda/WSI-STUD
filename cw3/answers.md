



| Głębokość biały/niebieski | 1         | 2          | 3     | 4     | 5         |
| ------------------------- | --------- | ---------- | ----- | ----- | --------- |
| 1                         | Niebieski | Biały      | Remis | Remis | Niebieski |
| 2                         | Biały     | Remis      | Remis | Remis | Remis     |
| 3                         | Biały     | Biały      | Biały | Remis | Remis     |
| 4                         | Biały     | Remis      | Remis | Remis | Niebieski |
| 5                         | Biały     | Biały      | Biały | Remis | Biały     |


ver0 - Za pion przyznajemy 1 punkt, za damkę 10 p.

ver1 - nagrody jak w wersji podstawowej + nagroda za stopień zwartości grupy (odejmuję pole pomiedzy najdalszymi pionkami / 3)

ver2 - za każdy pion na własnej połowie planszy otrzymuje się 5 nagrody, na połowie przeciwnika 7, a za każdą damkę 10.

ver3 - za każdy nasz pion otrzymuje się nagrodę w wysokości: (5 + numer wiersza, na którym stoi pion) (im jest bliżej wroga tym lepiej), a za każdą damkę: 10.



| Funkcja oceny biały/niebieski | ver0  | ver1  | ver2      | ver3  |
| ----------------------------- | ----- | ----- | --------- | ----- |
| ver0                          | Biały | Remis | Remis     | Remis |
| ver1                          | Remis | Remis | Niebieski | Remis |
| ver2                          | Biały | Remis | Remis     | Remis |
| ver3                          | Biały | Remis | Remis     | Remis |