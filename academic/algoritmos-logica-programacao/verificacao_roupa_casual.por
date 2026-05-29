programa {
  funcao inicio() {
    caracter convite, traje 
    logico casual 

    escreva("Informe o traje do convidado (E para esporte, S para social, C para casual): ")
    leia(traje)

    escreva("O nome do convidado está no convite? (S/N): ")
    leia(convite)

    casual =  (traje != 'S') ou (traje == 'S' e convite == 'S')
    se (casual == verdadeiro){
      escreva("O convidado pode usar roupa casual.")
    }senao se (casual == falso){
    escreva("O convidado não pode usar roupa casual.")
    }
  }
}
