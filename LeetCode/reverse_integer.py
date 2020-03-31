class Solution:
    def reverse(self, x: int) -> int:

        input_to_string = str(x)

        minus_sign = False

        if input_to_string[0] == '-':
            minus_sign = True
            input_to_string = input_to_string.replace('-','')

        split_input = [digit for digit in str(input_to_string)]

        split_input.reverse()

        number_result = ''.join(split_input)

        number_result = int(number_result)

        # note that, the result should fall within the 32-bit signed integer range
        # -0x80000000 = -2147483648
        # 0x7fffffff = 2147483647

        if number_result > 0x7fffffff:
            return 0

        if minus_sign == True:
            return '-' + str(number_result)
        else:
            return number_result
