import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    data = f.readlines()
    data = [d.strip('\n') for d in data]
    
# Part 1
def max_joltage(bank):
    best = 0
    n = len(bank)

    for i in range(n - 1):
        for j in range(i + 1, n):
            val = int(bank[i])*10 + int(bank[j])
            if val > best:
                best = val
    return best

def total_output_joltage(lines):
    sum = 0
    for line in lines:
        sum += max_joltage(line)
    return sum

print("Result 1:", total_output_joltage(data))


# Part 2
def max_k_joltage(bank):
    stack = []
    remove = len(bank) - 12

    for digit in bank:
        while remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)

    result = "".join(stack[:12])
    return int(result)

def total_output_joltage(lines):
    sum = 0
    for line in lines:
        sum += max_k_joltage(line)
    return sum

print("Result 2:", total_output_joltage(data))