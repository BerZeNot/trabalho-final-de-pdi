def showHelp():
    print("\nIMAGE TEXT EXTRATOR - v1.0.0")
    print("\nUso básico: Application.py nome-da-imagem.jpg")
    print("\nCom esse comando, o programa fará a extração do texto e exibirá na tela do console.")
    print("\nCaso deseje salvar o texto extraido em um arquivo, use o parâmetro '-o nome-do-arquivo-de-saida.txt'. Veja o exeplo:")
    print("\n\tApplication.py image.png -o textoExtraido.txt\n\n")
    print("₢ Ferreira & Oliveira Software House - Todos os direitos reservados.\n")

def saveTextIntoAFile(text, filename):
    print("Saving text...")
    file = open(filename, "a")
    file.write(text)
    file.close()
    print("Saved into ",filename)