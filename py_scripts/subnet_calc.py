#/usr/bin/python3

'''
Subnet calculator (without ipaddress package)
'''

import sys

network_addr, sub_mask = sys.argv[1].split("/")
network_addr: list[str] = network_addr.split('.')
sub_mask: int = int(sub_mask)

#gets how much bits spill on the pivot octet
pivot_bits = sub_mask%8
#if no pivot bits -> no spillage, mask == 255
pivot_mask = _ if (_:=int(pivot_bits*"1" + (8-pivot_bits)*"0", 2)) else 255

#network incremental digit
block_size = 256 - pivot_mask

#number of subnetworks
sub_n = 256//block_size

print(
    f'Number of subnets : {sub_n}',
    f'Number of potential host adresses : {2**(32-sub_mask)}\n',
    sep='\n'
    )

#no bit spillage
if sub_mask%8==0:
    pivot_i = sub_mask//8

    temp_addr = list(network_addr)
    subn_net_addr = '.'.join(temp_addr[:pivot_i]) + (4-pivot_i)*'.0'
    subn_broadc_addr = '.'.join(temp_addr[:pivot_i]) + (4-pivot_i)*'.255'

    print(
        f"Network addr : {subn_net_addr} ",
        f"Broadcast addr : {subn_broadc_addr}",
        sep='\n'
        )

#bit spillage
else:
    pivot_i = sub_mask//8 - 1

    for n in range(sub_n):
        temp_addr = list(network_addr)
        subn_net_addr = '.'.join(temp_addr[:pivot_i+1]) + f'.{n*block_size}' + (2-pivot_i)*'.0'
        subn_broadc_addr = '.'.join(temp_addr[:pivot_i+1]) + f'.{(n+1)*block_size-1}' + (2-pivot_i)*'.255'

        print(
            f"Subnet {n} :",
            f"Network addr : {subn_net_addr} ",
            f"Broadcast addr : {subn_broadc_addr}\n",
            sep='\n'
            )
