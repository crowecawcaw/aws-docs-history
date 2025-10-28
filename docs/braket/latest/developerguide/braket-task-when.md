# When will my quantum task run?

When you submit a circuit, Amazon Braket sends it to the device you specify.
Quantum Processing Unit (QPU) and on-demand simulator quantum tasks are queued
and processed in the order they are received. The time required to process your
quantum task after you submit it varies depending on the number and complexity
of tasks submitted by other Amazon Braket customers and the availability of the QPU selected.

###### In this section:

- [QPU availability windows and status](#braket-qpu-availability "#braket-qpu-availability")
- [Queue visibility](#braket-queue-visibility "#braket-queue-visibility")
- [Set up email or SMS notifications](status-change-notifications-in-email-or-sms.md "status-change-notifications-in-email-or-sms.md")

## QPU availability windows and status

QPU availability varies from device to device.

In the **Devices** page of the Amazon Braket
console, you can see the current and upcoming availability windows and device
status. Additionally, each device page shows individual queue depths for quantum
tasks and hybrid jobs.

A device is considered _offline_ if is not available to customers, regardless of availability window. For example, it could be offline due to scheduled maintenance, upgrades, or operational issues.

## Queue visibility

Before submitting a quantum task or hybrid job, you can view how many quantum tasks
or hybrid jobs are in front of you by checking device queue depth.

**Queue depth**

Queue depth refers to the number of quantum tasks
and hybrid jobs queued for a particular device. A device's quantum
task and hybrid job queue count are accessible through the Braket Software
Development Kit (SDK) or Amazon Braket Management Console.

1. _Task queue depth_ refers to the
   total number of quantum tasks currently waiting to run in normal priority.
2. _Priority task queue depth_ refers
   to the total number of submitted quantum tasks waiting to run through Amazon Braket
   Hybrid Jobs. These tasks run before standalone tasks.
3. _Hybrid jobs queue depth_ refers
   to the total number of hybrid jobs currently queued on a device.
   Quantum tasks submitted as part of a hybrid job have priority, and
   are aggregated in the Priority Task Queue.

Customers wishing to view queue depth through the Braket SDK can modify
the following code snippet to get the queue position of their quantum task
or hybrid job:

```
device = AwsDevice("arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1")

# returns the number of quantum tasks queued on the device
print(device.queue_depth().quantum_tasks)
{<QueueType.NORMAL: 'Normal'>: '0', <QueueType.PRIORITY: 'Priority'>: '0'}


# returns the number of hybrid jobs queued on the device
print(device.queue_depth().jobs)
'3'

```

Submitting a quantum task or hybrid job to a QPU may result in your workload being
in a `QUEUED` state. Amazon Braket provides customers visibility into their
quantum task and hybrid job queue position.

**Queue position**

Queue position refers to the current position of your quantum task
or hybrid job within a respective device queue. It can be obtained for quantum tasks
or hybrid jobs through the Braket Software Development Kit (SDK) or
Amazon Braket Management Console.

Customers wishing to view queue position through the Braket SDK can
modify the following code snippet to get the queue position of their quantum task or hybrid job:

```
# choose the device to run your circuit
device = AwsDevice("arn:aws:braket:eu-north-1::device/qpu/iqm/Garnet")

#execute the circuit
task = device.run(bell, s3_folder, shots=100)

# retrieve the queue position information
print(task.queue_position().queue_position)

# Returns the number of Quantum Tasks queued ahead of you
'2'


from braket.aws import AwsQuantumJob

job = AwsQuantumJob.create(
    "arn:aws:braket:eu-north-1::device/qpu/iqm/Garnet",
    source_module="algorithm_script.py",
    entry_point="algorithm_script:start_here",
    wait_until_complete=False
)

# retrieve the queue position information
print(job.queue_position().queue_position)
'3' # returns the number of hybrid jobs queued ahead of you
```
