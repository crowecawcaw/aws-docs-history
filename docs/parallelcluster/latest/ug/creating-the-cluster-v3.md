# Configure and create the cluster

The following is an example cluster configuration that includes an Amazon Elastic Block Store shared file system with encryption.

```

Region: `eu-west-1`
Image:
  Os: alinux2
HeadNode:
  InstanceType: t2.micro
  Networking:
    SubnetId: subnet-`abcdef01234567890`
  Ssh:
    KeyName: `my-ssh-key`
  Iam:
    AdditionalIamPolicies:
      - Policy: arn:aws:iam::`123456789012`:policy/ParallelClusterKmsPolicy
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: `q1`
      ComputeResources:
        - Name: t2micro
          InstanceType: t2.micro
          MinCount: 0
          MaxCount: 10
      Networking:
        SubnetIds:
          - subnet-`abcdef01234567890`
      Iam:
        AdditionalIamPolicies:
          - Policy: arn:aws:iam::`123456789012`:policy/ParallelClusterKmsPolicy
SharedStorage:
  - MountDir: /shared/`ebs1`
    Name: `shared-ebs1`
    StorageType: Ebs
    EbsSettings:
      Encrypted: True
      KmsKeyId: `abcd1234-ef56-gh78-ij90-abcd1234efgh5678`
```

Replace the items in red text with your own values. Then, create a cluster that uses your AWS KMS key to encrypt your data in Amazon EBS.

The configuration is similar for Amazon EFS and FSx for Lustre file systems.

The Amazon EFS `SharedStorage` configuration is as follows.

```
...
SharedStorage:
  - MountDir: /shared/`efs1`
    Name: `shared-efs1`
    StorageType: Efs
    EfsSettings:
      Encrypted: True
      KmsKeyId: `abcd1234-ef56-gh78-ij90-abcd1234efgh5678`
```

The FSx for Lustre `SharedStorage` configuration is as follows.

```
...
SharedStorage:
  - MountDir: /shared/`fsx1`
    Name: `shared-fsx1`
    StorageType: FsxLustre
    FsxLustreSettings:
      StorageCapacity: `1200`
      DeploymentType: `PERSISTENT_1`
      PerUnitStorageThroughput: `200`
      KmsKeyId: `abcd1234-ef56-gh78-ij90-abcd1234efgh5678`
```
