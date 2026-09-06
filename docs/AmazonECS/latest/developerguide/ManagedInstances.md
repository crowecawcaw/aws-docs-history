

# Architect for Amazon ECS Managed Instances
<a name="ManagedInstances"></a>

Amazon ECS Managed Instances is a fully managed compute option for Amazon ECS that enables you to run containerized workloads on the full range of Amazon EC2 instance types while offloading infrastructure management to AWS. With Amazon ECS Managed Instances, you can access specific compute capabilities such as GPU acceleration, particular CPU architectures, high network performance, and specialized instance types, while AWS handles provisioning, scaling, patching, and maintenance of the underlying infrastructure.

When you use Amazon ECS Managed Instances, you package your application in containers and specify your compute requirements. AWS automatically selects the most cost-optimized general-purpose Amazon EC2 instance types that meet your workload needs, or you can specify desired instance attributes including instance types, CPU manufacturers, and accelerators. Amazon ECS Managed Instances completely manage all aspects of infrastructure including, scaling, patching, and cost optimization - without trading off access to AWS capabilities and Amazon EC2 integrations.

Amazon ECS Managed Instances support Linux containers with platform-specific optimizations and security configurations. By default, Amazon ECS Managed Instances optimizes infrastructure utilization by placing multiple smaller tasks on larger instances, helping to reduce costs and improve task launch times.

This topic describes the different components of Amazon ECS Managed Instances tasks and services, and calls out special considerations for using Amazon ECS Managed Instances with Amazon ECS.

## Getting started
<a name="managed-instances-walkthrough"></a>

To get started with Amazon ECS Managed Instances, you create the required IAM roles and enable Amazon ECS Managed Instances in your AWS account. Then you can create a capacity provider and launch tasks or services using the Amazon ECS Managed Instances capacity provider.

For detailed instructions on getting started, see:
+ [Learn how to create a task for Amazon ECS Managed Instances](getting-started-managed-instances.md)
+ [Learn how to create a task for Amazon ECS Managed Instances with the AWS CLI](getting-started-managed-instances-cli.md)

## Capacity providers
<a name="managed-instances-capacity-providers"></a>

Amazon ECS Managed Instances uses capacity providers to manage compute capacity for your workloads. When you create a capacity provider, you can use default instance selection or specify custom instance requirements using `instanceRequirements`.

The following capacity provider options are available:
+ **Default capacity provider** - Automatically selects the most cost-optimized general-purpose instance types for your workload requirements.
+ **Custom capacity providers** - Allow you to specify instance attributes using attribute-based instance type selection, including vCPU count, memory, CPU manufacturers, accelerator types, and specific instance types.

A capacity provider strategy can only contain one capacity provider type from the following list:
+ Amazon ECS Managed Instances
+ Auto Scaling group
+ Fargate/Fargate\_SPOT

## Instance selection and optimization
<a name="managed-instances-instance-selection"></a>

Amazon ECS chooses instance types for your Amazon ECS Managed Instances workloads using one of the following methods:
+ **Automatic selection** - When using the default capacity provider, Amazon ECS automatically selects the most cost-optimized general-purpose instance types that meet the CPU and memory requirements specified in your task definition.
+ **Attribute-based selection** - When using custom capacity providers, you can specify instance attributes such as vCPU count, memory size, CPU manufacturers, accelerator types, and specific instance types. Amazon ECS selects from all instance types that match your specified attributes.

Amazon ECS Managed Instances optimizes infrastructure utilization and cost through several mechanisms:
+ Multi-task placement - By default, Amazon ECS places multiple smaller tasks on larger instances to maximize utilization and reduce costs.
+ Active workload consolidation - Amazon ECS identifies when container instances are truly idle while trying to avoid premature termination that could impact application availability or deployment performance. The system respects the minimum and maximum number of tasks set for a service, the start before stop behavior, and the task protection behavior.
+ Right-sizing - As workload requirements change, Amazon ECS launches replacement instances that are appropriately sized for current needs.

Amazon ECS uses Amazon EC2 event windows to schedule maintenance activities during your preferred time periods. Event windows allow you to define recurring time periods when AWS can perform maintenance on your instances, helping you minimize disruption to your workloads by aligning maintenance with your operational schedule. For more information, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html) in the *Amazon EC2 User Guide*.

