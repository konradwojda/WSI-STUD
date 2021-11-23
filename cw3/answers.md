# Domyślne ustawienia i przyjęte funkcje ewaluacji
Głębokość przeszukiwania: 5  

Heurystyki:

ver0 - Za pion przyznajemy 1 punkt, za damkę 10 p.

ver1 - nagrody jak w ver0 + nagroda za stopień zwartości grupy (odejmuję pole pomiedzy najdalszymi pionkami // 3)

ver2 - za każdy pion na własnej połowie planszy otrzymuje się 5 nagrody, na połowie przeciwnika 7, a za każdą damkę 10.

ver3 - za każdy nasz pion otrzymuje się nagrodę w wysokości: (5 + numer wiersza, na którym stoi pion) (im jest bliżej wroga tym lepiej), a za każdą damkę: 10.

# Odpowiedzi na pytania

## Czy gracz sterowany przez AI zachowuje się rozsądnie z ludzkiego punktu widzenia? Jeśli nie to co jest nie tak?

Przy podstawowych ustawieniach (depth = 5, ver0) sztuczna inteligencja zachowuje się rozsądnie, jednak ze względu na przyjętą heurystykę można zauwazyć dziwne zachowania np. zdobycie damki zamiast zbicia pionka lub unikanie zbicia pionka przeciwnika. 
Z punktu widzenia człowieka to wydaje się nienaturalne, jednak wiedząc jak działa algorytm - zrozumiałe.
Mimo to, ciężko jest pokonać taką sztuczną inteligencję.

Jeśli patrzymy na rozgrywkę AI vs AI spora część ruchów jest dziwna.
Oczywiście jest to spowodowane obranymi heurystykami.
Zdarza się, że jeden z graczy  przesuwa wszystkie swoje pionki na przód blokując swoje ruchy i w konsekwencji przegrywając.
W sytuacjach remisowych gracze wykonują na przemian te same ruchy damkami (przód - tył)
zamiast spróbować innych.

## Wpływ głębokości przeszukiwań na wyniki


| Głębokość biały/niebieski | 1         | 2          | 3     | 4     | 5         |
| ------------------------- | --------- | ---------- | ----- | ----- | --------- |
| 1                         | Niebieski | Biały      | Remis | Remis | Niebieski |
| 2                         | Biały     | Remis      | Remis | Remis | Remis     |
| 3                         | Biały     | Biały      | Biały | Remis | Remis     |
| 4                         | Biały     | Remis      | Remis | Remis | Niebieski |
| 5                         | Biały     | Biały      | Biały | Remis | Biały     |

Spodziewany wynik to taki, w którym, w większości przypadków, zwycięża gracz mający większą głębokość przeszukiwania.
Jednak, mimo takich samych funkcji ewaluacji, gracz biały ma zauważalną przewagę.
Gdy jego przeciwnik ma większą głębokość przeszukiwań - częściej jest w stanie zremisować lub nawet wygrać.
Czasami spowodowane jest to "głupim" działaniem algorytmu - jak zostało wspomniane wyżej.
Przewaga białego może również wynikać z tego, że wykonuje on ruch jako pierwszy. Dzięki temu szybciej zdobywa damkę, która daje mu duże ułatwienie w przypadku gdy przeciwnik ma wgląd w więcej ruchów "do przodu".

## Wpływ funkcji oceny na wyniki

| Funkcja oceny biały/niebieski | ver0  | ver1  | ver2      | ver3  |
| ----------------------------- | ----- | ----- | --------- | ----- |
| ver0                          | Biały | Remis | Remis     | Remis |
| ver1                          | Remis | Remis | Niebieski | Remis |
| ver2                          | Biały | Remis | Remis     | Remis |
| ver3                          | Biały | Remis | Remis     | Remis |

Zaimplementowane funkcje ewaluacji nie wpływają zbytnio na wynik rozgrywki, jednak obserwując zachowanie graczy mozna zauważyć którego algorytmu używają wybierając ruchy.