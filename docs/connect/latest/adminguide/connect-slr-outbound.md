# Use service-linked roles for outbound campaigns in

Amazon Connect

Amazon Connect outbound campaigns uses AWS Identity and Access Management service-linked roles. When an Amazon Connect instance is enabled to
use outbound campaigns, it creates a unique service linked role that allows it to perform actions on
the Amazon Connect instance.

A service-linked role makes setting up outbound campaigns easier because you don't have to manually
add the necessary permissions. Outbound campaigns defines the permissions of its service-linked
roles, and unless defined otherwise, only outbound campaigns can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that permissions policy
cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_. Look for the
services that have **Yes** in the **Service-Linked Role**
column. Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for

outbound campaigns

Outbound campaigns uses the service-linked role prefixed
`AWSServiceRoleForConnectCampaigns`—Grants outbound campaigns permission to
access AWS resources on your behalf.

The `AWSServiceRoleForConnectCampaigns` service-linked role trusts the
following services to assume the role:

- `connect-campaigns.amazonaws.com`

The [AmazonConnectCampaignsServiceLinkedRolePolicy](security_iam_awsmanpol.md#amazonconnectcampaignsservicelinkedrolepolicy "security_iam_awsmanpol.md#amazonconnectcampaignsservicelinkedrolepolicy") role permissions policy allows
outbound campaigns to complete the following actions on the specified resources. Additional
permissions are added for the service-linked role to access the resources:

- Action: Outbound campaigns `connect-campaigns:ListCampaigns` for the
  AWS account.
- Action: Amazon Connect

      + `connect:BatchPutContact`
      + `connect:StopContact`

  for all Amazon Connect instances.

- Action: Amazon Connect

      + `connect:StartOutboundVoiceContact`
      + `connect:GetMetricData`
      + `connect:GetCurrentMetricData`
      + `connect:BatchPutContact`
      + `connect:StopContact`
      + `connect:GetMetricDataV2`
      + `connect:DescribeContactFlow`
      + `connect:SendOutboundEmail`

  For the Amazon Connect instance specified.

- Action: EventBridge:

      + `events:ListRules`

  For all events.

- Action: EventBridge:

      + `events:DeleteRule`
      + `events:PutRule`
      + `events:PutTargets`
      + `events:RemoveTargets`
      + `events:ListTargetsByRule`

  for rules named `ConnectCampaignsRule*` managed by
  `connect-campaigns.amazonaws.com`.

- Action: Connect AI agents Message Templates:

      + `wisdom:GetMessageTemplate`
      + `wisdom:RenderMessageTemplate`

  on all resources tagged with
  `aws:ResourceTag/AmazonConnectCampaignsEnabled`.

Permissions for Amazon Connect Customer Profiles will be added to ezCRC template:
`ConnectCampaignsCustomerProfilesIntegrationAccess`.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Create a service-linked role for outbound campaigns

You don't need to manually create a service-linked role. When you associate an Amazon Connect
instance with outbound campaigns by invoking the `StartInstanceOnboardingJob` API,
outbound campaigns creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you associate a new Amazon Connect
instance with outbound campaigns, Amazon Connect creates the service-linked role for you again.

## Edit a service-linked role for outbound campaigns

Outbound campaigns does not allow you to edit the
`AWSServiceRoleForConnectCampaigns` service-linked role. After you create
a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM.
For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Delete a service-linked role for outbound campaigns

If you no longer need outbound campaigns, we recommend that you delete the associated
service-linked role. That way you don’t have an unused entity that is not actively
monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### To delete outbound campaigns resources used by the

`AWSServiceRoleForConnectCampaigns`

- Delete all campaigns setup for the AWS account.

###### To manually delete the service-linked role using IAM

- Use the IAM console, the AWS CLI, or the AWS API to delete the
  `AWSServiceRoleForConnectCampaigns` service-linked role. For more
  information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
  _IAM User Guide_.

## Supported Regions for outbound campaigns service-linked

roles

Outbound campaigns supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md#connect_region "../../../general/latest/gr/rande.md#connect_region").
