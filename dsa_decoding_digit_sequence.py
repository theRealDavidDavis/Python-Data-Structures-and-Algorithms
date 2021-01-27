
def decode(sequence):

    # This function takes an integer as an input and it determines the maximum number of possible decodings given the digit sequence
    digits = len(str(sequence))
    # This is the initial amount of possible solutions when ignoring concatenated digits
    possibilities = digits
    list_num = [int(x) for x in str(sequence)]

    for i in range(digits-1):
        if list_num[i] < 3:
            if list_num[i] == 2:
                if list_num[i+1] < 7:
                    tmp = str(list_num[i]) + str(list_num[i+1])
                    list_num.append(int(tmp))
                    possibilities += 1
            else:
                tmp = str(list_num[i]) + str(list_num[i+1])
                list_num.append(int(tmp))
                possibilities += 1
    return possibilities
