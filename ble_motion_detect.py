# Import necessary libraries
from bluepy.btle import Peripheral, UUID
import struct

# UUIDs for Accelerometer Service and Characteristics
ACCELEROMETER_SERVICE_UUID = UUID('0112233445566778899AABBCCDDEEFF0')
ACCELEROMETER_DATA_UUID = UUID('0112233445566778899AABBCCDDEEFF0')

try:
    # Connect to BLE device
    peripheral = Peripheral('00:90:78:56:34:12')

    # Get accelerometer service and data characteristics
    accelerometer_service = peripheral.getServiceByUUID(ACCELEROMETER_SERVICE_UUID)
    accelerometer_data = accelerometer_service.getCharacteristics(ACCELEROMETER_DATA_UUID)[0]

    # Read accelerometer data
    data = accelerometer_data.read()

    # Convert raw data to acceleration values
    x, y, z = struct.unpack('<hhh', data)

    # Detect movement
    if abs(x) > 100 or abs(y) > 100 or abs(z) > 100:
        print("The tag is moving")
    else:
        print("The tag is stationary")

    # Disconnect from BLE device
    peripheral.disconnect()

except Exception as e:
    print(f'Error connecting to BLE device: {e}')