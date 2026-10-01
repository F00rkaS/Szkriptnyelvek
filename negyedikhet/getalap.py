

def main():
    print("""---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C      [c]
q) quit""")

    input_choice = input("")
    if input_choice == "1":
        with open("alap.py", "w") as f:
            f.write("#!/usr/bin/env python3\n")
            f.write("\n")
            f.write("\n")
            f.write("def main():\n")
            f.write("    print('Py3')\n")
            f.write("\n")
            f.write("##############################################################################\n")
            f.write("\n")
            f.write("if __name__ == \"__main__\":\n")
            f.write("    main()\n")
    elif input_choice == "2":
        with open("alap.c", "w") as f:
            f.write("#include <stdio.h>\n")
            f.write("\n")
            f.write("int main() {\n")
            f.write("    printf(\"C\\n\");\n")
            f.write("    return 0;\n")
            f.write("}\n")
    elif input_choice == "q":
        return


if __name__ == "__main__":
    main()