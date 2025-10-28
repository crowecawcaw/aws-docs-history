# Tracking quantum tasks from the Amazon Braket SDK

The command `device.run(…​)` defines a quantum task with a unique quantum task ID. You can
query and track the status with `task.state()` as shown in the following
example.

**Note**: `task = device.run()` is an
asynchronous operation, which means that you can keep working while the system processes
your quantum task in the background.

**Retrieve a result**

When you call `task.result()`, the SDK begins polling
Amazon Braket to see whether the quantum task is complete. The SDK uses the
polling parameters you defined in `.run()`. After the quantum task is complete, the
SDK retrieves the result from the S3 bucket and returns it as a
`QuantumTaskResult` object.

```
# create a circuit, specify the device and run the circuit
circ = Circuit().rx(0, 0.15).ry(1, 0.2).cnot(0,2)
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
task = device.run(circ, s3_location, shots=1000)

# get ID and status of submitted task
task_id = task.id
status = task.state()
print('ID of task:', task_id)
print('Status of task:', status)
# wait for job to complete
while status != 'COMPLETED':
    status = task.state()
    print('Status:', status)
```

```
ID of task:
arn:aws:braket:us-west-2:123412341234:quantum-task/b68ae94b-1547-4d1d-aa92-1500b82c300d
Status of task: QUEUED
Status: QUEUED
Status: QUEUED
Status: QUEUED
Status: QUEUED
Status: QUEUED
Status: QUEUED
Status: QUEUED
Status: RUNNING
Status: RUNNING
Status: COMPLETED
```

**Cancel a quantum task**

To cancel a quantum task, call the `cancel()` method, as shown in the following
example.

```
# cancel quantum task
task.cancel()
status = task.state()
print('Status of task:', status)
```

```
Status of task: CANCELLING
```

**Check the metadata**

You can check the metadata of the finished quantum task, as shown in the following
example.

```
# get the metadata of the quantum task
metadata = task.metadata()
# example of metadata
shots = metadata['shots']
date = metadata['ResponseMetadata']['HTTPHeaders']['date']
# print example metadata
print("{} shots taken on {}.".format(shots, date))

# print name of the s3 bucket where the result is saved
results_bucket = metadata['outputS3Bucket']
print('Bucket where results are stored:', results_bucket)
# print the s3 object key (folder name)
results_object_key = metadata['outputS3Directory']
print('S3 object key:', results_object_key)

# the entire look-up string of the saved result data
look_up = 's3://'+results_bucket+'/'+results_object_key
print('S3 URI:', look_up)
```

```
1000 shots taken on Wed, 05 Aug 2020 14:44:22 GMT.
Bucket where results are stored: amazon-braket-123412341234
S3 object key: simulation-output/b68ae94b-1547-4d1d-aa92-1500b82c300d
S3 URI: s3://amazon-braket-123412341234/simulation-output/b68ae94b-1547-4d1d-aa92-1500b82c300d
```

**Retrieve a quantum task or result**

If your kernel dies after you submit the quantum task or if you close your notebook or
computer, you can reconstruct the `task` object with its unique ARN (quantum task
ID). Then you can call `task.result()` to get the result from the S3 bucket
where it is stored.

```
from braket.aws import AwsSession, AwsQuantumTask

# restore task with unique arn
task_load = AwsQuantumTask(arn=task_id)
# retrieve the result of the task
result = task_load.result()
```
