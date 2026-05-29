programa {
  funcao inicio() {
    inteiro idade 
    logico traje

    escreva ("Digite a idade do convidado:")
    leia (idade)

    traje = idade >= 18
    se (traje == verdadeiro){
        escreva("Convidado está apto para usar o Traje esporte.")
    }senao se (traje == falso){
        escreva ("Convidado não está apto para usar Traje esporte")
    }
    
  }
}