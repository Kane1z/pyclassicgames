

def header_bitmap(ficheiro):
    with open(ficheiro, 'rb') as f:
        #tamanho
        f.seek(2)
        a=f.read(4)
        tamanho=(a[0]<<0)+(a[1]<<8)+(a[2]<<16)+(a[3]<<24)
        # inicio imagem
        f.seek(10)
        a = f.read(4)
        inicio_imagem = (a[0] << 0) + (a[1] << 8) + (a[2] << 16) + (a[3] << 24)

        # dimensoes imagem
        f.seek(18)
        a = f.read(4)
        largura = (a[0] << 0) + (a[1] << 8) + (a[2] << 16) + (a[3] << 24)
        a = f.read(4)
        altura = (a[0] << 0) + (a[1] << 8) + (a[2] << 16) + (a[3] << 24)

        # bits por pixel
        f.seek(28)
        a = f.read(2)
        bits_pixel = (a[0] << 0) + (a[1] << 8)

    f.close()
    return (tamanho, largura, altura, inicio_imagem,bits_pixel)

def le_bitmap(ficheiro, inicio, largura, altura, bits_pixel):
    quadro=[]
    for i in range(altura):
        quadro.append([0]*largura)

    with open(ficheiro,'rb') as f:
        f.seek(inicio)
        for x in range(0,altura):
            y=0
            while y<largura:
                bitmap=f.read(4)
                for i in range(4): #para os 4 bytes

                    m = bits_pixel
                    while m<=8 and y<largura:
                        #quadro[x][y]=(bitmap[i]>>(8-m))&(2**(bits_pixel)-1)<<(8-m)
                        quadro[x][y] = ((bitmap[i]) & ((2 ** (bits_pixel) - 1) << (8 - m)))>>(8-m)
                        #mask=(mask>>bits_pixel)
                        m+=bits_pixel
                        y+=1
    f.close()
    return(quadro)

def print_bitmap(bitmap):
    for a in range(len(bitmap)-1,-1,-1):
        i=bitmap[a]
        for j in i:

            if j==0:
                print('+',"blue",end="")
            else:
                print('.',"white", end='')

        print('\n')





if __name__=="__main__":
    ficheiro='imagem1.bmp'
    (tamanho, largura, altura, inicio,bits_pixel)=header_bitmap(ficheiro)
    print("O tamanho da imagem é {0}".format(tamanho))
    print("Bits por pixel: ",bits_pixel)
    print("Altura: %d largura: %d"%(altura,largura))
    quadro=le_bitmap(ficheiro,inicio, largura, altura, bits_pixel)
    print_bitmap(quadro)
