<?php
session_start();

abstract class Pessoa {
    protected string $nome;
    public function __construct(string $nome) { $this->nome = $nome; }
    abstract public function apresentar(): string;
}

class Estudante extends Pessoa {
    private string $curso;
    private string $matricula;
    public function __construct(string $nome, string $curso, string $matricula) {
        parent::__construct($nome);
        $this->curso = $curso;
        $this->matricula = $matricula;
    }
    public function apresentar(): string {
        return "Estudante {$this->nome} - Curso: {$this->curso} - Matrícula: {$this->matricula}";
    }
}

abstract class Funcionario extends Pessoa {
    protected string $cargo;
    protected float $salario;
    public function __construct(string $nome, string $cargo, float $salario) {
        parent::__construct($nome);
        $this->cargo = $cargo;
        $this->salario = $salario;
    }
}

class Professor extends Funcionario {
    private string $areaAtuacao;
    public function __construct(string $nome, string $cargo, float $salario, string $areaAtuacao) {
        parent::__construct($nome, $cargo, $salario);
        $this->areaAtuacao = $areaAtuacao;
    }
    public function apresentar(): string {
        return "Professor {$this->nome} - Cargo: {$this->cargo}, Área: {$this->areaAtuacao}, Salário: R$ " 
             . number_format($this->salario, 2, ',', '.');
    }
}

class Servidor extends Funcionario {
    private string $setor;
    public function __construct(string $nome, string $cargo, float $salario, string $setor) {
        parent::__construct($nome, $cargo, $salario);
        $this->setor = $setor;
    }
    public function apresentar(): string {
        return "Servidor {$this->nome} - Cargo: {$this->cargo}, Setor: {$this->setor}, Salário: R$ " 
             . number_format($this->salario, 2, ',', '.');
    }
}

class Visitante extends Pessoa {
    private string $documento;
    public function __construct(string $nome, string $documento) {
        parent::__construct($nome);
        $this->documento = $documento;
    }
    public function apresentar(): string {
        return "Visitante {$this->nome} - Documento: {$this->documento}";
    }
}


if (!isset($_SESSION['pessoaIFTO'])) {
    $_SESSION['pessoaIFTO'] = [];
}
$pessoaIFTO = &$_SESSION['pessoaIFTO'];

if (isset($_GET['limpar'])) {
    $_SESSION['pessoaIFTO'] = [];
    header("Location: " . strtok($_SERVER["REQUEST_URI"], '?'));
    exit;
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['tipo'])) {
    $tipo = $_POST['tipo'];
    $nome = $_POST['nome'] ?? ''; 
    try {
        switch ($tipo) {
            case 'estudante':
                $pessoaIFTO[] = new Estudante($nome, $_POST['curso'], $_POST['matricula']);
                break;
            case 'professor':
                $pessoaIFTO[] = new Professor($nome, $_POST['cargo'], (float)$_POST['salario'], $_POST['areaAtuacao']);
                break;
            case 'servidor':
                $pessoaIFTO[] = new Servidor($nome, $_POST['cargo'], (float)$_POST['salario'], $_POST['setor']);
                break;
            case 'visitante':
                $pessoaIFTO[] = new Visitante($nome, $_POST['documento']);
                break;
        }
    } catch (Exception $e) {
        echo "Erro ao cadastrar: " . $e->getMessage();
    }
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
}

?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Pessoas - IFTO</title>
</head>
<body>
    <h1>Sistema de Cadastro de Pessoas no Campus IFTO</h1>

    <div class="container">

        <div class="cadastro">
            <h2>Formulários de Cadastro</h2>

            <table width="100%">
                <tr>
                    <td width="50%" valign="top">
                        <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
                            <fieldset>
                                <legend>Cadastrar Estudante</legend>
                                <input type="hidden" name="tipo" value="estudante">
                                <div>
                                    <label for="nome_est">Nome:</label>
                                    <input type="text" id="nome_est" name="nome" required>
                                </div>
                                <div>
                                    <label for="curso">Curso:</label>
                                    <input type="text" id="curso" name="curso" required>
                                </div>
                                <div>
                                    <label for="matricula">Matrícula:</label>
                                    <input type="text" id="matricula" name="matricula" required>
                                </div>
                                <br>
                                <button type="submit">Cadastrar Estudante</button>
                            </fieldset>
                        </form>
                    </td>
                    <td width="50%" valign="top">
                        <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
                            <fieldset>
                                <legend>Cadastrar Professor</legend>
                                <input type="hidden" name="tipo" value="professor">
                                <div>
                                    <label for="nome_prof">Nome:</label>
                                    <input type="text" id="nome_prof" name="nome" required>
                                </div>
                                <div>
                                    <label for="cargo_prof">Cargo:</label>
                                    <input type="text" id="cargo_prof" name="cargo" required>
                                </div>
                                <div>
                                    <label for="salario_prof">Salário (R$):</label>
                                    <input type="number" id="salario_prof" name="salario" step="0.01" required>
                                </div>
                                <div>
                                    <label for="areaAtuacao">Área de Atuação:</label>
                                    <input type="text" id="areaAtuacao" name="areaAtuacao" required>
                                </div>
                                <br>
                                <button type="submit">Cadastrar Professor</button>
                            </fieldset>
                        </form>
                    </td>
                </tr>
                
                <tr>
                    <td width="50%" valign="top">
                        <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
                            <fieldset>
                                <legend>Cadastrar Servidor</legend>
                                <input type="hidden" name="tipo" value="servidor">
                                <div>
                                    <label for="nome_serv">Nome:</label>
                                    <input type="text" id="nome_serv" name="nome" required>
                                </div>
                                <div>
                                    <label for="cargo_serv">Cargo:</label>
                                    <input type="text" id="cargo_serv" name="cargo" required>
                                </div>
                                <div>
                                    <label for="salario_serv">Salário (R$):</label>
                                    <input type="number" id="salario_serv" name="salario" step="0.01" required>
                                </div>
                                <div>
                                    <label for="setor">Setor:</label>
                                    <input type="text" id="setor" name="setor" required>
                                </div>
                                <br>
                                <button type="submit">Cadastrar Servidor</button>
                            </fieldset>
                        </form>
                    </td>
                    <td width="50%" valign="top">
                        <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
                            <fieldset>
                                <legend>Cadastrar Visitante</legend>
                                <input type="hidden" name="tipo" value="visitante">
                                <div>
                                    <label for="nome_vis">Nome:</label>
                                    <input type="text" id="nome_vis" name="nome" required>
                                </div>
                                <div>
                                    <label for="documento">Documento (RG/CPF):</label>
                                    <input type="text" id="documento" name="documento" required>
                                </div>
                                <br>
                                <button type="submit">Cadastrar Visitante</button>
                            </fieldset>
                        </form>
                    </td>
                </tr>
            </table>
            </div>

        <div class="listagem">
            <h2>Pessoas Cadastradas</h2>
            
            <?php if (empty($pessoaIFTO)): ?>
                <p>Nenhuma pessoa cadastrada ainda.</p>
            <?php else: ?>
                <ul>
                    <?php foreach ($pessoaIFTO as $pessoa): ?>
                        <li><?php echo htmlspecialchars($pessoa->apresentar(), ENT_QUOTES, 'UTF-8'); ?></li>
                    <?php endforeach; ?>
                </ul>
            <?php endif; ?>
            
            <a href="?limpar=true" class="link-limpar">Limpar Todos os Cadastros</a>
        </div>
    </div>

</body>
</html>