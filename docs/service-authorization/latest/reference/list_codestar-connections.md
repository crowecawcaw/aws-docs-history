

# Actions, resources, and condition keys for AWS CodeStar Connections
<a name="list_codestar-connections"></a>

AWS CodeStar Connections (service prefix: `codestar-connections`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codestar-connections/codestar-connections.json) for this service.

**Topics**
+ [API operations defined by AWS CodeStar Connections](#list_codestar-connections-operations)
+ [Actions defined by AWS CodeStar Connections](#list_codestar-connections-actions-as-permissions)
+ [Permission-only actions for AWS CodeStar Connections](#list_codestar-connections-permission-only-actions)
+ [Resource types defined by AWS CodeStar Connections](#list_codestar-connections-resources-for-iam-policies)
+ [Condition keys for AWS CodeStar Connections](#list_codestar-connections-policy-keys)

## API operations defined by AWS CodeStar Connections
<a name="list_codestar-connections-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codestar-connections-actions-as-permissions).




- **   CreateConnection  **
  - **IAM action:**  [codestar-connections:CreateConnection](#list_codestar-connections-action-CreateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:TagResource](#list_codestar-connections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:CreateConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:TagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateHost  **
  - **IAM action:**  [codestar-connections:CreateHost](#list_codestar-connections-action-CreateHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:TagResource](#list_codestar-connections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:CreateHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:TagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRepositoryLink  **
  - **IAM action:**  [codestar-connections:CreateRepositoryLink](#list_codestar-connections-action-CreateRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:PassConnection](#list_codestar-connections-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:TagResource](#list_codestar-connections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:UseConnection](#list_codestar-connections-action-UseConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:CreateRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:TagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateSyncConfiguration  **
  - **IAM action:**  [codestar-connections:CreateSyncConfiguration](#list_codestar-connections-action-CreateSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:PassRepository](#list_codestar-connections-action-PassRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:CreateSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.sync.codeconnections.amazonaws.com / **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [codestar-connections:DeleteConnection](#list_codestar-connections-action-DeleteConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:DeleteConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteHost  **
  - **IAM action:**  [codestar-connections:DeleteHost](#list_codestar-connections-action-DeleteHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:DeleteHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteRepositoryLink  **
  - **IAM action:**  [codestar-connections:DeleteRepositoryLink](#list_codestar-connections-action-DeleteRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:DeleteRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteSyncConfiguration  **
  - **IAM action:**  [codestar-connections:DeleteSyncConfiguration](#list_codestar-connections-action-DeleteSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:DeleteSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetConnection  **
  - **IAM action:**  [codestar-connections:GetConnection](#list_codestar-connections-action-GetConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:GetConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetHost  **
  - **IAM action:**  [codestar-connections:GetHost](#list_codestar-connections-action-GetHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:GetHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRepositoryLink  **
  - **IAM action:**  [codestar-connections:GetRepositoryLink](#list_codestar-connections-action-GetRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:GetRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRepositorySyncStatus  **
  - **IAM action:**  [codestar-connections:GetRepositorySyncStatus](#list_codestar-connections-action-GetRepositorySyncStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:GetRepositorySyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositorySyncStatus.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetResourceSyncStatus  **
  - **IAM action:**  [codestar-connections:GetResourceSyncStatus](#list_codestar-connections-action-GetResourceSyncStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:GetResourceSyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetResourceSyncStatus.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSyncBlockerSummary  **
  - **IAM action:**  [codestar-connections:GetSyncBlockerSummary](#list_codestar-connections-action-GetSyncBlockerSummary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:GetSyncBlockerSummary](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncBlockerSummary.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSyncConfiguration  **
  - **IAM action:**  [codestar-connections:GetSyncConfiguration](#list_codestar-connections-action-GetSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:GetSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListConnections  **
  - **IAM action:**  [codestar-connections:ListConnections](#list_codestar-connections-action-ListConnections)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codeconnections:ListConnections](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListConnections.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListHosts  **
  - **IAM action:**  [codestar-connections:ListHosts](#list_codestar-connections-action-ListHosts)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codeconnections:ListHosts](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListHosts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListRepositoryLinks  **
  - **IAM action:**  [codestar-connections:ListRepositoryLinks](#list_codestar-connections-action-ListRepositoryLinks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codeconnections:ListRepositoryLinks](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositoryLinks.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListRepositorySyncDefinitions  **
  - **IAM action:**  [codestar-connections:ListRepositorySyncDefinitions](#list_codestar-connections-action-ListRepositorySyncDefinitions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codeconnections:ListRepositorySyncDefinitions](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositorySyncDefinitions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListSyncConfigurations  **
  - **IAM action:**  [codestar-connections:ListSyncConfigurations](#list_codestar-connections-action-ListSyncConfigurations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codeconnections:ListSyncConfigurations](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListSyncConfigurations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codestar-connections:ListTagsForResource](#list_codestar-connections-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codeconnections:ListTagsForResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListTagsForResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   TagResource  **
  - **IAM action:**  [codestar-connections:TagResource](#list_codestar-connections-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:TagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [codestar-connections:UntagResource](#list_codestar-connections-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:UntagResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UntagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateHost  **
  - **IAM action:**  [codestar-connections:UpdateHost](#list_codestar-connections-action-UpdateHost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:UpdateHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateHost.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateRepositoryLink  **
  - **IAM action:**  [codestar-connections:PassConnection](#list_codestar-connections-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:UpdateRepositoryLink](#list_codestar-connections-action-UpdateRepositoryLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:UseConnection](#list_codestar-connections-action-UseConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:UpdateRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateRepositoryLink.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   UpdateSyncBlocker  **
  - **IAM action:**  [codestar-connections:UpdateSyncBlocker](#list_codestar-connections-action-UpdateSyncBlocker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:UpdateSyncBlocker](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncBlocker.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateSyncConfiguration  **
  - **IAM action:**  [codestar-connections:PassRepository](#list_codestar-connections-action-PassRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codestar-connections:UpdateSyncConfiguration](#list_codestar-connections-action-UpdateSyncConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeconnections:PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [codeconnections:UpdateSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncConfiguration.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.sync.codeconnections.amazonaws.com / **Access level:** Write



## Actions defined by AWS CodeStar Connections
<a name="list_codestar-connections-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateConnection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateConnection.html)  **
  - **Description:** Grants permission to create a Connection resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-connections-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)<br />[codestar-connections:ProviderType](#list_codestar-connections-codestar-connections_ProviderType)
  - **Access level:** Write

- **   [CreateHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateHost.html)  **
  - **Description:** Grants permission to create a host resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-connections-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)<br />[codestar-connections:ProviderType](#list_codestar-connections-codestar-connections_ProviderType)<br />[codestar-connections:VpcId](#list_codestar-connections-codestar-connections_VpcId)
  - **Access level:** Write

- **   [CreateRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateRepositoryLink.html)  **
  - **Description:** Grants permission to create a repository link
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-connections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_CreateSyncConfiguration.html)  **
  - **Description:** Grants permission to create a template sync config
  - **Resource types (\*required):** [RepositoryLink\*](#list_codestar-connections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:Branch](#list_codestar-connections-codestar-connections_Branch)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete a Connection resource
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteHost.html)  **
  - **Description:** Grants permission to delete a host resource
  - **Resource types (\*required):** [Host\*](#list_codestar-connections-resource-Host)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteRepositoryLink.html)  **
  - **Description:** Grants permission to delete a repository link
  - **Resource types (\*required):** [RepositoryLink\*](#list_codestar-connections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_DeleteSyncConfiguration.html)  **
  - **Description:** Grants permission to delete a sync configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetConnection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetConnection.html)  **
  - **Description:** Grants permission to get details about a Connection resource
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetHost.html)  **
  - **Description:** Grants permission to get details about a host resource
  - **Resource types (\*required):** [Host\*](#list_codestar-connections-resource-Host)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetRepositoryLink.html)  **
  - **Description:** Grants permission to describe a repository link
  - **Resource types (\*required):** [RepositoryLink\*](#list_codestar-connections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositorySyncStatus](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetRepositorySyncStatus.html)  **
  - **Description:** Grants permission to get the latest sync status for a repository
  - **Resource types (\*required):** [RepositoryLink\*](#list_codestar-connections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:Branch](#list_codestar-connections-codestar-connections_Branch)
  - **Access level:** Read

- **   [GetResourceSyncStatus](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetResourceSyncStatus.html)  **
  - **Description:** Grants permission to get the latest sync status for a resource (cfn stack or other resources)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSyncBlockerSummary](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetSyncBlockerSummary.html)  **
  - **Description:** Grants permission to describe service sync blockers on a resource (cfn stack or other resources)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetSyncConfiguration.html)  **
  - **Description:** Grants permission to describe a sync configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnections](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListConnections.html)  **
  - **Description:** Grants permission to list Connection resources
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:ProviderTypeFilter](#list_codestar-connections-codestar-connections_ProviderTypeFilter)
  - **Access level:** List

- **   [ListHosts](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListHosts.html)  **
  - **Description:** Grants permission to list host resources
  - **Resource types (\*required):** 
  - **Condition keys:** [codestar-connections:ProviderTypeFilter](#list_codestar-connections-codestar-connections_ProviderTypeFilter)
  - **Access level:** List

- **   [ListRepositoryLinks](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListRepositoryLinks.html)  **
  - **Description:** Grants permission to list repository links
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositorySyncDefinitions](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListRepositorySyncDefinitions.html)  **
  - **Description:** Grants permission to list repository sync definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSyncConfigurations](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListSyncConfigurations.html)  **
  - **Description:** Grants permission to list sync configurations for a repository link
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to the set of key-value pairs that are used to manage the resource
  - **Resource types (\*required):** [Connection](#list_codestar-connections-resource-Connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Host](#list_codestar-connections-resource-Host) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RepositoryLink](#list_codestar-connections-resource-RepositoryLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or modify the tags of the given resource
  - **Resource types (\*required):** [Connection](#list_codestar-connections-resource-Connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-connections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)
  - **Resource types (\*required):** [Host](#list_codestar-connections-resource-Host) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-connections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)
  - **Resource types (\*required):** [RepositoryLink](#list_codestar-connections-resource-RepositoryLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codestar-connections-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an AWS resource
  - **Resource types (\*required):** [Connection](#list_codestar-connections-resource-Connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)
  - **Resource types (\*required):** [Host](#list_codestar-connections-resource-Host) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)
  - **Resource types (\*required):** [RepositoryLink](#list_codestar-connections-resource-RepositoryLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codestar-connections-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnectionInstallation](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to update a Connection resource with an installation of the CodeStar Connections App
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:InstallationId](#list_codestar-connections-codestar-connections_InstallationId)
  - **Access level:** Write

- **   [UpdateHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateHost.html)  **
  - **Description:** Grants permission to update a host resource
  - **Resource types (\*required):** [Host\*](#list_codestar-connections-resource-Host)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:VpcId](#list_codestar-connections-codestar-connections_VpcId)
  - **Access level:** Write

- **   [UpdateRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateRepositoryLink.html)  **
  - **Description:** Grants permission to update a repository link
  - **Resource types (\*required):** [RepositoryLink\*](#list_codestar-connections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSyncBlocker](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateSyncBlocker.html)  **
  - **Description:** Grants permission to update a sync blocker for a resource (cfn stack or other resources)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_UpdateSyncConfiguration.html)  **
  - **Description:** Grants permission to update a sync configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [codestar-connections:Branch](#list_codestar-connections-codestar-connections_Branch)
  - **Access level:** Write



## Permission-only actions for AWS CodeStar Connections
<a name="list_codestar-connections-permission-only-actions"></a>

The following actions are defined by AWS CodeStar Connections but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetConnectionToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-getconnectiontoken)  **
  - **Description:** Grants permission to get a Connection token to call provider actions
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIndividualAccessToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:** [codestar-connections:ProviderType](#list_codestar-connections-codestar-connections_ProviderType)
  - **Access level:** Read

- **   [GetInstallationUrl](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:** [codestar-connections:ProviderType](#list_codestar-connections-codestar-connections_ProviderType)
  - **Access level:** Read

- **   [ListInstallationTargets](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  **
  - **Description:** Grants permission to pass a Connection resource to an AWS service that accepts a Connection ARN as input, such as codepipeline:CreatePipeline
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:PassedToService](#list_codestar-connections-codestar-connections_PassedToService)
  - **Access level:** Read

- **   [PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository)  **
  - **Description:** Grants permission to pass a repository link resource to an AWS service that accepts a RepositoryLinkId as input, such as codestar-connections:CreateSyncConfiguration
  - **Resource types (\*required):** [RepositoryLink\*](#list_codestar-connections-resource-RepositoryLink)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:PassedToService](#list_codestar-connections-codestar-connections_PassedToService)
  - **Access level:** Read

- **   [RegisterAppCode](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration)  **
  - **Description:** Grants permission to associate a third party server, such as a GitHub Enterprise Server instance, with a Host
  - **Resource types (\*required):** 
  - **Condition keys:** [codestar-connections:HostArn](#list_codestar-connections-codestar-connections_HostArn)
  - **Access level:** Read

- **   [StartAppRegistrationHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration)  **
  - **Description:** Grants permission to associate a third party server, such as a GitHub Enterprise Server instance, with a Host
  - **Resource types (\*required):** 
  - **Condition keys:** [codestar-connections:HostArn](#list_codestar-connections-codestar-connections_HostArn)
  - **Access level:** Read

- **   [StartOAuthHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  **
  - **Description:** Grants permission to associate a third party, such as a Bitbucket App installation, with a Connection
  - **Resource types (\*required):** 
  - **Condition keys:** [codestar-connections:ProviderType](#list_codestar-connections-codestar-connections_ProviderType)
  - **Access level:** Read

- **   [UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  **
  - **Description:** Grants permission to use a Connection resource to call provider actions
  - **Resource types (\*required):** [Connection\*](#list_codestar-connections-resource-Connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_)<br />[codestar-connections:BranchName](#list_codestar-connections-codestar-connections_BranchName)<br />[codestar-connections:FullRepositoryId](#list_codestar-connections-codestar-connections_FullRepositoryId)<br />[codestar-connections:OwnerId](#list_codestar-connections-codestar-connections_OwnerId)<br />[codestar-connections:ProviderAction](#list_codestar-connections-codestar-connections_ProviderAction)<br />[codestar-connections:ProviderPermissionsRequired](#list_codestar-connections-codestar-connections_ProviderPermissionsRequired)<br />[codestar-connections:RepositoryName](#list_codestar-connections-codestar-connections_RepositoryName)
  - **Access level:** Read



## Resource types defined by AWS CodeStar Connections
<a name="list_codestar-connections-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html)  | arn:${Partition}:codestar-connections:${Region}:${Account}:connection/${ConnectionId} | [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_) | 
|  [Host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-hosts.html)  | arn:${Partition}:codestar-connections:${Region}:${Account}:host/${HostId} | [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_) | 
|  [RepositoryLink](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks.html)  | arn:${Partition}:codestar-connections:${Region}:${Account}:repository-link/${RepositoryLinkId} | [aws:ResourceTag/${TagKey}](#list_codestar-connections-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CodeStar Connections
<a name="list_codestar-connections-policy-keys"></a>

AWS CodeStar Connections defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [codestar-connections:Branch](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  | Filters access by the branch name that is passed in the request | String | 
|   [codestar-connections:BranchName](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the branch name that is passed in the request. Applies only to UseConnection requests for access to a specific repository branch | String | 
|   [codestar-connections:FullRepositoryId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the repository that is passed in the request. Applies only to UseConnection requests for access to a specific repository | String | 
|   [codestar-connections:HostArn](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-hosts)  | Filters access by the host resource associated with the connection used in the request | ARN | 
|   [codestar-connections:InstallationId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake)  | Filters access by the third-party ID (such as the Bitbucket App installation ID for CodeStar Connections) that is used to update a Connection. Allows you to restrict which third-party App installations can be used to make a Connection | String | 
|   [codestar-connections:OwnerId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the owner of the third-party repository. Applies only to UseConnection requests for access to repositories owned by a specific user | String | 
|   [codestar-connections:PassedToService](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  | Filters access by the service to which the principal is allowed to pass a Connection or RepositoryLink | String | 
|   [codestar-connections:ProviderAction](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-access)  | Filters access by the provider action in a UseConnection request such as ListRepositories. See documentation for all valid values | String | 
|   [codestar-connections:ProviderPermissionsRequired](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the write permissions of a provider action in a UseConnection request. Valid types include read\_only and read\_write | String | 
|   [codestar-connections:ProviderType](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-managing)  | Filters access by the type of third-party provider passed in the request | String | 
|   [codestar-connections:ProviderTypeFilter](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-managing)  | Filters access by the type of third-party provider used to filter results | String | 
|   [codestar-connections:RepositoryName](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use)  | Filters access by the repository name that is passed in the request. Applies only to UseConnection requests for access to repositories owned by a specific user | String | 
|   [codestar-connections:VpcId](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-hosts)  | Filters access by the VpcId passed in the request | String | 