If you require strong isolation, you can configure Amazon ECS Managed Instances to run each task on a separate instance with VM-level security isolation boundaries.

## Task definitions
<a name="managed-instances-task-definitions"></a>

Tasks that use Amazon ECS Managed Instances support most Amazon ECS task definition parameters. Amazon ECS Managed Instances is compatible with existing Fargate task definitions using platform version 1.4.0, making migration straightforward.

To use Amazon ECS Managed Instances, set the `requiresCompatibilities` task definition parameter to include `MANAGED_INSTANCES`. Your task definitions can specify both Fargate and Amazon ECS Managed Instances compatibility for flexibility in deployment options.

## Operating system and CPU architecture
<a name="welcome-operating-system"></a>

The following operating systems are supported:
+ Bottlerocket

There are 2 architectures available for the Amazon ECS task definition, ARM and X86\_64.

When you run Linux containers on Amazon ECS Managed Instances, you can use the X86\_64 CPU architecture, or the ARM64 architecture for your ARM-based applications.

## Key features
<a name="managed-instances-key-features"></a>

The following are key features of Amazon ECS Managed Instances:
+ Select specific EC2 instance types to meet your application's requirements, enabling access to specialized hardware capabilities such as GPU-accelerated compute, specific CPU capabilities, and large memory sizes.
+ Optimize resource utilization and cost with multiple tasks on a single instance by default, unlike Fargate which runs each task in its own isolated environment.
+ Ensure security compliance and regular instance patching. ECS Managed Instances initiates instance draining after 14 days and automatically replaces service-based tasks to new instances.
+ Enable advanced networking and system administration functions within containers using privileged Linux capabilities, including CAP\_NET\_ADMIN, CAP\_SYS\_ADMIN, CAP\_BPF, and CAP\_PERFMON.

## IAM roles
<a name="managed-instances-iam-roles"></a>

Amazon ECS Managed Instances requires two IAM roles:
+ *Infrastructure Role*: This role allows AWS to manage the Amazon ECS Managed Instances on your behalf.
+ *Instance profile*: An instance profile is a way to pass an IAM role to Amazon ECS Managed Instances. This profile is used to:
  + Define the IAM permissions for the Amazon ECS Managed Instances that run your container workloads.
  + Allow AWS to manage these instances on your behalf.
  + Enable the instances to access AWS services according to the permissions defined in the profile.

## Security and compliance
<a name="managed-instances-security-compliance"></a>

Amazon ECS Managed Instances implements multiple layers of security to protect your workloads:
+ **Secure configuration** - Amazon ECS Managed Instances follow AWS security best practices including no SSH access, immutable root filesystem, and kernel-level mandatory access controls via SELinux.
+ **Automatic patching** - AWS regularly updates Amazon ECS Managed Instances with the latest security patches, respecting maintenance windows that you configure.
+ **Limited instance lifetime** - ECS automatically initiates instance draining after 14 days, ensuring your applications run on appropriately configured instances with up-to-date security patches.
+ **Privileged capabilities** - You can optionally enable privileged Linux capabilities for workloads that require them, such as network monitoring and observability solutions.

Amazon ECS Managed Instances support the same compliance programs as Amazon ECS, including PCI-DSS, HIPAA, and FedRAMP. In supported regions, you can configure FIPS endpoints at the capacity provider level to help achieve FedRAMP compliance.

## Networking
<a name="managed-instances-networking"></a>

Amazon ECS Managed Instances support the `awsvpc` and `host` network modes. The `awsvpc` network mode provides each task with its own elastic network interface and private IP address within your VPC. This enables fine-grained security group and network ACL controls at the task level. In the `host` network mode, tasks share the host Amazon ECS Managed Instance's network namespace. For more information about task networking on Amazon ECS Managed Instances, see [Amazon ECS task networking for Amazon ECS Managed Instances](managed-instance-networking.md).

## Instance storage
<a name="managed-instances-storage"></a>

