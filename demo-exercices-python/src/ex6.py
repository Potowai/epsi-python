import tempfile

input = input("Contenu du fichier temporaire :")

print(tempfile.gettempdir())  # prints the current temporary directory

with tempfile.TemporaryFile(mode='w+t',delete=False) as fp:
    fp.write(input)
    print(fp.name)
    fp.seek(0)
    print(fp.read())
