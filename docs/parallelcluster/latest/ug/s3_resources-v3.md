# Working with Amazon S3

You can configure AWS ParallelCluster's access to Amazon S3 through the [HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[Iam](HeadNode-v3.md#HeadNode-v3-Iam "HeadNode-v3.md#HeadNode-v3-Iam") / [S3Access](HeadNode-v3.md#yaml-HeadNode-Iam-S3Access "HeadNode-v3.md#yaml-HeadNode-Iam-S3Access") and
[Scheduling](Scheduling-v3.md "Scheduling-v3.md") / [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [- Name](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Name "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Name") /
[Iam](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Iam "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Iam") / [S3Access](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Iam-S3Access "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Iam-S3Access")
parameters in the AWS ParallelCluster configuration.

## Examples

The following example configures read-only access to all objects in `firstbucket/read_only/` and
read/write access to all objects in `secondbucket/read_and_write/`.

```
...
HeadNode:
  ...
  Iam:
    S3Access:
      - BucketName: `firstbucket`
        KeyName: `read_only/*`
        EnableWriteAccess: `false`
      - BucketName: `secondbucket`
        KeyName: `read_and_write/*`
        EnableWriteAccess: `true`
...
```

The next example configures read-only access to all objects in folder `read_only/` in any bucket (\*) in the account.

```
...
HeadNode:
  ...
  Iam:
    S3Access:
      - BucketName: `*`
        KeyName: `read_only/*`
        EnableWriteAccess: `false`
...
```

The final example configures read_only access to all buckets and objects in the account.

```
...
HeadNode:
  ...
  Iam:
    S3Access:
      - BucketName: *
...
```
