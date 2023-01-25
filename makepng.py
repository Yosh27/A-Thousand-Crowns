import png
import openpyxl

def strToLst(str):
    num = ''
    rgbaLst = []
    for i in range(len(str)):
        char = str[i]
        if char.isnumeric():
            num += char
            if not str[i + 1].isnumeric():
                rgbaLst += [int(num)]
                num = ''
    return rgbaLst


def getPixels(x, y):
    pixels = list()
    wbObj = openpyxl.load_workbook('C:\\Users\\...foo.xlsx') #Enter a path to a valid excel file here
    sheetObj = wbObj.active
    for row in range(1, y + 1):
        pixels += [[]]

        for column in range(1, x + 1):
            cellObj = sheetObj.cell(row, column)
            rgba = cellObj.value
            if rgba == None:
                rgba = [0, 0, 0, 0]
            
            else:
                rgba = strToLst(rgba)
            
            pixels[row - 1] += rgba

    return pixels


def makePNG(x, y, name = 'foo'):
    pixels = getPixels(x, y)
    png.from_array(pixels, 'RGBA').save(f'{name}.png')


if __name__=='__main__':
    makePNG(5465, 2821)
