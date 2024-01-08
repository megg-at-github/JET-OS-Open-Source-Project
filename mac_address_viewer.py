import uuid

def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                            for ele in range(0, 8 * 6, 8)][::-1])
    return mac_address

print(f"MAC Address: {get_mac_address()}")
