def conheses():  
    import random
    bodaq="\x1B[0mConheses o Boda? (Sim ou não) -> "
    bodatext="\x1B[3m-> O caralho que ta foda"
    espamaq="\x1B[0mE o Espama? -> "
    espamatext="\x1B[3m-> Espama a piça"
    teixeiraq="\x1B[0mE o Teixeira? -> "
    teixeiratext="\x1B[3m-> Pega no meu pau e cheira"
    pacauq="\x1B[0mE o Pacau? -> "
    pacautext="\x1B[3m-> Dá o cu que eu meto o pau"
    miroq="\x1B[0mE o Miro? -> "
    mirotext="\x1B[3m-> Miro no teu cu e atiro"
    marioq="\x1B[0mE o Mário? -> "
    mariotext="\x1B[3m-> O que te comeu atrás do armário"
    tatuq="\x1B[0mE o Tatú? -> "
    tatutext="\x1B[3m-> É o que te vai ao cu"
    joaoq="\x1B[0mE o João? -> "
    joaotext="\x1B[3m-> Então deixa eu passar a mão"
    bartoloq="\x1B[0mE o Bartolomeu? -> "
    bartolotext="\x1B[3m-> Bartolo, agora o teu cu é meu"
    manelq="\x1B[0mE o Manel? ->"
    maneltext="\x1B[3m-> Agarra-me aqui no pincel"
    inesq="\x1B[0mE a Inês? ->"
    inestext="\x1B[3m-> A inesquecível pirocada nesse cu"
    nicoq="\x1B[0mE o Nicolau? ->"
    nicotext="\x1B[3m-> Pega no meu pau"
    paveq="\x1B[0mE o Pavê? ->"
    pavetext="\x1B[3m-> Dá-me o cu e vê"
    ramaq="\x1B[0mE o Ramalho? ->"
    ramatext="\x1B[3m-> Mama-me aqui o caralho"
    abreuq="\x1B[0mE o Abreu? ->"
    abreutext="\x1B[3m-> Aquele que te comeu"
    sosaq="\x1B[0mE o Sosa? ->"
    sosatext="\x1B[3m-> Espreita aqui a grossa"
    albq="\x1B[0mE o Alberto? ->"
    albtext="\x1B[3m-> O que te deixou o cu aberto"
    semedoq="\x1B[0mE o Semedo? ->"
    semedotext="\x1B[3m-> O que te vai ao cu sem medo"
    carq="\x1B[0mE o Carriço? ->"
    cartext="\x1B[3m-> Agarra aqui o meu piço"
    susanaq="\x1B[0mE a Susana? ->"
    susanatext="\x1B[3m-> Come a minha banana"

    
    mas="\x1B[3m-> Mas..."
    escrita=["\x1B[3m-> Responde com sim ou não oh corno",\
             "\x1B[3m-> Wi para lá com isso, é sim ou não",\
             "\x1B[3m-> Forazz escreve sim ou não oh bartolo",\
             "\x1B[3m-> Caralho é sim ou não chabal"]
    sim=["sim","s","ya","yes","y"]
    não=["nao","não","n","no", "quem", "quem?"]
    talvez=["talvez", "tlvz"]
    talveztext=["\x1B[3mNão é talvez cabrão, é sim ou não",\
                "\x1B[3mQueres levar xinada? É sim ou não, não talvez",\
                "\x1B[3mTás a ser parvo ou o quê? Aqui não há talvez"]
    
    #No pila escreves tuples (pergunta, resposta)
    
    pila = [(espamaq,espamatext),\
            (teixeiraq,teixeiratext),\
            (pacauq,pacautext),\
            (miroq,mirotext),\
            (marioq,mariotext),\
            (tatuq,tatutext),\
            (joaoq,joaotext),\
            (bartoloq,bartolotext),\
            (manelq,maneltext),\
            (inesq,inestext),\
            (nicoq,nicotext),\
            (paveq,pavetext),\
            (ramaq,ramatext),\
            (abreuq,abreutext),\
            (sosaq,sosatext),\
            (albq,albtext),\
            (semedoq,semedotext),\
            (carq,cartext),\
            (susanaq,susanatext)]
    random.shuffle(pila)
    pila.append((bodaq,bodatext))
    pila.reverse()
    
    for item in pila:
        respondeu = False
        while not respondeu:
            answ=str(input(item[0])).lower()
            if answ in sim:
                print()
                print(mas)
                print()
                respondeu = True
            elif answ in não:
                print()
                print(item[1])
                print()
                respondeu = True
            elif answ in talvez:
                print()
                print(random.choice(talveztext))
                print()
            else:
                print()
                print(random.choice(escrita))
                print()
conheses()
