def readImage(filepath):
    with open(filepath, "r") as image:
        image.readline().strip()
        
        line = image.readline().strip()
        
        width, height = map(int, line.split())
        grayscaleBits = int(image.readline().strip())
        
        conteudo = image.read()
        numeros = conteudo.split()
        pixels = []
        row = []
        rgb = []
        for num in numeros:
            rgb.append(int(num))
            
            if len(rgb) == 3:
                row.append(rgb)
                rgb = []
            
            if len(row) == width: 
                pixels.append(row)
                row = []
        
    return pixels, grayscaleBits, width, height

def mediaCinza(pixels, width, height):
    convertedPixels = []
    for y in range(height):
        fixedRow = []
        for x in range(width):
            redValue = int(pixels[y][x][0])
            greenValue = int(pixels[y][x][1])
            blueValue = int(pixels[y][x][2])
            grayscale = (redValue + greenValue + blueValue) // 3
            
            
            fixedRow.append(grayscale)
        convertedPixels.append(fixedRow)
    
    return convertedPixels


def mediaCor(pixels, width, height):
    convertedPixels = []
    averageColor = 0
    averageRed = 0
    averageGreen = 0
    averageBlue = 0
    for y in range(height):
        fixedRow = []
        for x in range(width):
            redValue = int(pixels[y][x][0])
            greenValue = int(pixels[y][x][1])
            blueValue = int(pixels[y][x][2])
            averageRed += redValue 
            averageGreen += greenValue
            averageBlue += blueValue
    averageRed = averageRed // (width * height)
    averageGreen = averageGreen // (width * height)
    averageBlue = averageBlue // (width * height)
    averageColor = [averageRed, averageGreen, averageBlue]
    
    for y in range(height):
        fixedRow = []
        for x in range(width):        
            fixedRow.append(' '.join(map(str, averageColor)))
        convertedPixels.append(fixedRow)
    
    return convertedPixels


def saveIMG(filename, type, bits, pixels, width, height):
    with open(filename, "w") as newImage:
        newImage.write(type + "\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        newImage.write(str(bits) + "\n")
        
        for row in pixels:
            newImage.write(" ".join(map(str, row)) + "\n")
        print("saved")
            
originalIMG = "Fig4.ppm"

pixels, bits, width, height = readImage(originalIMG)
limiar = 40
convertedGreyscale = mediaCinza(pixels, width, height)
convertedColor = mediaCor(pixels, width, height)

output = "media.pgm"

saveIMG(output, "P2", bits, convertedGreyscale, width, height)
saveIMG("cor.ppm", "P3", bits, convertedColor, width, height)