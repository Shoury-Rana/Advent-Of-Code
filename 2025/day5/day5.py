import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    raw_lines = [line.strip() for line in f.readlines()]

# Part 1
ranges = []
candidates = []

for line in raw_lines:
    if line == '':
        continue
    
    elif '-' in line:
        parts = line.split('-')
        ranges.append((int(parts[0]), int(parts[1])))

    else:
        candidates.append(int(line))

fresh_count = 0

for id in candidates:
    is_fresh = False
    for r_start, r_end in ranges:
        if r_start <= id <= r_end:
            is_fresh = True
            break
    
    if is_fresh:
        fresh_count += 1

print(f"Result 1: {fresh_count}")


# Part 2
ranges.sort()
merged_ranges = []

curr_start, curr_end = ranges[0]

for i in range(1, len(ranges)):
    next_start, next_end = ranges[i]

    if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
    else:
        merged_ranges.append((curr_start, curr_end))
        curr_start, curr_end = next_start, next_end

merged_ranges.append((curr_start, curr_end))

total_id = 0
for r_start, r_end in merged_ranges:
    total_id += (r_end - r_start + 1)

print(f"Result 2: {total_id}")

