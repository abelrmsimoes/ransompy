import os
import uuid
from cryptography.fernet import Fernet

KEYS_DIR = "keys"


def generate_key(md5_hash):
    key = Fernet.generate_key()
    if not os.path.exists(KEYS_DIR):
        os.mkdir(KEYS_DIR)
    with open(f"{KEYS_DIR}/{md5_hash}.key", "wb") as key_file:
        key_file.write(key)


def load_key(md5_hash):
    return open(f"{KEYS_DIR}/{md5_hash}.key", "rb").read()


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
    choice = input("Você deseja criptografar (1) ou descriptografar (2) um diretório? ")

    if choice == "1":
        directory = input(
            "Digite o caminho completo do diretório que deseja criptografar: "
        )

        if not os.path.exists(directory):
            print("Diretório não encontrado.")
            return

        md5_hash = uuid.uuid5(uuid.NAMESPACE_DNS, directory).hex
        generate_key(md5_hash)
        key = load_key(md5_hash)

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Verificar se o arquivo já está criptografado
                    if not file_path.endswith(".key"):
                        encrypt_file(file_path, key)
                        print(f"{file} criptografado com sucesso.")
                except Exception as e:
                    print(f"{file} não pode ser criptografado! Erro: {e}")

    elif choice == "2":
        directory = input(
            "Digite o caminho completo do diretório que deseja descriptografar: "
        )

        if not os.path.exists(directory):
            print("Diretório não encontrado.")
            return

        md5_hash = uuid.uuid5(uuid.NAMESPACE_DNS, directory).hex
        key = load_key(md5_hash)
        can_remove_key = True

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Verificar se o arquivo já está descriptografado
                    if not file_path.endswith(".key"):
                        decrypt_file(file_path, key)
                        print(f"{file} descriptografado com sucesso.")
                except Exception as e:
                    print(f"{file} não pode ser descriptografado! Erro: {e}")
                    can_remove_key = False

        if can_remove_key:
            os.remove(f"{os.getcwd()}/{KEYS_DIR}/{md5_hash}.key")

    else:
        print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
