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
    writeFile(output, text)

def extract(inputFile, base64, output):
    verbose("Descomprimindo arquivo", inputFile.name)
    text = inputFile.read()
    # extrai e DEPOIS descodifica do base64
    if(base64):
        text = decodeBase64(text)
    writeFile(output, text)

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
