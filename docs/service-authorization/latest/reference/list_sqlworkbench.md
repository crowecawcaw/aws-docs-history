

# Actions, resources, and condition keys for AWS SQL Workbench
<a name="list_sqlworkbench"></a>

AWS SQL Workbench (service prefix: `sqlworkbench`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/redshift/latest/mgmt/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-authentication-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sqlworkbench/sqlworkbench.json) for this service.

**Topics**
+ [Actions defined by AWS SQL Workbench](#list_sqlworkbench-actions-as-permissions)
+ [Permission-only actions for AWS SQL Workbench](#list_sqlworkbench-permission-only-actions)
+ [Resource types defined by AWS SQL Workbench](#list_sqlworkbench-resources-for-iam-policies)
+ [Condition keys for AWS SQL Workbench](#list_sqlworkbench-policy-keys)

## Actions defined by AWS SQL Workbench
<a name="list_sqlworkbench-actions-as-permissions"></a>

AWS SQL Workbench has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS SQL Workbench
<a name="list_sqlworkbench-permission-only-actions"></a>

The following actions are defined by AWS SQL Workbench but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateConnectionWithChart](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to associate connection to a chart
  - **Resource types (\*required):** [chart\*](#list_sqlworkbench-resource-chart) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_sqlworkbench-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateConnectionWithTab](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to associate connection to a tab
  - **Resource types (\*required):** [connection\*](#list_sqlworkbench-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateNotebookWithTab](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to associate notebook to a tab
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateQueryWithTab](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to associate query to a tab
  - **Resource types (\*required):** [query\*](#list_sqlworkbench-resource-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteFolder](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to delete folders on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchGetNotebookCell](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get notebook cells content on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateAccount](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create SQLWorkbench account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateChart](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create new saved chart on your account
  - **Resource types (\*required):** [chart\*](#list_sqlworkbench-resource-chart)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create a new connection on your account
  - **Resource types (\*required):** [connection\*](#list_sqlworkbench-resource-connection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFolder](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create folder on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateNotebook](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create a new notebook on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNotebookCell](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create a notebook cell on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNotebookFromVersion](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create a new notebook from a notebook version on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNotebookVersion](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create a notebook version on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSavedQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create a new saved query on your account
  - **Resource types (\*required):** [query\*](#list_sqlworkbench-resource-query)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChart](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to remove charts on your account
  - **Resource types (\*required):** [chart\*](#list_sqlworkbench-resource-chart)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to remove connections on your account
  - **Resource types (\*required):** [connection\*](#list_sqlworkbench-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotebook](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to remove notebooks on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotebookCell](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to remove notebooks cells on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotebookVersion](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to remove notebooks cells on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQCustomContext](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to delete account-wide custom context
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSavedQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to remove saved queries on your account
  - **Resource types (\*required):** [query\*](#list_sqlworkbench-resource-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSqlGenerationContext](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to delete sql generation context
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTab](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to remove a tab on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DriverExecute](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to execute a query in your redshift cluster
  - **Resource types (\*required):** [connection\*](#list_sqlworkbench-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DuplicateNotebook](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create a new notebook by duplicating an existing one on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [ExportNotebook](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to export a notebook on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GenerateSession](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to generate a new session on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccountInfo](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get account info
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAutocompletionMetadata](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get database structure metadata for auto-completion
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAutocompletionResource](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get database structure information for auto-completion
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChart](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get charts on your account
  - **Resource types (\*required):** [chart\*](#list_sqlworkbench-resource-chart)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get connections on your account
  - **Resource types (\*required):** [connection\*](#list_sqlworkbench-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNotebook](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get notebook metadata on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNotebookVersion](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get the content of a notebook version on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQCustomContext](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get account-wide custom context
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQSqlPromptQuotas](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get Q generative SQL maximum prompt quotas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQSqlRecommendations](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get text to SQL recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQueryExecutionHistory](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get the query execution history on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSavedQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get saved query on your account
  - **Resource types (\*required):** [query\*](#list_sqlworkbench-resource-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchemaInference](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get the columns and data types inferred from a file
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSqlGenerationContext](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get sql generation context
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSqlRecommendations](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get text to SQL recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUserInfo](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get user info
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUserWorkspaceSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get workspace settings on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportNotebook](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to import a notebook on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [ListConnections](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list the connections on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatabases](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list databases of your redshift cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFiles](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list files and folders
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotebookVersions](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to get notebook versions metadata on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNotebooks](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list the notebooks on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQueryExecutionHistory](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list the query execution history on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRedshiftClusters](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list redshift clusters on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSampleDatabases](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list sample databases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSavedQueryVersions](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list versions of saved query on your account
  - **Resource types (\*required):** [query\*](#list_sqlworkbench-resource-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTabs](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list tabs on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTaggedResources](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list tagged resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list the tags of an sqlworkbench resource
  - **Resource types (\*required):** [chart](#list_sqlworkbench-resource-chart) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection](#list_sqlworkbench-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notebook](#list_sqlworkbench-resource-notebook) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [query](#list_sqlworkbench-resource-query) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PassAccountSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to provide account settings with the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutQCustomContext](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update account-wide custom context
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutSqlGenerationContext](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update sql generation context
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutTab](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create or update a tab on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutUserWorkspaceSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update workspace settings on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RestoreNotebookVersion](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to restore a notebook on your account to a version
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to tag an sqlworkbench resource
  - **Resource types (\*required):** [chart](#list_sqlworkbench-resource-chart) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Resource types (\*required):** [connection](#list_sqlworkbench-resource-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Resource types (\*required):** [notebook](#list_sqlworkbench-resource-notebook) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Resource types (\*required):** [query](#list_sqlworkbench-resource-query) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to untag an sqlworkbench resource
  - **Resource types (\*required):** [chart](#list_sqlworkbench-resource-chart) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Resource types (\*required):** [connection](#list_sqlworkbench-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Resource types (\*required):** [notebook](#list_sqlworkbench-resource-notebook) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Resource types (\*required):** [query](#list_sqlworkbench-resource-query) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountConnectionSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update account-wide connection settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountExportSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update account-wide export settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountGeneralSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update account-wide general settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountQSqlSettings](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update account-wide text to SQL settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateChart](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update a chart on your account
  - **Resource types (\*required):** [chart\*](#list_sqlworkbench-resource-chart)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateConnection](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update a connection on your account
  - **Resource types (\*required):** [connection\*](#list_sqlworkbench-resource-connection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateFileFolder](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to move files on your account
  - **Resource types (\*required):** [chart](#list_sqlworkbench-resource-chart) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [query](#list_sqlworkbench-resource-query) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFolder](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update a folder's name and details on your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateNotebook](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update a notebook metadata on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateNotebookCellContent](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update a notebook cell content on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateNotebookCellLayout](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update a notebook cell layout on your account
  - **Resource types (\*required):** [notebook\*](#list_sqlworkbench-resource-notebook)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateSavedQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to update a saved query on your account
  - **Resource types (\*required):** [query\*](#list_sqlworkbench-resource-query)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqlworkbench-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqlworkbench-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by AWS SQL Workbench
<a name="list_sqlworkbench-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [chart](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)  | arn:${Partition}:sqlworkbench:${Region}:${Account}:chart/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_) | 
|  [connection](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)  | arn:${Partition}:sqlworkbench:${Region}:${Account}:connection/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_) | 
|  [notebook](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)  | arn:${Partition}:sqlworkbench:${Region}:${Account}:notebook/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_) | 
|  [query](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)  | arn:${Partition}:sqlworkbench:${Region}:${Account}:query/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_sqlworkbench-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS SQL Workbench
<a name="list_sqlworkbench-policy-keys"></a>

AWS SQL Workbench defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags that are associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 