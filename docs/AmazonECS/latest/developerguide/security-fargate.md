

# Fargate security best practices in Amazon ECS
<a name="security-fargate"></a>

We recommend that you take into account the following best practices when you use AWS Fargate.

## Use AWS KMS to encrypt ephemeral storage for Fargate
<a name="security-fargate-ephemeral-storage-encryption"></a>

You should have your ephemeral storage encrypted by either AWS KMS or your own customer managed keys. For tasks that are hosted on Fargate using platform version `1.4.0` or later, each task receives 20 GiB of ephemeral storage. For more information, see [customer managed key (CMK)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-storage-encryption.html). You can increase the total amount of ephemeral storage, up to a maximum of 200 GiB, by specifying the `ephemeralStorage` parameter in your task definition. For such tasks that were launched on May 28, 2020 or later, the ephemeral storage is encrypted with an AES-256 encryption algorithm using an encryption key managed by Fargate.

For more information, see [Storage options for Amazon ECS tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html).

**Example: Launching an task on Fargate platform version 1.4.0 with ephemeral storage encryption**

The following command will launch a task on Fargate platform version 1.4. Because this task is launched as part of the cluster, it uses the 20 GiB of ephemeral storage that's automatically encrypted.

```
aws ecs run-task --cluster clustername \
  --task-definition {{taskdefinition}}:{{version}} \
  --count 1
  --launch-type "FARGATE" \
  --platform-version 1.4.0 \
  --network-configuration "awsvpcConfiguration={subnets=[{{subnetid}}],securityGroups=[{{securitygroupid}}]}" \ 
  --region region
```

## SYS\_PTRACE capability for kernel syscall tracing with Fargate
<a name="security-fargate-syscall-tracing"></a>

The default configuration of Linux capabilities that are added or removed from your container are provided by Docker.

Tasks that are launched on Fargate only support adding the `SYS_PTRACE` kernel capability.

The following video shows how to use this feature through the Sysdig [Falco](https://github.com/falcosecurity/falco) project.

[![AWS Videos](http://img.youtube.com/vi/OYGKjmFeLqI/0.jpg)](http://www.youtube.com/watch?v=OYGKjmFeLqI)


The code discussed in the previous video can be found on GitHub [here](https://github.com/paavan98pm/ecs-fargate-pv1.4-falco).

## Use Amazon GuardDuty with Fargate Runtime Monitoring
<a name="fargate-runtime-monitoring"></a>

Amazon GuardDuty is a threat detection service that helps protect your accounts, containers, workloads, and the data within your AWS environment. Using machine learning (ML) models, and anomaly and threat detection capabilities, GuardDuty continuously monitors different log sources and runtime activity to identify and prioritize potential security risks and malicious activities in your environment.

Runtime Monitoring in GuardDuty protects workloads running on Fargate by continuously monitoring AWS log and networking activity to identify malicious or unauthorized behavior. Runtime Monitoring uses a lightweight, fully managed GuardDuty security agent that analyzes on-host behavior, such as file access, process execution, and network connections. This covers issues including escalation of privileges, use of exposed credentials, or communication with malicious IP addresses, domains, and the presence of malware on your Amazon EC2 instances and container workloads. For more information, see [GuardDuty Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) in the *GuardDuty User Guide*.