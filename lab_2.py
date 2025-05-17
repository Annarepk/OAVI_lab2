from binarization import grayscale, singh

files = ['cat', 'hogwarts', 'map', 'text_flower', 'x_ray']

for name in files:
    filename = f"Pictures/{name}/{name}.png"
    resultFilename = f"Pictures/{name}/{name}"

    resultFiles = dict(grayscale=f"{resultFilename}Grayscale.bmp", binariz=f"{resultFilename}Singh.bmp")

    grayscale(filename, resultFiles['grayscale'])
    print('\n')

    singh(resultFiles['grayscale'], resultFiles['binariz'])
    # cat: k=0.15, R=80; hogwarts: k=0.25, R=90; map: k=0.15, R=130; text_flower: k=0.5, R=100; x_ray: k=0.15, R=7
    print('\n')