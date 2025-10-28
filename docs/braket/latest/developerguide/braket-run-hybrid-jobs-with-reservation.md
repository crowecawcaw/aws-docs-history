# Running hybrid jobs during a reservation

Once you have a Python function to run as a
hybrid job, you can run the hybrid job in a reservation by passing the `reservation_arn`
keyword argument. All the tasks within the hybrid job use the reservation ARN. Importantly, the hybrid
job with `reservation_arn`
_only spins up the classical compute once your reservation starts_.

###### Note

A hybrid job running during a reservation _only successfully runs_ quantum tasks on the reserved
device. Attempting to use a different on-demand Braket device will result in an error. If you need
to run tasks on both an on-demand simulator and the reserved device within the same hybrid job,
use `DirectReservation` instead.

The following code demonstrates how to run a hybrid job during a reservation.

```
from braket.aws import AwsDevice
from braket.devices import Devices
from braket.jobs import get_job_device_arn, hybrid_job

@hybrid_job(device=Devices.IonQ.Aria1, reservation_arn="<my_reservation_arn>")
def example_hybrid_job():
    # declare AwsDevice within the hybrid job
    device = AwsDevice(get_job_device_arn())
    bell = Circuit().h(0).cnot(0, 1)

    task = device.run(bell, shots=10)
```

For hybrid jobs that use a Python script (see the section on
[Creating your first Hybrid Job](braket-jobs-first.md "braket-jobs-first.md") in the developer guide),
you can run them within the reservation by passing the `reservation_arn` keyword argument when creating the job.

```
from braket.aws import AwsQuantumJob
from braket.devices import Devices

job = AwsQuantumJob.create(
    Devices.IonQ.Aria1,
    source_module="algorithm_script.py",
    entry_point="algorithm_script:start_here",
    reservation_arn="<my_reservation_arn>"
)
```
