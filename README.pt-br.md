[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/abelrmsimoes/ransompy/blob/main/README.md)

# Ransompy

Ransompy é uma aplicação de demonstração de criptografia simples para fins educacionais. Ela foi desenvolvida para ilustrar um cenário em que os arquivos de um diretório são criptografados e só podem ser descriptografados com a chave adequada.

⚠️ **AVISO**: Este projeto é apenas para fins educacionais e deve ser usado com responsabilidade. A criptografia de arquivos e qualquer tipo de atividade maliciosa são ilegais e eticamente condenáveis.

## Funcionamento

A aplicação Ransompy oferece duas funcionalidades principais:

1. Criptografar um diretório: Permite criptografar todos os arquivos de um diretório selecionado usando a biblioteca de criptografia "cryptography" e o algoritmo Fernet. Ao concluir a criptografia, os arquivos não poderão ser acessados sem a chave adequada.

2. Descriptografar um diretório: Permite descriptografar os arquivos previamente criptografados usando a chave gerada durante o processo de criptografia. Caso a chave seja removida ou perdida, os arquivos não poderão ser recuperados.

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório do Ransompy para o seu computador.
3. Navegue para o diretório do projeto usando o terminal ou prompt de comando.

```bash
git clone https://github.com/seu_usuario/ransompy.git
cd ransompy
```

4. É recomendável criar um ambiente virtual para instalar as dependências do projeto:

### No Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### No Windows

```bash
python -m venv venv
venv\Scripts\activate
```

5. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

6. Execute o arquivo "ransompy.py" para iniciar a aplicação.

```bash
python ransompy.py
```

7. Escolha a opção "1" para criptografar um diretório ou "2" para descriptografar um diretório.
8. Siga as instruções na tela para fornecer o caminho completo do diretório alvo.

⚠️ **IMPORTANTE**: Antes de executar a funcionalidade de descriptografia, tenha em mente que a chave para descriptografar os arquivos é essencial. Sem ela, os arquivos não poderão ser recuperados.

## Aviso de Responsabilidade

Este projeto é fornecido apenas para fins educacionais e demonstrativos. Seu uso para qualquer atividade maliciosa é estritamente proibido e ilegal. O autor e os contribuidores não se responsabilizam por qualquer uso indevido deste software.

## Contribuições

Se você deseja contribuir para este projeto ou relatar problemas, fique à vontade para abrir um "issue" ou enviar um "pull request" no repositório do Ransompy.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
