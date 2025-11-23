# Using service-linked roles for Amazon Connect

Managed Synchronization

Amazon Connect managed synchronization uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to Managed Synchronization. Service-linked roles are predefined by Managed Synchronization
and include all the permissions that the service requires to call other AWS services on
your behalf.

A service-linked role makes setting up Managed Synchronization easier because you don’t have to
manually add the necessary permissions. Managed Synchronization defines the permissions of its
service-linked roles, and unless defined otherwise, only Managed Synchronization can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your Managed Synchronization resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for Managed Synchronization

Managed Synchronization uses the service-linked role that is prefixed with
**AWSServiceRoleForAmazonConnectSynchronization** which grants Amazon Connect Managed Synchronization read, write, update, and delete permission to access AWS resources on your behalf. The full name of the role in your
account will contain the prefix and a unique ID that will be similar to the
following:

`**AWSServiceRoleForAmazonConnectSynchronization**`\_unique-id``

The **AWSServiceRoleForAmazonConnectSynchronization** prefixed service-linked role trusts the following
services to assume the role:

- `synchronization.connect.amazonaws.com`

The role permissions policy named [AmazonConnectSynchronizationServiceRolePolicy](security_iam_awsmanpol.md#amazonconnectsynchronizationservicerolepolicy "security_iam_awsmanpol.md#amazonconnectsynchronizationservicerolepolicy")
allows Managed Synchronization to complete the following actions on the specified
resources:

- Action: Amazon Connect for all Amazon Connect resources
  - `connect:Create*`
  - `connect:Update*`
  - `connect:Delete*`
  - `connect:Describe*`
  - `connect:BatchCreate*`
  - `connect:BatchUpdate*`
  - `connect:BatchDelete*`
  - `connect:BatchDescribe*`
  - `connect:List*`
  - `connect:Search*`
  - `connect:Associate*`
  - `connect:Disassociate*`
  - `connect:Get*`
  - `connect:BatchGet*`
  - `connect:Import*`
  - `connect:TagResource`
  - `connect:UntagResource`

- Action: Amazon CloudWatch metrics `cloudwatch:PutMetricData` to publish
  Amazon Connect usage metrics for an instance to your account.

The role permissions policy named [AmazonConnectSynchronizationServiceRolePolicy](security_iam_awsmanpol.md#amazonconnectsynchronizationservicerolepolicy "security_iam_awsmanpol.md#amazonconnectsynchronizationservicerolepolicy") disallows Managed
Synchronization from completing the following actions on the specified resources:

- Action: Amazon Connect for all Amazon Connect resources
  - `connect:Start*`
  - `connect:Stop*`
  - `connect:Resume*`
  - `connect:Suspend*`
  - `connect:*Contact`
  - `connect:*Contacts`
  - `connect:*ContactAttributes*`
  - `connect:*RealtimeContact*`
  - `connect:*AnalyticsData*`
  - `connect:*MetricData*`
  - `connect:*UserData*`
  - `connect:*ContactEvaluation`
  - `connect:*AttachedFile*`
  - `connect:UpdateContactSchedule`
  - `connect:UpdateContactRoutingData`
  - `connect:ListContactReferences`
  - `connect:CreateParticipant`
  - `connect:CreatePersistentContactAssociation`
  - `connect:CreateInstance`
  - `connect:DeleteInstance`
  - `connect:ListInstances`
  - `connect:ReplicateInstance`
  - `connect:GetFederationToken`
  - `connect:ClaimPhoneNumber`
  - `connect:ImportPhoneNumber`
  - `connect:ReleasePhoneNumber`
  - `connect:SearchAvailablePhoneNumbers`
  - `connect:CreateTrafficDistributionGroup`
  - `connect:DeleteTrafficDistributionGroup`
  - `connect:GetTrafficDistribution`
  - `connect:UpdateTrafficDistribution`

You must configure permissions to allow your users, groups, or roles to create, edit,
or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

Managed Synchronization

You don't need to manually create a service-linked role. When you replicate an Amazon Connect
instance by invoking the `ReplicateInstance` API, Managed Synchronization creates the
service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you replicate the Amazon Connect
instance again, Managed Synchronization creates the service-linked role for you again.

## Editing a service-linked role for

Managed Synchronization

Managed Synchronization does not allow you to edit the AWSServiceRoleForAmazonConnectSynchronization prefixed service-linked role.
After you create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the description of the
role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

Managed Synchronization

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is
not actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Managed Synchronization service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes and
try the operation again.

###### To delete Managed Synchronization resources used by the AWSServiceRoleForAmazonConnectSynchronization prefixed role

- Delete all replica Amazon Connect instances for the source instance.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonConnectSynchronization prefixed
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for

Managed Synchronization service-linked roles

Managed Synchronization supports using service-linked roles in all of the Regions where Amazon
Connect Global Resiliency is available. For more information, see [Set up Amazon Connect Global Resiliency](setup-connect-global-resiliency.md "setup-connect-global-resiliency.md").

| Region name           | Region identity | Support in Managed Synchronization |
| --------------------- | --------------- | ---------------------------------- |
| US East (N. Virginia) | us-east-1       | Yes                                |
| US West (Oregon)      | us-west-2       | Yes                                |
