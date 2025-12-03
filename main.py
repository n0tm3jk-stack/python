meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "sybau":"que te calles la boca",
            "bruh": "enserio o queeee",
            "lmao": "gracioso o toxico",
            "dogwater": "no sabes jugar juegos",
            "cracker": "eres jincho o palido",
            "MAGA": "culto de America",
            "calc": "abreviaccion de calculadora",
            "67": "meme de tiktok"}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("sorry la palabra que buscas no se encuentra")
