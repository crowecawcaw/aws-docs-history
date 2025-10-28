# Turn on the Amazon Braket Boto3

client

To use Boto3 with Amazon Braket, you must import Boto3 and then
define a client that you use to connect to the Amazon Braket
API. In the following example, the Boto3 client is named
`braket`.

```
import boto3
import botocore

braket = boto3.client("braket")
```

###### Note

[Braket supports IPv6](../../../vpc/latest/userguide/aws-ipv6-support.md "../../../vpc/latest/userguide/aws-ipv6-support.md").
If you are using an IPv6-only network or wish to ensure your workload uses IPv6 traffic, use the dual-stack endpoints as
outlined in the [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md") guide.

Now that you have a `braket` client established, you can make requests and
process responses from the Amazon Braket service. You can get more
detail on request and response data in the [API Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html").

###### The following examples show how to work with devices and quantum

tasks.

- [Search for
  devices](#braket-using-boto3-example-search-devices "#braket-using-boto3-example-search-devices")
- [Retrieve a
  device](#braket-using-boto3-example-retrieve-devices "#braket-using-boto3-example-retrieve-devices")
- [Create a quantum task](#braket-using-boto3-example-create-task "#braket-using-boto3-example-create-task")
- [Retrieve a quantum task](#braket-using-boto3-example-retrieve-task "#braket-using-boto3-example-retrieve-task")
- [Search for quantum tasks](#braket-using-boto3-example-search-tasks "#braket-using-boto3-example-search-tasks")
- [Cancel quantum task](#braket-using-boto3-example-cancel-task "#braket-using-boto3-example-cancel-task")

## Search for

devices

- `search_devices(**kwargs)`

Search for devices using the specified filters.

```
# Pass search filters and optional parameters when sending the
# request and capture the response
response = braket.search_devices(filters=[{
    'name': 'deviceArn',
    'values': ['arn:aws:braket:::device/quantum-simulator/amazon/sv1']
}], maxResults=10)

print(f"Found {len(response['devices'])} devices")

for i in range(len(response['devices'])):
    device = response['devices'][i]
    print(device['deviceArn'])
```

## Retrieve a

device

- `get_device(deviceArn)`

Retrieve the devices available in Amazon Braket.

```
# Pass the device ARN when sending the request and capture the repsonse
response = braket.get_device(deviceArn='arn:aws:braket:::device/quantum-simulator/amazon/sv1')

print(f"Device {response['deviceName']} is {response['deviceStatus']}")
```

## Create a quantum task

- `create_quantum_task(**kwargs)`

Create a quantum task.

```
# Create parameters to pass into create_quantum_task()
kwargs = {
    # Create a Bell pair
    'action': '{"braketSchemaHeader": {"name": "braket.ir.jaqcd.program", "version": "1"}, "results": [], "basis_rotation_instructions": [], "instructions": [{"type": "h", "target": 0}, {"type": "cnot", "control": 0, "target": 1}]}',
    # Specify the SV1 Device ARN
    'deviceArn': 'arn:aws:braket:::device/quantum-simulator/amazon/sv1',
    # Specify 2 qubits for the Bell pair
    'deviceParameters': '{"braketSchemaHeader": {"name": "braket.device_schema.simulators.gate_model_simulator_device_parameters", "version": "1"}, "paradigmParameters": {"braketSchemaHeader": {"name": "braket.device_schema.gate_model_parameters", "version": "1"}, "qubitCount": 2}}',
    # Specify where results should be placed when the quantum task completes.
    # You must ensure the S3 Bucket exists before calling create_quantum_task()
    'outputS3Bucket': 'amazon-braket-examples',
    'outputS3KeyPrefix': 'boto-examples',
    # Specify number of shots for the quantum task
    'shots': 100
}

# Send the request and capture the response
response = braket.create_quantum_task(**kwargs)

print(f"Quantum task {response['quantumTaskArn']} created")
```

## Retrieve a quantum task

- `get_quantum_task(quantumTaskArn)`

Retrieve the specified quantum task.

```
# Pass the quantum task ARN when sending the request and capture the response
response = braket.get_quantum_task(quantumTaskArn='arn:aws:braket:us-west-1:123456789012:quantum-task/ce78c429-cef5-45f2-88da-123456789012')

print(response['status'])
```

## Search for quantum tasks

- `search_quantum_tasks(**kwargs)`

Search for quantum tasks that match the specified filter values.

```
# Pass search filters and optional parameters when sending the
# request and capture the response
response = braket.search_quantum_tasks(filters=[{
    'name': 'deviceArn',
    'operator': 'EQUAL',
    'values': ['arn:aws:braket:::device/quantum-simulator/amazon/sv1']
}], maxResults=25)

print(f"Found {len(response['quantumTasks'])} quantum tasks")

for n in range(len(response['quantumTasks'])):
    task = response['quantumTasks'][n]
    print(f"Quantum task {task['quantumTaskArn']} for {task['deviceArn']} is {task['status']}")
```

## Cancel quantum task

- `cancel_quantum_task(quantumTaskArn)`

Cancel the specified quantum task.

```
# Pass the quantum task ARN when sending the request and capture the response
response = braket.cancel_quantum_task(quantumTaskArn='arn:aws:braket:us-west-1:123456789012:quantum-task/ce78c429-cef5-45f2-88da-123456789012')

print(f"Quantum task {response['quantumTaskArn']} is {response['cancellationStatus']}")
```
