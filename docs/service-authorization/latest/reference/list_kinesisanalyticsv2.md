

# Actions, resources, and condition keys for Amazon Kinesis Analytics V2

Amazon Kinesis Analytics V2 (service prefix: `kinesisanalytics`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/managed-flink/latest/apiv2/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/managed-flink/latest/apiv2/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/authentication-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kinesisanalytics/kinesisanalytics.json) for this service.

**Topics**
+ [API operations defined by Amazon Kinesis Analytics V2](#list_kinesisanalyticsv2-operations)
+ [Actions defined by Amazon Kinesis Analytics V2](#list_kinesisanalyticsv2-actions-as-permissions)
+ [Permission-only actions for Amazon Kinesis Analytics V2](#list_kinesisanalyticsv2-permission-only-actions)
+ [Resource types defined by Amazon Kinesis Analytics V2](#list_kinesisanalyticsv2-resources-for-iam-policies)
+ [Condition keys for Amazon Kinesis Analytics V2](#list_kinesisanalyticsv2-policy-keys)

## API operations defined by Amazon Kinesis Analytics V2
<a name="list_kinesisanalyticsv2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kinesisanalyticsv2-actions-as-permissions).




- **   AddApplicationCloudWatchLoggingOption  **
  - **IAM action:**  [kinesisanalytics:AddApplicationCloudWatchLoggingOption](#list_kinesisanalyticsv2-action-AddApplicationCloudWatchLoggingOption)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   AddApplicationInput  **
  - **IAM action:**  [kinesisanalytics:AddApplicationInput](#list_kinesisanalyticsv2-action-AddApplicationInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   AddApplicationOutput  **
  - **IAM action:**  [kinesisanalytics:AddApplicationOutput](#list_kinesisanalyticsv2-action-AddApplicationOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   AddApplicationReferenceDataSource  **
  - **IAM action:**  [kinesisanalytics:AddApplicationReferenceDataSource](#list_kinesisanalyticsv2-action-AddApplicationReferenceDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   AddApplicationVpcConfiguration  **
  - **IAM action:**  [kinesisanalytics:AddApplicationVpcConfiguration](#list_kinesisanalyticsv2-action-AddApplicationVpcConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [kinesisanalytics:CreateApplication](#list_kinesisanalyticsv2-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kinesisanalytics:TagResource](#list_kinesisanalyticsv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   CreateApplicationPresignedUrl  **
  - **IAM action:**  [kinesisanalytics:CreateApplicationPresignedUrl](#list_kinesisanalyticsv2-action-CreateApplicationPresignedUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateApplicationSnapshot  **
  - **IAM action:**  [kinesisanalytics:CreateApplicationSnapshot](#list_kinesisanalyticsv2-action-CreateApplicationSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSnapshot  **
  - **IAM action:**  [kinesisanalytics:CreateSnapshot](#list_kinesisanalyticsv2-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kinesisanalytics:TagResource](#list_kinesisanalyticsv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApplication  **
  - **IAM action:**  [kinesisanalytics:DeleteApplication](#list_kinesisanalyticsv2-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationCloudWatchLoggingOption  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationCloudWatchLoggingOption](#list_kinesisanalyticsv2-action-DeleteApplicationCloudWatchLoggingOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationInputProcessingConfiguration  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationInputProcessingConfiguration](#list_kinesisanalyticsv2-action-DeleteApplicationInputProcessingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationOutput  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationOutput](#list_kinesisanalyticsv2-action-DeleteApplicationOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationReferenceDataSource  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationReferenceDataSource](#list_kinesisanalyticsv2-action-DeleteApplicationReferenceDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationSnapshot  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationSnapshot](#list_kinesisanalyticsv2-action-DeleteApplicationSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationVpcConfiguration  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationVpcConfiguration](#list_kinesisanalyticsv2-action-DeleteApplicationVpcConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshot  **
  - **IAM action:**  [kinesisanalytics:DeleteSnapshot](#list_kinesisanalyticsv2-action-DeleteSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeApplication  **
  - **IAM action:**  [kinesisanalytics:DescribeApplication](#list_kinesisanalyticsv2-action-DescribeApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplicationOperation  **
  - **IAM action:**  [kinesisanalytics:DescribeApplicationOperation](#list_kinesisanalyticsv2-action-DescribeApplicationOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplicationSnapshot  **
  - **IAM action:**  [kinesisanalytics:DescribeApplicationSnapshot](#list_kinesisanalyticsv2-action-DescribeApplicationSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplicationVersion  **
  - **IAM action:**  [kinesisanalytics:DescribeApplicationVersion](#list_kinesisanalyticsv2-action-DescribeApplicationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshot  **
  - **IAM action:**  [kinesisanalytics:DescribeSnapshot](#list_kinesisanalyticsv2-action-DescribeSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshotOperation  **
  - **IAM action:**  [kinesisanalytics:DescribeSnapshotOperation](#list_kinesisanalyticsv2-action-DescribeSnapshotOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DiscoverInputSchema  **
  - **IAM action:**  [kinesisanalytics:DiscoverInputSchema](#list_kinesisanalyticsv2-action-DiscoverInputSchema)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   ExportSnapshot  **
  - **IAM action:**  [kinesisanalytics:ExportSnapshot](#list_kinesisanalyticsv2-action-ExportSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   ImportSnapshot  **
  - **IAM action:**  [kinesisanalytics:ImportSnapshot](#list_kinesisanalyticsv2-action-ImportSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   ListApplicationOperations  **
  - **IAM action:**  [kinesisanalytics:ListApplicationOperations](#list_kinesisanalyticsv2-action-ListApplicationOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplicationSnapshots  **
  - **IAM action:**  [kinesisanalytics:ListApplicationSnapshots](#list_kinesisanalyticsv2-action-ListApplicationSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplicationVersions  **
  - **IAM action:**  [kinesisanalytics:ListApplicationVersions](#list_kinesisanalyticsv2-action-ListApplicationVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **IAM action:**  [kinesisanalytics:ListApplications](#list_kinesisanalyticsv2-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSnapshotOperations  **
  - **IAM action:**  [kinesisanalytics:ListSnapshotOperations](#list_kinesisanalyticsv2-action-ListSnapshotOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSnapshots  **
  - **IAM action:**  [kinesisanalytics:ListSnapshots](#list_kinesisanalyticsv2-action-ListSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [kinesisanalytics:ListTagsForResource](#list_kinesisanalyticsv2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RollbackApplication  **
  - **IAM action:**  [kinesisanalytics:RollbackApplication](#list_kinesisanalyticsv2-action-RollbackApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartApplication  **
  - **IAM action:**  [kinesisanalytics:StartApplication](#list_kinesisanalyticsv2-action-StartApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopApplication  **
  - **IAM action:**  [kinesisanalytics:StopApplication](#list_kinesisanalyticsv2-action-StopApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [kinesisanalytics:TagResource](#list_kinesisanalyticsv2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kinesisanalytics:UntagResource](#list_kinesisanalyticsv2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [kinesisanalytics:UpdateApplication](#list_kinesisanalyticsv2-action-UpdateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   UpdateApplicationMaintenanceConfiguration  **
  - **IAM action:**  [kinesisanalytics:UpdateApplicationMaintenanceConfiguration](#list_kinesisanalyticsv2-action-UpdateApplicationMaintenanceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Kinesis Analytics V2
<a name="list_kinesisanalyticsv2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html)  **
  - **Description:** Grants permission to add cloudwatch logging option to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddApplicationInput](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationInput.html)  **
  - **Description:** Grants permission to add input to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddApplicationInputProcessingConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationInputProcessingConfiguration.html)  **
  - **Description:** Grants permission to add input processing configuration to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddApplicationOutput](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationOutput.html)  **
  - **Description:** Grants permission to add output to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationReferenceDataSource.html)  **
  - **Description:** Grants permission to add reference data source to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddApplicationVpcConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationVpcConfiguration.html)  **
  - **Description:** Grants permission to add VPC configuration to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesisanalyticsv2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalyticsv2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateApplicationPresignedUrl](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplicationPresignedUrl.html)  **
  - **Description:** Grants permission to create and return a URL that you can use to connect to an application's extension
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateApplicationSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplicationSnapshot.html)  **
  - **Description:** Grants permission to create a snapshot for an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateSnapshot.html)  **
  - **Description:** Grants permission to create a snapshot from a running application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesisanalyticsv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalyticsv2-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html)  **
  - **Description:** Grants permission to delete the specified cloudwatch logging option of the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationInputProcessingConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationInputProcessingConfiguration.html)  **
  - **Description:** Grants permission to delete the specified input processing configuration of the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationOutput](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationOutput.html)  **
  - **Description:** Grants permission to delete the specified output of the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationReferenceDataSource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationReferenceDataSource.html)  **
  - **Description:** Grants permission to delete the specified reference data source of the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationSnapshot.html)  **
  - **Description:** Grants permission to delete a snapshot for an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationVpcConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationVpcConfiguration.html)  **
  - **Description:** Grants permission to delete the specified VPC configuration of the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteSnapshot.html)  **
  - **Description:** Grants permission to delete a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_kinesisanalyticsv2-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplication.html)  **
  - **Description:** Grants permission to describe the specified application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApplicationOperation](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationOperation.html)  **
  - **Description:** Grants permission to describe an application operation of an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApplicationSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationSnapshot.html)  **
  - **Description:** Grants permission to describe an application snapshot
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApplicationVersion](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationVersion.html)  **
  - **Description:** Grants permission to describe the application version of an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeSnapshot.html)  **
  - **Description:** Grants permission to describe a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_kinesisanalyticsv2-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSnapshotOperation](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeSnapshotOperation.html)  **
  - **Description:** Grants permission to describe a snapshot operation for a snapshot like import, export, create and delete
  - **Resource types (\*required):** [snapshot\*](#list_kinesisanalyticsv2-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DiscoverInputSchema](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DiscoverInputSchema.html)  **
  - **Description:** Grants permission to discover the input schema for the application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ExportSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ExportSnapshot.html)  **
  - **Description:** Grants permission to export an MSF snapshot to a customer-managed S3 location
  - **Resource types (\*required):** [snapshot\*](#list_kinesisanalyticsv2-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ImportSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ImportSnapshot.html)  **
  - **Description:** Grants permission to import a Flink savepoint from a customer-managed S3 location as an MSF snapshot
  - **Resource types (\*required):** [snapshot\*](#list_kinesisanalyticsv2-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesisanalyticsv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalyticsv2-aws_TagKeys)
  - **Access level:** Write

- **   [ListApplicationOperations](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationOperations.html)  **
  - **Description:** Grants permission to list application operations of an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplicationSnapshots](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationSnapshots.html)  **
  - **Description:** Grants permission to list the snapshots for an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplicationVersions](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationVersions.html)  **
  - **Description:** Grants permission to list application versions of an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplications.html)  **
  - **Description:** Grants permission to list applications for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSnapshotOperations](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListSnapshotOperations.html)  **
  - **Description:** Grants permission to list snapshot operations for a snapshot like import, export, create and delete
  - **Resource types (\*required):** [snapshot\*](#list_kinesisanalyticsv2-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSnapshots](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListSnapshots.html)  **
  - **Description:** Grants permission to list snapshots in an account
  - **Resource types (\*required):** [application](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to fetch the tags associated with the resource like application, snapshot
  - **Resource types (\*required):** [application](#list_kinesisanalyticsv2-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_kinesisanalyticsv2-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RollbackApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RollbackApplication.html)  **
  - **Description:** Grants permission to perform rollback operation on an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StartApplication.html)  **
  - **Description:** Grants permission to start the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StopApplication.html)  **
  - **Description:** Grants permission to stop the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to the resource like an application, snapshot
  - **Resource types (\*required):** [application](#list_kinesisanalyticsv2-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesisanalyticsv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalyticsv2-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_kinesisanalyticsv2-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesisanalyticsv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalyticsv2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the resource like application, snapshot
  - **Resource types (\*required):** [application](#list_kinesisanalyticsv2-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalyticsv2-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_kinesisanalyticsv2-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalyticsv2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApplicationMaintenanceConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplicationMaintenanceConfiguration.html)  **
  - **Description:** Grants permission to update the maintenance configuration of an application
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Kinesis Analytics V2
<a name="list_kinesisanalyticsv2-permission-only-actions"></a>

The following actions are defined by Amazon Kinesis Analytics V2 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateSystemSnapshot](https://docs.aws.amazon.com/managed-flink/latest/java/security-iam-snapshots.html#security-iam-snapshots-actions)  **
  - **Description:** Grants permission to enable system snapshot creation for a running application from StartApplication, UpdateApplication, StopApplication, AddApplicationVPCConfiguration, DeleteApplicationVPCConfiguration, AddApplicationCloudWatchLoggingOption and DeleteApplicationCloudWatchLoggingOption
  - **Resource types (\*required):** [application\*](#list_kinesisanalyticsv2-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreFromSnapshot](https://docs.aws.amazon.com/managed-flink/latest/java/security-iam-snapshots.html#security-iam-snapshots-actions)  **
  - **Description:** Grants permission to restore an application from a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_kinesisanalyticsv2-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon Kinesis Analytics V2
<a name="list_kinesisanalyticsv2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-it-works.html)  | arn:${Partition}:kinesisanalytics:${Region}:${Account}:application/${ApplicationName} | [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_) | 
|  [snapshot](https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-how-it-works.html)  | arn:${Partition}:kinesisanalytics:${Region}:${Account}:snapshot/${SnapshotName} | [aws:ResourceTag/${TagKey}](#list_kinesisanalyticsv2-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Kinesis Analytics V2
<a name="list_kinesisanalyticsv2-policy-keys"></a>

Amazon Kinesis Analytics V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tag keys in the request | ArrayOfString | 