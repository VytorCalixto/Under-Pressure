![pressure](pressure.png)
# UnderPressure
Trabalho 3 de redes: compactador e descompatador de texto utilizando LZW

---

## Uso:
`pressure [OPÇÕES] [ARQUIVO]`

## Opções:
* `-c` para compactar
* `-x` para extrair
* `-b`
    * Ao compactar, transforma a entrada de dados em base64 antes da compactação
    * Ao descompactar, transformar o texto descompactado de base64 para a codificação original

## AVISO
O pressure só funciona com textos codificados em ASCII. Para codificações diferentes,
utilize a opção `-b` para converter o texto para base64 antes da compactação.
