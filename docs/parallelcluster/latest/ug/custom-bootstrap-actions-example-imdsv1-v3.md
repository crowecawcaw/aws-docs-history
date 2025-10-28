# Example of how to update a configuration

for IMDSv1

The following is an example of a cluster configuration that supports IMDSv1 when using AWS ParallelCluster
versions 3.7.0 and older.

```
Region: `us-east-1`
Imds:
  ImdsSupport: v1.0
Image:
  Os: `alinux2`
HeadNode:
  InstanceType: `t2.micro`
  Networking:
    SubnetId: `subnet-abcdef01234567890`
  Ssh:
    KeyName: `key-name`
  CustomActions:
    OnNodeConfigured:
      Script: `Script-path`
Scheduling:
  Scheduler: slurm
  SlurmQueues:
  - Name: `queue1`
    CustomActions:
      OnNodeConfigured:
        Script: `Script-path`
    ComputeResources:
    - Name: `t2micro`
      Instances:
      - InstanceType: `t2.micro`
      MinCount: `1`1
    Networking:
      SubnetIds:
      - `subnet-abcdef01234567890`
```
