def draw_board(positions):
    print("+-----------------+")
    for row in range(7, -1, -1):
        line = " ".join("Q" if positions[col] == row else "." for col in range(8))
        print(f"| {line} |")
    print("+-----------------+")

if __name__ == '__main__':
    draw_board([7, 3, 0, 2, 5, 1, 6, 4])
    print()
    draw_board([0, 4, 7, 5, 2, 6, 1, 3])