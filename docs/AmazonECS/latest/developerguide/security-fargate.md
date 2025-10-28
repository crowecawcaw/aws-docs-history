# Fargate security best practices in Amazon ECS

We recommend that you take into account the following best practices when you use
AWS Fargate. For additional guidance, see [Security overview of AWS Fargate](https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf "https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf").

## Use AWS KMS to encrypt

ephemeral storage for Fargate

You should have your ephemeral storage encrypted by either AWS KMS or your own
customer managed keys. For tasks that are hosted on Fargate using platform version
`1.4.0` or later, each task receives 20 GiB of ephemeral storage. For
more information, see [customer
managed key (CMK)](fargate-storage-encryption.md "fargate-storage-encryption.md"). You can increase the total amount of ephemeral storage,
up to a maximum of 200 GiB, by specifying the `ephemeralStorage` parameter in
your task definition. For such tasks that were launched on May 28, 2020 or later, the
ephemeral storage is encrypted with an AES-256 encryption algorithm using an encryption
key managed by Fargate.

For more information, see [Storage options for Amazon ECS tasks](using_data_volumes.md "using_data_volumes.md").

**Example: Launching an task on Fargate platform
version 1.4.0 with ephemeral storage encryption**

The following command will launch a task on Fargate platform version 1.4.
Because this task is launched as part of the cluster, it uses the 20 GiB of ephemeral
storage that's automatically encrypted.

```
aws ecs run-task --cluster clustername \
  --task-definition `taskdefinition`:`version` \
  --count 1
  --launch-type "FARGATE" \
  --platform-version 1.4.0 \
  --network-configuration "awsvpcConfiguration={subnets=[`subnetid`],securityGroups=[`securitygroupid`]}" \
  --region region

```

## SYS_PTRACE capability for kernel

syscall tracing with Fargate

The default configuration of Linux capabilities that are added or removed from
your container are provided by Docker.

Tasks that are launched on Fargate only support adding the
`SYS_PTRACE` kernel capability.

The following video shows how to use this feature through the Sysdig [Falco](https://github.com/falcosecurity/falco "https://github.com/falcosecurity/falco") project.

The code discussed in the previous video can be found on GitHub [here](https://github.com/paavan98pm/ecs-fargate-pv1.4-falco "https://github.com/paavan98pm/ecs-fargate-pv1.4-falco").

## Use Amazon GuardDuty with Fargate Runtime Monitoring

Amazon GuardDuty is a threat detection service that helps protect your accounts,
containers, workloads, and the data within your AWS environment. Using machine
learning (ML) models, and anomaly and threat detection capabilities, GuardDuty
continuously monitors different log sources and runtime activity to identify and
prioritize potential security risks and malicious activities in your
environment.

Runtime Monitoring in GuardDuty protects workloads running on Fargate by continuously
monitoring AWS log and networking activity to identify malicious or unauthorized
behavior. Runtime Monitoring uses a lightweight, fully managed GuardDuty security agent that
analyzes on-host behavior, such as file access, process execution, and network
connections. This covers issues including escalation of privileges, use of exposed
credentials, or communication with malicious IP addresses, domains, and the presence
of malware on your Amazon EC2 instances and container workloads. For more information,
see [GuardDuty Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring.md "../../../guardduty/latest/ug/runtime-monitoring.md") in the _GuardDuty User
Guide_.
