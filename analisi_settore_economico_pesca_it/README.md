# Analisi Settore Economico Pesca

## 1. Tecnologie Utilizzate

- **Python**: linguaggio principale del progetto.
- **FastAPI**: framework leggero e performante per la creazione di API REST.
- **Uvicorn**: server ASGI per eseguire l'applicazione FastAPI.
- **VSCode**: editor di codice utilizzato per lo sviluppo.
- **Pandas**: per l’analisi e la gestione di dati in formato CSV o Excel.
- **Ambiente virtuale (venv)**: per isolare le dipendenze del progetto.

## 2. Creazione del Progetto

- Il progetto è stato avviato tramite il comando `createFastApiEnvironment` disponibile nell’estensione di VSCode.
- L’ambiente virtuale (`venv`) è stato creato sempre tramite VSCode per gestire le librerie del progetto in modo separato dal sistema.
- Al termine, la struttura di base comprende:
  - `main.py` (file principale dell’API FastAPI)
  - `.venv/` (cartella con ambiente virtuale)
  - Cartelle aggiuntive come `data/` per i database e `statics/` per file CSV o Excel.

## 3. Avvio del Progetto

- Apri il terminale in VSCode e attiva l’ambiente virtuale:

  ```sh
  # Su Windows
  .\.economia_pesca_it_venv\Scripts\activate

  # Su Mac/Linux
  source .economia_pesca_it_venv/bin/activate
  ```

- In the VSCode terminal, create a `requirements.txt` file:

  ```sh
  pip freeze > requirements.txt
  ```

- Installa le dipendenze se necessario:

  ```sh
  pip install -r requirements.txt
  pip install fastapi
  pip install uvicorn
  ```

- Avvia il server di sviluppo FastAPI:

  ```sh
  uvicorn main:app --reload
  ```

> Dopo l’avvio, puoi accedere alla documentazione interattiva su [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
