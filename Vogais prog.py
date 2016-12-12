print("Contagem de  vogal\n")
texto="Minha terra  tem palmeira, onde canta o  sabiaammm"
texto=texto.lower()
texto=texto.replace(" ","")
texto=texto.replace("\n","")
texto=texto.replace(".","")
texto=texto.replace("," ,"")
texto=texto.replace("à", "a")
texto=texto.replace("ã,", "a")
texto=texto.replace("é","e")
vogais=0
consoante=0
for caracter in texto:
    if caracter in "aeiou":
        vogais=vogais +1
    else:
        consoantes=consoante +1
        
print("vogais %d"  % vogais)
print("Não declare consoantes")
print("Total de vogais: %d %s" % (len(texto),(vogais)))
