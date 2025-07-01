# regular brainfuck interpreter (made to avoid loops)

def step(code,tape,code_ptr,tape_ptr,loop_ctr):
    if loop_ctr==0:
        if code_ptr==len(code):
            return None
        elif code[code_ptr]==",":
            tape[tape_ptr]=int(input(">"))
        elif code[code_ptr]==".":
            print(tape[tape_ptr])
        elif code[code_ptr]=="[":
            if tape[tape_ptr]==0:
                loop_ctr=+1
        elif code[code_ptr]=="]":
            if tape[tape_ptr]!=0:
                code_ptr-=2
                loop_ctr=-1
        elif code[code_ptr]==">":
            tape_ptr+=1
            if tape_ptr==len(tape):
                tape = tape+[0]
        elif code[code_ptr]=="<":
            if tape_ptr==0:
                tape = [0]+tape
            else:
                tape_ptr-=1
        elif code[code_ptr]=="+":
            tape[tape_ptr]+=1
        elif code[code_ptr]=="-":
            tape[tape_ptr]-=1
        code_ptr+=1
    elif loop_ctr>0:
        if code[code_ptr]=="[":
            loop_ctr+=1
        elif code[code_ptr]=="]":
            loop_ctr-=1
        code_ptr+=1
    else:
        if code[code_ptr]=="[":
            loop_ctr+=1
            if loop_ctr==0:
                code_ptr+=2
        elif code[code_ptr]=="]":
            loop_ctr-=1
        code_ptr-=1
    return (code,tape,code_ptr,tape_ptr,loop_ctr)

# essentially the same code, but everything is nested if with variable changes only at the bottom level
# note that some extra else clauses have to be added

def step(code,tape,code_ptr,tape_ptr,loop_ctr):
    if loop_ctr==0:
        if code_ptr==len(code):
            return None
        elif code[code_ptr]==",":
            tape[tape_ptr]=int(input(">"))
            code_ptr+=1
        elif code[code_ptr]==".":
            print(tape[tape_ptr])
            code_ptr+=1
        elif code[code_ptr]=="[":
            if tape[tape_ptr]==0:
                loop_ctr=+1
                code_ptr+=1
            else:
                code_ptr+=1
        elif code[code_ptr]=="]":
            if tape[tape_ptr]!=0:
                loop_ctr=-1
                code_ptr-=1
            else:
                code_ptr+=1
        elif code[code_ptr]==">":
            if tape_ptr==len(tape)-1:
                tape = tape+[0]
                tape_ptr+=1
                code_ptr+=1
            else:
                tape_ptr+=1
                code_ptr+=1
        elif code[code_ptr]=="<":
            if tape_ptr==0:
                tape = [0]+tape
                code_ptr+=1
            else:
                tape_ptr-=1
                code_ptr+=1
        elif code[code_ptr]=="+":
            tape[tape_ptr]+=1
            code_ptr+=1
        elif code[code_ptr]=="-":
            tape[tape_ptr]-=1
            code_ptr+=1
    elif loop_ctr>0:
        if code[code_ptr]=="[":
            loop_ctr+=1
            code_ptr+=1
        elif code[code_ptr]=="]":
            loop_ctr-=1
            code_ptr+=1
        else:
            code_ptr+=1
    else:
        if code[code_ptr]=="[":
            if loop_ctr==-1:
                loop_ctr=0
                code_ptr+=1
            else:
                loop_ctr+=1
                code_ptr-=1
        elif code[code_ptr]=="]":
            loop_ctr-=1
            code_ptr-=1
        else:
            code_ptr-=1
    return (code,tape,code_ptr,tape_ptr,loop_ctr)

# and now everything is immutable!

