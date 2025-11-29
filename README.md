
# Hello DevOps – Flask alapú példaalkalmazás

Egyszerű Flask alapú „Hello DevOps” webalkalmazás, amely HTTP-n elérhető a http://localhost:8080 címen.  
A projekt célja a DevOps alaplépések bemutatása:

- kódkészítés
- verziókövetés (trunk-based fejlesztés)
- buildelés / futtatás
- Docker alapú konténerizálás
- Dev Container használata (VS Code fejlesztői konténer)

---

## 1. Előkészületek

A projekt futtatásához az alábbi eszközök szükségesek:

- **Python 3.x**
- **Git**
- **Docker Desktop** (konténerizáláshoz és Dev Containerhez)
- **Visual Studio Code**
  - *Dev Containers* bővítmény telepítve (Microsoft)

A forráskód alapértelmezett helye:  
`C:\Devops\hello-devops`

---

## 2. Alkalmazás felépítése

Főbb fájlok és mappák:

- `app.py`  
  Flask alapú webalkalmazás:
  - `udvozles()` függvény: a főoldal (`/`) kiszolgálása  
  - `informacio()` függvény: az `/info` végpont kiszolgálása  

- `requirements.txt`  
  A Python csomagfüggőségek listája (pl. Flask).

- `.gitignore`  
  Git által figyelmen kívül hagyandó fájlok és mappák (pl. `venv/`, `__pycache__/`).

- `Dockerfile`  
  A futtatáshoz használható Docker image definíciója (konténerizálás).

- `.devcontainer/devcontainer.json`  
  Dev Container konfiguráció VS Code-hoz.

- `.devcontainer/Dockerfile.dev`  
  Fejlesztői Docker image definíciója (Dev Container környezet).

---

## 3. Alkalmazás buildelése és futtatása lokálisan (Docker nélkül)

### 3.1 Virtuális környezet létrehozása és aktiválása

```bash
cd C:\Devops\hello-devops
python -m venv venv
venv\Scripts\activate
```

### 3.2 Szükséges csomagok telepítése

```bash
pip install -r requirements.txt
```

### 3.3 Alkalmazás futtatása

```bash
python app.py
```

Ezután a böngészőben elérhető:

- Főoldal: http://localhost:8080/
- Információs végpont: http://localhost:8080/info

---

## 4. Dockerizálás

A projekt tartalmaz egy `Dockerfile` fájlt, amelyből Docker image készíthető.

### 4.1 Image buildelése

```bash
cd C:\Devops\hello-devops
docker build -t hello-devops:latest .
```

### 4.2 Konténer futtatása

```bash
docker run -p 8080:8080 hello-devops:latest
```

Ezután az alkalmazás a konténerből lesz elérhető:

- Főoldal: http://localhost:8080/
- Információs végpont: http://localhost:8080/info

---

## 5. Git használata – trunk-based fejlesztés

A projekt GitHub repója:  
https://github.com/nandi111/hello-devops

Alap ág (trunk): `main`

### 5.1 Alap munkafolyamat

1. **Kiindulási ág:** `main`
2. **Új funkció fejlesztése:**
   - új branch létrehozása, pl.:
     ```bash
     git checkout -b feature/uj-vegpont
     ```
   - módosítások elvégzése
   - commit készítése:
     ```bash
     git add .
     git commit -m "Uj vegpont hozzaadasa"
     ```
   - branch feltöltése:
     ```bash
     git push -u origin feature/uj-vegpont
     ```
3. **Merge vissza a trunkre (`main`):**
   - GitHubon Pull Request létrehozása
   - kód áttekintés után merge a `main` ágba
   - lokálisan frissítés:
     ```bash
     git checkout main
     git pull
     ```

A commit üzenetek magyar nyelvűek és a változás tartalmára utalnak.

---

## 6. Dev Container használata (VS Code)

A projekt tartalmaz Dev Container konfigurációt, mellyel egységes fejlesztői környezet hozható létre VS Code-ban.

### 6.1 Előkészületek

- Visual Studio Code telepítve
- Dev Containers bővítmény telepítve
- Docker Desktop fut

### 6.2 Projekt megnyitása Dev Containerben

1. VS Code-ban nyisd meg a projekt mappáját:
   - `C:\Devops\hello-devops`
2. Nyomd meg:  
   `Ctrl + Shift + P`
3. Keresd meg:  
   **„Dev Containers: Reopen in Container”**
4. Válaszd ki, a VS Code pedig:
   - felépíti a dev konténert a `.devcontainer/Dockerfile.dev` alapján,
   - bemásolja a projektet a konténerbe,
   - lefuttatja a `pip install -r requirements.txt` parancsot.

### 6.3 Alkalmazás futtatása Dev Containerben

A Dev Containerben nyiss egy integrált terminált, majd:

```bash
python app.py
```

A böngészőből továbbra is a Windows host gépről tudod elérni:

- http://localhost:8080/
- http://localhost:8080/info

---

## 7. Összefoglalás

A projekt bemutatja:

- egy egyszerű Flask alapú webalkalmazás elkészítését,
- trunk-based Git használatot (main + feature branch),
- buildelést és futtatást lokális Python környezetben,
- Docker alapú konténerizálást,
- Visual Studio Code Dev Container használatát fejlesztői környezetként.
