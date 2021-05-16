#!/usr/bin/env python

import logging
import os
import re

import discord
import dotenv

from keep_alive import keep_alive


class AmenofisBot(discord.Client):
    """Amenofis Bot per a totes les necessitats Mecenils.

    Discord.py bot que respon a missatges amb tonteries i lore d'El Pony Pisador.
    """

    responses = {
        "amenofis": {
            "match": r"a+?(:?\s+?)?m+?(:?\s+?)?e+?(:?\s+?)?n+?(:?\s+?)?o+?(:?\s+?)?f+?(:?\s+?)?i+?(:?\s+?)?s+?",
            "response": "Dispensi?",
        },
        "jordi": {
            "match": "jordi",
            "response": "Jetpack",
        },
        "jetpack": {
            "match": "jetpack",
            "response": "Jordi",
        },
        "wolframi": {
            "match": "wolframi",
            "response": "Tungstè",
        },
        "tungste": {
            "match": r"tungst(?:e|è)",
            "response": "Wolframi",
        },
        "gos": {
            "match": "gos",
            "response": "gat",
        },
        "gat": {
            "match": "gat",
            "response": "Ocell",
        },
        "ocell": {
            "match": "ocell",
            "response": ":ocells:",
        },
        "llom": {
            "match": "llom",
            "response": "Diplodocus",
        },
        "formatge": {
            "match": "formatge",
            "response": "El meu pare és un Formatge!",
        },
        "garota": {
            "match": "garota",
            "response": "La meva mare és una Garota",
        },
        "pokemon": {
            "match": "un pokemon va",
            "response": "Us tinc dit que si voleu pokemons li heu de demanar al Pokétwo :/",
        },
    }

    async def on_ready(self) -> None:
        logging.info(f"We have logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        for item in self.responses.values():
            match, resposta = item["match"], item["response"]
            if re.match(match, message.content, re.I):
                return await message.channel.send(resposta)


def main():
    dotenv.load_dotenv()
    keep_alive()

    logging.basicConfig(level=logging.INFO, format="[{asctime}][{name}][{levelname}][{module}] {message}", style="{")

    AmenofisBot().run(os.getenv("TOKEN", ""))


if __name__ == "__main__":
    main()
