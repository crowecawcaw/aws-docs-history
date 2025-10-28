# Inspecting compiled circuits

When a quantum circuit needs to be run on a hardware device, such as a quantum processing unit (QPU),
the circuit must first be compiled into an acceptable format that the device can understand and process.
For example, transpiling the high-level quantum circuit down to the specific native gates supported by
the target QPU hardware. Inspecting the actual compiled output of the quantum circuit can be extremely
useful for debugging and optimization purposes. This knowledge can help identify potential issues,
bottlenecks, or opportunities for improving the performance and efficiency of the quantum application.
You can view and analyze the compiled output of your quantum circuits for both Rigetti and
IQM quantum computing devices using the code provided below.

```
task = AwsQuantumTask(arn=task_id, aws_session=session)
# After the task has finished running
task_result = task.result()
compiled_circuit = task_result.get_compiled_circuit()
```

###### Note

Currently, viewing the compiled circuit output for IonQ devices is not supported.
