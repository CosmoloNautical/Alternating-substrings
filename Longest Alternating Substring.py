def Alternating_substring(number):

    """
    Given a string of digits this program will return the longest substring within that alternates between odd and even numbers
    """

    odd_even_dict = {"odd": "even", "even": "odd"}

    def even_or_odd(large_number, depth, number):
        if int(large_number[number + depth]) % 2 == 0:
            odd_even = "even"
        else:
            odd_even = "odd"
        return odd_even

    def find_substrings(large_number):
        substrings = []

        for number in range(0, len(large_number)):
            try:
                small_number = ""
                depth = 0
                odd_even_first = even_or_odd(large_number, depth, number)
                small_number += large_number[number]
            except IndexError:
                break
            while True:
                try:
                    depth += 1
                    odd_even_second = even_or_odd(large_number, depth, number)
                    if odd_even_dict[odd_even_second] == odd_even_first:
                        odd_even_first = odd_even_second
                        small_number += large_number[number + depth]
                    else:
                        break
                except IndexError:
                    break
            if len(small_number) > 1:
                substrings.append(small_number)
            large_number = large_number.replace(small_number, "0", 1)

        def check_largest(substrings):
            biggest = substrings[0]
            for x in substrings:
                if len(x) > len(biggest):
                    biggest = x
            print(f"The substrings found in the number are:{substrings}\nThe largest substring found was:{biggest}")

        check_largest(substrings)

    find_substrings(number)
