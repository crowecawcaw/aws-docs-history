

# Actions, resources, and condition keys for AWS Backup Search
<a name="list_backupsearch"></a>

AWS Backup Search (service prefix: `backup-search`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-considerations.html#authentication) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/backup-search/backup-search.json) for this service.

**Topics**
+ [API operations defined by AWS Backup Search](#list_backupsearch-operations)
+ [Actions defined by AWS Backup Search](#list_backupsearch-actions-as-permissions)
+ [Resource types defined by AWS Backup Search](#list_backupsearch-resources-for-iam-policies)
+ [Condition keys for AWS Backup Search](#list_backupsearch-policy-keys)

## API operations defined by AWS Backup Search
<a name="list_backupsearch-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_backupsearch-actions-as-permissions).




- **   GetSearchJob  **
  - **IAM action:**  [backup-search:GetSearchJob](#list_backupsearch-action-GetSearchJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSearchResultExportJob  **
  - **IAM action:**  [backup-search:GetSearchResultExportJob](#list_backupsearch-action-GetSearchResultExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSearchJobBackups  **
  - **IAM action:**  [backup-search:ListSearchJobBackups](#list_backupsearch-action-ListSearchJobBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSearchJobResults  **
  - **IAM action:**  [backup-search:ListSearchJobResults](#list_backupsearch-action-ListSearchJobResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSearchJobs  **
  - **IAM action:**  [backup-search:ListSearchJobs](#list_backupsearch-action-ListSearchJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSearchResultExportJobs  **
  - **IAM action:**  [backup-search:ListSearchResultExportJobs](#list_backupsearch-action-ListSearchResultExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [backup-search:ListTagsForResource](#list_backupsearch-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartSearchJob  **
  - **IAM action:**  [backup-search:StartSearchJob](#list_backupsearch-action-StartSearchJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup-search:TagResource](#list_backupsearch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StopSearchJob  **
  - **IAM action:**  [backup-search:StopSearchJob](#list_backupsearch-action-StopSearchJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [backup-search:TagResource](#list_backupsearch-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [backup-search:UntagResource](#list_backupsearch-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Backup Search
<a name="list_backupsearch-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetSearchJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_GetSearchJob.html)  **
  - **Description:** Grants permission to get details of a search job
  - **Resource types (\*required):** [searchJob\*](#list_backupsearch-resource-searchJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSearchResultExportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_GetSearchResultExportJob.html)  **
  - **Description:** Grants permission to get details of a search result export job
  - **Resource types (\*required):** [searchExportJob\*](#list_backupsearch-resource-searchExportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSearchJobBackups](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchJobBackups.html)  **
  - **Description:** Grants permission to list backups in scope of a search job
  - **Resource types (\*required):** [searchJob\*](#list_backupsearch-resource-searchJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSearchJobResults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchJobResults.html)  **
  - **Description:** Grants permission to list results of a search job
  - **Resource types (\*required):** [searchJob\*](#list_backupsearch-resource-searchJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSearchJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchJobs.html)  **
  - **Description:** Grants permission to list search jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSearchResultExportJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchResultExportJobs.html)  **
  - **Description:** Grants permission to list search result export jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [searchExportJob](#list_backupsearch-resource-searchExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [searchJob](#list_backupsearch-resource-searchJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartSearchJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_StartSearchJob.html)  **
  - **Description:** Grants permission to create a search job
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backupsearch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backupsearch-aws_TagKeys)
  - **Access level:** Write

- **   [StartSearchResultExportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_StartSearchResultExportJob.html)  **
  - **Description:** Grants permission to start an export job for an existing search job
  - **Resource types (\*required):** [searchJob\*](#list_backupsearch-resource-searchJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backupsearch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backupsearch-aws_TagKeys)
  - **Access level:** Write

- **   [StopSearchJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_StopSearchJob.html)  **
  - **Description:** Grants permission to stop an in-progress search job
  - **Resource types (\*required):** [searchJob\*](#list_backupsearch-resource-searchJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [searchExportJob](#list_backupsearch-resource-searchExportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backupsearch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backupsearch-aws_TagKeys)
  - **Resource types (\*required):** [searchJob](#list_backupsearch-resource-searchJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backupsearch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backupsearch-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [searchExportJob](#list_backupsearch-resource-searchExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backupsearch-aws_TagKeys)
  - **Resource types (\*required):** [searchJob](#list_backupsearch-resource-searchJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backupsearch-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Backup Search
<a name="list_backupsearch-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [searchExportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-search.html)  | arn:${Partition}:backup-search:${Region}:${Account}:search-export-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_) | 
|  [searchJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-search.html)  | arn:${Partition}:backup-search:${Region}:${Account}:search-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_backupsearch-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Backup Search
<a name="list_backupsearch-policy-keys"></a>

AWS Backup Search defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 