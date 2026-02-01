• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Using roles to export Explorer OpsData

AWS Systems Manager Explorer uses the **AmazonSSMExplorerExportRole** service role to export operations data (OpsData) using the
`AWS-ExportOpsDataToS3` automation runbook.

## Service-linked

role permissions for Explorer

The `AmazonSSMExplorerExportRole` service-linked role trusts only
`ssm.amazonaws.com` to assume this role.

You can use the `AmazonSSMExplorerExportRole` service-linked role to export
operations data (OpsData) using the `AWS-ExportOpsDataToS3`
automation runbook. You can export 5,000 OpsData items from Explorer as a comma
separated value (.csv) file to an Amazon Simple Storage Service (Amazon S3) bucket.

The role permissions policy allows Systems Manager to complete the following
actions on the specified resources:

- `s3:PutObject`
- `s3:GetBucketAcl`
- `s3:GetBucketLocation`
- `sns:Publish`
- `logs:DescribeLogGroups`
- `logs:DescribeLogStreams`
- `logs:CreateLogGroup`
- `logs:PutLogEvents`
- `logs:CreateLogStream`
- `ssm:GetOpsSummary`

You must configure permissions to allow an IAM entity (such as a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the

`AmazonSSMExplorerExportRole` service-linked role for
Systems Manager

Systems Manager creates the `AmazonSSMExplorerExportRole` service-linked role when you
export OpsData using Explorer in the Systems Manager console. For more information, see
[Exporting OpsData from Systems Manager
Explorer](Explorer-exporting-OpsData.md "Explorer-exporting-OpsData.md").

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account.

## Editing the

`AmazonSSMExplorerExportRole` service-linked role for
Systems Manager

Systems Manager doesn't allow you to edit the `AmazonSSMExplorerExportRole`
service-linked role. After you create a service-linked role, you can't change
the name of the role because various entities might reference the role. However,
you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the

`AmazonSSMExplorerExportRole` service-linked role for
Systems Manager

If you no longer need to use any feature or service that requires a
service-linked role, then we recommend that you delete that role. That way you
don’t have an unused entity that isn't actively monitored or maintained. You can
use the IAM console, the AWS CLI, or the IAM API to manually delete the
service-linked role. To do this, you must first manually clean up the resources
for your service-linked role, and then you can manually delete it.

###### Note

If the Systems Manager service is using the role when you try to delete tags
or resource groups, then the deletion might fail. If that happens, wait for
a few minutes and try the operation again.

###### To delete Systems Manager resources used by the

`AmazonSSMExplorerExportRole`

1. To delete tags, see [Add and delete tags on an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").
2. To delete resource groups, see [Delete
   groups from AWS Resource Groups](../../../ARG/latest/userguide/deleting-resource-groups.md "../../../ARG/latest/userguide/deleting-resource-groups.md").

**To manually delete the `AmazonSSMExplorerExportRole`
service-linked role using IAM**

Use the IAM console, the AWS CLI, or the IAM API to delete the
`AmazonSSMExplorerExportRole` service-linked role. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for the

Systems Manager  `AmazonSSMExplorerExportRole` service-linked role

Systems Manager supports using the `AmazonSSMExplorerExportRole` service-linked
role in all of the AWS Regions where the service is available. For more
information, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md").
