Tässä on `Dijkstra`-luokan rivi riviltä -selitys suomeksi:

---

### `__init__` -metodi
```python
def __init__(self, input):
    self.input = input
    self.path = []
```

- **Tarkoitus**: Alustaa `Dijkstra`-olio.
- **Parametrit**:
  - `input`: 2D-lista (vierekkäisyysmatriisi), jossa jokainen alkio `input[i][j]` edustaa kaaren painoa solmusta `i` solmuun `j`. Jos kaarta ei ole, paino on `0`.
- **Attribuutit**:
  - `self.input`: Tallentaa graafin vierekkäisyysmatriisin.
  - `self.path`: Alustaa tyhjän listan, johon tallennetaan lasketut polut.

---

### `calculate` -metodi
```python
def calculate(self):
    return [self.calculateFromOrigin(i) for i, v in enumerate(self.input)]
```

- **Tarkoitus**: Laskee lyhimmät polut jokaisesta solmusta jokaiseen muuhun solmuun.
- **Toiminta**: 
  - Käyttää listatulkintaa ja suorittaa `calculateFromOrigin`-metodin jokaiselle solmulle `i`, eli suorittaa Dijkstran algoritmin jokaisesta solmusta.
- **Palauttaa**: Lista, jonka jokainen alkio on lista etäisyyksistä yhdestä solmusta kaikkiin muihin.

---

### `calculateFromOrigin` -metodi
```python
def calculateFromOrigin(self, origin):
    distance = [-1] * len(self.input)
    path = [-1] * len(self.input)  # vektori polun tallentamiseen

    # Etäisyys lähtösolmusta itseensä on aina 0
    distance[origin] = 0
    priority = list(range(len(self.input)))  # Muuntaa range-listaksi yhteensopivuuden vuoksi

    while priority:
        frm = self.getSmallestPossibleVertex(distance, priority)
        if frm == -1:
            break  # Ei enää saavutettavia solmuja
        priority.remove(frm)
        options = self.getOptionList(self.input[frm])
        for position, weight in options:
            dist = distance[frm] + weight
            if distance[position] == -1 or dist < distance[position]:
                distance[position] = dist
                path[position] = frm

    self.path.insert(origin, path)
    return distance
```

- **Tarkoitus**: Laskee lyhimmän polun tietystä lähtösolmusta kaikkiin muihin solmuihin käyttäen Dijkstran algoritmia.
- **Toiminta**:
  - `distance`: Lista, joka tallentaa lyhimmän etäisyyden `origin`-solmusta jokaiseen muuhun solmuun. Alustetaan `-1`:ksi (merkitsee käymättömiä solmuja).
  - `path`: Lista, joka seuraa edellistä solmua jokaiselle solmulle lyhyimmässä polussa.
  - `distance[origin] = 0`: Asettaa lähtösolmusta itseensä kuljetun etäisyyden `0`:ksi.
  - `priority`: Lista kaikista käymättömistä solmuista.
  - **Silmukan selitys**:
    - Etsii solmun `frm`, jolla on pienin etäisyys lähtösolmusta `priority`-listassa.
    - Poistaa `frm`:n `priority`-listasta eli merkitsee sen käydyksi.
    - Hakee `getOptionList`-metodin avulla listan kaarista, jotka lähtevät `frm`:stä.
    - Jokaiselle kaarelle `(position, weight)`:
      - Laskee etäisyyden `dist` solmuun `position`.
      - Jos etäisyys on lyhyempi, päivittää `distance[position]` ja `path[position]`.
  - **Palauttaa**: `distance`-listan, jossa on minimietäisyydet lähtösolmusta jokaiseen muuhun solmuun.

---

### `getSmallestPossibleVertex` -metodi
```python
def getSmallestPossibleVertex(self, distances, priority):
    smallestKey = -1
    smallestValue = float('inf')  # Käyttää ääretöntä vertailun helpottamiseksi
    for i in priority:
        if 0 <= distances[i] < smallestValue:
            smallestValue = distances[i]
            smallestKey = i
    return smallestKey
```

- **Tarkoitus**: Etsii käymättömistä solmuista sen, jolla on pienin etäisyys `distances`-listassa.
- **Toiminta**:
  - Alustaa `smallestValue` äärettömäksi.
  - Kiertää läpi solmut `priority`-listassa ja etsii solmun, jolla on pienin etäisyys.
  - Palauttaa solmun `smallestKey`, jolla on pienin etäisyys, tai `-1` jos yhtään solmua ei löydy.

---

### `getOptionList` -metodi
```python
def getOptionList(self, vector):
    return [[i, weight] for i, weight in enumerate(vector) if weight > 0]
```

- **Tarkoitus**: Palauttaa listan kaarista (naapurisolmuista), joilla on positiivinen paino nykyisestä solmusta.
- **Parametrit**:
  - `vector`: Nykyisen solmun vierekkäisyyslista.
- **Palauttaa**: Lista `[position, weight]` -pareja, joissa `weight > 0`.

---

### `getPath` -metodi
```python
def getPath(self):
    return self.path
```

- **Tarkoitus**: Palauttaa lasketut polut `calculate`-metodin suorittamisen jälkeen.
- **Palauttaa**: `self.path`-attribuutin, joka sisältää lyhimmät polut solmujen välillä.

---

### `getBestPath` -metodi
```python
def getBestPath(self, frm, to):
    return [i for i in reversed(self._getBestPath(frm, to, [to]))]
```

- **Tarkoitus**: Hakee lyhyimmän polun solmusta `frm` solmuun `to`.
- **Toiminta**:
  - Kutsuu `_getBestPath`-metodia rakentaakseen polun solmusta `frm` solmuun `to`.
  - Kääntää polun niin, että se alkaa solmusta `frm` ja päättyy solmuun `to`.
- **Palauttaa**: Lista, joka edustaa lyhintä polkua solmusta `frm` solmuun `to`.

---

### `_getBestPath` (yksityinen) -metodi
```python
def _getBestPath(self, frm, to, path):
    path_ = self.path[frm]
    lastNode = path_[to]
    path.append(lastNode)
    if lastNode == frm:
        return path
    else:
        return self._getBestPath(frm, lastNode, path)
```

- **Tarkoitus**: Rakentaa lyhyimmän polun solmusta `frm` solmuun `to` rekursiivisesti.
- **Parametrit**:
  - `frm`: Lähtösolmu.
  - `to`: Määränpääsolmu.
  - `path`: Lista, johon lisätään polun solmut.
- **Toiminta**:
  - Hakee edellisen solmun `lastNode` polusta `to`:hun.
  - Lisää `lastNode`:n `path`:iin.
  - Jos `lastNode` on sama kuin `frm`, polku on valmis.
  - Muutoin se jatkaa rekursiota siirtymällä `to`-solmusta `lastNode`-solmuun.
- **Palauttaa**: Lista `path`, jossa solmut ovat käänteisessä järjestyksessä (eli polku `to`-solmusta `frm`-solmuun), ja se käännetään `getBestPath`-metodissa.


---
