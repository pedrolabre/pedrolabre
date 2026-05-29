programa {
  funcao inicio() {
    inteiro valorCompra, cartao
    logico rabico

    escreva("Qual o valor da sua compra?" )
    leia(valorCompra)

    escreva("Você possui cartão fidelidade? (Sim = 1 / N = 0): ")
    leia(cartao)
    limpa()
   rabico = cartao == 1
   se (rabico == verdadeiro){
    escreva("\nO cliente tem direito a 5% de Desconto!")
   }

   rabico = valorCompra > 500 
   se (rabico == verdadeiro){
    escreva("\nO cliente tem direito a 10% de Desconto!")
   }

   rabico = valorCompra > 300 e valorCompra < 500
   se (rabico == verdadeiro){
    escreva ("\nO cliente possui Frete Grátis!")
   }
   rabico = cartao == 1 ou valorCompra > 500 ou (valorCompra > 300 e valorCompra < 500)
   se (rabico == verdadeiro){
    escreva ("\nO cliente tem direito a pelo menos UM benefício!")
   }senao se (rabico == falso){
    escreva ("\nO cliente NÃO tem direito a nenhum benefício!")
   }  
  }
}
    

