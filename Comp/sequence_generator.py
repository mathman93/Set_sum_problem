# Original Sequence
old = [18, 7, 29, 20, 16, 9, 27, 22, 3, 13, 12, 4, 5, 11, 14, 2, 23, 26, 10, 6, 30, 19, 17, 8, 28, 21, 15, 1, 24, 25]

a = 3 # Multiplier
s = -1 # Constant Shift (abs(s) < (a**2)/2)
# New Sequence
new = []
for i in range(len(old)):
    new.append(a**2 * old[i] + (s * (-1)**i))
#new = [a**2 * x + s for x in old]

print("New Path: {0}".format(new))
print("New Sequence: {0}".format(sorted(new)))