# -*- coding:utf-8 -*-
import argparse

def parse_args():
    # parser para os argumentos
    parser = argparse.ArgumentParser(description="UnderPressure: Comprime textos usando LZW", prog="pressure")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--compress", help="comprime o texto dado", action="store_true")
    group.add_argument("-x", "--extract", help="decomprime o texto dado", action="store_true")
    parser.add_argument("-b", "--base64", help="para textos não ASCII, utiliza essa opção para convertê-los para base64 antes", action="store_true")
    parser.add_argument("input", type=file, help="arquivo de texto para ser comprimido")
    parser.add_argument("output", help="nome do arquivo de saida")
    return parser.parse_args()

def compress(filename, base64, output):
    # tem que ler o arquivo aqui
    text = filename
    if(base64):
        text = encodeBase64(text)
    writeFile(output, text)

def extract(filename, base64, output):
    text = filename
    # extrai e DEPOIS tira do base64
    if(base64):
        text = decodeBase64(text)
    return text

def encodeBase64(text):
    print "Encoding in base64"

def decodeBase64(text):
    print "Decoding in base64"

def writeFile(filename, text):
    print "escrevendo arquivo..."

def main(args):
    if args.compress:
        compress(args.input, args.base64, args.output)
    if args.extract:
        extract(args.input, args.base64, args.output)

if __name__ == "__main__":
    args = parse_args()
    main(args)
