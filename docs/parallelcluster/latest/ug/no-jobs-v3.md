# Scenario 1: Spot Instance with no running jobs is interrupted

When this interruption occurs, AWS ParallelCluster tries to replace the instance if the scheduler queue has pending jobs that require additional
instances, or if the number of active instances is lower than the [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") /
[ComputeResources](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources "Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources") / [MinCount](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-MinCount "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-MinCount"). If AWS ParallelCluster can't provision new instances, then
a request for new instances is periodically repeated.
