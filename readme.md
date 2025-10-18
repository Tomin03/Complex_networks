# Sieci złożone - lista 1

W ramach tego zadania stworzono program do analizy sieci wykorzystujący bibliotekę `networkx` w Pythonie. Program umożliwia pracę z siećmi o rozmiarze od 500 do 1000 wierzchołków.

## Zadanie 1

Program realizuje następujące funkcjonalności:

- **Wczytywanie sieci:** Dane można wczytać z pliku krawędzi (np. `.edges`) i utworzyć graf w Pythonie.
- **Znajdowanie najkrótszej ścieżki:** Użytkownik podaje wierzchołek startowy i końcowy, a program wyznacza najkrótszą ścieżkę między nimi.
- **Sprawdzanie grafu eulerowskiego:** Można sprawdzić, czy graf lub wybrany podgraf jest eulerowski, czyli czy spełnia dwa warunki:
  - Graf jest spójny.
  - Każdy wierzchołek ma parzystą liczbę połączeń.  
  Jeśli graf jest eulerowski, program wypisuje trasę eulerowską (kolejne wierzchołki w terminalu).
- **Wyznaczanie maksymalnego przepływu:** Użytkownik podaje wierzchołki źródłowy i docelowy, a program wyznacza maksymalny przepływ pomiędzy nimi.



