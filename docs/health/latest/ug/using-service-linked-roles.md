# Using service-linked roles for

AWS Health

AWS Health uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to AWS Health. Service-linked roles are predefined by
AWS Health and include all the permissions that the service requires to call other
AWS services for you.

You can use a service-linked role to set up AWS Health to avoid manually adding the
necessary permissions. AWS Health defines the permissions of its service-linked roles,
and unless defined otherwise, only AWS Health can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that permissions policy
can't be attached to any other IAM entity.

## Service-linked role permissions for

AWS Health

AWS Health has two service-linked roles:

- [AWSServiceRoleForHealth_Organizations](https://console.aws.amazon.com/iam/home?#/roles/AWSServiceRoleForHealth_Organizations "https://console.aws.amazon.com/iam/home?#/roles/AWSServiceRoleForHealth_Organizations") –
  This role trusts the AWS Health (`health.amazonaws.com`) to assume
  the role to access AWS services for you. Attached to this role is the
  `Health_OrganizationsServiceRolePolicy` AWS managed
  policy.
- [AWSServiceRoleForHealth_EventProcessor](https://console.aws.amazon.com/iam/home?#/roles/AWSServiceRoleForHealth_EventProcessor "https://console.aws.amazon.com/iam/home?#/roles/AWSServiceRoleForHealth_EventProcessor") – This role trusts
  the AWS Health service principal
  (`event-processor.health.amazonaws.com`) to assume the role for
  you. Attached to this role is the `AWSHealth_EventProcessorServiceRolePolicy`
  AWS managed policy. The service principal uses the role to create an Amazon EventBridge
  managed rule for AWS Incident Detection and Response. This rule is the
  infrastructure required in your AWS account to deliver alarm state change
  information from your account to AWS Health.

For more information about the AWS managed policies, see [AWS managed policies for AWS Health](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Creating a service-linked role for

AWS Health

You don't need to create the AWSServiceRoleForHealth_Organizations
service-linked role. When you call the [EnableHealthServiceAccessForOrganization](../APIReference/API_EnableHealthServiceAccessForOrganization.md "../APIReference/API_EnableHealthServiceAccessForOrganization.md") operation, AWS Health creates the
this service-linked role in the account for you.

You must manually create the AWSServiceRoleForHealth_EventProcessor service-linked role
in your account. For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_.

## Editing a service-linked role for

AWS Health

AWS Health doesn't allow you to edit the service-linked role. After you create a
service-linked role, you can't change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM.
For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

AWS Health

To delete the AWSServiceRoleForHealth_Organizations role, you must
first call the [DisableHealthServiceAccessForOrganization](../APIReference/API_DisableHealthServiceAccessForOrganization.md "../APIReference/API_DisableHealthServiceAccessForOrganization.md") operation. You can then delete
the role through the IAM console, IAM API, or AWS Command Line Interface (AWS CLI).

To delete the AWSServiceRoleForHealth_EventProcessor role, contact AWS Support and ask
that they offboard your workloads from AWS Incident Detection and Response. After this process completes, you can
then delete either role through the IAM console, IAM API, or AWS CLI.

### Related

information

For more information, see [Using service-linked
roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the _IAM User Guide_.
