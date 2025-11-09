AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Using roles to collect inventory and view OpsData

Systems Manager uses the service-linked role named **`AWSServiceRoleForAmazonSSM`**. AWS Systems Manager uses this IAM service role to manage AWS resources on your behalf.

## Service-linked

role permissions for inventory, OpsData, and OpsItems

The `AWSServiceRoleForAmazonSSM` service-linked role trusts only
`ssm.amazonaws.com` to assume this role.

You can use the Systems Manager service-linked role `AWSServiceRoleForAmazonSSM` for the
following:

- The Systems Manager Inventory tool uses the service-linked role
  `AWSServiceRoleForAmazonSSM` to collect inventory metadata from tags
  and resource groups.
- The Explorer tool uses the service-linked role
  `AWSServiceRoleForAmazonSSM` to enable viewing OpsData and OpsItems from
  multiple accounts. This service-linked role also allows Explorer to
  create a managed rule when you enable Security Hub as a data source from
  Explorer or OpsCenter.

###### Important

Previously, the Systems Manager console provided you with the ability to choose the AWS managed
IAM service-linked role `AWSServiceRoleForAmazonSSM` to use as the maintenance
role for your tasks. Using this role and its associated policy,
`AmazonSSMServiceRolePolicy`, for maintenance window tasks is no longer
recommended. If you're using this role for maintenance window tasks now, we encourage
you to stop using it. Instead, create your own IAM role that enables communication between
Systems Manager and other AWS services when your maintenance window tasks run.

For more information, see [Setting up Maintenance Windows](setting-up-maintenance-windows.md "setting-up-maintenance-windows.md").

The managed policy that is used to provide permissions for the
`AWSServiceRoleForAmazonSSM` role is `AmazonSSMServiceRolePolicy`.
For details about the permissions it grants, see [AWS managed
policy: AmazonSSMServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSSMServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSSMServiceRolePolicy").

## Creating the

`AWSServiceRoleForAmazonSSM` service-linked role for
Systems Manager

You can use the IAM console to create a service-linked role with the
**EC2** use case. Using commands for IAM in the AWS Command Line Interface
(AWS CLI) or using the IAM API, create a service-linked role with the
`ssm.amazonaws.com` service name. For more information,
see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_.

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account.

## Editing the

`AWSServiceRoleForAmazonSSM` service-linked role for
Systems Manager

Systems Manager doesn't allow you to edit the `AWSServiceRoleForAmazonSSM`
service-linked role. After you create a service-linked role, you can't change
the name of the role because various entities might reference the role. However,
you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the

`AWSServiceRoleForAmazonSSM` service-linked role for
Systems Manager

If you no longer need to use any feature or service that requires a
service-linked role, then we recommend that you delete that role. That way you
don’t have an unused entity that isn't actively monitored or maintained. You can
use the IAM console, the AWS CLI, or the IAM API to manually delete the
service-linked role. To do this, you must first manually clean up the resources
for your service-linked role, and then you can manually delete it.

Because the `AWSServiceRoleForAmazonSSM` service-linked role can be used by
multiple tools, ensure that none are using the role before attempting to delete
it.

- **Inventory:** If you delete the
  service-linked role used by the Inventory tool, then the Inventory data
  for tags and resource groups will no longer be synchronized. You must
  clean up the resources for your service-linked role before you can
  manually delete it.
- **Explorer:** If you delete the
  service-linked role used by the Explorer tool, then the cross-account
  and cross-Region OpsData and OpsItems are no longer viewable.

###### Note

If the Systems Manager service is using the role when you try to delete tags
or resource groups, then the deletion might fail. If that happens, wait for
a few minutes and try the operation again.

###### To delete Systems Manager resources used by the

`AWSServiceRoleForAmazonSSM`

1. To delete tags, see [Add and delete tags on an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").
2. To delete resource groups, see [Delete
   groups from AWS Resource Groups](../../../ARG/latest/userguide/deleting-resource-groups.md "../../../ARG/latest/userguide/deleting-resource-groups.md").

**To manually delete the `AWSServiceRoleForAmazonSSM`
service-linked role using IAM**

Use the IAM console, the AWS CLI, or the IAM API to delete the
`AWSServiceRoleForAmazonSSM` service-linked role. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for the

Systems Manager  `AWSServiceRoleForAmazonSSM` service-linked role

Systems Manager supports using the `AWSServiceRoleForAmazonSSM` service-linked
role in all of the AWS Regions where the service is available. For more
information, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md").
