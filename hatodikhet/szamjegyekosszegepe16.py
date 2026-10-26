def main():
    number = 2 ** 1000
    digit_sum = sum(int(digit) for digit in str(number))
    print(digit_sum)

if __name__ == '__main__':
    main()