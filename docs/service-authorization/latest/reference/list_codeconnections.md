

# Actions, resources, and condition keys for AWS CodeConnections
<a name="list_codeconnections"></a>

AWS CodeConnections (service prefix: `codeconnections`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codeconnections/codeconnections.json) for this service.

**Topics**
+ [API operations defined by AWS CodeConnections](#list_codeconnections-operations)
+ [Actions defined by AWS CodeConnections](#list_codeconnections-actions-as-permissions)
+ [Permission-only actions for AWS CodeConnections](#list_codeconnections-permission-only-actions)
+ [Resource types defined by AWS CodeConnections](#list_codeconnections-resources-for-iam-policies)
+ [Condition keys for AWS CodeConnections](#list_codeconnections-policy-keys)

## API operations defined by AWS CodeConnections
<a name="list_codeconnections-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codeconnections-actions-as-permissions).




- **   CreateConnection  **
  - **IAM action:**  [codeconnections:CreateConnection](#list_codeconnections-action-CreateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:TagResource](#list_codeconnections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:CreateConnection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:TagResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateHost  **
  - **IAM action:**  [codeconnections:CreateHost](#list_codeconnections-action-CreateHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:TagResource](#list_codeconnections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:CreateHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:TagResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRepositoryLink  **
  - **IAM action:**  [codeconnections:CreateRepositoryLink](#list_codeconnections-action-CreateRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:PassConnection](#list_codeconnections-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:TagResource](#list_codeconnections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:UseConnection](#list_codeconnections-action-UseConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:CreateRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:TagResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateSyncConfiguration  **
  - **IAM action:**  [codeconnections:CreateSyncConfiguration](#list_codeconnections-action-CreateSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:PassRepository](#list_codeconnections-action-PassRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:CreateSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.sync.codeconnections.amazonaws.com / **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [codeconnections:DeleteConnection](#list_codeconnections-action-DeleteConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:DeleteConnection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteHost  **
  - **IAM action:**  [codeconnections:DeleteHost](#list_codeconnections-action-DeleteHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:DeleteHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteRepositoryLink  **
  - **IAM action:**  [codeconnections:DeleteRepositoryLink](#list_codeconnections-action-DeleteRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:DeleteRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteSyncConfiguration  **
  - **IAM action:**  [codeconnections:DeleteSyncConfiguration](#list_codeconnections-action-DeleteSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:DeleteSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetConnection  **
  - **IAM action:**  [codeconnections:GetConnection](#list_codeconnections-action-GetConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:GetConnection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetHost  **
  - **IAM action:**  [codeconnections:GetHost](#list_codeconnections-action-GetHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:GetHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRepositoryLink  **
  - **IAM action:**  [codeconnections:GetRepositoryLink](#list_codeconnections-action-GetRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:GetRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRepositorySyncStatus  **
  - **IAM action:**  [codeconnections:GetRepositorySyncStatus](#list_codeconnections-action-GetRepositorySyncStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:GetRepositorySyncStatus](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetRepositorySyncStatus.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetResourceSyncStatus  **
  - **IAM action:**  [codeconnections:GetResourceSyncStatus](#list_codeconnections-action-GetResourceSyncStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:GetResourceSyncStatus](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetResourceSyncStatus.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSyncBlockerSummary  **
  - **IAM action:**  [codeconnections:GetSyncBlockerSummary](#list_codeconnections-action-GetSyncBlockerSummary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:GetSyncBlockerSummary](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetSyncBlockerSummary.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSyncConfiguration  **
  - **IAM action:**  [codeconnections:GetSyncConfiguration](#list_codeconnections-action-GetSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:GetSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListConnections  **
  - **IAM action:**  [codeconnections:ListConnections](#list_codeconnections-action-ListConnections)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codestar-connections:ListConnections](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListConnections.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListHosts  **
  - **IAM action:**  [codeconnections:ListHosts](#list_codeconnections-action-ListHosts)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codestar-connections:ListHosts](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListHosts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListRepositoryLinks  **
  - **IAM action:**  [codeconnections:ListRepositoryLinks](#list_codeconnections-action-ListRepositoryLinks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codestar-connections:ListRepositoryLinks](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListRepositoryLinks.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListSyncConfigurations  **
  - **IAM action:**  [codeconnections:ListSyncConfigurations](#list_codeconnections-action-ListSyncConfigurations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codestar-connections:ListSyncConfigurations](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListSyncConfigurations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codeconnections:ListTagsForResource](#list_codeconnections-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codestar-connections:ListTagsForResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListTagsForResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   TagResource  **
  - **IAM action:**  [codeconnections:TagResource](#list_codeconnections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:TagResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [codeconnections:UntagResource](#list_codeconnections-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:UntagResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UntagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateHost  **
  - **IAM action:**  [codeconnections:UpdateHost](#list_codeconnections-action-UpdateHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:UpdateHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateRepositoryLink  **
  - **IAM action:**  [codeconnections:PassConnection](#list_codeconnections-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:UpdateRepositoryLink](#list_codeconnections-action-UpdateRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:UseConnection](#list_codeconnections-action-UseConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:UpdateRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   UpdateSyncBlocker  **
  - **IAM action:**  [codeconnections:UpdateSyncBlocker](#list_codeconnections-action-UpdateSyncBlocker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:UpdateSyncBlocker](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateSyncBlocker.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateSyncConfiguration  **
  - **IAM action:**  [codeconnections:PassRepository](#list_codeconnections-action-PassRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:UpdateSyncConfiguration](#list_codeconnections-action-UpdateSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:UpdateSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.sync.codeconnections.amazonaws.com / **Access level:** Write



## Actions defined by AWS CodeConnections
<a name="list_codeconnections-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateConnection.html)  **
  - **Description:** Grants permission to create a Connection resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeconnections-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)<br />[codeconnections:ProviderType](#list_codeconnections-codeconnections_ProviderType)
  - **Access level:** Write

- **   [CreateHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateHost.html)  **
  - **Description:** Grants permission to create a host resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeconnections-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)<br />[codeconnections:ProviderType](#list_codeconnections-codeconnections_ProviderType)<br />[codeconnections:VpcId](#list_codeconnections-codeconnections_VpcId)
  - **Access level:** Write

- **   [CreateRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateRepositoryLink.html)  **
  - **Description:** Grants permission to create a repository link
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeconnections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateSyncConfiguration.html)  **
  - **Description:** Grants permission to create a template sync config
  - **Resource types (\*required):** [RepositoryLink\*](#list_codeconnections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:Branch](#list_codeconnections-codeconnections_Branch)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete a Connection resource
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteHost.html)  **
  - **Description:** Grants permission to delete a host resource
  - **Resource types (\*required):** [Host\*](#list_codeconnections-resource-Host)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteRepositoryLink.html)  **
  - **Description:** Grants permission to delete a repository link
  - **Resource types (\*required):** [RepositoryLink\*](#list_codeconnections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteSyncConfiguration.html)  **
  - **Description:** Grants permission to delete a sync configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetConnection.html)  **
  - **Description:** Grants permission to get details about a Connection resource
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetHost.html)  **
  - **Description:** Grants permission to get details about a host resource
  - **Resource types (\*required):** [Host\*](#list_codeconnections-resource-Host)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositoryLink.html)  **
  - **Description:** Grants permission to describe a repository link
  - **Resource types (\*required):** [RepositoryLink\*](#list_codeconnections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositorySyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositorySyncStatus.html)  **
  - **Description:** Grants permission to get the latest sync status for a repository
  - **Resource types (\*required):** [RepositoryLink\*](#list_codeconnections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:Branch](#list_codeconnections-codeconnections_Branch)
  - **Access level:** Read

- **   [GetResourceSyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetResourceSyncStatus.html)  **
  - **Description:** Grants permission to get the latest sync status for a resource (cfn stack or other resources)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSyncBlockerSummary](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncBlockerSummary.html)  **
  - **Description:** Grants permission to describe service sync blockers on a resource (cfn stack or other resources)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncConfiguration.html)  **
  - **Description:** Grants permission to describe a sync configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnections](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListConnections.html)  **
  - **Description:** Grants permission to list Connection resources
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:ProviderTypeFilter](#list_codeconnections-codeconnections_ProviderTypeFilter)
  - **Access level:** List

- **   [ListHosts](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListHosts.html)  **
  - **Description:** Grants permission to list host resources
  - **Resource types (\*required):** 
  - **Condition keys:** [codeconnections:ProviderTypeFilter](#list_codeconnections-codeconnections_ProviderTypeFilter)
  - **Access level:** List

- **   [ListRepositoryLinks](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositoryLinks.html)  **
  - **Description:** Grants permission to list repository links
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositorySyncDefinitions](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositorySyncDefinitions.html)  **
  - **Description:** Grants permission to list repository sync definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSyncConfigurations](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListSyncConfigurations.html)  **
  - **Description:** Grants permission to list sync configurations for a repository link
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to the set of key-value pairs that are used to manage the resource
  - **Resource types (\*required):** [Connection](#list_codeconnections-resource-Connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Host](#list_codeconnections-resource-Host) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RepositoryLink](#list_codeconnections-resource-RepositoryLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or modify the tags of the given resource
  - **Resource types (\*required):** [Connection](#list_codeconnections-resource-Connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeconnections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)
  - **Resource types (\*required):** [Host](#list_codeconnections-resource-Host) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeconnections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)
  - **Resource types (\*required):** [RepositoryLink](#list_codeconnections-resource-RepositoryLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeconnections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an AWS resource
  - **Resource types (\*required):** [Connection](#list_codeconnections-resource-Connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)
  - **Resource types (\*required):** [Host](#list_codeconnections-resource-Host) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)
  - **Resource types (\*required):** [RepositoryLink](#list_codeconnections-resource-RepositoryLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeconnections-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnectionInstallation](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to update a Connection resource with an installation of the CodeStar Connections App
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:InstallationId](#list_codeconnections-codeconnections_InstallationId)
  - **Access level:** Write

- **   [UpdateHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateHost.html)  **
  - **Description:** Grants permission to update a host resource
  - **Resource types (\*required):** [Host\*](#list_codeconnections-resource-Host)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:VpcId](#list_codeconnections-codeconnections_VpcId)
  - **Access level:** Write

- **   [UpdateRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateRepositoryLink.html)  **
  - **Description:** Grants permission to update a repository link
  - **Resource types (\*required):** [RepositoryLink\*](#list_codeconnections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSyncBlocker](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncBlocker.html)  **
  - **Description:** Grants permission to update a sync blocker for a resource (cfn stack or other resources)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncConfiguration.html)  **
  - **Description:** Grants permission to update a sync configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [codeconnections:Branch](#list_codeconnections-codeconnections_Branch)
  - **Access level:** Write



## Permission-only actions for AWS CodeConnections
<a name="list_codeconnections-permission-only-actions"></a>

The following actions are defined by AWS CodeConnections but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetConnectionToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-getconnectiontoken)  **
  - **Description:** Grants permission to get a Connection token to call provider actions
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIndividualAccessToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:** [codeconnections:ProviderType](#list_codeconnections-codeconnections_ProviderType)
  - **Access level:** Read

- **   [GetInstallationUrl](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:** [codeconnections:ProviderType](#list_codeconnections-codeconnections_ProviderType)
  - **Access level:** Read

- **   [ListInstallationTargets](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  **
  - **Description:** Grants permission to pass a Connection resource to an AWS service that accepts a Connection ARN as input, such as codepipeline:CreatePipeline
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:PassedToService](#list_codeconnections-codeconnections_PassedToService)
  - **Access level:** Read

- **   [PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository)  **
  - **Description:** Grants permission to pass a repository link resource to an AWS service that accepts a RepositoryLinkId as input, such as codeconnections:CreateSyncConfiguration
  - **Resource types (\*required):** [RepositoryLink\*](#list_codeconnections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:PassedToService](#list_codeconnections-codeconnections_PassedToService)
  - **Access level:** Read

- **   [RegisterAppCode](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration)  **
  - **Description:** Grants permission to associate a third party server, such as a GitHub Enterprise Server instance, with a Host
  - **Resource types (\*required):** 
  - **Condition keys:** [codeconnections:HostArn](#list_codeconnections-codeconnections_HostArn)
  - **Access level:** Read

- **   [StartAppRegistrationHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration)  **
  - **Description:** Grants permission to associate a third party server, such as a GitHub Enterprise Server instance, with a Host
  - **Resource types (\*required):** 
  - **Condition keys:** [codeconnections:HostArn](#list_codeconnections-codeconnections_HostArn)
  - **Access level:** Read

- **   [StartOAuthHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:** [codeconnections:ProviderType](#list_codeconnections-codeconnections_ProviderType)
  - **Access level:** Read

- **   [UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  **
  - **Description:** Grants permission to use a Connection resource to call provider actions
  - **Resource types (\*required):** [Connection\*](#list_codeconnections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_)<br />[codeconnections:BranchName](#list_codeconnections-codeconnections_BranchName)<br />[codeconnections:FullRepositoryId](#list_codeconnections-codeconnections_FullRepositoryId)<br />[codeconnections:OwnerId](#list_codeconnections-codeconnections_OwnerId)<br />[codeconnections:ProviderAction](#list_codeconnections-codeconnections_ProviderAction)<br />[codeconnections:ProviderPermissionsRequired](#list_codeconnections-codeconnections_ProviderPermissionsRequired)<br />[codeconnections:RepositoryName](#list_codeconnections-codeconnections_RepositoryName)
  - **Access level:** Read



## Resource types defined by AWS CodeConnections
<a name="list_codeconnections-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html)  | arn:${Partition}:codeconnections:${Region}:${Account}:connection/${ConnectionId} | [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_) | 
|  [Host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-hosts.html)  | arn:${Partition}:codeconnections:${Region}:${Account}:host/${HostId} | [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_) | 
|  [RepositoryLink](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks.html)  | arn:${Partition}:codeconnections:${Region}:${Account}:repository-link/${RepositoryLinkId} | [aws:ResourceTag/${TagKey}](#list_codeconnections-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CodeConnections
<a name="list_codeconnections-policy-keys"></a>

AWS CodeConnections defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [codeconnections:Branch](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  | Filters access by the branch name that is passed in the request | String | 
|   [codeconnections:BranchName](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the branch name that is passed in the request. Applies only to UseConnection requests for access to a specific repository branch | String | 
|   [codeconnections:FullRepositoryId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the repository that is passed in the request. Applies only to UseConnection requests for access to a specific repository | String | 
|   [codeconnections:HostArn](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-hosts)  | Filters access by the host resource associated with the connection used in the request | ARN | 
|   [codeconnections:InstallationId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  | Filters access by the third-party ID (such as the Bitbucket App installation ID for CodeConnections) that is used to update a Connection. Allows you to restrict which third-party App installations can be used to make a Connection | String | 
|   [codeconnections:OwnerId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the owner of the third-party repository. Applies only to UseConnection requests for access to repositories owned by a specific user | String | 
|   [codeconnections:PassedToService](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  | Filters access by the service to which the principal is allowed to pass a Connection or RepositoryLink | String | 
|   [codeconnections:ProviderAction](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-access)  | Filters access by the provider action in a UseConnection request such as ListRepositories. See documentation for all valid values | String | 
|   [codeconnections:ProviderPermissionsRequired](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the write permissions of a provider action in a UseConnection request. Valid types include read\_only and read\_write | String | 
|   [codeconnections:ProviderType](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-managing)  | Filters access by the type of third-party provider passed in the request | String | 
|   [codeconnections:ProviderTypeFilter](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-managing)  | Filters access by the type of third-party provider used to filter results | String | 
|   [codeconnections:RepositoryName](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the repository name that is passed in the request. Applies only to UseConnection requests for access to repositories owned by a specific user | String | 
|   [codeconnections:VpcId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-hosts)  | Filters access by the VpcId passed in the request | String | 