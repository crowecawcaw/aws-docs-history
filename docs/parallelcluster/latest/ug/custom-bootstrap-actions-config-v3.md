# Configuration settings to define actions

and arguments

The following configuration settings are used to define
[HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[CustomActions](HeadNode-v3.md#HeadNode-v3-CustomActions "HeadNode-v3.md#HeadNode-v3-CustomActions") /
[OnNodeStart](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeStart "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeStart") &
[OnNodeConfigured](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeConfigured "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeConfigured") &
[OnNodeUpdated](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated") and
[Scheduling](Scheduling-v3.md "Scheduling-v3.md") /
[CustomActions](Scheduling-v3.md#Scheduling-v3-SlurmQueues-CustomActions "Scheduling-v3.md#Scheduling-v3-SlurmQueues-CustomActions") /
[OnNodeStart](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart") &
[OnNodeConfigured](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeConfigured "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeConfigured")
actions and arguments.

```
HeadNode:
  [...]
  CustomActions:
    OnNodeStart:
      # Script URL. This is run before any of the bootstrap scripts are run
      Script: s3://`amzn-s3-demo-bucket`/`on-node-start.sh`
      Args:
        - arg1
    OnNodeConfigured:
      # Script URL. This is run after all the bootstrap scripts are run
      Script: s3://`amzn-s3-demo-bucket`/`on-node-configured.sh`
      Args:
        - arg1
    OnNodeUpdated:
      # Script URL. This is run after the head node update is completed.
      Script: s3://`amzn-s3-demo-bucket`/`on-node-updated.sh`
      Args:
        - arg1
  # Bucket permissions
  Iam:
    S3Access:
      - BucketName: `bucket_name`
        EnableWriteAccess: false
Scheduling:
  Scheduler: slurm
   [...]
  SlurmQueues:
    - Name: queue1
      [...]
      CustomActions:
        OnNodeStart:
          Script: s3://`amzn-s3-demo-bucket`/`on-node-start.sh`
          Args:
            - arg1
        OnNodeConfigured:
          Script: s3://`amzn-s3-demo-bucket`/`on-node-configured.sh`
          Args:
            - arg1
      Iam:
        S3Access:
          - BucketName: `bucket_name`
            EnableWriteAccess: false
```

Using the `Sequence` setting (added in AWS ParallelCluster version 3.6.0):

```
HeadNode:
  [...]
  CustomActions:
    OnNodeStart:
      # Script URLs. The scripts are run in the same order as listed in the configuration, before any of the bootstrap scripts are run.
      Sequence:
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-start1.sh`
          Args:
            - arg1
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-start2.sh`
          Args:
            - arg1
        [...]
    OnNodeConfigured:
      # Script URLs. The scripts are run in the same order as listed in the configuration, after all the bootstrap scripts are run.
      Sequence:
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-configured1.sh`
          Args:
            - arg1
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-configured2.sh`
          Args:
            - arg1
        [...]
    OnNodeUpdated:
      # Script URLs. The scripts are run in the same order as listed in the configuration, after the head node update is completed.
      Sequence:
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-updated1.sh`
          Args:
            - arg1
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-updated2.sh`
          Args:
            - arg1
        [...]
  # Bucket permissions
  Iam:
    S3Access:
      - BucketName: `bucket_name`
        EnableWriteAccess: false
Scheduling:
  Scheduler: slurm
   [...]
  SlurmQueues:
    - Name: queue1
      [...]
      CustomActions:
        OnNodeStart:
          # Script URLs. The scripts are run in the same order as listed in the configuration, before any of the bootstrap scripts are run
          Sequence:
            - Script: s3://`amzn-s3-demo-bucket`/`on-node-start1.sh`
              Args:
                - arg1
            - Script: s3://`amzn-s3-demo-bucket`/`on-node-start2.sh`
              Args:
                - arg1
            [...]
        OnNodeConfigured:
          # Script URLs. The scripts are run in the same order as listed in the configuration, after all the bootstrap scripts are run
          Sequence:
            - Script: s3://`amzn-s3-demo-bucket`/`on-node-configured1.sh`
              Args:
                - arg1
            - Script: s3://`amzn-s3-demo-bucket`/`on-node-configured2.sh`
              Args:
                - arg1
            [...]
      Iam:
        S3Access:
          - BucketName: `bucket_name`
            EnableWriteAccess: false
```

The `Sequence` setting is added starting with AWS ParallelCluster version 3.6.0.
When you specify `Sequence`, you can list multiple scripts for a custom action.
AWS ParallelCluster continues to support configuring a custom action with a single script,
without including `Sequence`.

AWS ParallelCluster doesn't support including both a single script and `Sequence`
for the same custom action. For example, AWS ParallelCluster fails if you specify the following
configuration.

```
[...]
  CustomActions:
    OnNodeStart:
      # Script URL. This is run before any of the bootstrap scripts are run
      Script: s3://`amzn-s3-demo-bucket`/`on-node-start.sh`
          Args:
            - arg1
      # Script URLs. The scripts are run in the same order as listed in the configuration, before any of the bootstrap scripts are run.
      Sequence:
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-start1.sh`
          Args:
            - arg1
        - Script: s3://`amzn-s3-demo-bucket`/`on-node-start2.sh`
          Args:
            - arg1
[...]
```
