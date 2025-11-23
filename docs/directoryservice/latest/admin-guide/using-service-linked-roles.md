# Using service-linked roles for

Directory Service

AWS Directory Service uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Directory Service. Service-linked roles are predefined by Directory Service and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Directory Service easier because you don't have to
manually add the necessary permissions. Directory Service defines the permissions of its
service-linked roles, and unless defined otherwise, only Directory Service can assume its roles. The
defined permissions include the trust policy and the permissions policy, which cannot be
attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
prevents you from losing access to your Directory Service resources because you can't inadvertently
remove the permissions to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md").

###### Topics

- [Service-linked role permissions for Directory Service](#slr-permissions "#slr-permissions")
- [Creating a service-linked role for Directory Service](#create-slr "#create-slr")
- [Editing a service-linked role for Directory Service](#edit-slr "#edit-slr")
- [Deleting a service-linked role for Directory Service](#delete-slr "#delete-slr")
- [Supported Regions for Directory Service service-linked roles](#slr-regions "#slr-regions")

## Service-linked role permissions for Directory Service

Directory Service uses the service-linked role named **AWSServiceRoleForDirectoryService** –
Allows AWS to monitor customer's self-managed domain controllers.

The **AWSServiceRoleForDirectoryService** service-linked role trusts the following services to assume the
role:

- `ds.amazonaws.com`

The role permissions policy named AWSDirectoryServiceServiceRolePolicy allows Directory Service to complete the
following actions on the specified resources. For the complete policy permissions, see [AWSDirectoryServiceServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSDirectoryServiceServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSDirectoryServiceServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

- `ec2` – Allows the service to describe network resources such as
  VPCs, subnets, security groups, and network interfaces to validate hybrid connectivity
  configurations:
  - `ec2:DescribeAvailabilityZones`
  - `ec2:DescribeDhcpOptions`
  - `ec2:DescribeNetworkInterfaces`
  - `ec2:DescribeRouteTables`
  - `ec2:DescribeSecurityGroups`
  - `ec2:DescribeSubnets`
  - `ec2:DescribeVpcs`

- `ssm` – Allows the service to send and monitor PowerShell guilabels
  to on-premises domain controllers for monitoring and assessment purposes:
  - `ssm:Sendguilabel`
  - `ssm:Listguilabels`
  - `ssm:GetguilabelInvocation`
  - `ssm:DescribeInstanceInformation`
  - `ssm:GetConnectionStatus`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Directory Service

You don't need to manually create a service-linked role. When you
allows AWS to monitor customer's self-managed domain controllers in the AWS Management Console, the AWS CLI, or the AWS API, Directory Service creates
the service-linked role for you. For more information about this change, see [Policy updates](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
Directory Service service before January 1, 2017, when it began supporting service-linked roles,
then Directory Service created the **AWSServiceRoleForDirectoryService** role in your account. To learn more, see [A
new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

## Editing a service-linked role for Directory Service

Directory Service does not allow you to edit the **AWSServiceRoleForDirectoryService** service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Directory Service

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don't have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Directory Service service is using the role at the time that you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete Directory Service resources used by the AWSServiceRoleForDirectoryService

- To delete your directory, see [Deleting your AWS Managed Microsoft AD](ms_ad_delete.md "ms_ad_delete.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForDirectoryService** service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Directory Service service-linked roles

Directory Service does not support using service-linked roles in every Region where the
service is available. However, Directory Service uses the **AWSServiceRoleForDirectoryService** role only in AWS Regions where
you can opt-in to hybrid directories.

| Hybrid directory opt-in Region support | Region name    | Region identity | opt-in support |
| -------------------------------------- | -------------- | --------------- | -------------- |
| US East (N. Virginia)                  | us-east-1      | Yes             |
| US East (Ohio)                         | us-east-2      | Yes             |
| US West (N. California)                | us-west-1      | Yes             |
| US West (Oregon)                       | us-west-2      | Yes             |
| Europe (Stockholm)                     | eu-north-1     | Yes             |
| Middle East (Bahrain)                  | me-south-1     | Yes             |
| Asia Pacific (Mumbai)                  | ap-south-1     | Yes             |
| Europe (Paris)                         | eu-west-3      | Yes             |
| Asia Pacific (Jakarta)                 | ap-southeast-3 | Yes             |
| Africa (Cape Town)                     | af-south-1     | Yes             |
| Europe (Ireland)                       | eu-west-1      | Yes             |
| Middle East (UAE)                      | me-central-1   | Yes             |
| Europe (Frankfurt)                     | eu-central-1   | Yes             |
| South America (São Paulo)              | sa-east-1      | Yes             |
| Asia Pacific (Hong Kong)               | ap-east-1      | Yes             |
| Asia Pacific (Hyderabad)               | ap-south-2     | Yes             |
| Asia Pacific (Seoul)                   | ap-northeast-2 | Yes             |
| Asia Pacific (Osaka)                   | ap-northeast-3 | Yes             |
| Europe (London)                        | eu-west-2      | Yes             |
| Asia Pacific (Melbourne)               | ap-southeast-4 | Yes             |
| Europe (Milan)                         | eu-south-1     | Yes             |
| Asia Pacific (Tokyo)                   | ap-northeast-1 | Yes             |
| Asia Pacific (Singapore)               | ap-southeast-1 | Yes             |
| Asia Pacific (Sydney)                  | ap-southeast-2 | Yes             |
| Canada (Central)                       | ca-central-1   | Yes             |
| Europe (Spain)                         | eu-south-2     | Yes             |
| Europe (Zurich)                        | eu-central-2   | Yes             |
