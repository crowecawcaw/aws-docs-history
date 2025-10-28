# Turning on

Runtime Monitoring for Amazon ECS

You can configure GuardDuty to automatically manage the security agen for all your Fargate clusters.

## Prerequisites

The following are prerequisites for using Runtime Monitoring:

- The Fargate platform version must be `1.4.0` or later for
  Linux.
- IAM roles and permissions for Amazon ECS:
  - Fargate tasks must use a task execution role. This role grants the tasks
    permission to retrieve, update, and manage the GuardDuty security agent on your
    behalf. For more information see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").
  - You control Runtime Monitoring for a cluster with a pre-defined tag. If your access policies restrict access based on tags, you must grant explicit permissions to your IAM users to tag clusters. For more information, see [IAM tutorial: Define permissions to access AWS resources based on tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

- Connecting to the Amazon ECR repository:

The GuardDuty security agent is stored in an Amazon ECR repository. Each standalone
and service task must have access to the repository. You can use one of the
following options:

    + For tasks in public subnets, you can either use a public IP
     address for the task, or create a VPC endpoint for Amazon ECR in the
     subnet where the task runs. For more information, see [Amazon ECR
     interface VPC endpoints (AWS PrivateLink)](../../../AmazonECR/latest/userguide/vpc-endpoints.md "../../../AmazonECR/latest/userguide/vpc-endpoints.md") in the *Amazon Elastic Container Registry
     User Guide*.
    + For tasks in private subnets, you can use a Network Address Translation (NAT) gateway, or
     create a VPC endpoint for Amazon ECR in the subnet where the task
     runs.


    For more information, see [Private subnet and NAT gateway](networking-outbound.md#networking-private-subnet "networking-outbound.md#networking-private-subnet").

- You must have the `AWSServiceRoleForAmazonGuardDuty` role for GuardDuty. For more
  information, see [Service-linked role
  permissions for GuardDuty](../../../guardduty/latest/ug/slr-permissions.md "../../../guardduty/latest/ug/slr-permissions.md") in the _Amazon GuardDuty
  User Guide_.
- Any files that you want to protect with Runtime Monitoring must be accessible by
  the root user. If you manually changed the permissions of a file, you must
  set it to `755`.

The following are prerequisites for using Runtime Monitoring on EC2 container
instances:

- You must use version `20230929` or later of the
  Amazon ECS-AMI.
- You must run Amazon ECS agent to version `1.77` or later on the
  container instances.
- You must use kernel version `5.10` or later.
- For information about the supported Linux operating systems and
  architectures, see [Which operating models and workloads does GuardDuty Runtime Monitoring
  support](https://aws.amazon.com/guardduty/faqs/?nc1=h_ls#product-faqs#guardduty-faqs#guardduty-ecs-runtime-monitoring "https://aws.amazon.com/guardduty/faqs/?nc1=h_ls#product-faqs#guardduty-faqs#guardduty-ecs-runtime-monitoring").
- You can use Systems Manager to manage your container instances. For more
  information, see [Setting up Systems Manager for EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager Session Manager User Guide_.

## Procedure

You enable Runtime Monitoring in GuardDuty. For information about how to enable the feature,
see [Enabling
Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring-configuration.md "../../../guardduty/latest/ug/runtime-monitoring-configuration.md") in the _Amazon GuardDuty User
Guide_.
