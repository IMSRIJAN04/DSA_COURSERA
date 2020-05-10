def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    if n==0:
        return 0
    x=max(numbers)
    if x in numbers:
        numbers.remove(x)
    y=max(numbers)
    max_product=x*y
    return max_product


if __name__ == '__main__':
    n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
