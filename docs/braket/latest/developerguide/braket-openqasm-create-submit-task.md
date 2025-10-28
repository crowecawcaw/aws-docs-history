# Create and submit an example

OpenQASM 3.0 quantum task

You can use the Amazon Braket Python SDK, Boto3, or the AWS CLI to
submit OpenQASM 3.0 quantum tasks to an Amazon Braket device.

###### In this section:

- [An example OpenQASM 3.0 program](#braket-openqasm-example-program "#braket-openqasm-example-program")
- [Use the Python SDK to
  create OpenQASM 3.0 quantum tasks](#braket-openqasm-create-tasks-with-python-sdk "#braket-openqasm-create-tasks-with-python-sdk")
- [Use Boto3 to create
  OpenQASM 3.0 quantum tasks](#braket-openqasm-create-tasks-with-boto3 "#braket-openqasm-create-tasks-with-boto3")
- [Use the AWS CLI to create
  OpenQASM 3.0 tasks](#braket-openqasm-create-tasks-with-aws-cli "#braket-openqasm-create-tasks-with-aws-cli")

## An example OpenQASM 3.0 program

To create an OpenQASM 3.0 task, you can start with a basic OpenQASM 3.0 program
(ghz.qasm) that prepares a [GHZ state](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state "https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state") as shown in the following example.

```
// ghz.qasm
// Prepare a GHZ state
OPENQASM 3;

qubit[3] q;
bit[3] c;

h q[0];
cnot q[0], q[1];
cnot q[1], q[2];

c = measure q;
```

## Use the Python SDK to

create OpenQASM 3.0 quantum tasks

You can use the [Amazon Braket Python SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python") to submit this program to an Amazon Braket device with the following code.
Be sure to replace the example Amazon S3 bucket location “amzn-s3-demo-bucket” with your own Amazon S3 bucket name.

```
with open("ghz.qasm", "r") as ghz:
    ghz_qasm_string = ghz.read()

# Import the device module
from braket.aws import AwsDevice
# Choose the Rigetti device
device = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")
from braket.ir.openqasm import Program

program = Program(source=ghz_qasm_string)
my_task = device.run(program)

# Specify an optional s3 bucket location and number of shots
s3_location = ("amzn-s3-demo-bucket", "openqasm-tasks")
my_task = device.run(
    program,
    s3_location,
    shots=100,
)
```

## Use Boto3 to create

OpenQASM 3.0 quantum tasks

You can also use [AWS Python SDK for Braket (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html") to create the quantum tasks using
OpenQASM 3.0 strings, as shown in the following example. The following code snippet
references ghz.qasm that prepares a [GHZ state](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state "https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state") as shown above.

```
import boto3
import json

my_bucket = "amzn-s3-demo-bucket"
s3_prefix = "openqasm-tasks"

with open("ghz.qasm") as f:
    source = f.read()

action = {
    "braketSchemaHeader": {
        "name": "braket.ir.openqasm.program",
        "version": "1"
    },
    "source": source
}
device_parameters = {}
device_arn = "arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3"
shots = 100

braket_client = boto3.client('braket', region_name='us-west-1')
rsp = braket_client.create_quantum_task(
    action=json.dumps(
        action
    ),
    deviceParameters=json.dumps(
        device_parameters
    ),
    deviceArn=device_arn,
    shots=shots,
    outputS3Bucket=my_bucket,
    outputS3KeyPrefix=s3_prefix,
)
```

## Use the AWS CLI to create

OpenQASM 3.0 tasks

The [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") can also be
used to submit OpenQASM 3.0 programs, as shown in the following example.

```
aws braket create-quantum-task \
    --region "us-west-1" \
    --device-arn "arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3" \
    --shots 100 \
    --output-s3-bucket "amzn-s3-demo-bucket" \
    --output-s3-key-prefix "openqasm-tasks" \
    --action '{
        "braketSchemaHeader": {
            "name": "braket.ir.openqasm.program",
            "version": "1"
        },
        "source": $(cat ghz.qasm)
    }'
```
