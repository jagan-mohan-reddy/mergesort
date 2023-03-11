def bit_stuffing(data):
    stuffed_data=""
    count = 0
    for bit in data:
        stuffed_data += bit
        if bit == "1":
            count += 1
            if count == 5:
                stuffed_data += '0'
                count = 0
        else:
            count = 0
    # print(stuffed_data)cd Do  
    return stuffed_data

def bit_destuffing(data):
    destuffed_data = ""
    count = 0
    for  bit in  data:
        if bit == "1":
            count += 1
        elif (count==5):
            count=0
            continue
        else:
            count=0
        destuffed_data += bit
    return destuffed_data

data =input("Enter the Message:")

stuffed_data = bit_stuffing(data)
print("Bit Stuffed Data: ", stuffed_data)
destuffed_data = bit_destuffing(stuffed_data)
print("Bit Destuffed Data: ", destuffed_data)
