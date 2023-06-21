import sys
import Utils
import ImageProcessor
# se a quantidade de argumentos em argv for menor que 2, mostre a forma de usar o programa

if len(sys.argv) == 1:
    Utils.showHelp()
    exit()

resize=False
if sys.argv.__contains__("--resize"):
    resize=True

if len(sys.argv) == 2 or len(sys.argv) == 3:
    imageName = sys.argv[1]
    text = ImageProcessor.extractText(imageName, resize=resize)
    print(text)

elif len(sys.argv) == 4 or len(sys.argv) == 5:
    if sys.argv[2] == "-o":
        imageName = sys.argv[1]
        text = ImageProcessor.extractText(imageName, resize=resize)
        filename = sys.argv[3]
        Utils.saveTextIntoAFile(text, filename)
    else:
        print("O parâmetro ",sys.argv[2],"é inválido!")
else:
    print("Quantidade inválida de parâmetros!")
