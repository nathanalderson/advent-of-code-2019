import itertools

with open("input", "r") as f:
    program = [int(l) for l in f.read().split(",")]

def execute(program):
    pc = 0
    while True:
        opcode = program[pc]
        if opcode == 99:
            break
        elif opcode == 1:
            v1, v2, dest = program[pc + 1 : pc + 4]
            program[dest] = program[v1] + program[v2]
        elif opcode == 2:
            v1, v2, dest = program[pc + 1 : pc + 4]
            program[dest] = program[v1] * program[v2]
        else:
            raise Exception("Bad opcode")
        pc += 4


def test_execute():
    prog1 = [1,0,0,0,99]
    execute(prog1)
    assert prog1[0] == 2


def exec_with_inputs(noun, verb):
    prog = program[:]
    prog[1] = noun
    prog[2] = verb
    execute(prog)
    return prog[0], noun, verb

ans1, _, _ = exec_with_inputs(12, 2)
print(ans1)

inputs = itertools.product(range(100), repeat=2)
results = (exec_with_inputs(noun, verb) for noun, verb in inputs)
target = 19690720
result, noun, verb = next(x for x in results if x[0] == target)
ans2 = 100 * noun + verb
print(ans2)
