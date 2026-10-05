import os
import time
import math
from pathlib import Path

# ==========================================
# VARIANT 4
# Country: Poland
# Pattern: d
# Function: y = x^0.5
# ==========================================

WHITE = "\033[47m"
RED = "\033[41m"
RESET = "\033[0m"
CURSOR_HOME = "\033[H"


# ==========================================
# 1. FLAG OF POLAND
# ==========================================

print("1. FLAG OF POLAND\n")

width = 30
height = 10

for i in range(height):
    if i < height // 2:
        print(WHITE + " " * width + RESET)
    else:
        print(RED + " " * width + RESET)

input("\nPress Enter to continue...")


# ==========================================
# 2. PATTERN d
# ==========================================

os.system("cls" if os.name == "nt" else "clear")

print("2. PATTERN d\n")

pattern = (
    "████████████████████████\n"
    "        ████            \n"
    "████████████████████████\n"
    "            ████        \n"
    "████████████████████████\n"
)

print(pattern)
print(pattern)

input("Press Enter to continue...")


# ==========================================
# 3. ANIMATION - 4 FRAMES
# ==========================================

frames = [
    "●               ",
    "     ●           ",
    "          ●      ",
    "               ● "
]

for frame in frames:
    os.system("cls" if os.name == "nt" else "clear")
    print(CURSOR_HOME, end="")
    print("3. ANIMATION\n")
    print(frame)
    time.sleep(0.5)

input("\nPress Enter to continue...")


# ==========================================
# 4. SEQUENCE.TXT
# Average absolute values:
# first 125 and second 125
# ==========================================

os.system("cls" if os.name == "nt" else "clear")

print("4. SEQUENCE.TXT\n")

file_path = Path(__file__).with_name("sequence.txt")

if not file_path.exists():
    print("ERROR: sequence.txt was not found.")
    raise SystemExit

with open(file_path, "r", encoding="utf-8") as file:
    numbers = [
        float(line.strip())
        for line in file
        if line.strip()
    ]

if len(numbers) != 250:
    print("ERROR: sequence.txt must contain exactly 250 numbers.")
    raise SystemExit

first_group = numbers[:125]
second_group = numbers[125:]

average_first = sum(abs(x) for x in first_group) / 125
average_second = sum(abs(x) for x in second_group) / 125

total = average_first + average_second

percent_first = average_first / total * 100
percent_second = average_second / total * 100

print(f"Average absolute value of numbers 1-125: {average_first:.4f}")
print(f"Average absolute value of numbers 126-250: {average_second:.4f}")

print("\nPercentage ratio:\n")

bar_width = 40

bar1 = round(percent_first / 100 * bar_width)
bar2 = round(percent_second / 100 * bar_width)

print(
    f"1-125   |"
    f"{'█' * bar1}"
    f"{' ' * (bar_width - bar1)}| "
    f"{percent_first:.2f}%"
)

print(
    f"126-250 |"
    f"{'█' * bar2}"
    f"{' ' * (bar_width - bar2)}| "
    f"{percent_second:.2f}%"
)

print(f"\nTotal = {percent_first + percent_second:.2f}%")

input("\nPress Enter to continue...")


# ==========================================
# 5. ADDITIONAL TASK
# y = x^0.5
# ==========================================

os.system("cls" if os.name == "nt" else "clear")

print("5. ADDITIONAL TASK")
print("y = x^0.5\n")

graph_width = 45
graph_height = 12

canvas = [
    [" " for _ in range(graph_width + 1)]
    for _ in range(graph_height + 1)
]

# Y axis
for row in range(graph_height):
    canvas[row][0] = "│"

# X axis
for col in range(graph_width + 1):
    canvas[graph_height][col] = "─"

canvas[graph_height][0] = "└"

# y = sqrt(x)
for x in range(graph_width):
    y = math.sqrt(x)
    max_y = math.sqrt(graph_width - 1)

    scaled_y = round(
        y / max_y * (graph_height - 1)
    )

    row = graph_height - scaled_y
    col = x + 1

    if 0 <= row < graph_height:
        canvas[row][col] = "●"

graph = "\n".join("".join(row) for row in canvas)

print(graph)

print("\nFunction: y = x^0.5")
print("Variant 4 - Poland")