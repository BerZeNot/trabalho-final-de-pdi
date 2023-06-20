import sys
import Utils
import ImageProcessor
# se a quantidade de argumentos em argv for menor que 2, mostre a forma de usar o programa

if len(sys.argv) < 2:
    Utils.showHelp()

if len(sys.argv) == 2:
    imageName = sys.argv[1]
    text = ImageProcessor.extractText(imageName)
    print(text)

elif len(sys.argv) == 4:
    if sys.argv[2] == "-o":
        imageName = sys.argv[1]
        text = ImageProcessor.extractText(imageName)
        filename = sys.argv[3]
        Utils.saveTextIntoAFile(text, filename)