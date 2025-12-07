# Service-linked roles for AWS Security Hub

AWS Security Hub uses an AWS Identity and Access Management (IAM) [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") named `AWSServiceRoleForSecurityHub`. This
service-linked role is an IAM role that's linked directly to Security Hub. It's predefined by Security Hub, and it includes all
the permissions that Security Hub requires to call other AWS services and monitor AWS resources on your behalf. Security Hub uses
this service-linked role in all the AWS Regions where Security Hub is available.

A service-linked role makes setting up Security Hub easier because you don't have to manually add
the necessary permissions. Security Hub defines the permissions of its service-linked role, and
unless defined otherwise, only Security Hub can assume the role. The defined permissions include
the trust policy and the permissions policy, and you can't attach that permissions policy to
any other IAM entity.

To review the details of the service-linked role, you can use the Security Hub console. In the
navigation pane, choose **General** under **Settings**.
Then, in the **Service permissions** section, choose **View service
permissions**.

You can delete the Security Hub service-linked role only after you disable Security Hub in all the
Regions where it's enabled. This protects your Security Hub resources because you can't
inadvertently remove permissions to access them.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_ and locate the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to review the
service-linked role documentation for that service.

###### Topics

- [Service-linked role permissions for Security Hub](#slr-permissions "#slr-permissions")
- [Creating a service-linked role for Security Hub](#create-slr "#create-slr")
- [Editing a service-linked role for Security Hub](#edit-slr "#edit-slr")
- [Deleting a service-linked role for Security Hub](#delete-slr "#delete-slr")
- [Service-linked role for AWS Security Hub V2](#slr-permissions-v2 "#slr-permissions-v2")

## Service-linked role permissions for Security Hub

Security Hub uses the service-linked role named `AWSServiceRoleForSecurityHub`. It's a
service-linked role required for AWS Security Hub to access your resources. This service-linked role allows Security Hub to perform tasks such as receive
findings from other AWS services and configure the requisite AWS Config infrastructure to
run security checks for controls. The `AWSServiceRoleForSecurityHub` service-linked role trusts
the `securityhub.amazonaws.com` service to assume the role.

The `AWSServiceRoleForSecurityHub` service-linked role uses the managed
policy [AWSSecurityHubServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubservicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubservicerolepolicy").

You must grant permissions to allow an IAM identity (such as a role, group, or user)
to create, edit, or delete a service-linked role. For the `AWSServiceRoleForSecurityHub`
service-linked role to be successfully created, the IAM identity that you use to
access Security Hub must have the required permissions. To grant the required permissions,
attach the following policy to the IAM identity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "securityhub:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "securityhub.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Creating a service-linked role for Security Hub

The `AWSServiceRoleForSecurityHub` service-linked role is created automatically when you
enable Security Hub for the first time or you enable Security Hub in a Region where you didn't
previously enable it. You can also create the `AWSServiceRoleForSecurityHub` service-linked
role manually by using the IAM console, the IAM CLI, or the IAM API. For more
information about creating the role manually, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_.

###### Important

The service-linked role that's created for a Security Hub administrator account doesn't
apply to associated Security Hub member accounts.

## Editing a service-linked role for Security Hub

Security Hub doesn't allow you to edit the `AWSServiceRoleForSecurityHub` service-linked role. After
you create a service-linked role, you can't change the name of the role because various
entities might reference the role. However, you can edit the description of the role by
using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for Security Hub

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete the role. That way, you don't have an unused entity that
isn't actively monitored or maintained.

When you disable Security Hub, Security Hub doesn't automatically delete the `AWSServiceRoleForSecurityHub`
service-linked role for you. If you enable Security Hub again, the service can then start using
the existing service-linked role again. If you no longer need to use Security Hub, you can
manually delete the service-linked role.

###### Important

Before you delete the `AWSServiceRoleForSecurityHub` service-linked role, you must first
disable Security Hub in all the Regions where it's enabled. For more information, see [Disabling Security Hub CSPM](securityhub-disable.md "securityhub-disable.md"). If Security Hub
isn't disabled when you try to delete the service-linked role, the deletion
fails.

To delete the `AWSServiceRoleForSecurityHub` service-linked role, you can use the IAM
console, the IAM CLI, or the IAM API. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Service-linked role for AWS Security Hub V2

uses the service-linked role named `AWSServiceRoleForSecurityHubV2`. This
service-linked role allows to manage AWS Config rules and resources for your
organization and on your behalf. The `AWSServiceRoleForSecurityHubV2` service-linked role trusts
the `securityhub.amazonaws.com` service to assume the role.

The `AWSServiceRoleForSecurityHubV2` service-linked role uses the managed
policy [AWSSecurityHubV2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy").

###### Permissions details

This policy includes the following permissions:

- `cloudwatch` – Allows the role to retrieve metrics data to support metering capabilities for resources.
- `config` – Allows the role to manage service-linked configuration recorders for
  resources, including support for global AWS Config recorders.
- `ecr` – Allows the role to retrieve information about Amazon Elastic Container Registry images and repositories to support metering capabilities.
- `iam` – Allows the role to create the service-linked role for AWS Config and retrieve account information to support metering capabilities.
- `lambda` – Allows the role to retrieve AWS Lambda function information to support metering capabilities.
- `organizations` – Allows the role to retrieve account and organizational unit
  (OU) information for an organization.
- `securityhub` – Allows the role to manage the configuration.
- `tag` – Allows the role to retrieve information about resource tags.

You must grant permissions to allow an IAM identity (such as a role, group, or user)
to create, edit, or delete a service-linked role. For the `AWSServiceRoleForSecurityHubV2`
service-linked role to be successfully created, the IAM identity that you use to
access must have the required permissions. To grant the required permissions,
attach the following policy to the IAM identity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "securityhub:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "securityhub.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Creating a service-linked role for AWS Security Hub V2

The `AWSServiceRoleForSecurityHubV2` service-linked role is created automatically when you
enable for the first time or you enable in a Region where you didn't
previously enable it. You can also create the `AWSServiceRoleForSecurityHubV2` service-linked
role manually by using the IAM console, the IAM CLI, or the IAM API. For more
information about creating the role manually, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_.

###### Important

The service-linked role that's created for a administrator account doesn't
apply to associated member accounts.

### Editing a service-linked role for AWS Security Hub V2

doesn't allow you to edit the `AWSServiceRoleForSecurityHubV2` service-linked role. After
you create a service-linked role, you can't change the name of the role because various
entities might reference the role. However, you can edit the description of the role by
using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

### Deleting a service-linked role for AWS Security Hub V2

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete the role. That way, you don't have an unused entity that
isn't actively monitored or maintained.

When you disable , doesn't automatically delete the `AWSServiceRoleForSecurityHubV2`
service-linked role for you. If you enable again, the service can then start using
the existing service-linked role again. If you no longer need to use , you can
manually delete the service-linked role.

###### Important

Before you delete the `AWSServiceRoleForSecurityHubV2` service-linked role, you must first
disable in all the Regions where it's enabled. For more information, see [Disabling Security Hub CSPM](securityhub-disable.md "securityhub-disable.md"). If
isn't disabled when you try to delete the service-linked role, the deletion
fails.

To delete the `AWSServiceRoleForSecurityHubV2` service-linked role, you can use the IAM
console, the IAM CLI, or the IAM API. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
