# Running Braket hybrid jobs in your own container

To create a hybrid job with your own container, call `AwsQuantumJob.create()` with the argument
`image_uri` specified. You can use a QPU, an on-demand simulator, or run your code locally on the
classical processor available with Braket Hybrid Jobs. We recommend testing your code out on a simulator
like SV1, DM1, or TN1 before running on a real QPU.

To run your code on the classical processor, specify the `instanceType` and the `instanceCount`
you use by updating the `InstanceConfig`. Note that if you specify an `instance_count` > 1,
you need to make sure that your code can run across multiple hosts. The upper limit for the number of
instances you can choose is 5. For example:

```
job = AwsQuantumJob.create(
    source_module="source_dir",
    entry_point="source_dir.algorithm_script:start_here",
    image_uri="111122223333.dkr.ecr.us-west-2.amazonaws.com/my-byoc-container:latest",
    instance_config=InstanceConfig(instanceType="ml.p3.8xlarge", instanceCount=3),
    device="local:braket/braket.local.qubit",
    # ...)
```

###### Note

Use the device ARN to track the simulator you used as hybrid job metadata.
Acceptable values must follow the format `device = "local:<provider>/<simulator_name>"`.
Remember that `<provider>` and `<simulator_name>` must consist only of letters,
numbers, `_`, `-`, and `.` . The string is limited to 256 characters.

If you plan to use BYOC and you're not using the Braket SDK to create quantum tasks, you should pass the
value of the environmental variable `AMZN_BRAKET_JOB_TOKEN` to the `jobToken` parameter
in the `CreateQuantumTask` request. If you don't, the quantum tasks don't get priority and
are billed as regular standalone quantum tasks.
