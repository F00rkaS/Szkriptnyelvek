#!/usr/bin/env python3

def get_median(numbers):
        
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0

def main():

    print(get_median([1, 2, 3, 4, 5]) == 3)
    print(get_median([3, 1, 2, 5, 3]) == 3)
    print(get_median([1, 300, 2, 200, 1]) == 2)
    print(get_median([3, 6, 20, 99, 10, 15]) == 12.5)
    

    print("Eredmények:")
    print(f"[1, 2, 3, 4, 5] -> {get_median([1, 2, 3, 4, 5])}")
    print(f"[3, 1, 2, 5, 3] -> {get_median([3, 1, 2, 5, 3])}")
    print(f"[1, 300, 2, 200, 1] -> {get_median([1, 300, 2, 200, 1])}")
    print(f"[3, 6, 20, 99, 10, 15] -> {get_median([3, 6, 20, 99, 10, 15])}")

if __name__ == '__main__':
    main()