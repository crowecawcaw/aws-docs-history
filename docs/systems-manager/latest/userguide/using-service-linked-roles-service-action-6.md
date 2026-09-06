

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Using roles to export Explorer OpsData
<a name="using-service-linked-roles-service-action-6"></a>

AWS Systems Manager Explorer uses the **AmazonSSMExplorerExportRole** service role to export operations data (OpsData) using the `AWS-ExportOpsDataToS3` automation runbook.

## Service-linked role permissions for Explorer
<a name="service-linked-role-permissions-service-action-6"></a>

The `AmazonSSMExplorerExportRole` service-linked role trusts only `ssm.amazonaws.com` to assume this role. 

You can use the `AmazonSSMExplorerExportRole` service-linked role to export operations data (OpsData) using the `AWS-ExportOpsDataToS3` automation runbook. You can export 5,000 OpsData items from Explorer as a comma separated value (.csv) file to an Amazon Simple Storage Service (Amazon S3) bucket.

The role permissions policy allows Systems Manager to complete the following actions on the specified resources:
+ `s3:PutObject`
+ `s3:GetBucketAcl`
+ `s3:GetBucketLocation`
+ `sns:Publish`
+ `logs:DescribeLogGroups`
+ `logs:DescribeLogStreams`
+ `logs:CreateLogGroup`
+ `logs:PutLogEvents` 
+ `logs:CreateLogStream`
+ `ssm:GetOpsSummary`

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating the `AmazonSSMExplorerExportRole` service-linked role for Systems Manager
<a name="create-service-linked-role-service-action-6"></a>

Systems Manager creates the `AmazonSSMExplorerExportRole` service-linked role when you export OpsData using Explorer in the Systems Manager console. For more information, see [Exporting OpsData from Systems Manager Explorer](Explorer-exporting-OpsData.md).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. 

## Editing the `AmazonSSMExplorerExportRole` service-linked role for Systems Manager
<a name="edit-service-linked-role-service-action-6"></a>

Systems Manager doesn't allow you to edit the `AmazonSSMExplorerExportRole` service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting the `AmazonSSMExplorerExportRole` service-linked role for Systems Manager
<a name="delete-service-linked-role-service-action-6"></a>

If you no longer need to use any feature or service that requires a service-linked role, then we recommend that you delete that role. That way you don’t have an unused entity that isn't actively monitored or maintained. You can use the IAM console, the AWS CLI, or the IAM API to manually delete the service-linked role. To do this, you must first manually clean up the resources for your service-linked role. Then, you can manually delete it.

**Note**  
If the Systems Manager service is using the role when you try to delete tags or resource groups, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete Systems Manager resources used by the `AmazonSSMExplorerExportRole`**

1. To delete tags, see [Add and delete tags on an individual resource](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#adding-or-deleting-tags).

1. To delete resource groups, see [Delete groups from AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/deleting-resource-groups.html).

**To manually delete the `AmazonSSMExplorerExportRole` service-linked role using IAM**

Use the IAM console, the AWS CLI, or the IAM API to delete the `AmazonSSMExplorerExportRole` service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for the Systems Manager  `AmazonSSMExplorerExportRole` service-linked role
<a name="slr-regions-service-action-6"></a>

Systems Manager supports using the `AmazonSSMExplorerExportRole` service-linked role in all of the AWS Regions where the service is available. For more information, see [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html).