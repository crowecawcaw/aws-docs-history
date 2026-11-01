

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Example of how to update a configuration for IMDSv1
<a name="custom-bootstrap-actions-example-imdsv1-v3"></a>

The following is an example of a cluster configuration that supports IMDSv1 when using AWS ParallelCluster versions 3.7.0 and older.

```
Region: {{us-east-1}}
Imds:
  ImdsSupport: v1.0
Image:
  Os: {{alinux2023}}
HeadNode:
  InstanceType: {{t2.micro}}
  Networking:
    SubnetId: {{subnet-abcdef01234567890}}
  Ssh:
    KeyName: {{key-name}}
  CustomActions:
    OnNodeConfigured:
      Script: {{Script-path}}
Scheduling:
  Scheduler: slurm
  SlurmQueues:
  - Name: {{queue1}}
    CustomActions:
      OnNodeConfigured:
        Script: {{Script-path}}
    ComputeResources:
    - Name: {{t2micro}}
      Instances:
      - InstanceType: {{t2.micro}}
      MinCount: {{1}}1
    Networking:
      SubnetIds:
      - {{subnet-abcdef01234567890}}
```