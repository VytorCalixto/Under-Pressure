# -*- coding:utf-8 -*-
import argparse
import base64
import logging

def parseArgs():
    # parser para os argumentos
    parser = argparse.ArgumentParser(description="UnderPressure: Comprime textos usando LZW", prog="pressure")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--compress", help="Comprime o texto dado", action="store_true")
    group.add_argument("-x", "--extract", help="Decomprime o texto dado", action="store_true")
    parser.add_argument("-b", "--base64", help="Para textos não ASCII, utiliza essa opção para convertê-los para base64 antes", action="store_true")
    parser.add_argument("-v", "--verbose", help="Executa de forma verbosa", action="store_true")
    parser.add_argument("input", type=file, help="Arquivo de texto para ser comprimido")
    parser.add_argument("output", help="Nome do arquivo de saida")
    return parser.parse_args()

def compress(inputFile, base64, output):
    verbose("Comprimindo arquivo", inputFile.name)
    text = inputFile.read()
    # codifica em base64 e compacta
    if(base64):
        text = encodeBase64(text)
    # LZW em si
    dictSize = 256 # tamanho da tabela ASCII
    dictionary = {}
    # xrange usado por performance
    for i in xrange(dictSize):
        dictionary[chr(i)] = i
    compressed = []

    w = ""
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            dictionary[wc] = dictSize
            ++dictSize
            w = c
    if w:
        compressed.append(dictionary[w])

    # writeFile(output, compressed)
    f = open(output, "wb")
    byteArray = bytearray(compressed)
    f.write(byteArray)
    f.close()

def extract(inputFile, base64, output):
    verbose("Descomprimindo arquivo", inputFile.name)
    text = inputFile.read()
    
    # extrai e DEPOIS decodifica do base64
    dictSize = 256
    dictionary = {}
    for i in xrange(dictSize):
        dictionary[i] = chr(i)
    if text:
        w = chr(text.pop(0))
    else:
        raise ValueError, "empty"
    result = [w]
    for k in text:
        if k in dictionary:
            entry = dictionary[k]
        elif k == len(dictionary):
            entry = w + w[0]
        else:
            raise ValueError, "Bad compressed k: %d" % k
        result.append(entry)
        dictionary[dictSize] = w + entry[0]
        ++dictSize

        w = entry
    print result
    #if(base64):
    #    text = decodeBase64(text)


    # writeFile(output, text)

def encodeBase64(text):
    verbose("Codificando em Base64")
    encoded = base64.b64encode(text)
    verbose("Codificado!")
    return encoded

def decodeBase64(text):
    verbose("Decodificando de Base64")
    decoded = base64.b64decode(text)
    verbose("Decodificado!")
    return decoded

def writeFile(filename, text):
    verbose("Escrevendo arquivo de saída")
    f = open(filename, "w")
    f.write(text)
    verbose("Feito")

def main(args):
    if args.compress:
        compress(args.input, args.base64, args.output)
    elif args.extract:
        extract(args.input, args.base64, args.output)
    else:
        print "Nenhuma opção foi escolhida. Saindo."

if __name__ == "__main__":
    args = parseArgs()
    if(args.verbose):
        def verbose(*args):
            for arg in args:
                print arg,
            print
    else:
        verbose = lambda *a: None
    main(args)
