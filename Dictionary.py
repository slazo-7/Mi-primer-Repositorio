meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LIT": "Cuando algo es especialmente asombroso",
            "DMS": "Se refiere a los mensajes directos que recibes",
            "GOAT": "Abreviacion a Greatest of all time, o el mejor de todos los tiempos"
            }
            
            
word = input("Escribe una palabra que no entiendas (con mayúsculas):")







            
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("Esa palabra significa",meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no se encuentra en el meme_dict")
