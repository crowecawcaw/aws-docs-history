# AWS managed policies for Amazon Elastic Container Service

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services do not remove permissions from an AWS managed policy, so policy
updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service
launches a new feature, AWS adds read-only permissions for new operations and resources.
For a list and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

Amazon ECS and Amazon ECR provide several managed policies and trust relationships that you can
attach to users, groups, roles, Amazon EC2 instances, and Amazon ECS tasks that allow differing levels
of control over resources and API operations. You can apply these policies directly, or you
can use them as starting points for creating your own policies. For more information about
the Amazon ECR managed policies, see [Amazon ECR managed
policies](../../../AmazonECR/latest/userguide/ecr_managed_policies.md "../../../AmazonECR/latest/userguide/ecr_managed_policies.md").

## AmazonECS_FullAccess

You can attach the `AmazonECS_FullAccess` policy to your IAM identities.
This policy grants administrative access to Amazon ECS resources and grants an IAM identity
(such as a user, group, or role) access to the AWS services that Amazon ECS is integrated
with to use all of Amazon ECS features. Using this policy allows access to all of Amazon ECS
features that are available in the AWS Management Console.

To view the permissions for this policy, see [AmazonECS_FullAccess](../../../aws-managed-policy/latest/reference/AmazonECS_FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonECS_FullAccess.md") in the _AWS Managed Policy Reference_.

## AmazonECSInfrastructureRolePolicyForVolumes

You can attach the `AmazonECSInfrastructureRolePolicyForVolumes` managed
policy to your IAM entities.

The policy
grants the permissions that are needed by Amazon ECS to make AWS API calls on your behalf.
You can attach this policy to the IAM role that you provide with your volume
configuration when you launch Amazon ECS tasks and services. The role allows Amazon ECS to manage
volumes attached to your tasks. For more information, see [Amazon ECS
infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").

To view the permissions for this policy, see [AmazonECSInfrastructureRolePolicyForVolumes](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVolumes.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVolumes.md") in the _AWS Managed Policy
Reference_.

## AmazonEC2ContainerServiceforEC2Role

You can attach the `AmazonEC2ContainerServiceforEC2Role` policy to your
IAM identities. This policy grants administrative permissions that allow Amazon ECS
container instances to make calls to AWS on your behalf. For more information, see
[Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").

Amazon ECS attaches this policy to a service role that allows Amazon ECS to perform actions on
your behalf against Amazon EC2 instances or external instances.

To view the permissions for this policy, see [AmazonEC2ContainerServiceforEC2Role](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerServiceforEC2Role.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerServiceforEC2Role.md") in the _AWS Managed Policy
Reference_.

### Considerations

You should consider the following recommendations and considerations when using
the `AmazonEC2ContainerServiceforEC2Role` managed IAM policy.

- Following the standard security advice of granting least privilege, you
  can modify the `AmazonEC2ContainerServiceforEC2Role` managed
  policy to fit your specific needs. If any of the permissions granted in the
  managed policy aren't needed for your use case, create a custom policy
  and add only the permissions that you require. For example, the
  `UpdateContainerInstancesState` permission is provided for
  Spot Instance draining. If that permission isn't needed for your use case, exclude it
  using a custom policy.
- Containers that are running on your container instances have access to all
  of the permissions that are supplied to the container instance role through
  [instance
  metadata](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md"). We recommend that you limit the permissions in your
  container instance role to the minimal list of permissions that are provided
  in the managed `AmazonEC2ContainerServiceforEC2Role` policy. If
  the containers in your tasks need extra permissions that aren't listed, we
  recommend providing those tasks with their own IAM roles. For more
  information, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").

You can prevent containers on the `docker0` bridge from
accessing the permissions supplied to the container instance role. You can
do this while still allowing the permissions that are provided by [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md") by running the
following **iptables** command on your container instances.
Containers can't query instance metadata with this rule in effect. This
command assumes the default Docker bridge configuration and it doesn't work
with containers that use the `host` network mode. For more
information, see [Network mode](task_definition_parameters.md#network_mode "task_definition_parameters.md#network_mode").

```
`sudo yum install -y iptables-services; sudo iptables --insert DOCKER USER 1 --in-interface docker+ --destination 169.254.169.254/32 --jump DROP`
```

You must save this **iptables** rule on your container
instance for it to survive a reboot. For the Amazon ECS-optimized AMI, use the
following command. For other operating systems, consult the documentation
for that OS.

    + For the Amazon ECS-optimized Amazon Linux 2 AMI:



    ```
    `sudo iptables-save | sudo tee /etc/sysconfig/iptables && sudo systemctl enable --now iptables`
    ```
    + For the Amazon ECS-optimized Amazon Linux AMI:



    ```
    `sudo service iptables save`
    ```

## AmazonEC2ContainerServiceEventsRole

You can attach the `AmazonEC2ContainerServiceEventsRole` policy to your
IAM identities. This policy grants permissions that allow Amazon EventBridge (formerly CloudWatch Events) to
run tasks on your behalf. This policy can be attached to the IAM role that's specified
when you create scheduled tasks. For more information, see [Amazon ECS EventBridge IAM Role](CWE_IAM_role.md "CWE_IAM_role.md").

To view the permissions for this policy, see [AmazonEC2ContainerServiceEventsRole](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerServiceEventsRole.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerServiceEventsRole.md") in the _AWS Managed Policy
Reference_.

## AmazonECSTaskExecutionRolePolicy

The `AmazonECSTaskExecutionRolePolicy` managed IAM policy grants the
permissions that are needed by the Amazon ECS container agent and AWS Fargate container
agents to make AWS API calls on your behalf. This policy can be added to your task
execution IAM role. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

To view the permissions for this policy, see [AmazonECSTaskExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AmazonECSTaskExecutionRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonECSTaskExecutionRolePolicy.md") in the _AWS Managed Policy
Reference_.

## AmazonECSServiceRolePolicy

The `AmazonECSServiceRolePolicy` managed IAM policy enables Amazon Elastic Container Service to
manage your cluster. This policy can be added to your [AWSServiceRoleForECS](using-service-linked-roles-for-clusters.md#service-linked-role-permissions-clusters "using-service-linked-roles-for-clusters.md#service-linked-role-permissions-clusters") service-linked role.

To view the permissions for this policy, see [AmazonECSServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonECSServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonECSServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

## `AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity`

You can attach the `AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity` policy to your IAM entities. This policy grants administrative access to AWS Private Certificate Authority, Secrets Manager and other AWS Services required
to manage Amazon ECS Service Connect TLS features on your behalf.

To view the permissions for this policy, see [AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity.md") in the _AWS Managed Policy
Reference_.

## `AWSApplicationAutoscalingECSServicePolicy`

You can't attach `AWSApplicationAutoscalingECSServicePolicy` to your IAM
entities. This policy is attached to a service-linked role that allows Application Auto Scaling to
perform actions on your behalf. For more information, see [Service-linked roles for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md").

To view the permissions for this policy, see [AWSApplicationAutoscalingECSServicePolicy](../../../aws-managed-policy/latest/reference/AWSApplicationAutoscalingECSServicePolicy.md "../../../aws-managed-policy/latest/reference/AWSApplicationAutoscalingECSServicePolicy.md") in the _AWS Managed Policy Reference_.

## `AWSCodeDeployRoleForECS`

You can't attach `AWSCodeDeployRoleForECS` to your IAM entities. This
policy is attached to a service-linked role that allows CodeDeploy to perform actions on your
behalf. For more information, see [Create a
service role for CodeDeploy](../../../codedeploy/latest/userguide/getting-started-create-service-role.md "../../../codedeploy/latest/userguide/getting-started-create-service-role.md") in the _AWS CodeDeploy User Guide_.

To view the permissions for this policy, see [AWSCodeDeployRoleForECS](../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECS.md "../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECS.md") in the _AWS Managed Policy Reference_.

## `AWSCodeDeployRoleForECSLimited`

You can't attach `AWSCodeDeployRoleForECSLimited` to your IAM entities.
This policy is attached to a service-linked role that allows CodeDeploy to perform actions on
your behalf. For more information, see [Create a
service role for CodeDeploy](../../../codedeploy/latest/userguide/getting-started-create-service-role.md "../../../codedeploy/latest/userguide/getting-started-create-service-role.md") in the _AWS CodeDeploy User Guide_.

To view the permissions for this policy, see [AWSCodeDeployRoleForECSLimited](../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECSLimited.md "../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECSLimited.md") in the _AWS Managed Policy Reference_.

## `AmazonECSInfrastructureRolePolicyForLoadBalancers`

You can attach the `AmazonECSInfrastructureRolePolicyForLoadBalancers` policy to your IAM entities. This
policy grants permissions that allow Amazon ECS to manage Elastic Load Balancing resources on your behalf. The policy includes:

- Read-only permissions to describe listeners, rules, target groups, and target health
- Permissions to register and deregister targets with target groups
- Permissions to modify listeners for Application Load Balancers and Network Load Balancers
- Permissions to modify rules for Application Load Balancers

These permissions enable Amazon ECS to automatically manage load balancer configurations when services are created or updated, ensuring proper routing of traffic to your containers.

To view the permissions for this policy, see [AmazonECSInfrastructureRolePolicyForLoadBalancers](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForLoadBalancers.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForLoadBalancers.md") in the _AWS Managed Policy
Reference_.

## `AmazonECSInfrastructureRolePolicyForManagedInstances`

You can attach the `AmazonECSInfrastructureRolePolicyForManagedInstances` policy to your IAM entities. This
policy grants the permissions required by Amazon ECS to create and update Amazon EC2 resources for ECS Managed Instances on your behalf. The policy includes:

- Permissions to create and manage Amazon EC2 launch templates for managed instances
- Permissions to provision Amazon EC2 instances using CreateFleet and RunInstances
- Permissions to create and manage tags on Amazon EC2 resources created by ECS
- Permissions to pass IAM roles to Amazon EC2 instances for managed instances
- Permissions to create service-linked roles for Amazon EC2 Spot instances
- Read-only permissions to describe Amazon EC2 resources including instances, instance types, launch templates, network interfaces, availability zones, security groups, subnets, and VPCs

These permissions enable Amazon ECS to automatically provision and manage Amazon EC2 instances for your ECS Managed Instances, ensuring proper configuration and lifecycle management of the underlying compute resources.

To view the permissions for this policy, see [AmazonECSInfrastructureRolePolicyForManagedInstances](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForManagedInstances.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForManagedInstances.md") in the _AWS Managed Policy
Reference_.

## `AmazonECSInfrastructureRolePolicyForVpcLattice`

You can attach the `AmazonECSInfrastructureRolePolicyForVpcLattice` policy to your IAM entities. This
policy Provides access to other AWS service resources required to manage VPC Lattice
feature in Amazon ECS workloads on your behalf.

To view the permissions for this policy, see [AmazonECSInfrastructureRolePolicyForVpcLattice](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVpcLattice.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVpcLattice.md") in the _AWS Managed Policy
Reference_.

Provides access to other AWS service resources required to manage VPC Lattice
feature in Amazon ECS workloads on your behalf.

## `AmazonECSComputeServiceRolePolicy`

The `AmazonECSComputeServiceRolePolicy` policy is attached to the
AmazonECSComputeServiceRole service-linked role. For more information, see [Using roles to manage Amazon ECS Managed Instances](using-service-linked-roles-instances.md "using-service-linked-roles-instances.md").

This policy includes permissions that allow Amazon ECS to complete the following
tasks:

- Amazon ECS can describe and delete launch templates.
- Amazon ECS can describe and delete launch template versions.
- Amazon ECS can terminate instances.
- Amazon ECS can describe the following instance data parameters:
  - Instance
  - Instance network interfaces: Amazon ECS can describe the the to manage the
    EC2 instance lifecycle.
  - Instance event window: Amazon ECS can describe the event window information
    in order to determine if the workflow can be interrupted for patching
    the instance.
  - Instance status: Amazon ECS can describe the instance status in order to
    monitor the instance health.

To view the permissions for this policy, see [AmazonECSComputeServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonECSComputeServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonECSComputeServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

## `AmazonECSInstanceRolePolicyForManagedInstances`

The `AmazonECSInstanceRolePolicyForManagedInstances` policy provides permissions for Amazon ECS managed instances to register with Amazon ECS clusters and communicate with the Amazon ECS service.

This policy includes permissions that allow Amazon ECS managed instances to complete the following tasks:

- Register and deregister with Amazon ECS clusters.
- Submit container instance state changes.
- Submit task state changes.
- Discover polling endpoints for the Amazon ECS agent.

To view the permissions for this policy, see [AmazonECSInstanceRolePolicyForManagedInstances](../../../aws-managed-policy/latest/reference/AmazonECSInstanceRolePolicyForManagedInstances.md "../../../aws-managed-policy/latest/reference/AmazonECSInstanceRolePolicyForManagedInstances.md") in the _AWS Managed Policy
Reference_.

## Amazon ECS updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon ECS since this service
started tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the Amazon ECS Document history page.

| Change                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                           | Date                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Add new [AmazonECSInstanceRolePolicyForManagedInstances](#security-iam-awsmanpol-AmazonECSInstanceRolePolicyForManagedInstances "#security-iam-awsmanpol-AmazonECSInstanceRolePolicyForManagedInstances")                                                                                                                                        | Added new AmazonECSInstanceRolePolicyForManagedInstances policy that provides permissions for Amazon ECS managed instances to register with Amazon ECS clusters.                                                                                                                                                                                      | September 30, 2025  |
| Add new [AmazonECSInfrastructureRolePolicyForManagedInstances](#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForManagedInstances "#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForManagedInstances")                                                                                                                      | Added new AmazonECSInfrastructureRolePolicyForManagedInstances policy that provides Amazon ECS access to create and manage Amazon EC2 managed resources.                                                                                                                                                                                              | September, 30, 2025 |
| Add new [AmazonECSComputeServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSComputeServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSComputeServiceRolePolicy")                                                                                                                             | Allows Amazon ECS to manage your Amazon ECS Managed Instances and related resources.                                                                                                                                                                                                                                                                  | August 31, 2025     |
| Add permissions to [AmazonEC2ContainerServiceforEC2Role](#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role "#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role")                                                                                                                                                              | The `AmazonEC2ContainerServiceforEC2Role` managed IAM policy was updated to include the `ecs:ListTagsForResource` permission. This permission allows the Amazon ECS agent to retrieve task and container instance tags through the task metadata endpoint (`${ECS_CONTAINER_METADATA_URI_V4}/taskWithTags`).                                          | August 4, 2025      |
| Add permissions to [AmazonECSInfrastructureRolePolicyForLoadBalancers](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForLoadBalancers "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForLoadBalancers").                                                                 | The `AmazonECSInfrastructureRolePolicyForLoadBalancers` managed IAM policy was updated with new permissions for describing, deregistering, and registering target groups.                                                                                                                                                                             | July 25, 2025       |
| Add new [AmazonECSInfrastructureRolePolicyForLoadBalancers](#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForLoadBalancers "#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForLoadBalancers") policy                                                                                                                        | Added new AmazonECSInfrastructureRolePolicyForLoadBalancers policy that provides access to other AWS service resources required to manage load balancers associated with Amazon ECS workloads.                                                                                                                                                        | July 15, 2025       |
| Add permissions to [AmazonECSServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSServiceRolePolicy").                                                                                                                                      | The `AmazonECSServiceRolePolicy` managed IAM policy was updated with new AWS Cloud Map permissions which Amazon ECS can update AWS Cloud Map service attributes for services that Amazon ECS manages.                                                                                                                                                 | July 15, 2025       |
| Add permissions to [AmazonECSServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSServiceRolePolicy")                                                                                                                                       | The `AmazonECSServiceRolePolicy` managed IAM policy was updated with new AWS Cloud Map permissions which Amazon ECS can update AWS Cloud Map service attributes for services that Amazon ECS manages.                                                                                                                                                 | June 24, 2025       |
| Add permissions to [AmazonECSInfrastructureRolePolicyForVolumes](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVolumes "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVolumes")                                                                                    | The `AmazonECSInfrastructureRolePolicyForVolumes` policy has been updated to add the `ec2:DescribeInstances` permission. The permission helps prevent device name collision for Amazon EBS volumes that are attached to Amazon ECS tasks that run on the same container instance.                                                                     | June 2, 2025        |
| Add new [AmazonECSInfrastructureRolePolicyForVpcLattice](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVpcLattice "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVpcLattice")                                                                                      | Provides access to other AWS service resources required to manage VPC Lattice feature in Amazon ECS workloads on your behalf.                                                                                                                                                                                                                         | November 18, 2024   |
| Add permissions to [AmazonECSInfrastructureRolePolicyForVolumes](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVolumes "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVolumes")                                                                                    | The `AmazonECSInfrastructureRolePolicyForVolumes` policy has been updated to allow customers to create an Amazon EBS volume from a snapshot.                                                                                                                                                                                                          | October 10, 2024    |
| Added permissions to [AmazonECS_FullAccess](#security-iam-awsmanpol-AmazonECS_FullAccess "#security-iam-awsmanpol-AmazonECS_FullAccess")                                                                                                                                                                                                         | The `AmazonECS_FullAccess` policy was updated to add `iam:PassRole` permissions for IAM roles for a role named `ecsInfrastructureRole`. This is the default IAM role created by the AWS Management Console that is intended to be used as an ECS infrastructure role that allows Amazon ECS to manage Amazon EBS volumes attached to ECS tasks.       | August 13, 2024     |
| Add new [AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity") policy | Added new AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity policy that provides administrative access to AWS KMS, AWS Private Certificate Authority, Secrets Manager and enables Amazon ECS Service Connect TLS features to work properly.                                                                                    | January 22, 2024    |
| Add new policy [AmazonECSInfrastructureRolePolicyForVolumes](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVolumes "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSInfrastructureRolePolicyForVolumes")                                                                                        | The `AmazonECSInfrastructureRolePolicyForVolumes` policy was added. The policy grants the permissions that are needed by Amazon ECS to make AWS API calls to manage Amazon EBS volumes associated with Amazon ECS workloads.                                                                                                                          | January 11, 2024    |
| Add permissions to [AmazonECSServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSServiceRolePolicy")                                                                                                                                       | The `AmazonECSServiceRolePolicy` managed IAM policy was updated with new `events` permissions and additional `autoscaling` and `autoscaling-plans` permissions.                                                                                                                                                                                       | December 4, 2023    |
| Add permissions to [AmazonEC2ContainerServiceEventsRole](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerServiceEventsRole "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerServiceEventsRole")                                                                                                            | The `AmazonECSServiceRolePolicy` managed IAM policy was updated to allow access to the AWS Cloud Map `DiscoverInstancesRevision` API operation.                                                                                                                                                                                                       | October 4, 2023     |
| Add permissions to [AmazonEC2ContainerServiceforEC2Role](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role")                                                                                                            | The `AmazonEC2ContainerServiceforEC2Role` policy was modified to add the `ecs:TagResource` permission, which includes a condition that limits the permission only to newly created clusters and registered container instances.                                                                                                                       | March 6, 2023       |
| Add permissions to [AmazonECS_FullAccess](#security-iam-awsmanpol-AmazonECS_FullAccess "#security-iam-awsmanpol-AmazonECS_FullAccess")                                                                                                                                                                                                           | The `AmazonECS_FullAccess` policy was modified to add the `elasticloadbalancing:AddTags` permission, which includes a condition that limits the permission only to newly created load balancers, target groups, rules, and listeners created. This permission doesn't allow tags to be added to any already created Elastic Load Balancing resources. | January 4, 2023     |
| Amazon ECS started tracking changes                                                                                                                                                                                                                                                                                                              | Amazon ECS started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                     | June 8, 2021        |