Amazon ECS Managed Instances supports configuring the size of the Amazon EBS data volume that's attached to the instance. This storage is shared between all tasks that run on the instance and can be used for bind mounds. The volume can be shared and mounted among containers that use the `volumes`, `mountPoint`, and `volumesFrom` parameters in the task definition.

 The volume is attached during instance creation. You can specify the size of the volume, in GiB, when you create a Amazon ECS Managed Instances capacity provider by using the `storageConfiguration` parameter.

```
{
...

    "managedInstancesProvider": {
        "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
        "instanceLaunchTemplate": {
            "ec2InstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile",
            "networkConfiguration": {
                "subnets": [
                    "subnet-abcdef01234567",
                    "subnet-bcdefa98765432"
                ],
                "securityGroups": [ 
                    "sg-0123456789abcdef"
                ]
            },
            "storageConfiguration": {
                "storageSizeinGiB" : 100

            }
        }
    }
 ... 
}
```

The minimum size of this volume is 30 GiB and the maximum size is 16,384 GiB. By default, the size of this volume is 80 GiB.

The pulled, compressed, and the uncompressed container image for the task is stored in the volume. To determine the total amount of instance storage your task has to use as bind mount, you must subtract the amount of storage your container image uses from the total amount of instance storage your task is allocated.



The performance of Amazon EBS volumes attached to Amazon ECS Managed Instances matches the performance of corresponding Amazon EC2 instances, as outlined in the [Amazon EBS-optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) documentation in the *Amazon EC2 User Guide*.

You can create snapshots of the volume to perform a forensic analysis of security issues or to debug your application. For more information about creating snapshots of Amazon EBS volumes, see [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) in the *Amazon EBS User Guide*. If you have Amazon EBS encryption by default enabled, the volume will be encrypted with the AWS KMS key specified for encryption by default. For more information about encryption by default, see [Enable Amazon EBS encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html) in the *Amazon EBS User Guide*.

In addition to using the data volume attached to the instance, you can also configure data volumes for each task that runs on Amazon ECS Managed Instances. For more information about available task-level storage options, see [Storage options for Amazon ECS tasks](using_data_volumes.md).

## Local Storage
<a name="managed-instances-local-storage"></a>

[Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) provides temporary block-level storage for your Amazon EC2 instances. The storage provided by Amazon EC2 instance store is accessible through disks that are physically attached to the hosts. You can configure Amazon ECS Managed Instances to use instance store as a data volume for tasks running on the container instance. When you enable local storage and the instance has instance store volumes, Amazon ECS uses the instance store volumes instead of provisioning an Amazon EBS data volume. This can reduce storage costs and improve I/O performance for latency-sensitive workloads. There is no additional charge for using instance store volumes with Amazon ECS Managed Instances.

When an instance has multiple instance store volumes, Amazon ECS automatically combines them into a single RAID 0 volume and presents it as contiguous storage for tasks. When an instance doesn't have instance store volumes, or when local storage is disabled, Amazon ECS provisions an Amazon EBS data volume with the size specified in `storageSizeGiB`. Instance store volumes are ephemeral. Data on instance store volumes is lost when the instance is stopped, terminated, or when hardware fails. Do not use instance store for data that must persist.

To enable local storage, [create a new capacity provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity-provider-managed-instances.html) with the `localStorageConfiguration` parameter and set `useLocalStorage` to `true`. You can also use the `instanceRequirements` parameter to ensure that provisioned instances include local storage of a specific size.

**Note**  
When you create a cluster using the AWS Management Console, the default managed instances capacity provider that Amazon ECS creates doesn't include `localStorageConfiguration`.

The following example shows a capacity provider configuration with local storage enabled and instance requirements that specify SSD-based instance store with a minimum of 50 GiB.

```
{
...
    "managedInstancesProvider": {
        "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
        "instanceLaunchTemplate": {
            "ec2InstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile",
            "networkConfiguration": {
                "subnets": [
                    "subnet-abcdef01234567",
                    "subnet-bcdefa98765432"
                ],
                "securityGroups": [
                    "sg-0123456789abcdef"
                ]
            },
            "storageConfiguration": {
                "storageSizeGiB": 50
            },
            "localStorageConfiguration": {
                "useLocalStorage": true
            },
            "instanceRequirements": {
                "vCpuCount": {
                    "min": 0
                },
                "memoryMiB": {
                    "min": 0
                },
                "localStorage": "REQUIRED",
                "totalLocalStorageGB": {
                    "min": 50
                },
                "localStorageTypes": ["ssd"]
            }
        }
    }
}
```

