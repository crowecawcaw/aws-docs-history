

# Isolated and confidential tasks

Isolated and confidential tasks are a trusted execution capability of Amazon ECS Managed Instances. Each Amazon ECS task runs in its own lightweight virtual machine (VM) within an Amazon EC2 instance, managed by the AWS Nitro Hypervisor, which gives you hardware-enforced isolation between tasks on the same instance. Multiple isolated tasks can run on a single Managed Instance.

Amazon ECS Managed Instances integrates with AWS Nitro Sandboxes to provide isolated and confidential tasks. This feature delivers isolation guarantees similar to AWS Fargate, where one compromised task cannot access another task's data, while you keep the flexibility of Amazon ECS Managed Instances, including Amazon EC2 instance-type selection, multiple tasks per instance for cost efficiency through bin-packing, and Capacity Reservations.

**Related resources**

To learn more about the technologies behind isolated and confidential tasks, see the following resources:
+ [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) – the underlying hardware and hypervisor that provide the isolation boundary.
+ [AWS Nitro Sandboxes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html) – the isolated compute environments that run isolated and confidential tasks.
+ [AWS KMS support for AWS Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/services-nitro-enclaves.html) – how attestation gates access to your encryption keys.
+ [Confidential computing on AWS](https://aws.amazon.com/confidential-computing/) – background on protecting data in use.