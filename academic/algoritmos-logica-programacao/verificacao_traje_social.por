programa {
  funcao inicio() {
    caracter convite
    logico traje 

    escreva("O nome do convidado está no convite? (S/N): ")
    leia(convite)

    traje = convite == 'S'
    se (traje == verdadeiro){
       escreva("O convidado precisa usar traje social.")
    }senao se (traje == falso){
        escreva("O convidado não precisa usar traje social.")}
    
  }
}
