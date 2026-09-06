

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Mainframe Modernization API permissions: Actions, resources, and conditions reference
<a name="UsingWithM2_IAM_ResourcePermissions"></a>

When you are writing permissions policies that you can attach to an IAM identity (identity-based policies), you can use the following table as a reference. The table includes the following:
+ Each AWS Mainframe Modernization API operation.
+ The corresponding actions for which you can grant permissions to perform the action.
+ The AWS resource for which you can grant the permissions.

 You specify the actions in the policy's `Action` field and the resource value in the policy's `Resource` field. 

You can use AWS global condition keys in your AWS Mainframe Modernization policies to express conditions. For a complete list of AWS keys, see [Available Global Condition Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#AvailableKeys) in the *IAM User Guide*. 

**Note**  
To specify an action, use the `m2:` prefix followed by the API operation name (for example, `m2:CreateApplication`).


**AWS Mainframe Modernization API and required permissions for actions**  

| AWS Mainframe Modernization API Operations | Required Permissions (API Actions) | Resources | 
| --- | --- | --- | 
|  [CancelBatchJobExecution](https://docs.aws.amazon.com/m2/latest/APIReference/API_CancelBatchJobExecution.html)  |  | Application | 
| [CreateApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateApplication.html)  | `iam:PassRole`<br />`kms:DescribeKey`<br />`kms:CreateGrant`<br />`s3:GetObject`<br />`s3:ListBucket ` | Application | 
| [CreateDataSetImportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDataSetImportTask.html)  | `s3:GetObject` | Application | 
| [CreateDataSetExportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDataSetExportTask.html) | `kms:DescribeKey`<br />`s3:PutObject` | Application | 
| [CreateDeployment](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDeployment.html)  | `elasticloadbalancing:AddTags`<br />`elasticloadbalancing:CreateListener`<br />`elasticloadbalancing:CreateTargetGroup`<br />`elasticloadbalancing:RegisterTargets`<br />`elasticloadbalancing:DeleteListener`<br />`elasticloadbalancing:DeleteTargetGroup`<br />`elasticloadbalancing:DeregisterTargets`<br />`elasticloadbalancing:DeleteLoadBalancer`<br />`logs:CreateLogDelivery`<br />`logs:GetLogDelivery`<br />`logs:UpdateLogDelivery`<br />`logs:DeleteLogDelivery`<br />`logs:ListLogDeliveries`<br />`logs:PutResourcePolicy`<br />`logs:DescribeResourcePolicies`<br />`logs:DescribeLogGroups` | Application | 
|  [CreateEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateEnvironment.html)  | `ec2:CreateNetworkInterface`<br />`ec2:CreateNetworkInterfacePermission`<br />`ec2:DescribeNetworkInterfaces`<br />`ec2:DescribeSecurityGroups`<br />`ec2:DescribeSubnets`<br />`ec2:DescribeVpcAttribute`<br />`ec2:DescribeVpcs`<br />`ec2:ModifyNetworkInterfaceAttribute`<br />`elasticfilesystem:DescribeMountTargets`<br />`elasticloadbalancing:AddTags`<br />`elasticloadbalancing:CreateLoadBalancer`<br />`elasticloadbalancing:DeleteLoadBalancer`<br />`kms:DescribeKey`<br />`kms:CreateGrant`<br />`fsx:DescribeFileSystems`<br />`iam:CreateServiceLinkedRole` | Environment | 
|  [DeleteApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_DeleteApplication.html)  | `elasticloadbalancing:DeleteListener`<br />`elasticloadbalancing:DeleteTargetGroup`<br />`logs:DeleteLogDelivery` | Application | 
|  [DeleteApplicationFromEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_DeleteApplicationFromEnvironment.html)  | `elasticloadbalancing:DeleteListener`<br />`elasticloadbalancing:DeleteTargetGroup` | Application<br />Environment | 
|  [DeleteEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_DeleteEnvironment.html)  | `elasticloadbalancing:DeleteLoadBalancer` | Environment | 
|  [GetApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetApplication.html)  |   | Application | 
| [GetApplicationVersion](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetApplicationVersion.html)  |  | Application | 
|  [GetBatchJobExecution](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetBatchJobExecution.html)  |   | Application | 
|  [GetDataSetDetails](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetDetails.html)  |   | Application | 
|  [GetDataSetImportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetImportTask.html)  |   | Application | 
| [GetDataSetExportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetExportTask.html) |  | Application | 
|  [GetDeployment](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDeployment.html)  |   | Application | 
|  [GetEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetEnvironment.html)  |   | Environment | 
| [ListApplications](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListApplications.html)  |  | \* | 
|  [ListApplicationVersions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListApplicationVersions.html)  |   | \* | 
|  [ListBatchJobDefinitions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobDefinitions.html)  |   | \* | 
|  [ListBatchJobExecutions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobExecutions.html)  | `` | \* | 
|  [ListDataSetImportHistory](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDataSetImportHistory.html)  |   | \* | 
| [ListDataSetExportHistory](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDataSetExportHistory.html) |  | \* | 
|  [ListDataSets](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDataSets.html)  |   | \* | 
| [ListDeployments](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDeployments.html)  |  | \* | 
|  [ListEngineVersions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListEngineVersions.html)  |   | \* | 
| [ListEnvironments](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListEnvironments.html)  |  | \* | 
|  [ListTagsForResource](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListTagsForResource.html)  |  | \* | 
|  [StartApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_StartApplication.html)  |  | Application | 
|  [StartBatchJob](https://docs.aws.amazon.com/m2/latest/APIReference/API_StartBatchJob.html)  |   | Application | 
|  [StopApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_StopApplication.html)  |   | Application | 
|  [TagResource](https://docs.aws.amazon.com/m2/latest/APIReference/API_TagResource.html)  |   | \* | 
|  [UntagResource](https://docs.aws.amazon.com/m2/latest/APIReference/API_UntagResource.html)  |   | \* | 
|  [UpdateApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_UpdateApplication.html)  | `s3:GetObject`<br />`s3:ListBucket` | Application | 
|  [UpdateEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_UpdateEnvironment.html)  | `kms:DescribeKey` | Environment | 