
import socket
import os
import binascii
from datetime import datetime
import json
import select
import requests
import threading
import re
import time
import struct
import urllib3
import random
inviteD = False
inviteD = False
zix = False
invit_spam = False
V = 5

def g_m(pk, rp):
    rp = rp.encode('utf-8')
    rp = rp.hex()
    hd = pk[0:8]
    pL = pk[8:10]
    pB = pk[10:32]
    bL = pk[32:34]
    b2 = pk[34:60]
    p_l = pk[60:62]
    p_t = re.findall(r'{}(.*?)28'.format(p_l), pk[50:])[0]
    p_T = pk[int(int(len(p_t)) + 62):]

    nT = (hex((int(f'0x{p_l}', 16) - int(len(p_t) // 2)) + int(len(rp) // 2))[2:])
    if len(nT) == 1:
        nT = "0" + str(nT)

    np = hex(((int(f'0x{pL}', 16) - int((len(p_t)) // 2))) + int(len(rp) // 2))[2:]
    nb = hex(((int(f'0x{bL}', 16) - int(len(p_t) // 2))) + int(len(rp) // 2))[2:]

    fP = hd + np + pB + nb + b2 + nT + rp + p_T
    return str(fP)

yout1 = b"\x06\x00\x00\x00{\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*o\x08\x81\x80\x83\xb6\x01\x1a)[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf\xe3\x85\xa4\xd8\xa7\xd9\x84\xd8\xa8\xd9\x87\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xdc)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\tAO'-'TEAM\xf0\x01\x01\xf8\x01\xdc\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02F"
yout2 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xd6\xd1\xb9(\x1a![18ffff]\xef\xbc\xa8\xef\xbc\xac\xe3\x85\xa4Hassone.[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xcf\x1e\xd8\x01\xcc\xd6\xd0\xad\x03\xe0\x01\xed\xdc\x8d\xae\x03\xea\x01\x1d\xef\xbc\xb4\xef\xbc\xa8\xef\xbc\xa5\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xac\xef\xbc\xac\xe0\xbf\x90\xc2\xb9\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout3 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xe9\xa7\xe9\x1b\x1a [18ffff]DS\xe3\x85\xa4WAJIHANO\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xca2\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x10.DICTATORS\xe3\x85\xa4\xe2\x88\x9a\xf0\x01\x01\xf8\x01\xc4\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout4 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*n\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout5 = b"\x06\x00\x00\x00\x84\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*x\x08\xb6\xc0\xf1\xcc\x01\x1a'[18ffff]\xd9\x85\xd9\x84\xd9\x83\xd8\xa9*\xd9\x84\xd9\x85\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a\xd9\x86[18ffff]2\x02ME@G\xb0\x01\x05\xb8\x01\x82\x0b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x15\xe9\xbf\x84\xef\xbc\xac\xef\xbc\xaf\xef\xbc\xb2\xef\xbc\xa4\xef\xbc\xb3\xe9\xbf\x84\xf0\x01\x01\xf8\x01>\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x05\xd8\x02\x0e"
yout6 = b'\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xeb\x98\x88\x8e\x01\x1a"[18ffff]OP\xe3\x85\xa4BNL\xe3\x85\xa4\xe2\x9a\xa1\xe3\x85\xa4*[18ffff]2\x02ME@R\xb0\x01\x10\xb8\x01\xce\x16\xd8\x01\x84\xf0\xd2\xad\x03\xe0\x01\xa8\xdb\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x8f\xe1\xb4\xa0\xe1\xb4\x87\xca\x80\xe3\x85\xa4\xe1\xb4\x98\xe1\xb4\x8f\xe1\xb4\xa1\xe1\xb4\x87\xca\x80\xe2\x9a\xa1\xf0\x01\x01\xf8\x01A\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01\xe0\x02\xf3\x94\xf6\xb1\x03'
yout7 = b"\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xb0\xa4\xdb\x80\x01\x1a'[18ffff]\xd9\x85\xd9\x83\xd8\xa7\xd9\x81\xd8\xad\xd8\xa9.\xe2\x84\x93\xca\x99\xe3\x80\xb5..[18ffff]2\x02ME@T\xb0\x01\x13\xb8\x01\xfc$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x1d\xef\xbc\xad\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa1\xe3\x85\xa4\xe2\x8e\xb0\xe2\x84\x93\xca\x99\xe2\x8e\xb1\xf0\x01\x01\xf8\x01\xdb\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0f\xd8\x02>"
yout8 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xfd\x8a\xde\xb4\x02\x1a\x1f[18ffff]ITZ\xe4\xb8\xb6MOHA\xe3\x85\xa42M[18ffff]2\x02ME@C\xb0\x01\n\xb8\x01\xdf\x0f\xd8\x01\xac\xd8\xd0\xad\x03\xe0\x01\xf2\xdc\x8d\xae\x03\xea\x01\x15\xe3\x80\x9dITZ\xe3\x80\x9e\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf8\x01\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x026'
yout9 = b'\x06\x00\x00\x00w\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*k\x08\xc6\x99\xddp\x1a\x1b[18ffff]HEROSHIIMA1[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xb2\xef\xbc\xaf\xef\xbc\xb3\xef\xbc\xa8\xef\xbc\xa9\xef\xbc\xad\xef\xbc\xa1\xef\xa3\xbf\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout10 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout11 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout12 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout14 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout15 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\x90\xf6\x87\x15\x1a"[18ffff]V4\xe3\x85\xa4RIO\xe3\x85\xa46%\xe3\x85\xa4zt[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\x95&\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x0e\xe1\xb4\xa0\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x8f\xd1\x95\xf0\x01\x01\xf8\x01\xe2\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02^\xe0\x02\x85\xff\xf5\xb1\x03'
yout16 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout17 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout18 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout19 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout20 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout21= b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout22 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout23 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout24 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout25 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout26 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout27 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout28 = b"\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xaa\xdd\xf1'\x1a\x1d[18ffff]BM\xe3\x85\xa4ABDOU_YT[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xd4$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1d\xe2\x80\xa2\xc9\xae\xe1\xb4\x87\xca\x9f\xca\x9f\xe1\xb4\x80\xca\x8d\xe1\xb4\x80\xd2\x93\xc9\xaa\xe1\xb4\x80\xc2\xb0\xf0\x01\x01\xf8\x01\x8e\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x07\xd8\x02\x16"
yout29 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9a\xd6\xdcL\x1a-[18ffff]\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa4\xef\xbc\xa9[18ffff]2\x02ME@H\xb0\x01\x01\xb8\x01\xe8\x07\xea\x01\x15\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xc9\xb4\xef\xbd\x93\xe1\xb4\x9b\xe1\xb4\x87\xca\x80\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout30 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb6\x92\xa9\xc8\x01\x1a [18ffff]\xef\xbc\xaa\xef\xbc\xad\xef\xbc\xb2\xe3\x85\xa4200K[18ffff]2\x02ME@R\xb0\x01\x13\xb8\x01\xc3(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\n3KASH-TEAM\xf8\x012\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x06\xd8\x02\x13\xe0\x02\x89\xa0\xf8\xb1\x03'
yout31 = b"\x06\x00\x00\x00\x92\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x85\x01\x08\xa2\xd3\xf4\x81\x07\x1a'[18ffff]\xd8\xb3\xd9\x80\xd9\x86\xd9\x80\xd8\xaf\xd8\xb1\xd9\x8a\xd9\x84\xd8\xa71M\xe3\x85\xa4[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xc1 \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xad\xef\xbc\xa6\xef\xbc\x95\xef\xbc\xb2\xef\xbc\xa8\xe3\x85\xa4\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x98\xf0\x01\x01\xf8\x01\x8c\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x024\xe0\x02\x87\xff\xf5\xb1\x03"
yout32 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xe0\xe1\xdeu\x1a\x1a[18ffff]P1\xe3\x85\xa4Fahad[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xd0&\xd8\x01\xea\xd6\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xe3\x85\xa4\xef\xbc\xb0\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xa5\xef\xbc\xae\xef\xbc\xa9\xef\xbc\xb8\xc2\xb9\xf0\x01\x01\xf8\x01\x9e\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02*'
yout33 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[18ffff]@EL9YSAR[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03'
yout34 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xa9\x81\xe6^\x1a\x1e[18ffff]STRONG\xe3\x85\xa4CRONA[18ffff]2\x02ME@J\xb0\x01\x13\xb8\x01\xd8$\xd8\x01\xd8\xd6\xd0\xad\x03\xe0\x01\x92\xdb\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xbc\x01'
yout35 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xeb\x8d\x97\xec\x01\x1a&[18ffff]\xd8\xb9\xd9\x80\xd9\x85\xd9\x80\xd8\xaf\xd9\x86\xd9\x8a\xd9\x80\xd8\xaa\xd9\x80\xd9\x88[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xd3\x1a\xd8\x01\xaf\xd7\xd0\xad\x03\xe0\x01\xf4\xdc\x8d\xae\x03\xea\x01\rOSIRIS\xe3\x85\xa4MASR\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02\\\xe0\x02\xf4\x94\xf6\xb1\x03'
yout36 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xb4\xff\xa3\xef\x01\x1a\x1c[18ffff]ZAIN_YT_500K[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xa3#\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\xbb\xdb\x8d\xae\x03\xea\x01\x1b\xe1\xb6\xbb\xe1\xb5\x83\xe1\xb6\xa4\xe1\xb6\xb0\xe3\x85\xa4\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\\\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02('
yout37 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\x86\xa7\x9e\xa7\x0b\x1a([18ffff]\xe2\x80\x94\xcd\x9e\xcd\x9f\xcd\x9e\xe2\x98\x85\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8[18ffff]2\x02ME@d\xb0\x01\x13\xb8\x01\xe3\x1c\xe0\x01\xf2\x83\x90\xae\x03\xea\x01!\xe3\x85\xa4\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf8\x01u\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Y\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout38 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xc3\xcf\xe5H\x1a([18ffff]\xe3\x85\xa4BEE\xe2\x9c\xbfSTO\xe3\x85\xa4\xe1\xb5\x80\xe1\xb4\xb5\xe1\xb4\xb7[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xffP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x15TIK\xe2\x9c\xbfTOK\xe1\xb5\x80\xe1\xb4\xb1\xe1\xb4\xac\xe1\xb4\xb9\xf0\x01\x01\xf8\x01\xc8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02q'
yout39 = b'\x06\x00\x00\x00\x94\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x87\x01\x08\x97\xd5\x9a.\x1a%[18ffff]\xd8\xb9\xd9\x86\xd9\x83\xd9\x88\xd8\xb4\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe3\x85\xa4[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xe8(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe1\xb4\x9c\xea\x9c\xb1\xca\x9c\xe3\x85\xa4\xe1\xb4\x9b\xe1\xb4\x87\xe1\xb4\x80\xe1\xb4\x8d\xf0\x01\x01\xf8\x01\xb6\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02"\xe0\x02\xf2\x94\xf6\xb1\x03'
yout40 = b'\x06\x00\x00\x00\x8a\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*~\x08\xf7\xdf\xda\\\x1a/[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xad\xef\xbc\xb3\xef\xbc\xa9_\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xb9*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\x8e\x0e\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02S\xe0\x02\xc3\xb7\xf8\xb1\x03'
yout41 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xb5\xdd\xec\x8e\x01\x1a%[18ffff]\xd8\xa7\xd9\x88\xd9\x81\xe3\x80\x80\xd9\x85\xd9\x86\xd9\x83\xe3\x85\xa4\xe2\x9c\x93[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xdd#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x18\xef\xbc\xaf\xef\xbc\xa6\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf0\x01\x01\xf8\x01\xe8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Q'
yout42 = b'\x06\x00\x00\x00\x8b\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x7f\x08\x81\xf4\xba\xf8\x01\x1a%[18ffff]\xef\xbc\xa7\xef\xbc\xa2\xe3\x85\xa4\xef\xbc\xae\xef\xbc\xaf\xef\xbc\x91\xe3\x81\x95[18ffff]2\x02ME@N\xb0\x01\x0c\xb8\x01\xbd\x11\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xa7\xef\xbc\xb2\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xb4__\xef\xbc\xa2\xef\xbc\xaf\xef\xbc\xb9\xf8\x018\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02-\xe0\x02\x85\xff\xf5\xb1\x03'
yout43 = b'\x06\x00\x00\x00o\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*c\x08\xfb\x9d\xb9\xae\x06\x1a\x1c[18ffff]BT\xe3\x85\xa4BadroTV[18ffff]2\x02ME@@\xb0\x01\x13\xb8\x01\xe7\x1c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x91\xdb\x8d\xae\x03\xea\x01\nBadro_TV_F\xf0\x01\x01\xf8\x01\x91\x1a\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02!'
yout44 = b"\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xc4\xe5\xe1>\x1a'[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf~\xd8\xa7\xd9\x84\xd8\xba\xd9\x86\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@J\xb0\x01\x14\xb8\x01\xceP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x03Z7F\xf0\x01\x01\xf8\x01\xd0\x19\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\x9c\x01"
yout45 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xfd\xa4\xa6i\x1a$[18ffff]\xd8\xb2\xd9\x8a\xd9\x80\xd8\xb1\xc9\xb4\xcc\xb67\xcc\xb6\xca\x80\xe3\x85\xa4[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xe1(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x19\xc2\xb7\xe3\x85\xa4\xe3\x85\xa4N\xe3\x85\xa47\xe3\x85\xa4R\xe3\x85\xa4\xe3\x85\xa4\xc2\xb7\xf0\x01\x01\xf8\x01\x8f\t\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02k'
yout46 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xcc\xb9\xcc\xd4\x06\x1a"[18ffff]\xd8\xa8\xd9\x88\xd8\xad\xd8\xa7\xd9\x83\xd9\x80\xd9\x80\xd9\x80\xd9\x85[18ffff]2\x02ME@9\xb0\x01\x07\xb8\x01\xca\x0c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x11*\xef\xbc\x97\xef\xbc\xaf\xef\xbc\xab\xef\xbc\xa1\xef\xbc\xad*\xf0\x01\x01\xf8\x01\xad\x05\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout47 = b'\x06\x00\x00\x00e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*Y\x08\xe8\xbd\xc9b\x1a [18ffff]\xe3\x80\x8cvip\xe3\x80\x8dDR999FF[18ffff]2\x02ME@Q\xb0\x01\x10\xb8\x01\x94\x16\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xf0\x01\x01\xf8\x01\xa0\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout48 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\x86\xb7\x84\xf1\x01\x1a&[18ffff]\xd8\xa2\xd9\x86\xd9\x8a\xd9\x80\xd9\x80\xd9\x84\xd8\xa7\xce\x92\xe2\x92\x91\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\x82)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x13\xce\x92\xe2\x92\x91\xe3\x85\xa4MAFIA\xe3\x85\xa4\xef\xa3\xbf\xf0\x01\x01\xf8\x01\x95\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W'
yout49 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout50 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout51 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x028c8d99a21bn\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout_list = [yout1,yout2,yout3,yout4,yout5,yout6,yout7,yout8,yout9,yout10,yout11,yout12,yout14,yout15,yout16,yout17,yout18,yout19,yout20,yout21,yout22,yout23,yout24,yout25,yout26,yout27,yout28,yout29,yout30,yout31,yout32,yout33,yout34,yout35,yout36,yout37,yout38,yout39,yout40,yout41,yout42,yout43,yout44,yout45,yout46,yout47,yout48,yout49,yout50,yout51]

class Px:
    def __init__(self):
        self.u = "bot"
        self.p = "bot"
        self.yout_list = yout_list
        self.zix = False
        self.p1 = None
        self.p2 = None
        self.rt = None
        self.s5 = None
        self.s12 = None
        self.eP = None
        self.lag_0515_packet = None
        self.lag_remote = None
        self.lag_active = False
        self.lag_lock = threading.Lock()

    def zx(self, id):
        try:
            n = int(id)
            eB = []
            while True:
                b = n & 0x7F
                n >>= 7
                if n:
                    b |= 0x80
                eB.append(b)
                if not n:
                    break
            return ''.join(f'{b:02x}' for b in eB)
        except Exception as e:
            return None

    def sH(self, id, msg):
        try:
            eP = self.pP(msg, id)
            if self.s12:
                self.s12.send(bytes.fromhex(eP))
        except Exception as e:
            pass

    def send_yout_list(self):
        if not self.s5:
            print("[!] s5 not assigned.")
            return
        for i, packet in enumerate(self.yout_list):
            try:
                self.s5.send(packet)
                time.sleep(2)
            except Exception as e:
                print(f"[!] Error sending packet {i+1}: {e}")

    def bmw(self, id):
        try:
            number = int(id)
            encoded_bytes = []
            while True:
                byte = number & 0x7F   
                number >>= 7
                if number:
                    byte |= 0x80     
                encoded_bytes.append(byte)
                if not number:
                    break
            return ''.join(f'{b:02x}' for b in encoded_bytes)
        except Exception as e:
            print("error", e)
            return None

            
            
    def pP(self, txt, uid):
        try:
            if isinstance(uid, str):
                t_id = self.Dc(uid) if hasattr(self, 'Dc') else int(uid, 16)
            else:
                t_id = uid
            dt = {
                1: t_id,
                2: 18,
                4: 2,
                5: {
                    1: 240140842,
                    2: t_id,
                    4: txt,
                    5: 1776729600,
                    7: 2,
                    9: {
                        1: '[i][b][c][FF0000][b]e404 [00FFFF] Apk[FF00FF]++',
                        2: 902000306,
                        4: 330,
                        5: 827001006,
                        8: 'ZiX',
                        10: 1,
                        11: 1,
                        13: {1: 2},
                        14: {1: 1158053040, 2: 8, 3: {2: 21, 1: 10}}
                    },
                    10: 'en',
                    13: {2: 2, 3: 1}
                }
            }            
            hR = self.pH(dt)
            if hR:
                return self.zP("1200", hR)
            return None
        except Exception as e:
            return None

    def eV(self, val):
        res = bytearray()
        while val > 0x7F:
            res.append((val & 0x7F) | 0x80)
            val >>= 7
        res.append(val & 0x7F)
        return bytes(res)

    def eT(self, f_n, w_t):
        return self.eV((f_n << 3) | w_t)

    def e6(self, f_n, val):
        return self.eT(f_n, 0) + self.eV(val)

    def e3(self, f_n, val):
        return self.eT(f_n, 0) + self.eV(val)

    def eS(self, f_n, val):
        enc = val.encode('utf-8')
        return self.eT(f_n, 2) + self.eV(len(enc)) + enc

    def eM(self, f_n, data):
        return self.eT(f_n, 2) + self.eV(len(data)) + data

    def e14_3(self, data):
        buf = bytearray()
        if 1 in data:
            buf.extend(self.e3(1, data[1]))
        if 2 in data:
            buf.extend(self.e3(2, data[2]))
        return bytes(buf)

    def e9_14(self, data):
        buf = bytearray()
        if 1 in data:
            buf.extend(self.e3(1, data[1]))
        if 2 in data:
            buf.extend(self.e3(2, data[2]))
        if 3 in data and isinstance(data[3], dict):
            sub = self.e14_3(data[3])
            buf.extend(self.eM(3, sub))
        return bytes(buf)

    def e9_13(self, data):
        buf = bytearray()
        if 1 in data:
            buf.extend(self.e3(1, data[1]))
        return bytes(buf)

    def eU(self, data):
        buf = bytearray()
        if 1 in data:
            buf.extend(self.eS(1, data[1]))
        if 2 in data:
            buf.extend(self.e3(2, data[2]))
        if 4 in data:
            buf.extend(self.e3(4, data[4]))
        if 5 in data:
            buf.extend(self.e3(5, data[5]))
        if 8 in data:
            buf.extend(self.eS(8, data[8]))
        if 10 in data:
            buf.extend(self.e3(10, data[10]))
        if 11 in data:
            buf.extend(self.e3(11, data[11]))
        if 13 in data:
            s13 = self.e9_13(data[13])
            buf.extend(self.eM(13, s13))
        if 14 in data:
            s14 = self.e9_14(data[14])
            buf.extend(self.eM(14, s14))
        return bytes(buf)

    def eA(self, data):
        buf = bytearray()
        if 2 in data:
            buf.extend(self.e3(2, data[2]))
        if 3 in data:
            buf.extend(self.e3(3, data[3]))
        return bytes(buf)

    def eI(self, data):
        buf = bytearray()
        if 1 in data:
            buf.extend(self.e6(1, data[1]))
        if 2 in data:
            buf.extend(self.e6(2, data[2]))
        if 4 in data:
            buf.extend(self.eS(4, data[4]))
        if 5 in data:
            buf.extend(self.e3(5, data[5]))
        if 7 in data:
            buf.extend(self.e3(7, data[7]))
        if 9 in data:
            u_d = self.eU(data[9])
            buf.extend(self.eM(9, u_d))
        if 10 in data:
            buf.extend(self.eS(10, data[10]))
        if 13 in data:
            a_d = self.eA(data[13])
            buf.extend(self.eM(13, a_d))
        return bytes(buf)

    def eO(self, data):
        buf = bytearray()
        if 1 in data:
            buf.extend(self.e6(1, data[1]))
        if 2 in data:
            buf.extend(self.e3(2, data[2]))
        if 4 in data:
            buf.extend(self.e3(4, data[4]))
        if 5 in data:
            i_d = self.eI(data[5])
            buf.extend(self.eM(5, i_d))
        return bytes(buf)

    def pH(self, data):
        enc = self.eO(data)
        return binascii.hexlify(enc).decode('utf-8')

    def zP(self, st, pk):
        p_len = len(pk)//2
        l_h = hex(p_len).split('x')[-1]
        z = "0000" if len(l_h) == 2 else "000" if len(l_h) == 3 else "00" if len(l_h) == 4 else "0"
        return f"{st}{z}{l_h}{pk}"

    def En(self, val):
        try:
            val = int(val)
            res = []
            while val > 0:
                b = val & 0x7F
                val >>= 7
                if val > 0:
                    b |= 0x80
                res.append(b)
            return bytes(res).hex()
        except Exception as e:
            return None

    def Dc(self, h_v):
        try:
            b_v = bytes.fromhex(h_v)
            r, sh = 0, 0
            for b in b_v:
                r |= (b & 0x7F) << sh
                if not (b & 0x80):
                    break
                sh += 7
            return r
        except Exception as e:
            return None
            
    def ff(self, c, i):
        try:
            if len(i) == 8:
                p = '060000007508d4d7faba1d100620022a6908cec2f1051a195b3030666666665d5b635d5b625d626f54207e2041706b000032024d454064b00101b801e807d801d4d8d0ad03e001b2dd8dae03ea011eefbca8efbca5efbcb2efbcafefbcb3efbca8efbca9efbcadefbca1efa3bf8002fd98a8dd03900201d00201'
                p = re.sub(r'cec2f105', i, p)
                c.send(bytes.fromhex(p))
            elif len(i) == 10:
                p = '060000006b08d4d7faba1d100620022a5f08fb9db9ae061a185b4646303030305d5b635d5b625d20424f547e61706b000032024d454064b00113b801e71cd801d4d8d0ad03e001b2dd8dae03ea010a5a45522d49534b494e47f00101f801911a8002fd98a8dd03900201d0020ad80221'
                p = re.sub(r'fb9db9ae06', i, p)
                c.send(bytes.fromhex(p))
        except Exception as e:
            pass

    def zx2(self, i):
        try:
            n = int(i)
            e = []
            while True:
                b = n & 0x7F
                n >>= 7
                if n:
                    b |= 0x80
                e.append(b)
                if not n:
                    break
            return ''.join(f'{b:02x}' for b in e)
        except:
            return None
            
    def spy(self, id):
        ep = f"050000040108{id}100520062af40708{id}12024d451801200332c90408{id}121a544fe385a4efbcb3efbd81efbd8cefbd81efbd8defbd8fe29cb01a024d452087b68faa06284030a9cbd13038324218dcf38766f4aae860efb7ce64e39ba361e99fe061e8b6ce64480150d30158b9106886db8dae037a05b38ec5b00382011d08efdaf1eb041203357635180620f087d4f0042a0808c89d85f30410038801c2ffc4b00392010c0107090a0b1216191a1e20239801d501a00131a80185fff5b103c00101c80101e80101880203920208b930e532fe0ac205aa020a080110a84618807d2003aa0208080210fa3318f403aa0208080f109b7118904eaa0205081710e751aa0205081810ba41aa0205081a10c435aa0205081b109b71aa0205081c109539aa0205082010d338aa0205082110f736aa0205082210c435aa0205082b108835aa02050823109b71aa02050831108835aa02050839109b71aa0205083d109b71aa02050841109b71aa0205084910e432aa0205084d10e432aa02050834109b71aa0205082810e432aa0205082910e432b00201c2024012041a0201041a21084812060104050607021a0b08011003189b0320bc9b011a08080210022092ed021a0508501201631a0508511201652207120565ed0e890ed802a9a38daf03ea02520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3339303835333639383032393935362f706963747572653f77696474683d313630266865696768743d31363010011801f202090882cab5ee0110f9028a03060802100218059203009803f7c282ac0ba2030c2144454144e385a4484f4d4532d30208{id}120b544f502d464952452d50431a024d45208cb68faa0628043085cbd13038324218c09ae061c0b5ce64c091e66080c3856680a897638096a361480150c90158e80792010601090a1219209801c901c00101c80101e801018802049202059603000000aa0208080110ff34188064aa020b080f10fd3218b086012001aa0205080210e432aa0205081810fd32aa0205081a10fd32aa0205081c10fd32aa0205082010fd32aa0205082210fd32aa0205082110fd32aa0205081710e432aa0205082310fd32aa0205082b10fd32aa0205083110fd32aa0205083910fd32aa0205083d10fd32aa0205084110fd32aa0205084910d836aa0205084d10e432aa0205081b10fd32aa0205083410fd32aa0205082810e432aa0205082910e432c2022112041a0201041a0508501201631a0508511201651a090848120501040506072200ea0204100118018a03009203003a0101400150016801721e313639383934353830303230323738373034345f346a7867796f626e397988018190ae92d194c8ef17a20100a80101b001e001ea010449444331"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))            

    def goi(self, id):
        ep = f"050000025908{id}100520012acc0408{id}12024d451801200332b60308{id}121f5b4646303046465d5b425d5b435d626f54205b4646454142395d7e2041706b1a024d4520c5c6b8d00628643087cbd13038324205d2afe96000480150ca02589f8d066082d8d0ad03708080027a06eae5cab003009201009801c302a001ba01e80101aa020a080110e43218807d2003aa020a080f10e43218807d2003aa0209082510f02e18002003b00203c2021d12021a001a060848120202001a0508501201631a060851120265662200d00203d802a5a38daf03ea0204100118018a0302080192030098039bb99fc50ba20303657370e20300ea0300f20300fa030908d1afe96010351807fa03090892b4a66110351807fa030908d1b8e36110351807fa030908d6d3d16410351807fa030908d7d3d16410351807fa03090888e18866103518078004649004029a040a08c5c6b8d00620014001a00465aa040408011001aa040408011003aa0404080f1a00ba0400ca0406080110808002da041408{id}10081a0020c05728c05730c09a0cf0040afa0405080310f602fa04050804108103fa04050805109f01fa0405081d10c801fa040408161059fa0405080e109001fa0402081580050a9005e9073a004001500260016801721e313737393331313432393837343632343235325f7538303535723965376e880180e0b3e394e6aac61ca20100b001c902ea010449444332fa011e313737393331313432393837343632363532315f7877776a7478693669388a021e313737393331313432393837343632383235345f30386e68663076707961"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))                        
            
    def q5(self, id):
        ep = f"050000012808{id}1005203a2a9b0208{id}12024d451801200432a10108{id}12165b464630304530d98e5d5a495820414e44204d45524f1a024d4520d78aa5b40628023086cbd1303832420880c38566fa96e660480150c90158e8079201009801c901c00101e80101880203920200aa0205082910e432c2020c12021a001a04084812002200ea0204100118018a03009203009803b7919db30ba20319c2b27854e19687e197a95fe191ade192aae197a95945e19687e20301523a00403e50056801721e313732303237323231313638373535353930315f736f3278687a61366e347801820103303b30880180e0aecdacceba8e19a20100b00114ea010449444332fa011e313732303237323231313638373535383330335f71356f79736b3934716d"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))
            
    def spy_room(self, id):
        ep = f"0e1500000050d6d519002bdcc64de8a42c1aaedf5c3aaacf7ce694efbfc1f11f026809b625e793614dd13ffa38eecc554ff320a61b8ac69699a8eb5edab73b39e9d9107a50d5e083a2bc8c01fbad64dbce6b8581cd50"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))            
            

    def q6(self, id):
        ep = f"050000019008{id}100520082a830308dbdcd7cb251afa0208{id}12024d451801200532870208{id}12105b4646303030305d5a4958264d45524f1a024d4520ebdd88b90628363087cbd1303832420880c38566949be061480150d60158991468b7db8dae037a0082011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010220229801db01a0014fc00101d001ada48aaf03e80101880203920200aa0205082910e432c2021a12021a001a100851120265661a08086620822d289e0522021200d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a00403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))
            
    def dm(self, id):
        ep = f"080000001708{id}100820022a0b089f8d06109f8d0618c801"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))
            


    def y10(self, id):
        ep = f"12000000F308{id}101220022ae60108{id}10{id}2883bbbcc40642247b225469746c654944223a3930343939303037322c2274797065223a225469746c65227d4a520a13e29dbc2ecfbb2ee29dbce385a4524544464f5810edb58fae0318b1b1d2ad0320c10228c3b7f8b10338024214e3808e4164e3808fc39fc581c398c48ccca3c6986a00720c08{id}10011a0210155202656e6a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3131393337333137393632373538352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.s12:
            self.s12.send(bytes.fromhex(ep))

    def y9(self, id):
        ep = f"12000000d208{id}101220022ac50108{id}10{id}2883bbbcc40642247b225469746c654944223a3930343939303037312c2274797065223a225469746c65227d4a310a037a697810edb58fae0318b1b1d2ad0320c10228c3b7f8b103380242037a69786a00720c08{id}10011a0210155202656e6a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3131393337333137393632373538352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.s12:
            self.s12.send(bytes.fromhex(ep))

    def y8(self, id):
        ep = f"12000000d208{id}101220022ac50108{id}10{id}2883bbbcc40642247b225469746c654944223a3930343939303037302c2274797065223a225469746c65227d4a310a037a697810edb58fae0318b1b1d2ad0320c10228c3b7f8b103380242037a69786a00720c08{id}10011a0210155202656e6a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3131393337333137393632373538352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.s12:
            self.s12.send(bytes.fromhex(ep))

    def y7(self, id):
        ep = f"12000000F308{id}101220022AE60108{id}10{id}2883BBBCC40642247B225469746C654944223A3930343039303032372C2274797065223A225469746C65227D4A520A13E29DBC2ECFBB2EE29DBCE385A4524544464F5810EDB58FAE0318B1B1D2AD0320C10228C3B7F8B10338024214E3808E4164E3808FC39FC581C398C48CCCA3C6986A00720C08{id}10011A0210155202656E6A520A4C68747470733A2F2F67726170682E66616365626F6F6B2E636F6D2F76392E302F3131393337333137393632373538352F706963747572653F77696474683D313630266865696768743D313630100118017200"
        if self.s12:
            self.s12.send(bytes.fromhex(ep))

    def y6(self, id):
        ep = f"12000000F308{id}101220022AE60108{id}10{id}2883BBBCC40642247B225469746C654944223A3930343039303032362C2274797065223A225469746C65227D4A520A13E29DBC2ECFBB2EE29DBCE385A4524544464F5810EDB58FAE0318B1B1D2AD0320C10228C3B7F8B10338024214E3808E4164E3808FC39FC581C398C48CCCA3C6986A00720C08{id}10011A0210155202656E6A520A4C68747470733A2F2F67726170682E66616365626F6F6B2E636F6D2F76392E302F3131393337333137393632373538352F706963747572653F77696474683D313630266865696768743D313630100118017200"
        if self.s12:
            self.s12.send(bytes.fromhex(ep))

    def st(self, id):
        ep = f"120000009708{id}101220022a8a0108{id}10{id}28a0acb4d00642337b22537469636b6572537472223a225b313d313230303030303030312d31395d222c2274797065223a22537469636b6572227d4a350a19d985d98ad8b1d988e385a4d8a8db92d980d984d8a7d8b1d8a920b40228f194f6b1036a00720d08{id}10011a030910155202656e6a04100118017200"
        if self.s12:
            self.s12.send(bytes.fromhex(ep))

    def xp(self, id):
        ep = f"0e0000020d08{id}100e20172a800408abb3e42412ea030881e1f6921c1081e1f6921c1ae4025b625d5b635d5b4646303030305d5a6978265b3030666630305d4d65526f2653746576650a2020202020202020202020200a5b435d5b425d5b4646464630305d446f6e4520537461725420426f5420466f6c6c6f77204d652034204e65772054470a0a5b4646303030305d204d65526f0a20203d3e200a5b3030464630305d74656c656772616d203a2020406d65726f7076700a5b3030464630305d696e7374616772616d203a206d65726f2e616e746962616e0a0a5b4646303035305d7a6958206f6666696369616c0a20203d3e200a74656c656772616d203a20204058695a59454c466c0a696e7374616772616d203a20745f715f685f690a0a5b4646303037305d2053746556650a20203d3e200a5b3030464630305d74656c656772616d203a202040535445564531313534320a5b3030464630305d696e7374616772616d203a2067706c782e616e746962616e310a0a5b3030304646465d426f54204534303428b2dd8dae03300138d4d8d0ad034a0050bee8fbfd02580160ca0268dd1f70be02784d800182c0b5c187eca3c61cb2010410011801ba0100c201024d45ca0100d20100da0100e00168ea0100fa010e08ffdacddf1810011a0030f9b80182020208159802aa0ca00201ca0204e024a218d0029fdaf1eb041801200f280330e3c2c1be213801"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))
            
    def pc(self, id):
        ep = f"05000003b608{id}100520062aa90708d3858dd22312024d451801200332a50408d3858dd22312125b6666303030305d626f54207e2041706b201a024d4520a6e38baa0628443087cbd1303832420de0f38766e796a3618a94e66000480150ce01588e0c60f5d7d0ad0368c2dc8dae037a0082012b08b3daf1eb0412115b6666303030305d626f54207e2041706b180620b687d4f0042a0808c49d85f30410038801ed89c5b003920104020020239801cd01a00111a80185fff5b103c00101c80101d001bace89af03e80101880203920203c20500aa020a080110c03e18f0602002aa0205080210b232aa0205080310e432aa020a080f10918a0118a09c01aa0205081710e750aa0205081810b768aa0205081a10da74aa0206081b10918a01aa0206081c10958c01aa02050820108b79aa0205082110eb7aaa0205082210a275aa0206082310dc8701aa0205082b10f476aa0205083110f476aa0206083910918a01aa0206083d10918a01aa0206084110918a01aa0205084910e432aa0205084d10e432aa0206083410918a01aa0205082810e432aa0205082910e432c2021a12021a001a04084812001a0508501201631a0508511201652200ea02520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3237373631373532363237343633352f706963747572653f77696474683d313630266865696768743d31363010011801f202090887cab5ee0110870a8a030808021003180528019203009803f3e78ea30ba203115b6666303030305d626f54207e2041706b32af0208{id}12115b6666303030305d626f54207e2041706b1a024d452096ed8baa0628043089cbd13038324200480150c90158e8079201009801c901c00101c80101e80101880204920200aa0208080110ff34188064aa020b080f10fd3218b086012001aa0205080210e432aa0205081810fd32aa0205081a10fd32aa0205081c10fd32aa0205082010fd32aa0205082210fd32aa0205082110fd32aa0205081710e432aa0205082310fd32aa0205082b10fd32aa0205083110fd32aa0205083910fd32aa0205083d10fd32aa0205084110fd32aa0205084910d836aa0205084d10e432aa0205081b10fd32aa0205083410fd32aa0205082810e432aa0205082910e432c2021a12021a001a04084812001a0508501201631a0508511201652200ea0204100118018a03009203003a00400150016801721e313639383838363035353130343733333939355f6a67386c37333431646688018090aefec3978fef17a20100b001e001ea010449444331"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))       

    def d1(self):
        ep = f"060000005c08d4d7faba1d100620022a5008ece39cf1081a155b4646303030305d5b635d5b625d784d65526f000032024d454064b00101b801e807d801d4d8d0ad03e001b2dd8dae03ea01084534303420424f548002fd98a8dd03900201d00201"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))  

    def d2(self):
        ep = f"060000005c08d4d7faba1d100620022a5008c2cfd6d9071a155b4646303030305d5b635d5b625d5354455645000032024d454064b00101b801e807d801d4d8d0ad03e001b2dd8dae03ea01084534303420424f548002fd98a8dd03900201d00201"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))   

    def d3(self):
        ep = f"060000005a08d4d7faba1d100620022a4e08c8f0dacb081a135b4646303030305d5b635d5b625d5a4958000032024d454064b00101b801e807d801d4d8d0ad03e001b2dd8dae03ea01084534303420424f548002fd98a8dd03900201d00201"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))     

    def skin1(self, id):
        ent_packet = f"050000025808{id}100520542acb0408a5f1a5c90310{id}1abc0408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042108a5f1a5c903121484a5d164bf9ce061b5c38566839aa361f780e96018b3cbd130f00407fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
            
    def skin2(self, id):
        ent_packet = f"050000025c08{id}100520542acf0408a5f1a5c90310{id}1ac00408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c90312188cf6d064cf85d164bf9ce061b5c385669abfa5619dcae86018b3cbd130f00406fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
    def skin3(self, id):
        ent_packet = f"050000025c08{id}100520542acf0408a5f1a5c90310{id}1ac00408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c9031218b5c38566d0fda561c8e1e860d7bace64c9ded064929be06118b3cbd130f00408fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")

    def skin4(self, id):
        ent_packet = f"050000025a08{id}100520502acd0408a5f1a5c90310{id}1abe0408{id}120b2b2b2b2b464f582b2b2b2b1a024d452099d98dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb876650ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a0899d98dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c9031218929be061b5c38566d0fda561e0e1e860899dd1648bf6d06418b3cbd130f00409fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")   
            
    def skin5(self, id):
        ent_packet = f"050000022e08{id}100520502aa10408{id}10{id}1a920408{id}120c75776a736a736a736e646a641a024d4520c6befec40628023087cbd13038324218c09ae06180a89763c091e660c0b5ce6480c385668096a361480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a03020801920300ea0300f203008004649004029a040a08b6befec40620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508{id}1218b597a361909ce660c0b5ce6480a89763929be061b5c3856618b3cbd130f00408fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa04020815"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
                                          
    def skin6(self, id):
        ent_packet = f"050000025c08{id}100520542acf0408a5f1a5c90310{id}1ac00408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c9031218b5c38566d0fda561c8e1e860d0b5ce64c9ded064929be06118b3cbd130f00408fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
    def skin7(self, id):
        ent_packet = f"050000023708{id}100520502aaa0408{id}10{id}1a9b0408{id}120c75776a736a736a736e646a641a024d4520a0c0fec40628023087cbd13038324218c09ae06180a89763c091e660c0b5ce6480c385668096a361480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a03020801920300e203024f52ea0300f203008004649004029a040a08a0c0fec40620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042908{id}121c909ce660c0b5ce6480a89763929be061b5c38566ddd9e860b597a36118b3cbd130f00407fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa04020815"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")

    def zix_dens17(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}109184bbb1032a0c08{id}189184bbb10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
                        
    def zix_dens16(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}109afbb8b1032a0c08{id}189afbb8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
    def zix_dens15(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10e193bbb1032a0c08{id}18e193bbb10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")


    def zix_dens14(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}108bfbb8b1032a0c08{id}188bfbb8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
            
    def zix_dens13(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}1095fbb8b1032a0c08{id}1895fbb8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
    def zix_dens12(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d9fab8b1032a0c08{id}18d9fab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")

    def zix_dens11(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d5fab8b1032a0c08{id}18d5fab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")   
            
    def zix_dens10(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d0fab8b1032a0c08{id}18d0fab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
                                          
    def zix_dens9(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10f4fab8b1032a0c08{id}18f4fab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
    def zix_dens8(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10fffab8b1032a0c08{id}18fffab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")  
            
    def zix_dens1(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10f0fab8b1032a0c08{id}18f0fab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
            
    def zix_dens2(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d4fab8b1032a0c08{id}18d4fab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
    def zix_dens3(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10cbfab8b1032a0c08{id}18cbfab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")

    def zix_dens4(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10cefab8b1032a0c08{id}18cefab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")   
            
    def zix_dens5(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10ccfab8b1032a0c08{id}18ccfab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
                                          
    def zix_dens6(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10c6fab8b1032a0c08{id}18c6fab8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
            
    def zix_dens7(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}1091fbb8b1032a0c08{id}1891fbb8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")  

    def zix_dens18(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}109afbb8b1032a0c08{id}189afbb8b10330b7d7bc8206"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")


    def gt(self, id):
        ep = f"05000002e008{id}1005203f2ad30508{id}12024d4518012003328d0408{id}1210d8a7d984d8b3d8a7d8add8b1324c324d1a024d4520e4a3becc0628023087cbd1303832421880c3856680a89763c09ae061c0b5ce648096a361c091e660480150ad0258e80792010a0107090a0b12191a20279801ad02c00101e80101880208920208c205b622ba10da16aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a030208019203009803d38ffdc10ba2030b77776164616d68616a6a69e203034f5219ea0300f203008004649004029a040a08e4a3becc0620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}f0040afa04050803108703fa04050804108103fa0405080510c001fa0405081d10cc01fa040408161073fa0405080e10af01fa0402081580050b9005e9073a0101400150016801721e313737313031363637363837343838333631325f7a6b6f6d64736b753264880180a0f79289a7c4881ca20100b001c902ea010449444331f2012e08{id}10d0b8d0a5301a0e5a49587e424f542d56392de280a228daa3becc06302b380b4204100118014801fa011e313737313031363637363837343838363232325f663539756b6978696a318a021e313737313031363637363837343838383430325f75737a6474316c79666b"
        if self.s5:
            self.s5.send(bytes.fromhex(ep))

    def ghostx(self, id):
        ent_packet = f"05000002bf08{id}1005203f2ab20508{id}12024d451801200332ec0308{id}120f5b3030464646465d424f542041504b1a024d4520e4a3becc0628023087cbd1303832421880c3856680a89763c09ae061c0b5ce648096a361c091e660480150ad0258e80792010202009801ad02c00101e80101880208920200aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2021d12021a001a060848120202001a0508501201631a060851120265662200ea0204100118018a030208019203009803d38ffdc10ba2030b77776164616d68616a6a69e20300ea0300f203008004649004029a040a08e4a3becc0620014001a00465aa040408011001aa040408011003aa0404080f1a00ba0400ca0400da040608{id}f0040afa04050803108703fa04050804108103fa0405080510c001fa0405081d10cc01fa040408161073fa0405080e10af01fa0402081580050b9005e9073a00400150016801721e313737313031363637363837343838333631325f7a6b6f6d64736b753264880180a0f79289a7c4881ca20100b001c902ea010449444331f2012f08{id}10d0b8d0a5301a0f5b4646303030305d626f747e61706b28daa3becc06302b380b4204100118014801fa011e313737313031363637363837343838363232325f663539756b6978696a318a021e313737313031363637363837343838383430325f75737a6474316c79666b"
        if self.s5:
            self.s5.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] s5 not assigned.")
   
    def send_lag_loop(self, packet, remote, user_id):
        start_time = time.time()
        duration = 60
        sent_count = 0
        
        start_msg = """[00FF00]يجب عليك ضغط على زر الاستعداد او الغاء في الفريق بدا تعليق الفريق
        
ملاحظة يجب عليك ان تكون عضو ليس قائد للفريق[00FF00]"""
        threading.Thread(target=self.sH, args=(user_id, start_msg)).start()
        
        try:
            while time.time() - start_time < duration:
                try:
                    remote.send(packet)
                    sent_count += 1
                    time.sleep(0.001)
                except Exception as e:
                    break
            
            elapsed = time.time() - start_time
            finish_msg = f"[00FF00]تم التعليق الفريق بنجاح تم إرسال {sent_count} حزمة في {elapsed:.1f} ثانية[00FF00]"
            threading.Thread(target=self.sH, args=(user_id, finish_msg)).start()
            
        finally:
            with self.lag_lock:
                self.lag_active = False

    def hC(self, conn):
        ver, n_m = conn.recv(2)
        mths = self.gA(n_m, conn)
        if 2 not in set(mths):
            conn.close()
            return
        conn.sendall(bytes([V, 2]))
        if not self.vC(conn):
            return
        ver, cmd, _, a_t = conn.recv(4)
        if a_t == 1:
            addr = socket.inet_ntoa(conn.recv(4))
        elif a_t == 3:
            d_len = conn.recv(1)[0]
            addr = conn.recv(d_len)
            addr = socket.gethostbyname(addr)
        port = int.from_bytes(conn.recv(2), 'big', signed=False)
        try:
            if cmd == 1:
                rem = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                rem.connect((addr, port))
                b_a = rem.getsockname()
            else:
                conn.close()
                return
            ad = int.from_bytes(socket.inet_aton(b_a[0]), 'big', signed=False)
            port = b_a[1]
            rep = b''.join([
                V.to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(1).to_bytes(1, 'big'),
                ad.to_bytes(4, 'big'),
                port.to_bytes(2, 'big')
            ])
        except Exception as e:
            rep = self.h(a_t, 5)
        conn.sendall(rep)
        if rep[1] == 0 and cmd == 1:
            self.eL(conn, rem)
        conn.close()

    def eL(self, cl, rem):
        global inviteD
        while True:
            r, w, e = select.select([cl, rem], [], [])

            if cl in r:
                dC = cl.recv(4096)

                if '0515' in dC.hex()[0:4] and len(dC.hex()) == 44:
                    with self.lag_lock:
                        self.lag_0515_packet = dC
                        self.lag_remote = rem

                if '0515' in dC.hex()[0:4] and len(dC.hex()) < 50:
                    self.p2 = dC
                    self.rt = rem
                    
                if '0515' in dC.hex()[0:4] and len(dC.hex()) >= 141:
                    self.p1 = dC
                    self.rt = rem

                if "39699" in str(rem):
                    self.op = dC
                if "39801" in str(rem):
                    self.xz = rem

                if '0515' in dC.hex()[0:4] and len(dC.hex()) >= 820 and inviteD == True:
                    for i in range(10):
                        for _ in range(15):
                            rem.send(dC)
                            time.sleep(0.04)
                            time.sleep(0.2)

                if rem.send(dC) <= 0:
                    break
            if rem in r:
                dt = rem.recv(4096)    
                
                if '0500' in dt.hex()[:4]:
                    self.s5 = cl
                if '1200' in dt.hex()[:4]:
                    self.s12 = cl
                    

                if dt.hex().startswith("0500000") and len(dt) >= 600:
                    id = dt.hex()[12:22]
                    c_m = "[C][B][FF0000]WelcomE To BoT\n To See Cmd /help"
                    threading.Thread(target=self.st, args=(id,)).start()         

                    
                if '1200' in dt.hex()[0:4] and b'/6s' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.q6, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE ChangE sQ To 6\n\n اذهب افتح تجنيد"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()   

                if '1200' in dt.hex()[0:4] and b'/5s' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.q5, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE ChangE sQ To 5\n\n اذهب افتح تجنيد"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()

                if '1200' in dt.hex()[0:4] and b'/ghost' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.ghostx, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE Ghost"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:4] and b'/spyrom' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.spy_room, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE ChangE spy To room"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()                    
                    
                if '1200' in dt.hex()[0:4] and b'/3s' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.s3, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE ChangE sQ To 3\n\n اذهب افتح تجنيد"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()

                if '1200' in dt.hex()[0:4] and b'/gt' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.gt, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE GhOSt"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()                                        
                                                                                
                if '1200' in dt.hex()[0:4] and b'/pc' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.pc, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE pC"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()                    

                if '1200' in dt.hex()[0:4] and b'/dm' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.dm, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT Diamond"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()

                if '1200' in dt.hex()[0:4] and b'/gd' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.gd, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT Gold"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()

                if '1200' in dt.hex()[0:4] and b'/lag' in dt:
                    try:
                        id = dt.hex()[12:22]
                        
                        with self.lag_lock:
                            if self.lag_0515_packet is not None and self.lag_remote is not None and not self.lag_active:
                                self.lag_active = True
                                captured_packet = self.lag_0515_packet
                                target_remote = self.lag_remote
                                threading.Thread(target=self.send_lag_loop, args=(captured_packet, target_remote, id)).start()
                            elif self.lag_active:
                                stop_msg = "[FFA500]الامر قيد تشغيل[FFA500]"
                                threading.Thread(target=self.sH, args=(id, stop_msg)).start()
                            else:
                                error_msg = "[FF0000]يجب الدخول لفريق أولاً قبل استخدام هذا الأمر[FF0000]"
                                threading.Thread(target=self.sH, args=(id, error_msg)).start()
                            
                    except Exception as e:
                        pass


                if '1200' in dt.hex()[0:6] and b'/stop' in dt:
                    try:
                        id = dt.hex()[12:22]
                        
                        with self.lag_lock:
                            if self.lag_0515_packet is not None and self.lag_remote is not None and not self.lag_active:
                                self.lag_active = True
                                captured_packet = self.lag_0515_packet
                                target_remote = self.lag_remote
                                threading.Thread(target=self.send_lag_loop, args=(captured_packet, target_remote, id)).start()
                            elif self.lag_active:
                                stop_msg = "[FFA500]SPY..."
                                threading.Thread(target=self.sH, args=(id, stop_msg)).start()
                            else:
                                error_msg = "[FF0000]يجب الدخول لفريق أولاً قبل استخدام هذا الأمر[FF0000]"
                                threading.Thread(target=self.sH, args=(id, error_msg)).start()
                            
                    except Exception as e:
                        pass


                if '1200' in dt.hex()[0:5] and b'/y10' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.y10, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT 10y"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:5] and b'/spy' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.spy, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT spy"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()                    
                    
                    
                if '1200' in dt.hex()[0:5] and b'/y9' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.y9, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT 9y"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()                    

                if '1200' in dt.hex()[0:5] and b'/proxy' in dt:
                    try:
                        items_ids = ['a796e660', 'a896e660', 'a996e660', 'aa96e660', 'ab96e660', 'ac96e660', 'ad96e660', 'ae96e660', 'af96e660', 'b096e660', 'b196e660', 'b296e660', 'b396e660', 'b496e660', 'b596e660', 'b696e660', 'b796e660', 'b896e660', 'b996e660', 'ba96e660', 'bb96e660', 'bc96e660', 'bd96e660', 'be96e660', 'bf96e660', 'c096e660', 'c196e660', 'c296e660', 'c396e660', 'c496e660', 'c596e660', 'c696e660', 'c796e660', 'c896e660', 'c996e660', 'ca96e660', 'cb96e660', 'cc96e660', 'cd96e660', 'ce96e660', 'cf96e660', 'd096e660', 'd196e660', 'd296e660', 'd396e660', 'd496e660', 'd596e660', 'd696e660', 'd796e660', 'd896e660', 'd996e660', 'da96e660', 'db96e660', 'dc96e660', 'dd96e660', 'de96e660', 'df96e660', 'e096e660', 'e196e660', 'e296e660', 'e396e660', 'e496e660', 'e596e660', 'e696e660', 'e796e660', 'e896e660', 'e996e660', 'ea96e660', 'eb96e660', 'ec96e660', 'ed96e660', 'ee96e660', 'ef96e660', 'f096e660', 'f196e660', 'f296e660', 'f396e660', 'f496e660', 'f596e660', 'f696e660', 'f796e660', 'f896e660', 'f996e660', 'fa96e660', 'fb96e660', 'fc96e660', 'fd96e660', 'fe96e660', 'ff96e660', '8097e660', '8197e660', '8297e660', '8397e660', '8497e660', '8597e660', '8697e660', '8797e660', '8897e660', '8997e660', '8a97e660', '8b97e660', '8c97e660', '8d97e660', '8e97e660', '8f97e660', '9097e660', '9197e660', '9297e660', '9397e660', '9497e660', '9597e660', '9697e660', '9797e660', '9897e660', '9997e660', '9a97e660', '9b97e660', '9c97e660', '9d97e660', '9e97e660', '9f97e660', 'a097e660', 'a197e660', 'a297e660', 'a397e660', 'a497e660', 'a597e660', 'a697e660', 'a797e660', 'a897e660', 'a997e660', 'aa97e660', 'ab97e660', 'ac97e660', 'ad97e660', 'ae97e660', 'af97e660', 'b097e660', 'b197e660', 'b297e660', 'b397e660', 'b497e660', 'b597e660', 'b697e660', 'b797e660', 'b897e660', 'b997e660', 'ba97e660', 'bb97e660', 'bc97e660', 'bd97e660', 'be97e660', 'bf97e660', 'c097e660', 'c197e660', 'c297e660', 'c397e660', 'c497e660', 'c597e660', 'c697e660', 'c797e660', 'c897e660', 'c997e660', 'ca97e660', 'cb97e660', 'cc97e660', 'cd97e660', 'ce97e660', 'cf97e660', 'd097e660', 'd197e660', 'd297e660', 'd397e660', 'd497e660', 'd597e660', 'd697e660', 'd797e660', 'd897e660', 'd997e660', 'da97e660', 'db97e660', 'dc97e660', 'dd97e660', 'de97e660', 'df97e660', 'e097e660', 'e197e660', 'e297e660', 'e397e660', 'e497e660', 'e597e660', 'e697e660', 'e797e660', 'e897e660', 'e997e660', 'ea97e660', 'eb97e660', 'ec97e660', 'ed97e660', 'ee97e660', 'ef97e660', 'f097e660', 'f197e660', 'f297e660', 'f397e660', 'f497e660', 'f597e660', 'f697e660', 'f797e660', 'f897e660', 'f997e660', 'fa97e660', 'fb97e660', 'fc97e660', 'fd97e660', 'fe97e660', 'ff97e660', '8098e660', '8198e660', '8298e660', '8398e660', '8498e660', '8598e660', '8698e660', '8798e660', '8898e660', '8998e660', '8a98e660', '8b98e660', '8c98e660', '8d98e660', '8e98e660', '8f98e660', '9098e660', '9198e660', '9298e660', '9398e660', '9498e660', '9598e660', '9698e660', '9798e660', '9898e660', '9998e660', '9a98e660', '9b98e660', '9c98e660', '9d98e660', '9e98e660', '9f98e660', 'a098e660', 'a198e660', 'a298e660', 'a398e660', 'a498e660', 'a598e660', 'a698e660', 'a798e660', 'a898e660', 'a998e660', 'aa98e660', 'ab98e660', 'ac98e660', 'ad98e660', 'ae98e660', 'af98e660', 'b098e660', 'b198e660', 'b298e660', 'b398e660', 'b498e660', 'b598e660', 'b698e660', 'b798e660', 'b898e660', 'b998e660', 'ba98e660', 'bb98e660', 'bc98e660', 'bd98e660', 'be98e660', 'bf98e660', 'c098e660', 'c198e660', 'c298e660', 'c398e660', 'c498e660', 'c598e660', 'c698e660', 'c798e660', 'c898e660', 'c998e660', 'ca98e660', 'cb98e660', 'cc98e660', 'cd98e660', 'ce98e660', 'cf98e660', 'd098e660', 'd198e660', 'd298e660', 'd398e660', 'd498e660', 'd598e660', 'd698e660', 'd798e660', 'd898e660', 'd998e660', 'da98e660', 'db98e660', 'dc98e660', 'dd98e660', 'de98e660', 'df98e660', 'e098e660', 'e198e660', 'e298e660', 'e398e660', 'e498e660', 'e598e660', 'e698e660', 'e798e660', 'e898e660', 'e998e660', 'ea98e660', 'eb98e660', 'ec98e660', 'ed98e660', 'ee98e660', 'ef98e660', 'f098e660', 'f198e660', 'f298e660', 'f398e660', 'f498e660', 'f598e660', 'f698e660', 'f798e660', 'f898e660', 'f998e660', 'fa98e660', 'fb98e660', 'fc98e660', 'fd98e660', 'fe98e660', 'ff98e660', '8099e660', '8199e660', '8299e660', '8399e660', '8499e660', '8599e660', '8699e660', '8799e660', '8899e660', '8999e660', '8a99e660', '8b99e660', '8c99e660', '8d99e660', '8e99e660', '8f99e660', '9099e660', '9199e660', '9299e660', '9399e660', '9499e660', '9599e660', '9699e660', '9799e660', '9899e660', '9999e660', '9a99e660', '9b99e660', '9c99e660', '9d99e660', '9e99e660', '9f99e660', 'a099e660', 'a199e660', 'a299e660', 'a399e660', 'a499e660', 'a599e660', 'a699e660', 'a799e660', 'a899e660', 'a999e660', 'aa99e660', 'ab99e660', 'ac99e660', 'ad99e660', 'ae99e660', 'af99e660', 'b099e660', 'b199e660', 'b299e660', 'b399e660', 'b499e660', 'b599e660', 'b699e660', 'b799e660', 'b899e660', 'b999e660', 'ba99e660', 'bb99e660', 'bc99e660', 'bd99e660', 'be99e660', 'bf99e660', 'c099e660', 'c199e660', 'c299e660', 'c399e660', 'c499e660', 'c599e660', 'c699e660', 'c799e660', 'c899e660', 'c999e660', 'ca99e660', 'cb99e660', 'cc99e660', 'cd99e660', 'ce99e660', 'cf99e660', 'd099e660', 'd199e660', 'd299e660', 'd399e660', 'd499e660', 'd599e660', 'd699e660', 'd799e660', 'd899e660', 'd999e660', 'da99e660', 'db99e660', 'dc99e660', 'dd99e660', 'de99e660', 'df99e660', 'e099e660', 'e199e660', 'e299e660', 'e399e660', 'e499e660', 'e599e660', 'e699e660', 'e799e660', 'e899e660', 'e999e660', 'ea99e660', 'eb99e660', 'ec99e660', 'ed99e660', 'ee99e660', 'ef99e660', 'f099e660', 'f199e660', 'f299e660', 'f399e660', 'f499e660', 'f599e660', 'f699e660', 'f799e660', 'f899e660', 'f999e660', 'fa99e660', 'fb99e660', 'fc99e660', 'fd99e660', 'fe99e660', 'ff99e660', '809ae660', '819ae660', '829ae660', '839ae660', '849ae660', '859ae660', '869ae660', '879ae660', '889ae660', '899ae660', '8a9ae660', '8b9ae660', '8c9ae660', '8d9ae660', '8e9ae660', '8f9ae660', '909ae660', '919ae660', '929ae660', '939ae660', '949ae660', '959ae660', '969ae660', '979ae660', '989ae660', '999ae660', '9a9ae660', '9b9ae660', '9c9ae660', '9d9ae660', '9e9ae660', '9f9ae660', 'a09ae660', 'a19ae660', 'a29ae660', 'a39ae660', 'a49ae660', 'a59ae660', 'a69ae660', 'a79ae660', 'a89ae660', 'a99ae660', 'aa9ae660', 'ab9ae660', 'ac9ae660', 'ad9ae660', 'ae9ae660', 'af9ae660', 'b09ae660', 'b19ae660', 'b29ae660', 'b39ae660', 'b49ae660', 'b59ae660', 'b69ae660', 'b79ae660', 'b89ae660', 'b99ae660', 'ba9ae660', 'bb9ae660', 'bc9ae660', 'bd9ae660', 'be9ae660', 'bf9ae660', 'c09ae660', 'c19ae660', 'c29ae660', 'c39ae660', 'c49ae660', 'c59ae660', 'c69ae660', 'c79ae660', 'c89ae660', 'c99ae660', 'ca9ae660', 'cb9ae660', 'cc9ae660', 'cd9ae660', 'ce9ae660', 'cf9ae660', 'd09ae660', 'd19ae660', 'd29ae660', 'd39ae660', 'd49ae660', 'd59ae660', 'd69ae660', 'd79ae660', 'd89ae660', 'd99ae660', 'da9ae660', 'db9ae660', 'dc9ae660', 'dd9ae660', 'de9ae660', 'df9ae660', 'e09ae660', 'e19ae660', 'e29ae660', 'e39ae660', 'e49ae660', 'e59ae660', 'e69ae660', 'e79ae660', 'e89ae660', 'e99ae660', 'ea9ae660', 'eb9ae660', 'ec9ae660', 'ed9ae660', 'ee9ae660', 'ef9ae660', 'f09ae660', 'f19ae660', 'f29ae660', 'f39ae660', 'f49ae660', 'f59ae660', 'f69ae660', 'f79ae660', 'f89ae660', 'f99ae660', 'fa9ae660', 'fb9ae660', 'fc9ae660', 'fd9ae660', 'fe9ae660', 'ff9ae660', '809be660', '819be660', '829be660', '839be660', '849be660', '859be660', '869be660', '879be660', '889be660', '899be660', '8a9be660', '8b9be660', '8c9be660', '8d9be660', '8e9be660', '8f9be660', '909be660', '919be660', '929be660', '939be660', '949be660', '959be660', '969be660', '979be660', '989be660', '999be660', '9a9be660', '9b9be660', '9c9be660', '9d9be660', '9e9be660', '9f9be660', 'a09be660', 'a19be660', 'a29be660', 'a39be660', 'a49be660', 'a59be660', 'a69be660', 'a79be660', 'a89be660', 'a99be660', 'aa9be660', 'ab9be660', 'ac9be660', 'ad9be660', 'ae9be660', 'af9be660', 'b09be660', 'b19be660', 'b29be660', 'b39be660', 'b49be660', 'b59be660', 'b69be660', 'b79be660', 'b89be660', 'b99be660', 'ba9be660', 'bb9be660', 'bc9be660', 'bd9be660', 'be9be660', 'bf9be660', 'c09be660', 'c19be660', 'c29be660', 'c39be660', 'c49be660', 'c59be660', 'c69be660', 'c79be660', 'c89be660', 'c99be660', 'ca9be660', 'cb9be660', 'cc9be660', 'cd9be660', 'ce9be660', 'cf9be660', 'd09be660', 'd19be660', 'd29be660', 'd39be660',"c19ae061", "c29ae061", "c39ae061", "c49ae061", "c59ae061", "c69ae061", "c79ae061", "c89ae061", "c99ae061", "ca9ae061", "cb9ae061", "cc9ae061", "cd9ae061", "ce9ae061", "cf9ae061",
    "d09ae061", "d19ae061", "d29ae061", "d39ae061", "d49ae061", "d59ae061", "d69ae061", "d79ae061", "d89ae061", "d99ae061", "da9ae061", "db9ae061", "dc9ae061", "dd9ae061", "de9ae061", "df9ae061",
    "e09ae061", "e19ae061", "e29ae061", "e39ae061", "e49ae061", "e59ae061", "e69ae061", "e79ae061", "e89ae061", "e99ae061", "ea9ae061", "eb9ae061", "ec9ae061", "ed9ae061", "ee9ae061", "ef9ae061",
    "f09ae061", "f19ae061", "f29ae061", "f39ae061", "f49ae061", "f59ae061", "f69ae061", "f79ae061", "f89ae061", "f99ae061", "fa9ae061", "fb9ae061", "fc9ae061", "fd9ae061", "fe9ae061", "ff9ae061",
    "809be061", "819be061", "829be061", "839be061", "849be061", "859be061", "869be061", "879be061", "889be061", "899be061", "8a9be061", "8b9be061", "8c9be061", "8d9be061", "8e9be061", "8f9be061",
    "909be061", "919be061", "929be061", "939be061", "949be061", "959be061", "969be061", "979be061", "989be061", "999be061", "9a9be061", "9b9be061", "9c9be061", "9d9be061", "9e9be061", "9f9be061",
    "a09be061", "a19be061", "a29be061", "a39be061", "a49be061", "a59be061", "a69be061", "a79be061", "a89be061", "a99be061", "aa9be061", "ab9be061", "ac9be061", "ad9be061", "ae9be061", "af9be061",
    "b09be061", "b19be061", "b29be061", "b39be061", "b49be061", "b59be061", "b69be061", "b79be061", "b89be061", "b99be061", "ba9be061", "bb9be061", "bc9be061", "bd9be061", "be9be061", "bf9be061",
    "c09be061", "c19be061", "c29be061", "c39be061", "c49be061", "c59be061", "c69be061", "c79be061", "c89be061", "c99be061", "ca9be061", "cb9be061", "cc9be061", "cd9be061", "ce9be061", "cf9be061",
    "d09be061", "d19be061", "d29be061", "d39be061", "d49be061", "d59be061", "d69be061", "d79be061", "d89be061", "d99be061", "da9be061", "db9be061", "dc9be061", "dd9be061", "de9be061", "df9be061",
    "e09be061", "e19be061", "e29be061", "e39be061", "e49be061", "e59be061", "e69be061", "e79be061", "e89be061", "e99be061", "ea9be061", "eb9be061", "ec9be061", "ed9be061", "ee9be061", "ef9be061",
    "f09be061", "f19be061", "f29be061", "f39be061", "f49be061", "f59be061", "f69be061", "f79be061", "f89be061", "f99be061", "fa9be061", "fb9be061", "fc9be061", "fd9be061", "fe9be061", "ff9be061",
    "809ce061", "819ce061", "829ce061", "839ce061", "849ce061", "859ce061", "869ce061", "879ce061", "889ce061", "899ce061", "8a9ce061", "8b9ce061", "8c9ce061", "8d9ce061", "8e9ce061", "8f9ce061",
    "909ce061", "919ce061", "929ce061", "939ce061", "949ce061", "959ce061", "969ce061", "979ce061", "989ce061", "999ce061", "9a9ce061", "9b9ce061", "9c9ce061", "9d9ce061", "9e9ce061", "9f9ce061",
    "a09ce061", "a19ce061", "a29ce061", "a39ce061", "a49ce061", "a59ce061", "a69ce061", "a79ce061", "a89ce061", "a99ce061", "aa9ce061", "ab9ce061", "ac9ce061", "ad9ce061", "ae9ce061", "af9ce061",
    "b09ce061", "b19ce061", "b29ce061", "b39ce061", "b49ce061", "b59ce061", "b69ce061", "b79ce061", "b89ce061", "b99ce061", "ba9ce061", "bb9ce061", "bc9ce061", "bd9ce061", "be9ce061", "bf9ce061",
    "c09ce061", "c19ce061", "c29ce061", "c39ce061", "c49ce061", "c59ce061", "c69ce061", "c79ce061", "c89ce061", "c99ce061", "ca9ce061", "cb9ce061", "cc9ce061", "cd9ce061", "ce9ce061", "cf9ce061",
    "d09ce061", "d19ce061", "d29ce061", "d39ce061", "d49ce061", "d59ce061", "d69ce061", "d79ce061", "d89ce061", "d99ce061", "da9ce061", "db9ce061", "dc9ce061", "dd9ce061", "de9ce061", "df9ce061",
    "e09ce061", "e19ce061", "e29ce061", "e39ce061", "e49ce061", "e59ce061", "e69ce061", "e79ce061", "e89ce061", "e99ce061", "ea9ce061", "eb9ce061", "ec9ce061", "ed9ce061", "ee9ce061", "ef9ce061",
    "f09ce061", "f19ce061", "f29ce061", "f39ce061", "f49ce061", "f59ce061", "f69ce061", "f79ce061", "f89ce061", "f99ce061", "fa9ce061", "fb9ce061", "fc9ce061", "fd9ce061", "fe9ce061", "ff9ce061",
    "809de061", "819de061", "829de061", "839de061", "849de061", "859de061", "869de061", "879de061", "889de061", "899de061", "8a9de061", "8b9de061", "8c9de061", "8d9de061", "8e9de061", "8f9de061",
    "909de061", "919de061", "929de061", "939de061", "949de061", "959de061", "969de061", "979de061", "989de061", "999de061", "9a9de061", "9b9de061", "9c9de061", "9d9de061", "9e9de061", "9f9de061",
    "a09de061", "a19de061", "a29de061", "a39de061", "a49de061", "a59de061", "a69de061", "a79de061", "a89de061", "a99de061", "aa9de061", "ab9de061", "ac9de061", "ad9de061", "ae9de061", "af9de061",
    "b09de061", "b19de061", "b29de061", "b39de061", "b49de061", "b59de061", "b69de061", "b79de061", "b89de061", "b99de061", "ba9de061", "bb9de061", "bc9de061", "bd9de061", "be9de061", "bf9de061",
    "c09de061", "c19de061", "c29de061", "c39de061", "c49de061", "c59de061", "c69de061", "c79de061", "c89de061", "c99de061", "ca9de061", "cb9de061", "cc9de061", "cd9de061", "ce9de061", "cf9de061",
    "d09de061", "d19de061", "d29de061", "d39de061", "d49de061", "d59de061", "d69de061", "d79de061", "d89de061", "d99de061", "da9de061", "db9de061", "dc9de061", "dd9de061", "de9de061", "df9de061",
    "e09de061", "e19de061", "e29de061", "e39de061", "e49de061", "e59de061", "e69de061", "e79de061", "e89de061", "e99de061", "ea9de061", "eb9de061", "ec9de061", "ed9de061", "ee9de061", "ef9de061",
    "f09de061", "f19de061", "f29de061", "f39de061", "f49de061", "f59de061", "f69de061", "f79de061", "f89de061", "f99de061", "fa9de061", "fb9de061", "fc9de061", "fd9de061", "fe9de061", "ff9de061",
    "809ee061", "819ee061", "829ee061", "839ee061", "849ee061", "859ee061", "869ee061", "879ee061", "889ee061", "899ee061", "8a9ee061", "8b9ee061", "8c9ee061", "8d9ee061", "8e9ee061", "8f9ee061",
    "909ee061", "919ee061", "929ee061", "939ee061", "949ee061", "959ee061", "969ee061", "979ee061", "989ee061", "999ee061", "9a9ee061", "9b9ee061", "9c9ee061", "9d9ee061", "9e9ee061", "9f9ee061",
    "a09ee061", "a19ee061", "a29ee061", "a39ee061", "a49ee061", "a59ee061", "a69ee061", "a79ee061", "a89ee061", "a99ee061", "aa9ee061", "ab9ee061", "ac9ee061", "ad9ee061", "ae9ee061", "af9ee061",
    "b09ee061", "b19ee061", "b29ee061", "b39ee061", "b49ee061", "b59ee061", "b69ee061", "b79ee061", "b89ee061", "b99ee061", "ba9ee061", "bb9ee061", "bc9ee061", "bd9ee061", "be9ee061", "bf9ee061",
    "c09ee061", "c19ee061", "c29ee061", "c39ee061", "c49ee061", "c59ee061", "c69ee061", "c79ee061", "c89ee061", "c99ee061", "ca9ee061", "cb9ee061", "cc9ee061", "cd9ee061", "ce9ee061", "cf9ee061",
    "d09ee061", "d19ee061", "d29ee061", "d39ee061", "d49ee061", "d59ee061", "d69ee061", "d79ee061", "d89ee061", "d99ee061", "da9ee061", "db9ee061", "dc9ee061", "dd9ee061", "de9ee061", "df9ee061",
    "e09ee061", "e19ee061", "e29ee061", "e39ee061", "e49ee061", "e59ee061", "e69ee061", "e79ee061", "e89ee061", "e99ee061", "ea9ee061", "eb9ee061", "ec9ee061", "ed9ee061", "ee9ee061", "ef9ee061",
    "f09ee061", "f19ee061", "f29ee061", "f39ee061", "f49ee061", "f59ee061", "f69ee061", "f79ee061", "f89ee061", "f99ee061", "fa9ee061", "fb9ee061", "fc9ee061", "fd9ee061", "fe9ee061", "ff9ee061",
    "809fe061", "819fe061", "829fe061", "839fe061", "849fe061", "859fe061", "869fe061", "879fe061", "889fe061", "899fe061", "8a9fe061", "8b9fe061", "8c9fe061", "8d9fe061", "8e9fe061", "8f9fe061",
    "909fe061", "919fe061", "929fe061", "939fe061", "949fe061", "959fe061", "969fe061", "979fe061", "989fe061", "999fe061", "9a9fe061", "9b9fe061", "9c9fe061", "9d9fe061", "9e9fe061", "9f9fe061",
    "a09fe061", "a1a0e061", "a2a0e061", "a3a0e061", "a4a0e061", "a5a0e061", "a6a0e061", "a7a0e061", "a8a0e061", "a9a0e061", "aaa0e061", "aba0e061", "aca0e061", "ada0e061", "aea0e061", "afa0e061",
    "b0a0e061", "b1a0e061", "b2a0e061", "b3a0e061", "b4a0e061", "b5a0e061", "b6a0e061", "b7a0e061", "b8a0e061", "b9a0e061", "baa0e061", "bba0e061", "bca0e061", "bda0e061", "bea0e061", "bfa0e061",
    "c0a0e061", "c1a0e061", "c2a0e061", "c3a0e061", "c4a0e061", "c5a0e061", "c6a0e061", "c7a0e061", "c8a0e061", "c9a0e061", "caa0e061", "cba0e061", "cca0e061", "cda0e061", "cea0e061", "cfa0e061",
    "d0a0e061", "d1a0e061", "d2a0e061", "d3a0e061", "d4a0e061", "d5a0e061", "d6a0e061", "d7a0e061", "d8a0e061", "d9a0e061", "daa0e061", "dba0e061", "dca0e061", "dda0e061", "dea0e061", "dfa0e061",
    "e0a0e061", "e1a0e061", "e2a0e061", "e3a0e061", "e4a0e061", "e5a0e061", "e6a0e061", "e7a0e061", "e8a0e061", "e9a0e061", "eaa0e061", "eba0e061", "eca0e061", "eda0e061", "eea0e061", "efa0e061",
    "f0a0e061", "f1a0e061", "f2a0e061", "f3a0e061", "f4a0e061", "f5a0e061", "f6a0e061", "f7a0e061", "f8a0e061", "f9a0e061", "faa0e061", "fba0e061", "fca0e061", "fda0e061", "fea0e061", "ffa0e061",
    "80a1e061", "81a1e061", "82a1e061", "83a1e061", "84a1e061", "85a1e061", "86a1e061", "87a1e061", "88a1e061", "89a1e061", "8aa1e061", "8ba1e061", "8ca1e061", "8da1e061", "8ea1e061", "8fa1e061",
    "90a1e061", "91a1e061", "92a1e061", "93a1e061", "94a1e061", "95a1e061", "96a1e061", "97a1e061", "98a1e061", "99a1e061", "9aa1e061", "9ba1e061", "9ca1e061", "9da1e061", "9ea1e061", "9fa1e061",
    "a0a1e061", "a1a1e061", "a2a1e061", "a3a1e061", "a4a1e061", "a5a1e061", "a6a1e061", "a7a1e061", "a8a1e061", "a9a1e061", "aaa1e061", "aba1e061", "aca1e061", "ada1e061", "aea1e061", "afa1e061",
    "b0a1e061", "b1a1e061", "b2a1e061", "b3a1e061", "b4a1e061", "b5a1e061", "b6a1e061", "b7a1e061", "b8a1e061", "b9a1e061", "baa1e061", "bba1e061", "bca1e061", "bda1e061", "bea1e061", "bfa1e061",
    "c0a1e061", "c1a1e061", "c2a1e061", "c3a1e061", "c4a1e061", "c5a1e061", "c6a1e061", "c7a1e061", "c8a1e061", "c9a1e061", "caa1e061", "cba1e061", "cca1e061", "cda1e061", "cea1e061", "cfa1e061",
    "d0a1e061", "d1a1e061", "d2a1e061", "d3a1e061", "d4a1e061", "d5a1e061", "d6a1e061", "d7a1e061", "d8a1e061", "d9a1e061", "daa1e061", "dba1e061", "dca1e061", "dda1e061", "dea1e061", "dfa1e061",
    "e0a1e061", "e1a1e061", "e2a1e061", "e3a1e061", "e4a1e061", "e5a1e061", "e6a1e061", "e7a1e061", "e8a1e061", "e9a1e061", "eaa1e061", "eba1e061", "eca1e061", "eda1e061", "eea1e061", "efa1e061",
    "f0a1e061", "f1a1e061", "f2a1e061", "f3a1e061", "f4a1e061", "f5a1e061", "f6a1e061", "f7a1e061", "f8a1e061", "f9a1e061", "faa1e061", "fba1e061", "fca1e061", "fda1e061", "fea1e061", "ffa1e061"]
                        for ids in items_ids:
                            self.s5.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"error ~ /proxy ")





                if '1200' in dt.hex()[0:5] and b'/y8' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.y8, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT 8y"
                    threading.Thread(target=self.sH, args=(id, c_m)).start() 

                if '1200' in dt.hex()[0:5] and b'/y7' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.y7, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT 7y"
                    threading.Thread(target=self.sH, args=(id, c_m)).start() 

                if '1200' in dt.hex()[0:5] and b'/yt' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.send_yout_list).start()
                    c_m = "[C][B][00FF00]DonE Youtybr"
                    threading.Thread(target=self.sH, args=(id, c_m)).start() 

                if '1200' in dt.hex()[0:4] and b'/fr' in dt:
                    id = dt.hex()[12:22]
                    c_m = "[C][B][00FF00]DonE Add FrienD"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    try:
                        i = str(dt).split('/fr')[1]
                        if '***' in i:
                            i = i.replace('***', '106')
                        x = str(i).split('(\\x')[0]
                        x = self.zx2(x)
                        if x:
                            self.ff(self.s5, x)
                    except Exception as e:
                        pass

                if '1200' in dt.hex()[0:5] and b'/y6' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.y6, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT 6y"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()  
                if '1200' in dt.hex()[0:6] and b'/skin1' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.skin1, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT skin"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/skin2' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.skin2, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT skin"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/skin3' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.skin3, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT skin"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/skin4' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.skin4, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT skin"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/skin5' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.skin5, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT skin"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/skin6' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.skin6, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT skin"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/skin7' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.skin7, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT skin"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    

                if '1200' in dt.hex()[0:6] and b'/dance1' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens1, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance2' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens2, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance3' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens3, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance4' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens4, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance5' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens5, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance6' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens6, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance7' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens7, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance8' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens8, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:6] and b'/dance9' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens9, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance10' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens10, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance11' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens11, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance12' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens12, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance13' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens13, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance14' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens14, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance15' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens15, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance16' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens16, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance17' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens17, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()
                    
                if '1200' in dt.hex()[0:7] and b'/dance18' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.zix_dens18, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT dens"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()             
                    
                if '1200' in dt.hex()[0:6] and b'/goi' in dt:
                    id = dt.hex()[12:22]
                    threading.Thread(target=self.goi, args=(id,)).start()
                    c_m = "[C][B][00FF00]DonE SenT v youtuber on squad"
                    threading.Thread(target=self.sH, args=(id, c_m)).start()                                  

                if '1200' in dt.hex()[0:4] and b'/skins' in dt:
                    try:
                        u_id = dt.hex()[12:22]
                        hlp = """[b][c][FFFFFF]Uniform list in squad
[FF3C3C][b][c]
/skin1
/skin2
/skin3
/skin4
/skin5
/skin6
/skin7"""
                        threading.Thread(target=self.sH, args=(u_id, hlp)).start()
                    except Exception as e:
                        pass

                if '1200' in dt.hex()[0:4] and b'/dances' in dt:
                    try:
                        u_id = dt.hex()[12:22]
                        hlp = """[FFFFFF][b][c]Promotion list
[FF3C3C][b][c]
/dance1
/dance2
/dance3
/dance4
/dance5
/dance6
/dance7
/dance8
/dance9
/dance10
/dance11
/dance12
/dance13
/dance14
/dance15
/dance16
/dance17
/dance18"""
                        threading.Thread(target=self.sH, args=(u_id, hlp)).start()
                    except Exception as e:
                        pass         
                                                                
                if '1200' in dt.hex()[0:4] and b'/help' in dt:
                    try:
                        u_id = dt.hex()[12:22]
                        hlp = """[b][c][FF7B00]Welcome Bot Free Fire
[00FFD5][b][c]━━━━━━━━━━━━━━━━━━━━━━ 
[00FFD5][b][c]تحويل الفريق إلى
[00FF6A][b][c] Squad 3 --->[b][681ed6]  /3s
[00FF6A][b][c] Squad 5 --->[b][681ed6]  /5s
[00FF6A][b][c] Squad 6 --->[b][681ed6]  /6s

[FFFFFF][b][c] تهكير القولد و الجواهر
[FF3C3C][b][c]/dm

[FFFFFF][b][c] اختفاء داخل الفريق
[FF3C3C][b][c]/spy

[FFFFFF][b][c] اختفاء في الروم
[FF3C3C][b][c]/spyrom

[FFFFFF]توقيف ميزة اختفاء في الروم و فريق
[FF3C3C][b][c]/stop

[FFFFFF][b][c] جلب جميع اليتيوبرز اصدقاء
[FF3C3C][b][c]/yt

[FFFFFF][b][c]جلب شبح للفريق وهمي
[FF3C3C][b][c]/ghost

[FFFFFF][b][c] صديق وهمي
[FF3C3C][b][c]/fr 123456xx

[FFFFFF] لاج في الفريق (اضغط على استعداد )
[FF3C3C][b][c]/lag

[FFFFFF][b][c] بروكسي ملابس 
[FF3C3C][b][c]/proxy

[FFFFFF][b][c] سكنات في الفريق
[FF3C3C][b][c]/skins

[FFFFFF][b][c] رقصات في الفريق
[FF3C3C][b][c]/dances

[FFFFFF][b][c]شارات سنوات في شات الفريق
[FF3C3C][b][c]/y6 ,/y7 ,/y8 ,/y9 ,/y10
[00FFD5][b][c]━━━━━━━━━━━━━━━━━━━━━━"""
                        threading.Thread(target=self.sH, args=(u_id, hlp)).start()
                    except Exception as e:
                        pass

                if cl.send(dt) <= 0:
                    break

    def h(self, a_t, e_n):
        return b''.join([
            V.to_bytes(1, 'big'),
            e_n.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            a_t.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])

    def vC(self, conn):
        ver = conn.recv(1)[0]
        u_len = conn.recv(1)[0]
        usr = conn.recv(u_len).decode('utf-8')
        p_len = conn.recv(1)[0]
        pwd = conn.recv(p_len).decode('utf-8')

        if usr == self.u and pwd == self.p:
            resp = bytes([ver, 0])
            conn.sendall(resp)
            return True
        else:
            resp = bytes([ver, 0])
            conn.sendall(resp)
            return True

    def gA(self, n_m, conn):
        mths = []
        for _ in range(n_m):
            mths.append(conn.recv(1)[0])
        return mths

    def rn(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen()
        print(f"code run {ip} --> {port}")

        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=self.hC, args=(conn,))
            t.start()

def st():
    Px().rn('127.0.0.1', 5000)

st()
