• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Using roles to create OpsData and OpsItems for Explorer

Systems Manager uses the service-linked role named **`AWSServiceRoleForSystemsManagerOpsDataSync`**. AWS Systems Manager uses this IAM service role for Explorer to create OpsData and OpsItems.

## Service-linked role permissions

for Systems Manager OpsData sync

The `AWSServiceRoleForSystemsManagerOpsDataSync` service-linked role trusts the following
services to assume the role:

- `opsdatasync.ssm.amazonaws.com`

The role permissions policy allows Systems Manager to complete the following
actions on the specified resources:

- Systems Manager Explorer requires that a service-linked role grant permission to update
  a security finding when an OpsItem is updated, create and update an OpsItem,
  and turn off the Security Hub CSPM data source when an SSM managed rule is deleted
  by customers.

The managed policy that is used to provide permissions for the
`AWSServiceRoleForSystemsManagerOpsDataSync` role is
`AWSSystemsManagerOpsDataSyncServiceRolePolicy`. For details
about the permissions it grants, see [AWS managed policy: AWSSystemsManagerOpsDataSyncServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy").

You must configure permissions to allow an IAM entity (such as a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the

`AWSServiceRoleForSystemsManagerOpsDataSync` service-linked role for
Systems Manager

You don't need to manually create a service-linked role. When you enable
Explorer in the AWS Management Console, Systems Manager creates the service-linked role for
you.

###### Important

This service-linked role can be displayed in your account if you completed
an action in another service that uses the features supported by this role.
Also, if you were using the Systems Manager service before January 1, 2017,
when it began supporting service-linked roles, then Systems Manager created
the `AWSServiceRoleForSystemsManagerOpsDataSync` role in your account. To learn more, see
[A new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account. When you enable
Explorer in the AWS Management Console, Systems Manager creates the service-linked role for you
again.

You can also use the IAM console to create a service-linked role with the
**AWS service role that allows Explorer to create OpsData and OpsItems** use case. In the AWS CLI or the
AWS API, create a service-linked role with the
`opsdatasync.ssm.amazonaws.com` service name. For more information,
see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_. If you delete this service-linked
role, you can use this same process to create the role again.

## Editing the `AWSServiceRoleForSystemsManagerOpsDataSync`

service-linked role for Systems Manager

Systems Manager doesn't allow you to edit the `AWSServiceRoleForSystemsManagerOpsDataSync`
service-linked role. After you create a service-linked role, you can't change
the name of the role because various entities might reference the role. However,
you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the

`AWSServiceRoleForSystemsManagerOpsDataSync` service-linked role for
Systems Manager

If you no longer need to use a feature or service that requires a
service-linked role, we recommend that you delete that role. That way you don’t
have an unused entity that isn't actively monitored or maintained. However, you
must clean up the resources for your service-linked role before you can manually
delete it.

###### Note

If the Systems Manager service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few
minutes and try the operation again.

The procedure for deleting Systems Manager resources used by the
`AWSServiceRoleForSystemsManagerOpsDataSync` role depends on if you've configured Explorer or
OpsCenter to integrate with Security Hub CSPM.

###### To delete Systems Manager resources used by the `AWSServiceRoleForSystemsManagerOpsDataSync`

role

- To stop Explorer from creating new OpsItems for Security Hub CSPM findings, see [How to stop
  receiving findings](explorer-securityhub-integration.md#explorer-securityhub-integration-disable-receive "explorer-securityhub-integration.md#explorer-securityhub-integration-disable-receive").
- To stop OpsCenter from creating new OpsItems for Security Hub CSPM findings, see

**To manually delete the `AWSServiceRoleForSystemsManagerOpsDataSync`
service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForSystemsManagerOpsDataSync` service-linked role. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for the

Systems Manager  `AWSServiceRoleForSystemsManagerOpsDataSync` service-linked role

Systems Manager supports using service-linked roles in all of the Regions where
the service is available. For more information, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md").

Systems Manager doesn't support using service-linked roles in every Region where
the service is available. You can use the `AWSServiceRoleForSystemsManagerOpsDataSync` role in
the following Regions.

| AWS Region name           | Region identity | Support in Systems Manager |
| ------------------------- | --------------- | -------------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                        |
| US East (Ohio)            | us-east-2       | Yes                        |
| US West (N. California)   | us-west-1       | Yes                        |
| US West (Oregon)          | us-west-2       | Yes                        |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                        |
| Asia Pacific (Osaka)      | ap-northeast-3  | Yes                        |
| Asia Pacific (Seoul)      | ap-northeast-2  | Yes                        |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                        |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                        |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                        |
| Canada (Central)          | ca-central-1    | Yes                        |
| Europe (Frankfurt)        | eu-central-1    | Yes                        |
| Europe (Ireland)          | eu-west-1       | Yes                        |
| Europe (London)           | eu-west-2       | Yes                        |
| Europe (Paris)            | eu-west-3       | Yes                        |
| Europe (Stockholm)        | eu-north-1      | Yes                        |
| South America (São Paulo) | sa-east-1       | Yes                        |
| AWS GovCloud (US)         | us-gov-west-1   | No                         |
