# amenofis-discord-bot
Bot de discord mega fàcil, no hi ha gaire res a explicar la veritat.
Escrit originalment a la plataforma repl.it en python.

Per afegir missages afegir un nou item al diccionari `responses` que
contingui un diccionari amb les claus `match` i `response`. El match
es fara servir per comparar com a regex (case insensitive) i response
la resposta que enviara el bot al canal.

## Local

Per a fer correr el bot en local hauras de tenir un fitxer anomentat `.env` escrit amb el seguent format:

```bash
TOKEN="<el-token-del-bot-aniria-aqui>"
```

Per a l'entorn de produccio caldra crear la variable d'entorn `TOKEN` amb la mateixa informacio.

### Entorn Virtual

Crear un entorn virtual instal·lar dependències:
```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements-dev.txt
```

### Run

I finalment es pot correr el bot amb:

```bash
python ./bot.py
```

### Format

El codi esta formatejat fent servir [Black](https://github.com/psf/black).