def step(code,tape,code_ptr,tape_ptr,loop_ctr):
    if loop_ctr==0:
        if code_ptr==len(code):
            return None
        elif code[code_ptr]==",":
            return (code,
                    tape[:tape_ptr]+[int(input(">"))]+tape[tape_ptr+1:],
                    code_ptr+1,
                    tape_ptr,loop_ctr)
        elif code[code_ptr]==".":
            return (print(tape[tape_ptr]),
                    (code,tape,
                     code_ptr+1,
                     tape_ptr,loop_ctr)
                    )[1]
        elif code[code_ptr]=="[":
            if tape[tape_ptr]==0:
                return (code,tape,code_ptr+1,tape_ptr,loop_ctr+1)
            else:
                return (code,tape,code_ptr+1,tape_ptr,loop_ctr)
        elif code[code_ptr]=="]":
            if tape[tape_ptr]!=0:
                return (code,tape,code_ptr-1,tape_ptr,loop_ctr-1)
            else:
                return (code,tape,code_ptr+1,tape_ptr,loop_ctr)
        elif code[code_ptr]==">":
            if tape_ptr==len(tape)-1:
                return (code,tape+[0],code_ptr+1,tape_ptr+1,loop_ctr)
            else:
                return (code,tape,code_ptr+1,tape_ptr+1,loop_ctr)
        elif code[code_ptr]=="<":
            if tape_ptr==0:
                return (code,[0]+tape,code_ptr+1,tape_ptr,loop_ctr)
            else:
                return (code,tape,code_ptr+1,tape_ptr-1,loop_ctr)
        elif code[code_ptr]=="+":
            return (code,
                    tape[:tape_ptr]+[tape[tape_ptr]+1]+tape[tape_ptr+1:],
                    code_ptr+1,tape_ptr,loop_ctr)
        elif code[code_ptr]=="-":
            return (code,
                    tape[:tape_ptr]+[tape[tape_ptr]-1]+tape[tape_ptr+1:],
                    code_ptr+1,tape_ptr,loop_ctr)
    elif loop_ctr>0:
        if code[code_ptr]=="[":
            return (code,tape,code_ptr+1,tape_ptr,loop_ctr+1)
        elif code[code_ptr]=="]":
            return (code,tape,code_ptr+1,tape_ptr,loop_ctr-1)
        else:
            return (code,tape,code_ptr+1,tape_ptr,loop_ctr)
    else:
        if code[code_ptr]=="[":
            if loop_ctr==-1:
                return (code,tape,code_ptr+1,tape_ptr,0)
            else:
                return (code,tape,code_ptr-1,tape_ptr,loop_ctr+1)
        elif code[code_ptr]=="]":
            return (code,tape,code_ptr-1,tape_ptr,loop_ctr-1)
        else:
            return (code,tape,code_ptr-1,tape_ptr,loop_ctr)

#now stuff everything into a mess of ternary expressions
        
