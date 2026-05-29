<?php

class Caixa 
{
    public $saldo;
    public $titular;

    public function __construct($nome, $saldoComeca = 0) 
    {
        $this->titular = $nome;
        $this->saldo = 0;
    }

    public function depositar($valor) 
    {
        if ($valor > 0) {
            $this->saldo += $valor; 
            echo "Depósito de R$ {$valor} efetuado.<br>";
        }
    }

    public function sacar($valor) 
    {
        if ($this->saldo >= $valor && $valor > 0) {
            $this->saldo -= $valor; 
            echo "Saque de R$ {$valor} efetuado.<br>";
        } else {
            echo "Saldo insuficiente.<br>";
        }
    }

    public function emitirExtrato() 
    {
        echo "Titular: {$this->titular} | Saldo: R$ {$this->saldo}<hr>";
    }
}

// teste-

$minhaConta = new Caixa("Pedro Labre", 0);
$minhaConta->emitirExtrato();

$minhaConta->depositar(100);
$minhaConta->emitirExtrato();

$minhaConta->sacar(50);
$minhaConta->emitirExtrato();

$minhaConta->sacar(500);
$minhaConta->emitirExtrato();

?>