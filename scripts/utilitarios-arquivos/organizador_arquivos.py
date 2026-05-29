#!/usr/bin/env python3
"""
Organizador de Arquivos por Extensão
Organiza arquivos em pastas separadas baseado em suas extensões.
"""

import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class OrganizadorArquivos:
    def __init__(self, diretorio_alvo: str = None):
        """
        Inicializa o organizador de arquivos.
        
        Args:
            diretorio_alvo: Diretório para organizar. Se None, usa o diretório atual.
        """
        self.diretorio_alvo = Path(diretorio_alvo) if diretorio_alvo else Path.cwd()
        self.categorias = self._definir_categorias()
        self.arquivos_movidos = 0
        self.erros = []
        
    def _definir_categorias(self) -> Dict[str, List[str]]:
        """Define as categorias de arquivos e suas extensões."""
        return {
            "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico"],
            "Documentos": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
            "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
            "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
            "Executaveis": [".exe", ".msi", ".deb", ".rpm", ".dmg", ".pkg"],
            "Codigo": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".rb", ".go"],
            "Planilhas": [".xls", ".xlsx", ".csv", ".ods"],
            "Apresentacoes": [".ppt", ".pptx", ".odp"],
            "Fontes": [".ttf", ".otf", ".woff", ".woff2"],
            "Outros": []  # Para extensões não categorizadas
        }
    
    def _obter_categoria(self, extensao: str) -> str:
        """
        Determina a categoria de um arquivo baseado em sua extensão.
        
        Args:
            extensao: Extensão do arquivo (ex: ".jpg")
            
        Returns:
            Nome da categoria
        """
        extensao = extensao.lower()
        
        for categoria, extensoes in self.categorias.items():
            if categoria != "Outros" and extensao in extensoes:
                return categoria
        
        return "Outros"
    
    def _criar_diretorios(self) -> None:
        """Cria os diretórios das categorias se não existirem."""
        for categoria in self.categorias.keys():
            diretorio_categoria = self.diretorio_alvo / categoria
            if not diretorio_categoria.exists():
                try:
                    diretorio_categoria.mkdir(exist_ok=True)
                    print(f"Criado diretorio: {categoria}")
                except Exception as e:
                    self.erros.append(f"Erro ao criar diretorio {categoria}: {e}")
    
    def _mover_arquivo(self, arquivo: Path, diretorio_destino: Path) -> bool:
        """
        Move um arquivo para o diretório de destino.
        
        Args:
            arquivo: Caminho do arquivo a ser movido
            diretorio_destino: Diretório de destino
            
        Returns:
            True se o movimento foi bem-sucedido, False caso contrário
        """
        try:
            # Verifica se já existe um arquivo com o mesmo nome no destino
            destino_final = diretorio_destino / arquivo.name
            contador = 1
            
            while destino_final.exists():
                nome_base = arquivo.stem
                extensao = arquivo.suffix
                novo_nome = f"{nome_base}_{contador}{extensao}"
                destino_final = diretorio_destino / novo_nome
                contador += 1
            
            shutil.move(str(arquivo), str(destino_final))
            self.arquivos_movidos += 1
            return True
            
        except Exception as e:
            self.erros.append(f"Erro ao mover arquivo {arquivo.name}: {e}")
            return False
    
    def organizar(self) -> Tuple[int, List[str]]:
        """
        Organiza os arquivos no diretório alvo.
        
        Returns:
            Tuple com (número de arquivos movidos, lista de erros)
        """
        print(f"Organizando arquivos em: {self.diretorio_alvo}")
        print("=" * 50)
        
        # Cria os diretórios das categorias
        self._criar_diretorios()
        
        # Percorre todos os arquivos no diretório
        arquivos_processados = 0
        
        for item in self.diretorio_alvo.iterdir():
            # Ignora diretórios e o próprio script
            if item.is_dir() or item.name == "organizador_arquivos.py":
                continue
            
            try:
                extensao = item.suffix
                categoria = self._obter_categoria(extensao)
                diretorio_destino = self.diretorio_alvo / categoria
                
                if self._mover_arquivo(item, diretorio_destino):
                    print(f"{item.name} -> {categoria}/")
                    arquivos_processados += 1
                    
            except Exception as e:
                self.erros.append(f"Erro ao processar {item.name}: {e}")
        
        print("=" * 50)
        print(f"Resumo:")
        print(f"   Arquivos organizados: {arquivos_processados}")
        print(f"   Erros: {len(self.erros)}")
        
        if self.erros:
            print("\nErros encontrados:")
            for erro in self.erros:
                print(f"   • {erro}")
        
        return arquivos_processados, self.erros
    
    def listar_categorias(self) -> None:
        """Lista todas as categorias e suas extensões."""
        print("Categorias de Arquivos:")
        print("=" * 40)
        
        for categoria, extensoes in self.categorias.items():
            if categoria == "Outros":
                print(f"{categoria}: Arquivos nao categorizados")
            else:
                extensoes_formatadas = ", ".join(exensoes) if extensoes else "Nenhuma"
                print(f"{categoria}: {extensoes_formatadas}")
        
        print("=" * 40)


def main():
    """Função principal do script."""
    print("Organizador de Arquivos por Extensao")
    print("=" * 50)
    
    # Verifica se um diretório foi especificado
    diretorio_alvo = None
    if len(sys.argv) > 1:
        diretorio_alvo = sys.argv[1]
        if not os.path.exists(diretorio_alvo):
            print(f"Erro: O diretorio '{diretorio_alvo}' nao existe.")
            return
    
    # Cria o organizador
    organizador = OrganizadorArquivos(diretorio_alvo)
    
    # Menu interativo
    while True:
        print("\nOpcoes:")
        print("1. Organizar arquivos")
        print("2. Listar categorias")
        print("3. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (1-3): ").strip()
            
            if opcao == "1":
                print()
                organizador.organizar()
            elif opcao == "2":
                print()
                organizador.listar_categorias()
            elif opcao == "3":
                print("\nAté logo!")
                break
            else:
                print("Opcao invalida. Tente novamente.")
                
        except KeyboardInterrupt:
            print("\n\nOperacao cancelada. Ate logo!")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