When you omit the `instanceRequirements` configuration, Amazon ECS defaults `localStorage` to `INCLUDED`. In this case, Amazon ECS considers instances both with and without instance store volumes for provisioning. Instances with instance store volumes use an instance store for data volume, while instances without instance store volumes use an Amazon EBS data volume. When `totalLocalStorageGB` is not specified, Amazon ECS uses all available instance storage, with no minimum size enforced.

The `storageSizeGiB` value in `storageConfiguration` defines only the Amazon EBS data volume size and is used when instance storage is unavailable. The `totalLocalStorageGB` value in `instanceRequirements` controls the minimum instance storage size required on provisioned instances. To guarantee that all instances use local storage, set `localStorage` to `REQUIRED` and specify a minimum size by using `totalLocalStorageGB`.

To verify whether a specific provisioned container instance is using local storage, check for the `ecs.capability.storage.local-storage-enabled` attribute on the container instance.

## Service load balancing
<a name="managed-instances-load-balancing"></a>

Your Amazon ECS services using Amazon ECS Managed Instances can be configured to use Elastic Load Balancing to distribute traffic evenly across the tasks in your service.

Amazon ECS services on Amazon ECS Managed Instances support Application Load Balancer, Network Load Balancer, and Gateway Load Balancer load balancer types. Application Load Balancers route HTTP/HTTPS (layer 7) traffic, while Network Load Balancers route TCP or UDP (layer 4) traffic.

When you create a target group for these services, you must choose `ip` as the target type, not `instance`. This is because tasks using the `awsvpc` network mode are associated with an elastic network interface, not directly with an Amazon EC2 instance.

## Monitoring and observability
<a name="managed-instances-monitoring"></a>

Amazon ECS Managed Instances provides comprehensive monitoring capabilities through CloudWatch metrics and integration with observability tools:
+ **CloudWatch metrics** - Monitor CPU, memory, network, and storage utilization at both the task and instance level.
+ **Container Insights** - Get detailed performance metrics and logs for your containerized applications.
+ **Third-party integrations** - With privileged capabilities enabled, you can run advanced monitoring and observability solutions that require elevated Linux permissions.

## Pricing and cost optimization
<a name="managed-instances-pricing"></a>

With Amazon ECS Managed Instances, you are billed for the entire Amazon EC2 instance that runs your tasks. The pricing depends on the instance types selected for your workloads.

Amazon ECS Managed Instances provides several cost optimization features:
+ **Multi-task optimization** - Maximize instance utilization by running multiple tasks on appropriately sized instances.

Your Compute and Instance Savings Plans also apply to Amazon ECS Managed Instances workloads.

## Service quotas
<a name="managed-instances-service-quotas"></a>

Amazon ECS Managed Instances workloads are subject to your Amazon EC2 On-Demand instance service quotas. Your Amazon ECS services using Amazon ECS Managed Instances are subject to Amazon ECS service quotas.

For more information about service quotas, see:
+ [Amazon EC2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html) in the *Amazon Web Services General Reference*
+ [Amazon ECS service quotas](service-quotas.md)

## Migration considerations
<a name="managed-instances-migration"></a>

Migrating to Amazon ECS Managed Instances is straightforward for most workloads:
+ **From Fargate** - Requires only a capacity provider configuration change and redeployment. Existing task definitions using platform version 1.4.0 are fully compatible.
+ **From EC2** - Similar to migrating to Fargate, but you retain access to Amazon EC2 capabilities such as specific instance types.

Consider the following when planning your migration:
+ Applications should tolerate the 14-day instance lifetime and planned maintenance windows.
+ Long-running tasks (exceeding 14 days) are not suitable for Amazon ECS Managed Instances.
+ Custom AMIs are not supported - Amazon ECS Managed Instances use AWS-managed, security-optimized AMIs.

