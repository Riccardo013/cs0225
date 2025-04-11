import datetime 
def assistente_virtuale(comando):
    comando = comando.strip().lower()
    if comando == "":
        return "riformula la tua domanda."    
    if comando in ["Qual è la data di oggi?", "data di oggi",
                    "che data è oggi", "oggi che giorno è?"]:   
        oggi = datetime.date.today()    
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y") 
    elif comando in ["Che ore sono?", "mi dici l' ora ?", 
                     "orario attuale", "dimmi l'ora"]:      
        ora_attuale = datetime.datetime.now().time()        
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")    
    elif comando in ["Come ti chiami?", "chi sei ?", 
                     "dimmi il tuo nome","presentati"]:        
        risposta = "Mi chiamo Assistente Virtuale"  
    else:      
        risposta = "Non ho capito la tua domanda."  
    return risposta
    
while True: 
        comando_utente = input("Cosa vuoi sapere? ") 
        if comando_utente.lower() == "esci":
            print("Arrivederci!")        
            break    
        else:        
             print(assistente_virtuale(comando_utente)) 