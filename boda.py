def conheses():  
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

    
    mas="\x1B[3m-> Mas..."
    escrita="\x1B[3m-> Responde com sim ou não oh corno"
    sim=["sim","s","ya","yes","y"]
    não=["nao","não","n","no"]
    
    #No pila escreves tuples (pergunta, resposta)
    pila = [(bodaq,bodatext),\
            (espamaq,espamatext),\
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
                                                                            	(carq,cartext)]
    
    for item in (pila):
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
            else:
                print()
                print(escrita)
                print()
conheses()
