# Using service-linked roles for Automation

AWS Compute Optimizer uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") named AWSServiceRoleForComputeOptimizerAutomation. A service-linked role is a unique type of
IAM role that's linked directly to Compute Optimizer Automation. Service-linked roles are predefined by
Compute Optimizer Automation and include all of the permissions that the service requires to call other on your
behalf.

With a service-linked role, setting up Compute Optimizer Automation doesn't require manually adding the
necessary permissions. Compute Optimizer Automation defines the permissions of its service-linked roles, and
unless defined otherwise, only Compute Optimizer Automation can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Role** column. Choose a
**Yes** with a link to view the service-linked role documentation
for that service.

###### Topics

- [Service-linked role permissions for
  Compute Optimizer Automation](#slr-permissions-automation "#slr-permissions-automation")
- [Service-linked role
  permissions](#service-linked-role-permissions-automation "#service-linked-role-permissions-automation")
- [Creating a Service-Linked Role for
  Compute Optimizer Automation](#create-slr-automation "#create-slr-automation")
- [Editing a Service-Linked Role for Compute Optimizer Automation](#edit-slr-automation "#edit-slr-automation")
- [Deleting a Service-Linked Role for
  Compute Optimizer Automation](#delete-slr-automation "#delete-slr-automation")
- [Supported Regions for Compute Optimizer Automation service-linked Roles](#slr-regions "#slr-regions")

## Service-linked role permissions for

Compute Optimizer Automation

Compute Optimizer Automation uses the service-linked role that's named **AWSServiceRoleForComputeOptimizerAutomation**
which enables access to AWS services and resources used or managed by Compute Optimizer Automation. This
service-linked role allows Compute Optimizer Automation to implement optimization recommendations by
performing tasks such as creating, modifying, and deleting resources through other AWS
services.

The AWSServiceRoleForComputeOptimizerAutomation service-linked role trusts the `aco-automation.amazonaws.com`
services to assume the role.

The `AWSServiceRoleForComputeOptimizerAutomation` service-linked role uses the
managed policy `AWSComputeOptimizerAutomationRolePolicy`.

## Service-linked role

permissions

To create a service-linked role for Compute Optimizer Automation, configure permissions to allow an IAM
entity (such as a user, group, or role) to create the service-linked role. For more
information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

Add the following policy to the IAM entity that needs to create the service-linked
role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        }
    ]
}

```

## Creating a Service-Linked Role for

Compute Optimizer Automation

The AWSServiceRoleForComputeOptimizerAutomation service-linked role is created automatically when you enable Compute Optimizer Automation.
You can enable the AWSServiceRoleForComputeOptimizerAutomation manually in the AWS CLI or the IAM API.

The service-linked role created for a Compute Optimizer Automation management account does
not apply to member accounts. Compute Optimizer Automation creates a separate service-linked
role for each account when the feature is enabled. When a management account enables
Automation for a member account, Compute Optimizer Automation creates the service-linked role
on-demand the first time it implements a recommended action for that account. This occurs
either when the management account or member account initiates the action directly or when an
automation rule executes an action for that member account.

## Editing a Service-Linked Role for Compute Optimizer Automation

Compute Optimizer Automation doesn't allow you to edit the AWSServiceRoleForComputeOptimizerAutomation service-linked role. After you
create a service-linked role, you can't change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a Service-Linked Role for

Compute Optimizer Automation

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete the role. That way, you don't have an unused entity that isn't
actively monitored or maintained.

When you disable Compute Optimizer Automation, Compute Optimizer Automation doesn't
automatically delete the AWSServiceRoleForComputeOptimizerAutomation service-linked role for you. If you enable Compute
Optimizer Automation again, the service can then start using the existing service-linked role
again. If you no longer need to use Compute Optimizer Automation, you can manually delete the
service-linked role.

###### Important

Before you delete the AWSServiceRoleForComputeOptimizerAutomation service-linked role, you must first disable Compute
Optimizer Automation. If Compute Optimizer Automation isn't disabled when you try to delete
the service-linked role, the deletion fails.

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForComputeOptimizerAutomation service-linked
role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Compute Optimizer Automation service-linked Roles

Compute Optimizer Automation supports using service-linked roles in all of the Regions where the service
is available. To view the currently supported AWS Regions and endpoints for Compute Optimizer, see [Compute Optimizer Endpoints and
Quotas](../../../general/latest/gr/compute-optimizer.md "../../../general/latest/gr/compute-optimizer.md") in the _AWS General Reference_.
