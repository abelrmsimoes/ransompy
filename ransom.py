import os
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def encrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file_path, "wb") as f:
        f.write(encrypted)


def decrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path, "wb") as f:
        f.write(decrypted_data)


def main():
    choice = input(
        "Você deseja criptografar (1) ou descriptografar (2) um diretório? ")

    if choice == "1":
        generate_key()
        key = load_key()
        directory = input(
            "Digite o caminho completo do diretório que deseja criptografar: ")
        for root, dirs, files in os.walk(directory):
            for file in files:
                try:
                    encrypt_file(os.path.join(root, file), key)
                    print(f"{file} criptografado com sucesso!")
                except:
                    print(f"{file} não pode ser criptografado!")
        print("Arquivos criptografados com sucesso!")

    elif choice == "2":
        key = load_key()
        directory = input(
            "Digite o caminho completo do diretório que deseja descriptografar: ")
        for root, dirs, files in os.walk(directory):
            for file in files:
                try:
                    decrypt_file(os.path.join(root, file), key)
                    print(f"{file} descriptografado com sucesso!")
                except:
                    print(f"{file} não pode ser descriptografado!")
        print("Arquivos descriptografados com sucesso!")

    else:
        print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
