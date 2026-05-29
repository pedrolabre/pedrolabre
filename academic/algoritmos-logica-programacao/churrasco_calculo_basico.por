programa {
  funcao inicio() {
    real carne, bebida, tempo
    inteiro convidado
    logico rabico

    escreva ("Churrasco")

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

    rabico = carne > 2 e bebida > convidado e tempo > 3 
      se (rabico == verdadeiro){
          escreva ("\nTodas as condições para o churrasco estão satisfeitas!")
      }senao{
        escreva("\nCondições para o churrasco não foram atendidas")
      }
  }
}
