AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Mainframe Modernization API permissions: Actions,

resources, and conditions reference

When you are writing permissions policies that you can attach to an IAM identity
(identity-based policies), you can use the following table as a reference. The table
includes the following:

- Each AWS Mainframe Modernization API operation.
- The corresponding actions for which you can grant permissions to perform
  the action.
- The AWS resource for which you can grant the permissions.
  You specify the actions in the policy's `Action` field and the
  resource value in the policy's `Resource` field.

You can use AWS global condition keys in your AWS Mainframe Modernization policies to express
conditions. For a complete list of AWS keys, see [Available Global Condition Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys") in the
_IAM User Guide_.

###### Note

To specify an action, use the `m2:` prefix followed by the API
operation name (for example, `m2:CreateApplication`).

AWS Mainframe Modernization API and required permissions
for actions | AWS Mainframe Modernization API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [CancelBatchJobExecution](../APIReference/API_CancelBatchJobExecution.md "../APIReference/API_CancelBatchJobExecution.md") | | Application |
| [CreateApplication](../APIReference/API_CreateApplication.md "../APIReference/API_CreateApplication.md") | `iam:PassRole`<br>`kms:DescribeKey`<br>`kms:CreateGrant`<br>`s3:GetObject`<br>`s3:ListBucket` | Application |
| [CreateDataSetImportTask](../APIReference/API_CreateDataSetImportTask.md "../APIReference/API_CreateDataSetImportTask.md") | `s3:GetObject` | Application |
| [CreateDataSetExportTask](../APIReference/API_CreateDataSetExportTask.md "../APIReference/API_CreateDataSetExportTask.md") | `kms:DescribeKey`<br>`s3:PutObject` | Application |
| [CreateDeployment](../APIReference/API_CreateDeployment.md "../APIReference/API_CreateDeployment.md") | `elasticloadbalancing:AddTags`<br>`elasticloadbalancing:CreateListener`<br>`elasticloadbalancing:CreateTargetGroup`<br>`elasticloadbalancing:RegisterTargets`<br>`elasticloadbalancing:DeleteListener`<br>`elasticloadbalancing:DeleteTargetGroup`<br>`elasticloadbalancing:DeregisterTargets`<br>`elasticloadbalancing:DeleteLoadBalancer`<br>`logs:CreateLogDelivery`<br>`logs:GetLogDelivery`<br>`logs:UpdateLogDelivery`<br>`logs:DeleteLogDelivery`<br>`logs:ListLogDeliveries`<br>`logs:PutResourcePolicy`<br>`logs:DescribeResourcePolicies`<br>`logs:DescribeLogGroups` | Application |
| [CreateEnvironment](../APIReference/API_CreateEnvironment.md "../APIReference/API_CreateEnvironment.md") | `ec2:CreateNetworkInterface`<br>`ec2:CreateNetworkInterfacePermission`<br>`ec2:DescribeNetworkInterfaces`<br>`ec2:DescribeSecurityGroups`<br>`ec2:DescribeSubnets`<br>`ec2:DescribeVpcAttribute`<br>`ec2:DescribeVpcs`<br>`ec2:ModifyNetworkInterfaceAttribute`<br>`elasticfilesystem:DescribeMountTargets`<br>`elasticloadbalancing:AddTags`<br>`elasticloadbalancing:CreateLoadBalancer`<br>`elasticloadbalancing:DeleteLoadBalancer`<br>`kms:DescribeKey`<br>`kms:CreateGrant`<br>`fsx:DescribeFileSystems`<br>`iam:CreateServiceLinkedRole` | Environment |
| [DeleteApplication](../APIReference/API_DeleteApplication.md "../APIReference/API_DeleteApplication.md") | `elasticloadbalancing:DeleteListener`<br>`elasticloadbalancing:DeleteTargetGroup`<br>`logs:DeleteLogDelivery` | Application |
| [DeleteApplicationFromEnvironment](../APIReference/API_DeleteApplicationFromEnvironment.md "../APIReference/API_DeleteApplicationFromEnvironment.md") | `elasticloadbalancing:DeleteListener`<br>`elasticloadbalancing:DeleteTargetGroup` | Application<br>Environment |
| [DeleteEnvironment](../APIReference/API_DeleteEnvironment.md "../APIReference/API_DeleteEnvironment.md") | `elasticloadbalancing:DeleteLoadBalancer` | Environment |
| [GetApplication](../APIReference/API_GetApplication.md "../APIReference/API_GetApplication.md") | | Application |
| [GetApplicationVersion](../APIReference/API_GetApplicationVersion.md "../APIReference/API_GetApplicationVersion.md") | | Application |
| [GetBatchJobExecution](../APIReference/API_GetBatchJobExecution.md "../APIReference/API_GetBatchJobExecution.md") | | Application |
| [GetDataSetDetails](../APIReference/API_GetDataSetDetails.md "../APIReference/API_GetDataSetDetails.md") | | Application |
| [GetDataSetImportTask](../APIReference/API_GetDataSetImportTask.md "../APIReference/API_GetDataSetImportTask.md") | | Application |
| [GetDataSetExportTask](../APIReference/API_GetDataSetExportTask.md "../APIReference/API_GetDataSetExportTask.md") | | Application |
| [GetDeployment](../APIReference/API_GetDeployment.md "../APIReference/API_GetDeployment.md") | | Application |
| [GetEnvironment](../APIReference/API_GetEnvironment.md "../APIReference/API_GetEnvironment.md") | | Environment |
| [ListApplications](../APIReference/API_ListApplications.md "../APIReference/API_ListApplications.md") | | \* |
| [ListApplicationVersions](../APIReference/API_ListApplicationVersions.md "../APIReference/API_ListApplicationVersions.md") | | \* |
| [ListBatchJobDefinitions](../APIReference/API_ListBatchJobDefinitions.md "../APIReference/API_ListBatchJobDefinitions.md") | | \* |
| [ListBatchJobExecutions](../APIReference/API_ListBatchJobExecutions.md "../APIReference/API_ListBatchJobExecutions.md") | | \* |
| [ListDataSetImportHistory](../APIReference/API_ListDataSetImportHistory.md "../APIReference/API_ListDataSetImportHistory.md") | | \* |
| [ListDataSetExportHistory](../APIReference/API_ListDataSetExportHistory.md "../APIReference/API_ListDataSetExportHistory.md") | | \* |
| [ListDataSets](../APIReference/API_ListDataSets.md "../APIReference/API_ListDataSets.md") | | \* |
| [ListDeployments](../APIReference/API_ListDeployments.md "../APIReference/API_ListDeployments.md") | | \* |
| [ListEngineVersions](../APIReference/API_ListEngineVersions.md "../APIReference/API_ListEngineVersions.md") | | \* |
| [ListEnvironments](../APIReference/API_ListEnvironments.md "../APIReference/API_ListEnvironments.md") | | \* |
| [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") | | \* |
| [StartApplication](../APIReference/API_StartApplication.md "../APIReference/API_StartApplication.md") | | Application |
| [StartBatchJob](../APIReference/API_StartBatchJob.md "../APIReference/API_StartBatchJob.md") | | Application |
| [StopApplication](../APIReference/API_StopApplication.md "../APIReference/API_StopApplication.md") | | Application |
| [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") | | \* |
| [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") | | \* |
| [UpdateApplication](../APIReference/API_UpdateApplication.md "../APIReference/API_UpdateApplication.md") | `s3:GetObject`<br>`s3:ListBucket` | Application |
| [UpdateEnvironment](../APIReference/API_UpdateEnvironment.md "../APIReference/API_UpdateEnvironment.md") | `kms:DescribeKey` | Environment |
