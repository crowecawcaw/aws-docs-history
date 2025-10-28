# Scenario 3: Spot Instance running multi-node jobs is

interrupted

The job fails with a state code of `NODE_FAIL`, and the job is requeued (unless
`--no-requeue` was specified when the job was submitted). If the node is a static node, it's replaced.
If the node is a dynamic node, the node is terminated and reset. Other nodes that were running the terminated jobs
might be allocated to other pending jobs, or scaled down after the configured [SlurmSettings](Scheduling-v3.md#Scheduling-v3-SlurmSettings "Scheduling-v3.md#Scheduling-v3-SlurmSettings") /
[ScaledownIdletime](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-ScaledownIdletime "Scheduling-v3.md#yaml-Scheduling-SlurmSettings-ScaledownIdletime") time has passed.
