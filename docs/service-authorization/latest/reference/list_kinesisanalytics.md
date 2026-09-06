

# Actions, resources, and condition keys for Amazon Kinesis Analytics
<a name="list_kinesisanalytics"></a>

Amazon Kinesis Analytics (service prefix: `kinesisanalytics`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/authentication-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kinesisanalytics/kinesisanalytics.json) for this service.

**Topics**
+ [API operations defined by Amazon Kinesis Analytics](#list_kinesisanalytics-operations)
+ [Actions defined by Amazon Kinesis Analytics](#list_kinesisanalytics-actions-as-permissions)
+ [Permission-only actions for Amazon Kinesis Analytics](#list_kinesisanalytics-permission-only-actions)
+ [Resource types defined by Amazon Kinesis Analytics](#list_kinesisanalytics-resources-for-iam-policies)
+ [Condition keys for Amazon Kinesis Analytics](#list_kinesisanalytics-policy-keys)

## API operations defined by Amazon Kinesis Analytics
<a name="list_kinesisanalytics-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kinesisanalytics-actions-as-permissions).




- **   AddApplicationCloudWatchLoggingOption  **
  - **IAM action:**  [kinesisanalytics:AddApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   AddApplicationInput  **
  - **IAM action:**  [kinesisanalytics:AddApplicationInput](#list_kinesisanalytics-action-AddApplicationInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   AddApplicationOutput  **
  - **IAM action:**  [kinesisanalytics:AddApplicationOutput](#list_kinesisanalytics-action-AddApplicationOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   AddApplicationReferenceDataSource  **
  - **IAM action:**  [kinesisanalytics:AddApplicationReferenceDataSource](#list_kinesisanalytics-action-AddApplicationReferenceDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [kinesisanalytics:CreateApplication](#list_kinesisanalytics-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kinesisanalytics:TagResource](#list_kinesisanalytics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [kinesisanalytics:DeleteApplication](#list_kinesisanalytics-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationCloudWatchLoggingOption  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationInputProcessingConfiguration  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationInputProcessingConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationInputProcessingConfiguration.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationOutput  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationOutput](#list_kinesisanalytics-action-DeleteApplicationOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationReferenceDataSource  **
  - **IAM action:**  [kinesisanalytics:DeleteApplicationReferenceDataSource](#list_kinesisanalytics-action-DeleteApplicationReferenceDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeApplication  **
  - **IAM action:**  [kinesisanalytics:DescribeApplication](#list_kinesisanalytics-action-DescribeApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DiscoverInputSchema  **
  - **IAM action:**  [kinesisanalytics:DiscoverInputSchema](#list_kinesisanalytics-action-DiscoverInputSchema)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write

- **   ListApplications  **
  - **IAM action:**  [kinesisanalytics:ListApplications](#list_kinesisanalytics-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [kinesisanalytics:ListTagsForResource](#list_kinesisanalytics-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartApplication  **
  - **IAM action:**  [kinesisanalytics:StartApplication](#list_kinesisanalytics-action-StartApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopApplication  **
  - **IAM action:**  [kinesisanalytics:StopApplication](#list_kinesisanalytics-action-StopApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [kinesisanalytics:TagResource](#list_kinesisanalytics-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kinesisanalytics:UntagResource](#list_kinesisanalytics-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [kinesisanalytics:UpdateApplication](#list_kinesisanalytics-action-UpdateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kinesisanalytics.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Kinesis Analytics
<a name="list_kinesisanalytics-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddApplicationInput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationInput.html)  **
  - **Description:** Grants permission to add input to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddApplicationOutput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationOutput.html)  **
  - **Description:** Grants permission to add output to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html)  **
  - **Description:** Grants permission to add reference data source to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesisanalytics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalytics-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationOutput](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplicationOutput.html)  **
  - **Description:** Grants permission to delete the specified output of the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DeleteApplicationReferenceDataSource.html)  **
  - **Description:** Grants permission to delete the specified reference data source of the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html)  **
  - **Description:** Grants permission to describe the specified application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DiscoverInputSchema](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DiscoverInputSchema.html)  **
  - **Description:** Grants permission to discover the input schema for the application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListApplications.html)  **
  - **Description:** Grants permission to list applications for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to fetch the tags associated with the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_StartApplication.html)  **
  - **Description:** Grants permission to start the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_StopApplication.html)  **
  - **Description:** Grants permission to stop the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kinesisanalytics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalytics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kinesisanalytics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update the application
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Kinesis Analytics
<a name="list_kinesisanalytics-permission-only-actions"></a>

The following actions are defined by Amazon Kinesis Analytics but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetApplicationState](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/api-permissions-reference.html#api-permissions-reference-gas)  **
  - **Description:** Grants permission to Kinesis Data Analytics console to display stream results for Kinesis Data Analytics SQL runtime applications
  - **Resource types (\*required):** [application\*](#list_kinesisanalytics-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon Kinesis Analytics
<a name="list_kinesisanalytics-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html)  | arn:${Partition}:kinesisanalytics:${Region}:${Account}:application/${ApplicationName} | [aws:ResourceTag/${TagKey}](#list_kinesisanalytics-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Kinesis Analytics
<a name="list_kinesisanalytics-policy-keys"></a>

Amazon Kinesis Analytics defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value assoicated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tag keys in the request | ArrayOfString | 