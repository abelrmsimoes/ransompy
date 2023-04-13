# Ransompy

Ransompy é um script Python que permite criptografar e descriptografar arquivos usando o algoritmo Fernet da biblioteca Cryptography.

Esse projeto foi criado com fins educacionais e de estudo sobre criptografia e segurança da informação.

## Instalação

Para executar o Ransompy é necessário ter o Python 3 instalado e a biblioteca Cryptography. Você pode instalar a biblioteca usando o pip:

```bash
pip install cryptography
```

## Como usar

Para usar o Ransompy, execute o arquivo ransom.py em um terminal. O script irá perguntar se você deseja criptografar ou descriptografar um arquivo.

```bash
python ransom.py
```

Se você escolher criptografar um arquivo, o script irá pedir o caminho completo do arquivo a ser criptografado. Após a criptografia, o script irá gerar uma chave única e salvar em um arquivo `key.key`.

Se você escolher descriptografar um arquivo, o script irá pedir o caminho completo do diretório que contém os arquivos criptografados. O script irá usar a chave gerada anteriormente para descriptografar os arquivos.

## Aviso

Esse projeto é apenas para fins educacionais e de estudo. Não use esse script para fins maliciosos e não criptografe arquivos que não pertencem a você. O autor não se responsabiliza pelo uso indevido desse script.
