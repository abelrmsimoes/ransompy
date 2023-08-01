[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/abelrmsimoes/ransompy/blob/main/README.pt-br.md)

# Ransompy

Ransompy is a simple encryption demonstration application for educational purposes. It was developed to illustrate a scenario where the files in a directory are encrypted and can only be decrypted with the proper key.

⚠️ **WARNING**: This project is for educational purposes only and should be used responsibly. File encryption and any form of malicious activities are illegal and ethically condemnable.

## How It Works

The Ransompy application provides two main functionalities:

1. Encrypt a directory: Allows encrypting all the files in a selected directory using the "cryptography" encryption library and the Fernet algorithm. Once encrypted, the files cannot be accessed without the proper key.

2. Decrypt a directory: Allows decrypting previously encrypted files using the key generated during the encryption process. If the key is removed or lost, the files cannot be recovered.

## How to Use

1. Make sure you have Python installed on your machine.
2. Clone the Ransompy repository to your computer.
3. Navigate to the project directory using the terminal or command prompt.

```bash
git clone https://github.com/seu_usuario/ransompy.git
cd ransompy
```

4. It is recommended to create a virtual environment to install the project dependencies:

### On Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

5. Install the project dependencies:

```bash
pip install -r requirements.txt
```

6. Run the "ransompy.py" file to start the application.

```bash
python ransompy.py
```

7. Choose option "1" to encrypt a directory or "2" to decrypt a directory.
8. Follow the on-screen instructions to provide the full path of the target directory.

⚠️ IMPORTANT: Before executing the decryption functionality, keep in mind that the decryption key is essential. Without it, the files cannot be recovered.

## Disclaimer

This project is provided for educational and demonstration purposes only. Its use for any malicious activity is strictly prohibited and illegal. The author and contributors are not responsible for any misuse of this software.

## Contributions

If you wish to contribute to this project or report issues, feel free to open an issue or submit a pull request on the Ransompy repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
