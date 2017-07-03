"""
IDOL Protocol classification util.

Require : python3
Syntax of run command : python3 <name_of_program> <name_of_packets_stack>
"""

import sys

# Receivers
IVASYK = "Ivasyk"
DMYTRYK = "Dmytryk"
OSTAP = "Ostap"
LESYA = "Lesya"
# Sign values used to detect receiver.
IVASYK_SIGN_VAL = 0
LESYA_SIGN_VAL = "end"


def packets_to_file(receivers):
    """
     Function packets_to_file() used to write content of dictionary values
     to files with key as name of file.
    """
    for receiver in receivers:
        with open("{}.txt".format(receiver), "w") as file:
            for packet in receivers[receiver]:
                file.write("{}\n".format(packet))


def clasify_packets(packets, receivers):
    """
     Function clasify_packets() used to classify received packets.
     Packet represented by lines.
    """
    for packet in packets:
        packet = packet.strip('\n')
        if(len(packet) == 0):
            continue

        # if packet contain even number of symbols - it`s Ivasyk
        if(len(packet) % 2 == IVASYK_SIGN_VAL):
            (receivers[IVASYK]).append(packet)

        # if packet first letter is capitalized and it`s not for Ivasyk
        # - it`s Dmytryk
        elif(packet[0].isupper()):
            (receivers[DMYTRYK]).append(packet)

        # if packet is not for Lesya && not for anyone - it`s Ostap
        elif(packet[-len(LESYA_SIGN_VAL):] != LESYA_SIGN_VAL):
            (receivers[OSTAP]).append(packet)

        # if packet last letters is LESYA_SIGN_VAL - it`s Lesya
        if(packet[-len(LESYA_SIGN_VAL):] == LESYA_SIGN_VAL):
            (receivers[LESYA]).append(packet)


def open_logs(filePath):
    """
     Function open_logs() used to open file that contain all
     received packets. If something goes wrong, it print message to inform
     user about possible problem.
    """
    try:
        # attemp to open stack of IDOL packets
        with open(filePath, "r") as file:
            packets = file.readlines()
    except FileNotFoundError:
        print(" [Problem] | File doesn`t exist. Please, check file name.")
        exit(1)
    except Exception:
        print(""" [Problem] | Unknown type of problem. Please, send this
                              information to idolprotocol_support@gmail.com .""")
        exit(1)

    return packets


def main():
    """
     Function main() realize calls of all functions.
    """
    receivers = {IVASYK: [], DMYTRYK: [], OSTAP: [], LESYA: []}

    try:
        packets = open_logs(sys.argv[1])
    except IndexError:
        print(" [Problem] | You should enter name of file as first argument.")
        exit(1)

    clasify_packets(packets, receivers)
    packets_to_file(receivers)

    # unnecessary information. Just to see some result.
    print(" Sucessfully sorted.")


if __name__ == "__main__":
    main()

