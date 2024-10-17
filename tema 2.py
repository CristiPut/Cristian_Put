text= ("Republica Moldova îşi votează viitorul euro- pean cu umbra Rusiei în spate Stiri externe.")
jumatate=len(text)//2
prima_jumatate=text[:jumatate]
a_doua_jumatate=text[jumatate:]
prima_jumatate=prima_jumatate.upper()
prima_jumatate=prima_jumatate.strip()
a_doua_jumatate=a_doua_jumatate[::-1].strip()
a_doua_jumatate=a_doua_jumatate.strip()
a_doua_jumatate=a_doua_jumatate.capitalize()
a_doua_jumatate=a_doua_jumatate.replace(".", "")
a_doua_jumatate=a_doua_jumatate.replace(",", "")
a_doua_jumatate=a_doua_jumatate.replace("?", "")
a_doua_jumatate=a_doua_jumatate.replace("!", "")
text=prima_jumatate+a_doua_jumatate
print(text)


