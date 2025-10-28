# Local quantum device emulator

With Amazon Braket's local emulator tool, you can emulate your verbatim quantum programs
locally before running them on actual quantum hardware. The emulator uses device calibration
data to validate the verbatim circuits, allowing you to catch compatibility issues earlier.

Additionally, the local emulator simulates quantum hardware noise through the following process:

- Using device calibration data to construct the noise model
- Applying depolarizing noise to each gate in your circuit
- Applying readout error at the end of your circuit
- Simulating the noisy circuit with a local density matrix simulator
  For more information on using a local emulator, see
  [Local emulation for verbatim circuits on Amazon Braket](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/braket_features/Device_emulation/01_Local_Emulation_for_Verbatim_Circuits_on_Amazon_Braket.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/braket_features/Device_emulation/01_Local_Emulation_for_Verbatim_Circuits_on_Amazon_Braket.ipynb") in the amazon-braket-examples GitHub repository.

###### In this section:

- [Benefits of local emulation](#braket-local-emulator-benefits "#braket-local-emulator-benefits")
- [Create a local emulator](#braket-create-local-emulator "#braket-create-local-emulator")

## Benefits of local emulation

- Validate verbatim circuits against device constraints using real-time or historical calibration data.
- Debug issues before submitting tasks to quantum hardware.
- Compare noiseless and noisy emulations with hardware results to understand noise effects.
- Streamline the workflow of developing noise aware quantum algorithms.

## Create a local emulator

A local quantum device emulator can be created directly from a quantum device or a set of
device properties. When directly emulating a device, the emulator uses the most recent calibration
data from the instantiated device. The following code example demonstrates how to directly emulate Rigetti's Ankaa-3
device.

```
from braket.aws.aws_device import AwsDevice

ankaa3 = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")
ankaa3_emulator = ankaa3.emulator()
```

The following example shows creating a local device emulator from a set of Ankaa-3 device properties in the JSON format.

```
from braket.aws import AwsDevice
from braket.emulation.local_emulator import LocalEmulator
import json

# Instantiate the device
ankaa3 = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")
ankaa3_properties = ankaa3.properties

# Put the Ankaa-3 properties in a file named ankaa3_device_properties.json
with open("ankaa3_device_properties.json", "w") as f:
    json.dump(ankaa3_properties.json(), f)

# Load the json into the ankaa3_data_json variable
with open("ankaa3_device_properties.json", "r") as json_file:
    ankaa3_data_json = json.load(json_file)

# Create the Ankaa-3 local emulator from the json file you created
ankaa3_emulator = LocalEmulator.from_json(ankaa3_data_json)
```

You can customize the example by:

- Using properties from a different QPU device
- Specifying a different JSON file for the emulator
- Changing the values of the device properties before instantiating the emulator
