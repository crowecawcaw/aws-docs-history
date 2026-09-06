

# Actions, resources, and condition keys for AWS Compute Optimizer
<a name="list_compute-optimizer"></a>

AWS Compute Optimizer (service prefix: `compute-optimizer`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/compute-optimizer/compute-optimizer.json) for this service.

**Topics**
+ [API operations defined by AWS Compute Optimizer](#list_compute-optimizer-operations)
+ [Actions defined by AWS Compute Optimizer](#list_compute-optimizer-actions-as-permissions)
+ [Resource types defined by AWS Compute Optimizer](#list_compute-optimizer-resources-for-iam-policies)
+ [Condition keys for AWS Compute Optimizer](#list_compute-optimizer-policy-keys)

## API operations defined by AWS Compute Optimizer
<a name="list_compute-optimizer-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_compute-optimizer-actions-as-permissions).




- **   DeleteRecommendationPreferences  **
  - **IAM action:**  [compute-optimizer:DeleteRecommendationPreferences](#list_compute-optimizer-action-DeleteRecommendationPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeRecommendationExportJobs  **
  - **IAM action:**  [compute-optimizer:DescribeRecommendationExportJobs](#list_compute-optimizer-action-DescribeRecommendationExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ExportAutoScalingGroupRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportAutoScalingGroupRecommendations](#list_compute-optimizer-action-ExportAutoScalingGroupRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetAutoScalingGroupRecommendations](#list_compute-optimizer-action-GetAutoScalingGroupRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [autoscaling:DescribeAutoScalingGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ExportEBSVolumeRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportEBSVolumeRecommendations](#list_compute-optimizer-action-ExportEBSVolumeRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetEBSVolumeRecommendations](#list_compute-optimizer-action-GetEBSVolumeRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeVolumes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ExportEC2InstanceRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportEC2InstanceRecommendations](#list_compute-optimizer-action-ExportEC2InstanceRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetEC2InstanceRecommendations](#list_compute-optimizer-action-GetEC2InstanceRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ExportECSServiceRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportECSServiceRecommendations](#list_compute-optimizer-action-ExportECSServiceRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetECSServiceRecommendations](#list_compute-optimizer-action-GetECSServiceRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ecs:ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ecs:ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ExportIdleRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportIdleRecommendations](#list_compute-optimizer-action-ExportIdleRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetIdleRecommendations](#list_compute-optimizer-action-GetIdleRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ExportLambdaFunctionRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportLambdaFunctionRecommendations](#list_compute-optimizer-action-ExportLambdaFunctionRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetLambdaFunctionRecommendations](#list_compute-optimizer-action-GetLambdaFunctionRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [lambda:ListFunctions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [lambda:ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListProvisionedConcurrencyConfigs.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ExportLicenseRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportLicenseRecommendations](#list_compute-optimizer-action-ExportLicenseRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetLicenseRecommendations](#list_compute-optimizer-action-GetLicenseRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ExportRDSDatabaseRecommendations  **
  - **IAM action:**  [compute-optimizer:ExportRDSDatabaseRecommendations](#list_compute-optimizer-action-ExportRDSDatabaseRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [compute-optimizer:GetRDSDatabaseRecommendations](#list_compute-optimizer-action-GetRDSDatabaseRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [rds:DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [rds:DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetAutoScalingGroupRecommendations  **
  - **IAM action:**  [compute-optimizer:GetAutoScalingGroupRecommendations](#list_compute-optimizer-action-GetAutoScalingGroupRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [autoscaling:DescribeAutoScalingGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetEBSVolumeRecommendations  **
  - **IAM action:**  [compute-optimizer:GetEBSVolumeRecommendations](#list_compute-optimizer-action-GetEBSVolumeRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeVolumes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetEC2InstanceRecommendations  **
  - **IAM action:**  [compute-optimizer:GetEC2InstanceRecommendations](#list_compute-optimizer-action-GetEC2InstanceRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetEC2RecommendationProjectedMetrics  **
  - **IAM action:**  [compute-optimizer:GetEC2RecommendationProjectedMetrics](#list_compute-optimizer-action-GetEC2RecommendationProjectedMetrics)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetECSServiceRecommendationProjectedMetrics  **
  - **IAM action:**  [compute-optimizer:GetECSServiceRecommendationProjectedMetrics](#list_compute-optimizer-action-GetECSServiceRecommendationProjectedMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetECSServiceRecommendations  **
  - **IAM action:**  [compute-optimizer:GetECSServiceRecommendations](#list_compute-optimizer-action-GetECSServiceRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ecs:ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ecs:ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetEffectiveRecommendationPreferences  **
  - **IAM action:**  [compute-optimizer:GetEffectiveRecommendationPreferences](#list_compute-optimizer-action-GetEffectiveRecommendationPreferences)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [autoscaling:DescribeAutoScalingGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [autoscaling:DescribeAutoScalingInstances](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetEnrollmentStatus  **
  - **IAM action:**  [compute-optimizer:GetEnrollmentStatus](#list_compute-optimizer-action-GetEnrollmentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetEnrollmentStatusesForOrganization  **
  - **IAM action:**  [compute-optimizer:GetEnrollmentStatusesForOrganization](#list_compute-optimizer-action-GetEnrollmentStatusesForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetIdleRecommendations  **
  - **IAM action:**  [compute-optimizer:GetIdleRecommendations](#list_compute-optimizer-action-GetIdleRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetLambdaFunctionRecommendations  **
  - **IAM action:**  [compute-optimizer:GetLambdaFunctionRecommendations](#list_compute-optimizer-action-GetLambdaFunctionRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [lambda:ListFunctions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [lambda:ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListProvisionedConcurrencyConfigs.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetLicenseRecommendations  **
  - **IAM action:**  [compute-optimizer:GetLicenseRecommendations](#list_compute-optimizer-action-GetLicenseRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetRDSDatabaseRecommendationProjectedMetrics  **
  - **IAM action:**  [compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics](#list_compute-optimizer-action-GetRDSDatabaseRecommendationProjectedMetrics)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [rds:DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetRDSDatabaseRecommendations  **
  - **IAM action:**  [compute-optimizer:GetRDSDatabaseRecommendations](#list_compute-optimizer-action-GetRDSDatabaseRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [rds:DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [rds:DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetRecommendationPreferences  **
  - **IAM action:**  [compute-optimizer:GetRecommendationPreferences](#list_compute-optimizer-action-GetRecommendationPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendationSummaries  **
  - **IAM action:**  [compute-optimizer:GetRecommendationSummaries](#list_compute-optimizer-action-GetRecommendationSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutRecommendationPreferences  **
  - **IAM action:**  [compute-optimizer:PutRecommendationPreferences](#list_compute-optimizer-action-PutRecommendationPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnrollmentStatus  **
  - **IAM action:**  [compute-optimizer:UpdateEnrollmentStatus](#list_compute-optimizer-action-UpdateEnrollmentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Compute Optimizer
<a name="list_compute-optimizer-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DeleteRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DeleteRecommendationPreferences.html)  | Grants permission to delete recommendation preferences |  | [compute-optimizer:ResourceType](#list_compute-optimizer-compute-optimizer_ResourceType) | Write | 
|   [DescribeRecommendationExportJobs](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DescribeRecommendationExportJobs.html)  | Grants permission to view the status of recommendation export jobs |  |   | List | 
|   [ExportAutoScalingGroupRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportAutoScalingGroupRecommendations.html)  | Grants permission to export AutoScaling group recommendations to S3 for the provided accounts |  |   | Write | 
|   [ExportEBSVolumeRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportEBSVolumeRecommendations.html)  | Grants permission to export EBS volume recommendations to S3 for the provided accounts |  |   | Write | 
|   [ExportEC2InstanceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportEC2InstanceRecommendations.html)  | Grants permission to export EC2 instance recommendations to S3 for the provided accounts |  |   | Write | 
|   [ExportECSServiceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportECSServiceRecommendations.html)  | Grants permission to export ECS service recommendations to S3 for the provided accounts |  |   | Write | 
|   [ExportIdleRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportIdleRecommendations.html)  | Grants permission to export idle recommendations to S3 for the provided accounts |  |   | Write | 
|   [ExportLambdaFunctionRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportLambdaFunctionRecommendations.html)  | Grants permission to export Lambda function recommendations to S3 for the provided accounts |  |   | Write | 
|   [ExportLicenseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportLicenseRecommendations.html)  | Grants permission to export license recommendations to S3 for the provided account(s) |  |   | Write | 
|   [ExportRDSDatabaseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportRDSDatabaseRecommendations.html)  | Grants permission to export rds recommendations to S3 for the provided accounts |  |   | Write | 
|   [GetAutoScalingGroupRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetAutoScalingGroupRecommendations.html)  | Grants permission to get recommendations for the provided AutoScaling groups |  |   | List | 
|   [GetEBSVolumeRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEBSVolumeRecommendations.html)  | Grants permission to get recommendations for the provided EBS volumes |  |   | List | 
|   [GetEC2InstanceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2InstanceRecommendations.html)  | Grants permission to get recommendations for the provided EC2 instances |  |   | List | 
|   [GetEC2RecommendationProjectedMetrics](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2RecommendationProjectedMetrics.html)  | Grants permission to get the recommendation projected metrics of the specified instance |  |   | List | 
|   [GetECSServiceRecommendationProjectedMetrics](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetECSServiceRecommendationProjectedMetrics.html)  | Grants permission to get the recommendation projected metrics of the specified ECS service |  |   | List | 
|   [GetECSServiceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetECSServiceRecommendations.html)  | Grants permission to get recommendations for the provided ECS services |  |   | List | 
|   [GetEffectiveRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEffectiveRecommendationPreferences.html)  | Grants permission to get recommendation preferences that are in effect |  | [compute-optimizer:ResourceType](#list_compute-optimizer-compute-optimizer_ResourceType) | Read | 
|   [GetEnrollmentStatus](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEnrollmentStatus.html)  | Grants permission to get the enrollment status for the specified account |  |   | List | 
|   [GetEnrollmentStatusesForOrganization](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEnrollmentStatusesForOrganization.html)  | Grants permission to get the enrollment statuses for member accounts of the organization |  |   | List | 
|   [GetIdleRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetIdleRecommendations.html)  | Grants permission to get idle recommendations for the specified account(s) |  |   | List | 
|   [GetLambdaFunctionRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetLambdaFunctionRecommendations.html)  | Grants permission to get recommendations for the provided Lambda functions |  |   | List | 
|   [GetLicenseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetLicenseRecommendations.html)  | Grants permission to get license recommendations for the specified account(s) |  |   | List | 
|   [GetRDSDatabaseRecommendationProjectedMetrics](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRDSDatabaseRecommendationProjectedMetrics.html)  | Grants permission to get the recommendation projected metrics of the specified instance |  |   | List | 
|   [GetRDSDatabaseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRDSDatabaseRecommendations.html)  | Grants permission to get rds recommendations for the specified account(s) |  |   | List | 
|   [GetRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRecommendationPreferences.html)  | Grants permission to get recommendation preferences |  | [compute-optimizer:ResourceType](#list_compute-optimizer-compute-optimizer_ResourceType) | Read | 
|   [GetRecommendationSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRecommendationSummaries.html)  | Grants permission to get the recommendation summaries for the specified account(s) |  |   | List | 
|   [PutRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_PutRecommendationPreferences.html)  | Grants permission to put recommendation preferences |  | [compute-optimizer:ResourceType](#list_compute-optimizer-compute-optimizer_ResourceType) | Write | 
|   [UpdateEnrollmentStatus](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_UpdateEnrollmentStatus.html)  | Grants permission to update the enrollment status |  |   | Write | 

## Resource types defined by AWS Compute Optimizer
<a name="list_compute-optimizer-resources-for-iam-policies"></a>

AWS Compute Optimizer does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Compute Optimizer
<a name="list_compute-optimizer-policy-keys"></a>

AWS Compute Optimizer defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [compute-optimizer:ResourceType](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html)  | Filters access by the resource type | String | 