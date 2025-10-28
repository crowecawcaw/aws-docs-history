# Example: Submitting a quantum task to a QPU

Amazon Braket allows you to run a quantum circuit on a QPU device. The
following example shows how to submit a quantum task to Rigetti or
IonQ devices.

**Choose the Rigetti Ankaa-3 device, then look at
the associated connectivity graph**

```
# import the QPU module
from braket.aws import AwsDevice
# choose the Rigetti device
device = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")

# take a look at the device connectivity graph
device.properties.dict()['paradigm']['connectivity']
```

```
{'fullyConnected': False,
 'connectivityGraph': {'0': ['1', '7'],
  '1': ['0', '2', '8'],
  '2': ['1', '3', '9'],
  '3': ['2', '4', '10'],
  '4': ['3', '5', '11'],
  '5': ['4', '6', '12'],
  '6': ['5', '13'],
  '7': ['0', '8', '14'],
  '8': ['1', '7', '9', '15'],
  '9': ['2', '8', '10', '16'],
  '10': ['3', '9', '11', '17'],
  '11': ['4', '10', '12', '18'],
  '12': ['5', '11', '13', '19'],
  '13': ['6', '12', '20'],
  '14': ['7', '15', '21'],
  '15': ['8', '14', '22'],
  '16': ['9', '17', '23'],
  '17': ['10', '16', '18', '24'],
  '18': ['11', '17', '19', '25'],
  '19': ['12', '18', '20', '26'],
  '20': ['13', '19', '27'],
  '21': ['14', '22', '28'],
  '22': ['15', '21', '23', '29'],
  '23': ['16', '22', '24', '30'],
  '24': ['17', '23', '25', '31'],
  '25': ['18', '24', '26', '32'],
  '26': ['19', '25', '33'],
  '27': ['20', '34'],
  '28': ['21', '29', '35'],
  '29': ['22', '28', '30', '36'],
  '30': ['23', '29', '31', '37'],
  '31': ['24', '30', '32', '38'],
  '32': ['25', '31', '33', '39'],
  '33': ['26', '32', '34', '40'],
  '34': ['27', '33', '41'],
  '35': ['28', '36', '42'],
  '36': ['29', '35', '37', '43'],
  '37': ['30', '36', '38', '44'],
  '38': ['31', '37', '39', '45'],
  '39': ['32', '38', '40', '46'],
  '40': ['33', '39', '41', '47'],
  '41': ['34', '40', '48'],
  '42': ['35', '43', '49'],
  '43': ['36', '42', '44', '50'],
  '44': ['37', '43', '45', '51'],
  '45': ['38', '44', '46', '52'],
  '46': ['39', '45', '47', '53'],
  '47': ['40', '46', '48', '54'],
  '48': ['41', '47', '55'],
  '49': ['42', '56'],
  '50': ['43', '51', '57'],
  '51': ['44', '50', '52', '58'],
  '52': ['45', '51', '53', '59'],
  '53': ['46', '52', '54'],
  '54': ['47', '53', '55', '61'],
  '55': ['48', '54', '62'],
  '56': ['49', '57', '63'],
  '57': ['50', '56', '58', '64'],
  '58': ['51', '57', '59', '65'],
  '59': ['52', '58', '60', '66'],
  '60': ['59'],
  '61': ['54', '62', '68'],
  '62': ['55', '61', '69'],
  '63': ['56', '64', '70'],
  '64': ['57', '63', '65', '71'],
  '65': ['58', '64', '66', '72'],
  '66': ['59', '65', '67'],
  '67': ['66', '68'],
  '68': ['61', '67', '69', '75'],
  '69': ['62', '68', '76'],
  '70': ['63', '71', '77'],
  '71': ['64', '70', '72', '78'],
  '72': ['65', '71', '73', '79'],
  '73': ['72', '80'],
  '75': ['68', '76', '82'],
  '76': ['69', '75', '83'],
  '77': ['70', '78'],
  '78': ['71', '77', '79'],
  '79': ['72', '78', '80'],
  '80': ['73', '79', '81'],
  '81': ['80', '82'],
  '82': ['75', '81', '83'],
  '83': ['76', '82']}}
```

The preceding dictionary `connectivityGraph` lists the neighboring
qubits for each qubit in the Rigetti device.

**Choose the IonQ Aria-1 device**

For the IonQ Aria-1 device, the `connectivityGraph` is
empty, as shown in the following example, because the device offers
_all-to-all_ connectivity. Therefore, a detailed
`connectivityGraph` is not needed.

```
# or choose the IonQ Aria-1 device
device = AwsDevice("arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1")

# take a look at the device connectivity graph
device.properties.dict()['paradigm']['connectivity']
```

```
{'fullyConnected': True, 'connectivityGraph': {}}
```

As shown in the following example, you have the option to adjust the
shots (default=1000), the `poll_timeout_seconds` (default =
432000 = 5 days), the `poll_interval_seconds` (default = 1), and the location
of the S3 bucket (`s3_location`) where your results will be stored if you
choose to specify a location other than the default bucket.

```
my_task = device.run(circ, s3_location = 'amazon-braket-my-folder', shots=100, poll_timeout_seconds = 100, poll_interval_seconds = 10)
```

The IonQ and Rigetti devices compile the provided
circuit into their respective native gate sets automatically, and they map the abstract
qubit indices to physical qubits on the respective
QPU.

###### Note

QPU devices have limited capacity. You can expect longer wait times when capacity
is reached.

Amazon Braket can run QPU quantum tasks within certain availability windows,
but you can still submit quantum tasks any time (24/7) because all corresponding data and
metadata are stored reliably in the appropriate S3 bucket. As shown in the next section,
you can recover your quantum task using `AwsQuantumTask` and your unique quantum task
ID.
