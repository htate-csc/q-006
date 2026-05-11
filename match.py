N = int(input())
S = input()

buffer = set([(0, 0)])
current = [0, 0]
i = 0
while i < N:
    match S[i]:
        case 'R':
            current[0] += 1
        case 'L':
            current[0] -= 1
        case 'U':
            current[1] += 1
        case 'D':
            current[1] -= 1
    buffer.add((current[0], current[1]))
    if (len(buffer) != i + 2):
        print('Yes')
        break
    else:
        i += 1
if (i == N):
    print('No')
