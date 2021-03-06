#!/bin/bash

originalsize=$(du moby-dick.txt)
python pressure -cv moby-dick.txt moby-dick-compressed.txt
compressedsize=$(du moby-dick-compressed.txt)
python pressure -xv moby-dick-compressed.txt moby-dick-uncompressed.txt

originalsize=$(du war-and-peace.txt)
python pressure -cv war-and-peace.txt war-and-peace-compressed.txt
compressedsize=$(du war-and-peace-compressed.txt)
echo -e "Tamanho original: $originalsize. Comprimido: $compressedsize."
python pressure -xv war-and-peace-compressed.txt war-and-peace-uncompressed.txt

originalsize=$(du les-miserables.txt)
python pressure -cbv les-miserables.txt les-miserables-compressed.txt
compressedsize=$(du les-miserables-compressed.txt)
echo -e "Tamanho original: $originalsize. Comprimido: $compressedsize."
python pressure -xbv les-miserables-compressed.txt les-miserables-uncompressed.txt

diff moby-dick.txt moby-dick-uncompressed.txt && diff war-and-peace.txt war-and-peace-uncompressed.txt && diff les-miserables.txt les-miserables-uncompressed.txt && exit 0
exit 1
