#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════════════╗
# ║                 JXE OBFUSCATED 7-LAYER LAUNCHER                      ║
# ║  ENCODE BY : @Itz_Jahid_X   |   TG : @Jahid_x_Empire                  ║
# ╚══════════════════════════════════════════════════════════════════════╝
import base64 as IllllIllIllI
import sys as IlllIllIlIll
import zlib as lIIIllIIIIII
try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM as lIIllllIIlII
except ImportError:
    print('Missing dependency: python -m pip install cryptography')
    raise SystemExit(1)
IIllllIIIIll = b'ItzJahidXSecretKey2026!@#$12345\x00'
IIlIlIIIIIlI = b'JXE-7-LAYER-KEY'
lllIIlIlllll = b'JXE_ENCODED_SOURCE_V2\x00'
lIIlIlIIIIll = b'JXE_7LAYER_V1\x00'
# JXE_PAYLOAD_BEGIN
IlllIlIIIIlI = (
    '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'
    'eL5Hw8CroMPad+75t87waf/7738cqYHY'
)
def IIIIIIlllIll(IIlIIIIlIlIl):
    return bytes(v ^ IIlIlIIIIIlI[i % len(IIlIlIIIIIlI)] for i, v in enumerate(IIlIIIIlIlIl))
try:
    IIlIIlIlIIll = IllllIllIllI.b64decode(''.join(IlllIlIIIIlI.split()), validate=True)
    if not IIlIIlIlIIll.startswith(lIIlIlIIIIll):
        raise ValueError('Invalid layer signature')
    IIlIIIIlIlIl = lIIIllIIIIII.decompress(IIlIIlIlIIll[len(lIIlIlIIIIll):])
    IIlIIIIlIlIl = IllllIllIllI.b64decode(IIlIIIIlIlIl, validate=True)
    IIlIIIIlIlIl = bytes.fromhex(IIlIIIIlIlIl.decode('ascii'))[::-1]
    IIlIIIIlIlIl = IIIIIIlllIll(IIlIIIIlIlIl)
    if not IIlIIIIlIlIl.startswith(lllIIlIlllll):
        raise ValueError('Layer verification failed')
    IIIllIlIlIII = len(lllIIlIlllll)
    IIlIlllIIlII = IIlIIIIlIlIl[IIIllIlIlIII:IIIllIlIlIII+12]
    llIIlIIlllIl = IIlIIIIlIlIl[IIIllIlIlIII+12:]
    llllIlIlIllI = lIIllllIIlII(IIllllIIIIll).decrypt(IIlIlllIIlII, llIIlIIlllIl, lllIIlIlllll)
    IIllIlIllIll = lIIIllIIIIII.decompress(llllIlIlIllI)
    exec(compile(IIllIlIllIll, __file__, 'exec'), {'__name__': '__main__', '__file__': __file__})
except Exception as IlIllllIllII:
    print('Could not run encoded source:', IlIllllIllII, file=IlllIllIlIll.stderr)
    raise SystemExit(1)
