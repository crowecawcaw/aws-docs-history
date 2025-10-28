# Using roles to manage Amazon ECS Managed Instances

Amazon Elastic Container Service uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon ECS. Service-linked roles are predefined by Amazon ECS and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Amazon ECS easier because you don’t have to
manually add the necessary permissions. Amazon ECS defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon ECS can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your Amazon ECS resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose
a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for Amazon ECS

Amazon ECS uses the service-linked role named **AWSServiceRoleForECSCompute** –
Role to allow Amazon ECS to manage Amazon EC2 managed instances, provisioned by the Amazon ECS Managed Instances capacity provider.

The AWSServiceRoleForECSCompute service-linked role trusts the following services to assume
the role:

- `ecs-compute.amazonaws.com`

The role permissions policy named [AmazonECSComputeServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSComputeServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECSComputeServiceRolePolicy") allows
Amazon ECS complete the following tasks:

- Amazon ECS can describe and delete launch templates.
- Amazon ECS can describe and delete launch template versions.
- Amazon ECS can terminate instances.
- Amazon ECS can describe the following instance data parameters:
  - Instance
  - Instance network interfaces: Amazon ECS can describe the the to manage the EC2
    instance lifecycle.
  - Instance event window: Amazon ECS can describe the event window information in order
    to determine if the workflow can be interrupted for patching the instance.
  - Instance status: Amazon ECS can describe the instance status in order to monitor the
    instance health.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

Amazon ECS

You don't need to manually create a service-linked role. When you
create a capacity provider for Amazon ECS Managed Instances in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECS
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in another
service that uses the features supported by this role.

If you were using the Amazon ECS service before January 1, 2017, when it began
supporting service-linked roles, then Amazon ECS created the AmazonECSComputeServiceRolePolicy role in
your account.
To
learn more, see [A new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create a capacity provider for Amazon ECS Managed Instances, Amazon ECS creates the service-linked role for you again.

If you delete this service-linked role, you can use the same IAM process to create the
role again.

## Editing a service-linked role for

Amazon ECS

Amazon ECS does not allow you to edit the AmazonECSComputeServiceRolePolicy service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

Amazon ECS

You don't need to manually delete the AmazonECSComputeServiceRolePolicy role. When you
delete all Amazon ECS Managed Instances capacity providers in all Regions in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECS
cleans up the resources and deletes the service-linked role for you.

### Manually delete the service-linked

role

Use the IAM console, the AWS CLI, or the AWS API to delete the AmazonECSComputeServiceRolePolicy
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Amazon ECS

service-linked roles

Amazon ECS supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
