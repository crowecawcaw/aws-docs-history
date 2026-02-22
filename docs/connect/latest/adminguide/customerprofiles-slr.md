# Using service-linked roles for Amazon Connect Customer Profiles

Amazon Connect Customer Profiles uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Customer Profiles. Service-linked roles are predefined by Customer Profiles and include all the
permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon Connect Customer Profiles easier because you don’t have to manually
add the necessary permissions. Amazon Connect Customer Profiles defines the permissions of its service-linked roles,
and unless defined otherwise, only Amazon Connect Customer Profiles can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to view the service-linked
role documentation for that service.

## Service-linked role permissions for Amazon Connect

Customer Profiles

Amazon Connect Customer Profiles uses the service-linked role named
**AWSServiceRoleForProfile\_**`unique-id`
which allows Amazon Connect Customer Profiles to access AWS services and resources on your behalf..

The **AWSServiceRoleForProfile** prefixed service-linked role trusts the following
services to assume the role:

- `profile.amazonaws.com`

The role permissions policy named [CustomerProfilesServiceLinkedRolePolicy](security_iam_awsmanpol.md#customerprofilesservicelinkedrolepolicy "security_iam_awsmanpol.md#customerprofilesservicelinkedrolepolicy") allows Amazon Connect Customer Profiles to complete the following actions on the
specified resources:

- Action: Amazon CloudWatch Metrics `cloudwatch:PutMetricData` to publish
  Amazon Connect usage metrics for an instance to your account.
- Action: IAM `iam:DeleteRole` to delete the **AWSServiceRoleForProfile**
  prefixed service-linked role itself when associated Amazon Connect Customer Profiles
  Domain is deleted.
- Action: Amazon Connect Outbound Campaigns
  `connect-campaigns:PutProfileOutboundRequestBatch` to trigger a campaign
  based on your Customer Profiles Event Trigger Definition.
- Action: Amazon Connect Customer Profiles `profile:BatchGetProfile` to
  retrieve profile information necessary for triggering a campaign.
- Action: Amazon Connect Customer Profiles `profile:GetRecommender` to
  retrieve recommenders necessary for triggering a campaign.
- Action: Amazon Connect Customer Profiles `profile:GetCalculatedAttributeForProfile` to
  retrieve calculated attributes necessary for triggering a campaign.
- Action: Amazon Connect Customer Profiles `profile:GetProfileRecommendations` to
  retrieve profile recommendations necessary for triggering a campaign.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Amazon Connect

Customer Profiles

You don't need to manually create a service-linked role. When you
create your first Amazon Connect Customer Profiles Domain in the AWS Management Console, the AWS CLI, or the AWS API, Customer Profiles creates the
service-linked role for you. Note each Amazon Connect Customer Profiles domain requires a dedicated SLR in order for
Amazon Connect Customer Profiles to take actions for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
Amazon Connect Customer Profiles service before June 8, 2023, when it began supporting service-linked roles,
then Amazon Connect Customer Profiles created the **AWSServiceRoleForProfile** prefixed role in your account.
To learn more, see [A
new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create your first Amazon Connect Customer Profiles Domain, Customer Profiles
creates the service-linked role for you again.

## Editing a service-linked role for Amazon Connect

Customer Profiles

Amazon Connect Customer Profiles does not allow you to edit the **AWSServiceRoleForProfile** prefixed
service-linked role. After you create a service-linked role, you cannot change the name of the
role because various entities might reference the role. However, you can edit the description
of the role using IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon Connect

Customer Profiles

You don't need to manually delete the **AWSServiceRoleForProfile** prefixed role. When
you delete the Amazon Connect Customer Profiles Domain in the AWS Management Console, the AWS CLI, or the AWS API, Customer Profiles cleans up
the resources and deletes the service-linked role for you.

You can also use the AWS CLI or the AWS API to manually delete the service-linked role. To
do this, you must first manually clean up the resources for your service-linked role and then
you can manually delete it.

###### Note

If the Amazon Connect Customer Profiles service is using the role when you try to delete the resources, then
the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete Amazon Connect Customer Profiles resources used by the AWSServiceRoleForProfile prefixed service-linked

role

- Delete the Amazon Connect Customer Profiles domain in the AWS Management Console, the AWS CLI, or the AWS API.

**To manually delete the service-linked role using
IAM**

Use the AWS CLI or the AWS API to delete the **AWSServiceRoleForProfile** prefixed
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for Amazon Connect Customer Profiles service-linked

roles

Amazon Connect Customer Profiles supports using service-linked roles in all of the regions where the service is
available. For more information, see [AWS regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

| Region name              | Region identity | Support in Amazon Connect |
| ------------------------ | --------------- | ------------------------- |
| US East (N. Virginia)    | us-east-1       | Yes                       |
| US West (Oregon)         | us-west-2       | Yes                       |
| Asia Pacific (Seoul)     | ap-northeast-2  | Yes                       |
| Asia Pacific (Singapore) | ap-southeast-1  | Yes                       |
| Asia Pacific (Sydney)    | ap-southeast-2  | Yes                       |
| Asia Pacific (Tokyo)     | ap-northeast-1  | Yes                       |
| Canada (Central)         | ca-central-1    | Yes                       |
| Europe (Frankfurt)       | eu-central-1    | Yes                       |
| Europe (London)          | eu-west-2       | Yes                       |
| Africa (Cape Town)       | af-south-1      | Yes                       |
