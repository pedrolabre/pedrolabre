programa {
  funcao inicio() {
    real carne, bebida, tempo
    inteiro convidado
    logico rabico
    
    escreva ("\nDigite a quantidade de carne em kg: ")
    leia (carne)

    escreva ("Digite a quantidade de bebida em litros: ")
    leia (bebida)

    escreva("Digite o tempo disponível em horas: ")
    leia(tempo)

    escreva("Digite o número de convidados: ")
    leia(convidado)

    se (carne < 2 ){
      escreva ("\nQuantidade de carne insuficiente.")
    }senao{
       escreva ("\nQuantidade de carne suficiente.")
    }

    se (bebida < convidado){
      escreva("\nQuantidade de bebida insuficiente.")
    }senao {
      escreva("\nQuantidade de bebida suficiente.")
    }

    se (tempo < 3){
      escreva ("\nTempo disponível insuficiente.")
    }senao{
      escreva ("\nTempo disponível suficiente.")
    }

    rabico = carne > 2 ou bebida > convidado  ou tempo > 3
    se (rabico == verdadeiro){
      escreva("\nPelo menos uma das condições para o churrasco está satisfeita!")
    }senao{
      escreva("\nVocê não atende nenhuma condicções para o churrasco")
    }
    
  }
}
