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


def main(args):
    base64 = False
    if args.compress:
        print "Compress"
    if args.extract:
        print "Extract"
    if args.base64:
        print "Base64"
        base64 = True

if __name__ == "__main__":
    args = parse_args()
    main(args)
