# Sample packets
packets = [
    '0201060303E1FF1216E1FFA10364FFF4000FFF003772A33F23AC',
    '0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8',
    '0201060303E1FF1216E1FFA10364FFF60011FF003772A33F23AC',
    '0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8',
    '0201060303E1FF1216E1FFA10364FFF40011FF033772A33F23AC',
    '0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8'
]

for packet in packets:
    # Accelerometer packet
    if packet.startswith('0201060303E1FF'):
        x, y, z = int(packet[26:30], 16), int(packet[30:34], 16), int(packet[34:38], 16)
        stationary = x == y == z == 0
        print(f"Accelerometer {'Stationary' if stationary else 'Moving'}: x={x}, y={y}, z={z}")

    # iBeacon packet
    elif packet.startswith('0201061AFF4C000215'):
        mac_address = ':'.join([packet[i:i+2] for i in range(38, 50, 2)])
        print(f"MAC address: {mac_address}")