def step(code,tape,code_ptr,tape_ptr,loop_ctr):
    return  (
                (
                    None
                if code_ptr==len(code) else
                    (
                        (code,
                        tape[:tape_ptr]+[int(input(">"))]+tape[tape_ptr+1:],
                        code_ptr+1,
                        tape_ptr,loop_ctr)
                    if code[code_ptr]=="," else
                        (
                            (print(tape[tape_ptr]),
                             (code,tape,
                              code_ptr+1,
                              tape_ptr,loop_ctr)
                            )[1]
                        if code[code_ptr]=="." else
                            (
                                (
                                    (code,tape,code_ptr+1,tape_ptr,loop_ctr+1)
                                if tape[tape_ptr]==0 else
                                    (code,tape,code_ptr+1,tape_ptr,loop_ctr)
                                )
                            if code[code_ptr]=="[" else
                                (
                                    (
                                        (code,tape,code_ptr-1,tape_ptr,loop_ctr-1)
                                    if tape[tape_ptr]!=0 else
                                        (code,tape,code_ptr+1,tape_ptr,loop_ctr)
                                    )
                                if code[code_ptr]=="]" else
                                    (
                                        (
                                            (code,tape+[0],code_ptr+1,tape_ptr+1,loop_ctr)
                                        if tape_ptr==len(tape)-1 else
                                            (code,tape,code_ptr+1,tape_ptr+1,loop_ctr)
                                        )
                                    if code[code_ptr]==">" else
                                        (
                                            (
                                                (code,[0]+tape,code_ptr+1,tape_ptr,loop_ctr)
                                            if tape_ptr==0 else
                                                (code,tape,code_ptr+1,tape_ptr-1,loop_ctr)
                                            )
                                        if code[code_ptr]=="<" else
                                            (
                                                (code,
                                                 tape[:tape_ptr]+[tape[tape_ptr]+1]+tape[tape_ptr+1:],
                                                 code_ptr+1,tape_ptr,loop_ctr)
                                            if code[code_ptr]=="+" else #everything else should be a -
                                                (code,
                                                 tape[:tape_ptr]+[tape[tape_ptr]-1]+tape[tape_ptr+1:],
                                                 code_ptr+1,tape_ptr,loop_ctr)
                                                
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            if loop_ctr==0 else
                (
                    (
                        (code,tape,code_ptr+1,tape_ptr,loop_ctr+1)
                    if code[code_ptr]=="[" else
                        (
                            (code,tape,code_ptr+1,tape_ptr,loop_ctr-1)
                        if code[code_ptr]=="]" else
                            (code,tape,code_ptr+1,tape_ptr,loop_ctr)
                        )
                    )
                if loop_ctr>0 else
                    (
                        (
                            (
                                (code,tape,code_ptr+1,tape_ptr,0)
                            if loop_ctr==-1 else
                                (code,tape,code_ptr-1,tape_ptr,loop_ctr+1)
                            )
                        if code[code_ptr]=="[" else
                            (2
                                (code,tape,code_ptr-1,tape_ptr,loop_ctr-1)
                            if code[code_ptr]=="]" else
                                (code,tape,code_ptr-1,tape_ptr,loop_ctr)
                            )
                        )
                    )
                )
            )

#which can be rewritten in one line

step = lambda code,tape,code_ptr,tape_ptr,loop_ctr: ( ( None if code_ptr==len(code) else ( (code, tape[:tape_ptr]+[int(input(">"))]+tape[tape_ptr+1:], code_ptr+1, tape_ptr,loop_ctr) if code[code_ptr]=="," else ( (print(tape[tape_ptr]), (code,tape, code_ptr+1, tape_ptr,loop_ctr) )[1] if code[code_ptr]=="." else ( ( (code,tape,code_ptr+1,tape_ptr,loop_ctr+1) if tape[tape_ptr]==0 else (code,tape,code_ptr+1,tape_ptr,loop_ctr) ) if code[code_ptr]=="[" else ( ( (code,tape,code_ptr-1,tape_ptr,loop_ctr-1) if tape[tape_ptr]!=0 else (code,tape,code_ptr+1,tape_ptr,loop_ctr) ) if code[code_ptr]=="]" else ( ( (code,tape+[0],code_ptr+1,tape_ptr+1,loop_ctr) if tape_ptr==len(tape)-1 else (code,tape,code_ptr+1,tape_ptr+1,loop_ctr) ) if code[code_ptr]==">" else ( ( (code,[0]+tape,code_ptr+1,tape_ptr,loop_ctr) if tape_ptr==0 else (code,tape,code_ptr+1,tape_ptr-1,loop_ctr) ) if code[code_ptr]=="<" else ( (code, tape[:tape_ptr]+[tape[tape_ptr]+1]+tape[tape_ptr+1:], code_ptr+1,tape_ptr,loop_ctr) if code[code_ptr]=="+" else (code, tape[:tape_ptr]+[tape[tape_ptr]-1]+tape[tape_ptr+1:], code_ptr+1,tape_ptr,loop_ctr)  ) ) ) ) ) ) ) ) if loop_ctr==0 else ( ( (code,tape,code_ptr+1,tape_ptr,loop_ctr+1) if code[code_ptr]=="[" else ( (code,tape,code_ptr+1,tape_ptr,loop_ctr-1) if code[code_ptr]=="]" else (code,tape,code_ptr+1,tape_ptr,loop_ctr) ) ) if loop_ctr>0 else ( ( ( (code,tape,code_ptr+1,tape_ptr,0) if loop_ctr==-1 else (code,tape,code_ptr-1,tape_ptr,loop_ctr+1) ) if code[code_ptr]=="[" else ( (code,tape,code_ptr-1,tape_ptr,loop_ctr-1) if code[code_ptr]=="]" else (code,tape,code_ptr-1,tape_ptr,loop_ctr) ) ) ) ) )
bfeval = None
bfeval = lambda *args: ((lambda x: None if x is None else bfeval(*x))(step(*args)))

double = ",[->++<]>."
mult = ",>,<[->[->+>+<<]>[-<+>]<<]>>>."
fib = ">+[.[->+>+<<]>[-<+>]<<[->>+>>+<<<<]>>>>[-<<<<+>>>>]<[-<+>]<]"
code,tape,code_ptr,tape_ptr,loop_ctr = mult,[0],0,0,0

bfeval(code,tape,code_ptr,tape_ptr,loop_ctr)
print(jjsj)

while True:
    print(" ".join(map(str,tape[:tape_ptr]))+"["+str(tape[tape_ptr])+"]"+" ".join(map(str,tape[tape_ptr+1:])))
    #print("  ".join(code[:code_ptr])+" ("+code[code_ptr]+") "+"  ".join(code[code_ptr+1:]))
    #print("----")
    code,tape,code_ptr,tape_ptr,loop_ctr=step(code,tape,code_ptr,tape_ptr,loop_ctr)
