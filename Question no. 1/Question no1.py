
def encrypt_file (filename,key):
    with open(filename,"r+" as file ):
        content = file.red()
        file.seek(0)
        file.write(encrypt_text(content,key))
        file.truncate()
    print(f"file:{filename} encrypted sucessfully")

"""Decrypt file function to decrypt the text file """

def decrypt_file (filename,key):
    with open(filename,"r+" as file ):
        content = file.red()
        file.seek(0)
        file.write(decrypt_text(content,key))
        file.truncate()
    print(f"file:{filename} decrypt sucessfully")

    #running the scruipt 

    filename+ "text.txt" # enter your text file name or path 

    if __name__ == "__main__":
        #encrypt_file(filename,5)
        decrypt_file(filename,5)


