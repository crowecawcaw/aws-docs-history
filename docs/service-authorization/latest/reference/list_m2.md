

# Actions, resources, and condition keys for AWS Mainframe Modernization Service
<a name="list_m2"></a>

AWS Mainframe Modernization Service (service prefix: `m2`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/m2/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/m2/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/m2/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/m2/m2.json) for this service.

**Topics**
+ [API operations defined by AWS Mainframe Modernization Service](#list_m2-operations)
+ [Actions defined by AWS Mainframe Modernization Service](#list_m2-actions-as-permissions)
+ [Resource types defined by AWS Mainframe Modernization Service](#list_m2-resources-for-iam-policies)
+ [Condition keys for AWS Mainframe Modernization Service](#list_m2-policy-keys)

## API operations defined by AWS Mainframe Modernization Service
<a name="list_m2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_m2-actions-as-permissions).




- **   CancelBatchJobExecution  **
  - **IAM action:**  [m2:CancelBatchJobExecution](#list_m2-action-CancelBatchJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [m2:CreateApplication](#list_m2-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [m2:TagResource](#list_m2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** m2.amazonaws.com / **Access level:** Write

- **   CreateDataSetExportTask  **
  - **IAM action:**  [m2:CreateDataSetExportTask](#list_m2-action-CreateDataSetExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataSetImportTask  **
  - **IAM action:**  [m2:CreateDataSetImportTask](#list_m2-action-CreateDataSetImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDeployment  **
  - **IAM action:**  [m2:CreateDeployment](#list_m2-action-CreateDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironment  **
  - **IAM action:**  [m2:CreateEnvironment](#list_m2-action-CreateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [m2:TagResource](#list_m2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApplication  **
  - **IAM action:**  [m2:DeleteApplication](#list_m2-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationFromEnvironment  **
  - **IAM action:**  [m2:DeleteApplicationFromEnvironment](#list_m2-action-DeleteApplicationFromEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [m2:DeleteEnvironment](#list_m2-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [m2:GetApplication](#list_m2-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationVersion  **
  - **IAM action:**  [m2:GetApplicationVersion](#list_m2-action-GetApplicationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBatchJobExecution  **
  - **IAM action:**  [m2:GetBatchJobExecution](#list_m2-action-GetBatchJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSetDetails  **
  - **IAM action:**  [m2:GetDataSetDetails](#list_m2-action-GetDataSetDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSetExportTask  **
  - **IAM action:**  [m2:GetDataSetExportTask](#list_m2-action-GetDataSetExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSetImportTask  **
  - **IAM action:**  [m2:GetDataSetImportTask](#list_m2-action-GetDataSetImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployment  **
  - **IAM action:**  [m2:GetDeployment](#list_m2-action-GetDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironment  **
  - **IAM action:**  [m2:GetEnvironment](#list_m2-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSignedBluinsightsUrl  **
  - **IAM action:**  [m2:GetSignedBluinsightsUrl](#list_m2-action-GetSignedBluinsightsUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplicationVersions  **
  - **IAM action:**  [m2:ListApplicationVersions](#list_m2-action-ListApplicationVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **IAM action:**  [m2:ListApplications](#list_m2-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBatchJobDefinitions  **
  - **IAM action:**  [m2:ListBatchJobDefinitions](#list_m2-action-ListBatchJobDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBatchJobExecutions  **
  - **IAM action:**  [m2:ListBatchJobExecutions](#list_m2-action-ListBatchJobExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBatchJobRestartPoints  **
  - **IAM action:**  [m2:ListBatchJobRestartPoints](#list_m2-action-ListBatchJobRestartPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataSetExportHistory  **
  - **IAM action:**  [m2:ListDataSetExportHistory](#list_m2-action-ListDataSetExportHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataSetImportHistory  **
  - **IAM action:**  [m2:ListDataSetImportHistory](#list_m2-action-ListDataSetImportHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataSets  **
  - **IAM action:**  [m2:ListDataSets](#list_m2-action-ListDataSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDeployments  **
  - **IAM action:**  [m2:ListDeployments](#list_m2-action-ListDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEngineVersions  **
  - **IAM action:**  [m2:ListEngineVersions](#list_m2-action-ListEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEnvironments  **
  - **IAM action:**  [m2:ListEnvironments](#list_m2-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [m2:ListTagsForResource](#list_m2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartApplication  **
  - **IAM action:**  [m2:StartApplication](#list_m2-action-StartApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBatchJob  **
  - **IAM action:**  [m2:StartBatchJob](#list_m2-action-StartBatchJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopApplication  **
  - **IAM action:**  [m2:StopApplication](#list_m2-action-StopApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [m2:TagResource](#list_m2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [m2:UntagResource](#list_m2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [m2:UpdateApplication](#list_m2-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironment  **
  - **IAM action:**  [m2:UpdateEnvironment](#list_m2-action-UpdateEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Mainframe Modernization Service
<a name="list_m2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelBatchJobExecution](https://docs.aws.amazon.com/m2/latest/APIReference/API_CancelBatchJobExecution.html)  **
  - **Description:** Grants permission to cancel the execution of a batch job
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_m2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_m2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSetExportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDataSetExportTask.html)  **
  - **Description:** Grants permission to create a data set export task
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataSetImportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDataSetImportTask.html)  **
  - **Description:** Grants permission to create a data set import task
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDeployment](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDeployment.html)  **
  - **Description:** Grants permission to create a deployment
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Environment](#list_m2-resource-Environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to Create an environment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_m2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_m2-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationFromEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_DeleteApplicationFromEnvironment.html)  **
  - **Description:** Grants permission to delete an application from a runtime environment
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete a runtime environment
  - **Resource types (\*required):** [Environment\*](#list_m2-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetApplication.html)  **
  - **Description:** Grants permission to retrieve an application
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApplicationVersion](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetApplicationVersion.html)  **
  - **Description:** Grants permission to retrieve an application version
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBatchJobExecution](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetBatchJobExecution.html)  **
  - **Description:** Grants permission to retrieve a batch job execution
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSetDetails](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetDetails.html)  **
  - **Description:** Grants permission to retrieve data set details
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSetExportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetExportTask.html)  **
  - **Description:** Grants permission to export a data set at the specified S3 location
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSetImportTask](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetImportTask.html)  **
  - **Description:** Grants permission to retrieve a data set import task
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeployment](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDeployment.html)  **
  - **Description:** Grants permission to retrieve a deployment
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to retrieve a runtime environment
  - **Resource types (\*required):** [Environment\*](#list_m2-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSignedBluinsightsUrl](https://docs.aws.amazon.com/m2/latest/APIReference/API_GetSignedBluinsightsUrl.html)  **
  - **Description:** Grants permission to create a signed Bluinsights url
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListApplicationVersions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListApplicationVersions.html)  **
  - **Description:** Grants permission to list the versions of an application
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBatchJobDefinitions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobDefinitions.html)  **
  - **Description:** Grants permission to list batch job definitions
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBatchJobExecutions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobExecutions.html)  **
  - **Description:** Grants permission to list executions for a batch job
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBatchJobRestartPoints](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobRestartPoints.html)  **
  - **Description:** Grants permission to retrieve a batch job execution
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDataSetExportHistory](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDataSetExportHistory.html)  **
  - **Description:** Grants permission to list data set export history
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDataSetImportHistory](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDataSetImportHistory.html)  **
  - **Description:** Grants permission to list data set import history
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDataSets](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDataSets.html)  **
  - **Description:** Grants permission to list data sets
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeployments](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListDeployments.html)  **
  - **Description:** Grants permission to list deployments
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEngineVersions](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListEngineVersions.html)  **
  - **Description:** Grants permission to list engine versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEnvironments](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list runtime environments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_StartApplication.html)  **
  - **Description:** Grants permission to start an application
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBatchJob](https://docs.aws.amazon.com/m2/latest/APIReference/API_StartBatchJob.html)  **
  - **Description:** Grants permission to start a batch job
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_StopApplication.html)  **
  - **Description:** Grants permission to stop an application
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/m2/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [Application](#list_m2-resource-Application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_m2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_m2-aws_TagKeys)
  - **Resource types (\*required):** [Environment](#list_m2-resource-Environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_m2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_m2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/m2/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [Application](#list_m2-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_m2-aws_TagKeys)
  - **Resource types (\*required):** [Environment](#list_m2-resource-Environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_m2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/m2/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an application
  - **Resource types (\*required):** [Application\*](#list_m2-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/m2/latest/APIReference/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update a runtime environment
  - **Resource types (\*required):** [Environment\*](#list_m2-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Mainframe Modernization Service
<a name="list_m2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Application](https://docs.aws.amazon.com/m2/latest/userguide/concept-m2.html#application-concept)  | arn:${Partition}:m2:${Region}:${Account}:app/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_) | 
|  [Environment](https://docs.aws.amazon.com/m2/latest/userguide/concept-m2.html#environment-concept)  | arn:${Partition}:m2:${Region}:${Account}:env/${EnvironmentId} | [aws:ResourceTag/${TagKey}](#list_m2-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Mainframe Modernization Service
<a name="list_m2-policy-keys"></a>

AWS Mainframe Modernization Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 