## Limitations and considerations
<a name="managed-instances-limitations"></a>

The following limitations apply to Amazon ECS Managed Instances:
+ Custom AMIs - The AMI is owned and managed by AWS
+ Instance lifetime - Maximum runtime of 14 days per instance to ensure security patching and compliance.
+ SSH access - Not available for security reasons. Use Amazon ECS Exec for debugging and troubleshooting. Management operations through Amazon ECS APIs only.

## Organization controls
<a name="managed-instances-organization-controls"></a>

Some organization controls can prevent Amazon ECS Managed Instances from functioning correctly. If so, you must update these controls to allow Amazon ECS to have the permissions required to manage EC2 instances on your behalf.

Amazon ECS uses an infrastructure role for launching the EC2 instances that back Amazon ECS Managed Instances. This infrastructure role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) which is created in your account that allows Amazon ECS to manage the Amazon ECS Managed Instances on your behalf. [Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) always apply to actions performed with infrastructure roles. This allows an SCP to inhibit Amazon ECS Managed Instances operations. The most common occurrence is when an SCP is used to restrict the Amazon Machine Images (AMIs) that can be launched. To allow Amazon ECS Managed Instances to function, modify the SCP to permit launching AMIs from Amazon ECS Managed Instances AMI accounts.

You can also use the [EC2 Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) feature to limit the visibility of AMIs in other accounts. If you use this feature, you must expand the image criteria to also include the Amazon ECS Managed Instances AMI accounts in the regions of interest.

### Example SCP to block all AMIs except for Amazon ECS Managed Instances AMIs
<a name="example-scp-managed-instances"></a>

The SCP below prevents calling `ec2:RunInstances` unless the AMI belongs to the Amazon ECS Managed Instances AMI account for us-west-2 or us-east-1.

**Note**  
It's important **not** to use the `ec2:Owner` context key. Amazon owns the Amazon ECS Managed Instances AMI accounts and the value for this key will always be `amazon`. Constructing an SCP that allows launching AMIs if the `ec2:Owner` is `amazon` will allow launching any Amazon owned AMI, not just those for Amazon ECS Managed Instances.

```
{
  "Version":"2012-10-17",		 	 	                                 
  "Statement": [
    {
      "Sid": "DenyAMI",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:*:ec2:*::image/ami-*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceAccount": [
            "187296253231",
            "260073348889"
          ]
        }
      }
    }
  ]
}
```

### Amazon ECS Managed Instances AMI accounts
<a name="managed-instances-ami-accounts"></a>

AWS accounts that vary by region host Amazon ECS Managed Instances public AMIs.


| AWS Region | Account | 
| --- | --- | 
| af-south-1 | 070957084703 | 
| ap-east-1 | 587573215167 | 
| ap-northeast-1 | 679336465495 | 
| ap-northeast-2 | 309903600357 | 
| ap-northeast-3 | 384570461223 | 
| ap-south-1 | 062344138989 | 
| ap-south-2 | 624198668379 | 
| ap-southeast-1 | 832199679391 | 
| ap-southeast-2 | 552073033681 | 
| ap-southeast-3 | 368903466070 | 
| ap-southeast-4 | 696793786439 | 
| ap-southeast-5 | 003457290689 | 
| ap-southeast-6 | 465836752572 | 
| ap-southeast-7 | 622515864387 | 
| ca-central-1 | 853167153192 | 
| ca-west-1 | 899469777611 | 
| eu-central-1 | 832570432258 | 
| eu-central-2 | 041659148495 | 
| eu-north-1 | 851563870067 | 
| eu-south-1 | 766433696616 | 
| eu-south-2 | 003380494496 | 
| eu-west-1 | 986619735082 | 
| eu-west-2 | 591706807364 | 
| eu-west-3 | 108582616801 | 
| il-central-1 | 009537862704 | 
| me-central-1 | 540883425316 | 
| me-south-1 | 181438624895 | 
| mx-central-1 | 210749644920 | 
| sa-east-1 | 591338347621 | 
| us-east-1 | 260073348889 | 
| us-east-2 | 292185169523 | 
| us-west-1 | 187296253231 | 
| us-west-2 | 491085424538 | 