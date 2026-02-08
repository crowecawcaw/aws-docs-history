# Running quantum tasks during a reservation

After obtaining a valid reservation ARN from [Create a reservation](braket-reservations.md#braket-create-a-reservation "braket-reservations.md#braket-create-a-reservation"), you can create quantum tasks to run during the reservation. Quantum tasks and hybrid jobs submitted with a reservation ARN will not show up in a device queue. Tasks submitted before reservation start time will remain in the `QUEUED` state until your reservation begins.

###### Note

Reservations are AWS account and device-specific. Only the AWS account that created the reservation can use your reservation ARN.

During a reservation, both reservation and regular tasks can be created. To verify that a created Braket quantum task is associated with a reservation, check the “Reservation ARN” field on the page of the quantum task in the Braket console, or query the same field in the task metadata using the SDK. The rest of this page describes how to specify which tasks are associated to the reseravation.

You can create quantum tasks using Python SDKs such as
[Braket](braket-references.md "braket-references.md"), [CUDA-Q](https://github.com/NVIDIA/cuda-quantum "https://github.com/NVIDIA/cuda-quantum"), [PennyLane](https://github.com/amazon-braket/amazon-braket-pennylane-plugin-python "https://github.com/amazon-braket/amazon-braket-pennylane-plugin-python"), [Qiskit](https://github.com/qiskit-community/qiskit-braket-provider "https://github.com/qiskit-community/qiskit-braket-provider"), or directly with boto3 ([Working with Boto3](braket-using-boto3.md "braket-using-boto3.md")). To use reservations, you must have version [v1.79.0](https://github.com/amazon-braket/amazon-braket-sdk-python/releases/tag/v1.79.0 "https://github.com/amazon-braket/amazon-braket-sdk-python/releases/tag/v1.79.0") or higher of the [Amazon Braket Python SDK](https://github.com/amazon-braket/amazon-braket-sdk-python "https://github.com/amazon-braket/amazon-braket-sdk-python"). You can update to the latest Braket SDK, Qiskit provider and PennyLane plugin with the following code.

```
pip install --upgrade amazon-braket-sdk amazon-braket-pennylane-plugin qiskit-braket-provider
```

**Run tasks with the `DirectReservation` context manager**

The recommended way to run a task within your scheduled reservation is to use the `DirectReservation` context manager.
By specifying your target device and reservation ARN, the context manager ensures that all tasks created within the Python
`with` statement are run with exclusive access to the device.

First, define a quantum circuit and the device. Then use the reservation context and run the task. **Ensure that your entire workload is run inside the `with` block; anything run outside the scope of the `with` block will not be associated with your reservation!**

```
from braket.aws import AwsDevice, DirectReservation
from braket.circuits import Circuit
from braket.devices import Devices

bell = Circuit().h(0).cnot(0, 1)
device = AwsDevice(Devices.IonQ.Aria1)

# run the circuit in a reservation
with DirectReservation(device, reservation_arn="<my_reservation_arn>"):
    task = device.run(bell, shots=100)
```

You can create quantum tasks in a reservation using CUDA-Q, PennyLane, and Qiskit plugins, as long as the `DirectReservation` context is active while creating quantum tasks. For example, with the Qiskit-Braket provider, you can run tasks as follows.

```
from braket.devices import Devices
from braket.aws import DirectReservation
from qiskit import QuantumCircuit
from qiskit_braket_provider import BraketProvider


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

aria = BraketProvider().get_backend("Aria 1")

# run the circuit in a reservation
with DirectReservation(Devices.IonQ.Aria1, reservation_arn="<my_reservation_arn>"):
    aria_task = aria.run(qc, shots=10)
```

Similarly, the following code runs a circuit during a reservation using the Braket-PennyLane plugin.

```
from braket.devices import Devices
from braket.aws import DirectReservation
import pennylane as qml


dev = qml.device("braket.aws.qubit", device_arn=Devices.IonQ.Aria1.value, wires=2, shots=10)

@qml.qnode(dev)
def bell_state():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

# run the circuit in a reservation
with DirectReservation(Devices.IonQ.Aria1, reservation_arn="<my_reservation_arn>"):
    probs = bell_state()
```

**Manually setting the reservation context**

Alternatively, you can manually set the reservation context with the following code.

```
# set reservation context
reservation_context = DirectReservation(device, reservation_arn="<my_reservation_arn>").start()

# run circuit during reservation
task = device.run(bell, shots=100)
```

This is ideal for Jupyter notebooks where the context can be run in the first cell and all subsequent tasks will run in the reservation.

###### Note

The cell containing the `.start()` call should _only be run once_.

To switch back to the on-demand mode: Restart the Jupyter notebook, or call the following to change the context back to on-demand mode.

```
reservation_context.stop()  # unset reservation context
```

###### Note

Reservations have a pre-determined start and end time (see [Create a reservation](braket-reservations.md#braket-create-a-reservation "braket-reservations.md#braket-create-a-reservation")). The `reservation_context.start()` and `reservation_context.stop()` methods **do not begin or terminate a reservation**. Instead, while the context is active, any quantum tasks that you create will be associated with your reservation, and will run only during your scheduled reservation. The reservation context has no effect on the scheduled reservation time.

**Explicitly pass the reservation ARN when creating task**

Another way to create tasks during a reservation is to explicitly pass the reservation ARN when calling `device.run()`.

```
task = device.run(bell, shots=100, reservation_arn="<my_reservation_arn>")
```

This method directly associates the quantum task with the reservation ARN, ensuring it runs during the reserved period. For this option, add the reservation ARN to each task you plan to run during a reservation. However, note that when using third-party libraries such as Qiskit or PennyLane, it may be difficult to ensure that submitted tasks are using the correct reservation ARN. For this reason, using the DirectReservation context manager is recommended.

When directly using boto3, pass the reservation ARN as an association when creating a task.

```
import boto3

braket_client = boto3.client("braket")


kwargs["associations"] = [
    {
        "arn": "<my_reservation_arn>",
        "type": "RESERVATION_TIME_WINDOW_ARN",
    }
]

response = braket_client.create_quantum_task(**kwargs)
```
