# 2 Pass Nasm Assembler

Nasm 64 bit 2-Pass assembler that support 64 bit instruction and debugger written in purely in python2.7 instruction that support ADD, SUB, MUL, DIV ,MOV, and debugg whole program.

  ## Pass-1:
- Define symbols and literals and remember them in symbol table and literal table   respectively.
- Keep track of location counter
- Process pseudo-operations
## Pass-2:
- Generate object code by converting symbolic op-code into respective numeric op-code
- Generate data for literals and look for values of symbols
## Debugger
- Debugg given program line by line by built in debugger
