

# Actions, resources, and condition keys for Amazon Athena
<a name="list_athena"></a>

Amazon Athena (service prefix: `athena`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/athena/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/athena/latest/ug/security-iam-athena.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/athena/athena.json) for this service.

**Topics**
+ [API operations defined by Amazon Athena](#list_athena-operations)
+ [Actions defined by Amazon Athena](#list_athena-actions-as-permissions)
+ [Resource types defined by Amazon Athena](#list_athena-resources-for-iam-policies)
+ [Condition keys for Amazon Athena](#list_athena-policy-keys)

## API operations defined by Amazon Athena
<a name="list_athena-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_athena-actions-as-permissions).




- **   BatchGetNamedQuery  **
  - **IAM action:**  [athena:BatchGetNamedQuery](#list_athena-action-BatchGetNamedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetPreparedStatement  **
  - **IAM action:**  [athena:BatchGetPreparedStatement](#list_athena-action-BatchGetPreparedStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetQueryExecution  **
  - **IAM action:**  [athena:BatchGetQueryExecution](#list_athena-action-BatchGetQueryExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CancelCapacityReservation  **
  - **IAM action:**  [athena:CancelCapacityReservation](#list_athena-action-CancelCapacityReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCapacityReservation  **
  - **IAM action:**  [athena:CreateCapacityReservation](#list_athena-action-CreateCapacityReservation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [athena:TagResource](#list_athena-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataCatalog  **
  - **IAM action:**  [athena:CreateDataCatalog](#list_athena-action-CreateDataCatalog)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [athena:TagResource](#list_athena-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNamedQuery  **
  - **IAM action:**  [athena:CreateNamedQuery](#list_athena-action-CreateNamedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNotebook  **
  - **IAM action:**  [athena:CreateNotebook](#list_athena-action-CreateNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePreparedStatement  **
  - **IAM action:**  [athena:CreatePreparedStatement](#list_athena-action-CreatePreparedStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePresignedNotebookUrl  **
  - **IAM action:**  [athena:CreatePresignedNotebookUrl](#list_athena-action-CreatePresignedNotebookUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkGroup  **
  - **IAM action:**  [athena:CreateWorkGroup](#list_athena-action-CreateWorkGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [athena:TagResource](#list_athena-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** athena.amazonaws.com / **Access level:** Write

- **   DeleteCapacityReservation  **
  - **IAM action:**  [athena:DeleteCapacityReservation](#list_athena-action-DeleteCapacityReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataCatalog  **
  - **IAM action:**  [athena:DeleteDataCatalog](#list_athena-action-DeleteDataCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNamedQuery  **
  - **IAM action:**  [athena:DeleteNamedQuery](#list_athena-action-DeleteNamedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotebook  **
  - **IAM action:**  [athena:DeleteNotebook](#list_athena-action-DeleteNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePreparedStatement  **
  - **IAM action:**  [athena:DeletePreparedStatement](#list_athena-action-DeletePreparedStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkGroup  **
  - **IAM action:**  [athena:DeleteWorkGroup](#list_athena-action-DeleteWorkGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportNotebook  **
  - **IAM action:**  [athena:ExportNotebook](#list_athena-action-ExportNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCalculationExecution  **
  - **IAM action:**  [athena:GetCalculationExecution](#list_athena-action-GetCalculationExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCalculationExecutionCode  **
  - **IAM action:**  [athena:GetCalculationExecutionCode](#list_athena-action-GetCalculationExecutionCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCalculationExecutionStatus  **
  - **IAM action:**  [athena:GetCalculationExecutionStatus](#list_athena-action-GetCalculationExecutionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCapacityAssignmentConfiguration  **
  - **IAM action:**  [athena:GetCapacityAssignmentConfiguration](#list_athena-action-GetCapacityAssignmentConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCapacityReservation  **
  - **IAM action:**  [athena:GetCapacityReservation](#list_athena-action-GetCapacityReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataCatalog  **
  - **IAM action:**  [athena:GetDataCatalog](#list_athena-action-GetDataCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDatabase  **
  - **IAM action:**  [athena:GetDatabase](#list_athena-action-GetDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNamedQuery  **
  - **IAM action:**  [athena:GetNamedQuery](#list_athena-action-GetNamedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotebookMetadata  **
  - **IAM action:**  [athena:GetNotebookMetadata](#list_athena-action-GetNotebookMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPreparedStatement  **
  - **IAM action:**  [athena:GetPreparedStatement](#list_athena-action-GetPreparedStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryExecution  **
  - **IAM action:**  [athena:GetQueryExecution](#list_athena-action-GetQueryExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResults  **
  - **IAM action:**  [athena:GetQueryResults](#list_athena-action-GetQueryResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryRuntimeStatistics  **
  - **IAM action:**  [athena:GetQueryRuntimeStatistics](#list_athena-action-GetQueryRuntimeStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceDashboard  **
  - **IAM action:**  [athena:GetResourceDashboard](#list_athena-action-GetResourceDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **IAM action:**  [athena:GetSession](#list_athena-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSessionEndpoint  **
  - **IAM action:**  [athena:GetSessionEndpoint](#list_athena-action-GetSessionEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSessionStatus  **
  - **IAM action:**  [athena:GetSessionStatus](#list_athena-action-GetSessionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableMetadata  **
  - **IAM action:**  [athena:GetTableMetadata](#list_athena-action-GetTableMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkGroup  **
  - **IAM action:**  [athena:GetWorkGroup](#list_athena-action-GetWorkGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportNotebook  **
  - **IAM action:**  [athena:ImportNotebook](#list_athena-action-ImportNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListApplicationDPUSizes  **
  - **IAM action:**  [athena:ListApplicationDPUSizes](#list_athena-action-ListApplicationDPUSizes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCalculationExecutions  **
  - **IAM action:**  [athena:ListCalculationExecutions](#list_athena-action-ListCalculationExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCapacityReservations  **
  - **IAM action:**  [athena:ListCapacityReservations](#list_athena-action-ListCapacityReservations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataCatalogs  **
  - **IAM action:**  [athena:ListDataCatalogs](#list_athena-action-ListDataCatalogs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatabases  **
  - **IAM action:**  [athena:ListDatabases](#list_athena-action-ListDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEngineVersions  **
  - **IAM action:**  [athena:ListEngineVersions](#list_athena-action-ListEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExecutors  **
  - **IAM action:**  [athena:ListExecutors](#list_athena-action-ListExecutors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNamedQueries  **
  - **IAM action:**  [athena:ListNamedQueries](#list_athena-action-ListNamedQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotebookMetadata  **
  - **IAM action:**  [athena:ListNotebookMetadata](#list_athena-action-ListNotebookMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotebookSessions  **
  - **IAM action:**  [athena:ListNotebookSessions](#list_athena-action-ListNotebookSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPreparedStatements  **
  - **IAM action:**  [athena:ListPreparedStatements](#list_athena-action-ListPreparedStatements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueryExecutions  **
  - **IAM action:**  [athena:ListQueryExecutions](#list_athena-action-ListQueryExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSessions  **
  - **IAM action:**  [athena:ListSessions](#list_athena-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTableMetadata  **
  - **IAM action:**  [athena:ListTableMetadata](#list_athena-action-ListTableMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [athena:ListTagsForResource](#list_athena-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWorkGroups  **
  - **IAM action:**  [athena:ListWorkGroups](#list_athena-action-ListWorkGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutCapacityAssignmentConfiguration  **
  - **IAM action:**  [athena:PutCapacityAssignmentConfiguration](#list_athena-action-PutCapacityAssignmentConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCalculationExecution  **
  - **IAM action:**  [athena:StartCalculationExecution](#list_athena-action-StartCalculationExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQueryExecution  **
  - **IAM action:**  [athena:StartQueryExecution](#list_athena-action-StartQueryExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSession  **
  - **IAM action:**  [athena:ListTagsForResource](#list_athena-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [athena:StartSession](#list_athena-action-StartSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [athena:TagResource](#list_athena-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** athena.amazonaws.com / **Access level:** Write

- **   StopCalculationExecution  **
  - **IAM action:**  [athena:StopCalculationExecution](#list_athena-action-StopCalculationExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopQueryExecution  **
  - **IAM action:**  [athena:StopQueryExecution](#list_athena-action-StopQueryExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [athena:TagResource](#list_athena-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateSession  **
  - **IAM action:**  [athena:TerminateSession](#list_athena-action-TerminateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [athena:UntagResource](#list_athena-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCapacityReservation  **
  - **IAM action:**  [athena:UpdateCapacityReservation](#list_athena-action-UpdateCapacityReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataCatalog  **
  - **IAM action:**  [athena:UpdateDataCatalog](#list_athena-action-UpdateDataCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNamedQuery  **
  - **IAM action:**  [athena:UpdateNamedQuery](#list_athena-action-UpdateNamedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNotebook  **
  - **IAM action:**  [athena:UpdateNotebook](#list_athena-action-UpdateNotebook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNotebookMetadata  **
  - **IAM action:**  [athena:UpdateNotebookMetadata](#list_athena-action-UpdateNotebookMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePreparedStatement  **
  - **IAM action:**  [athena:UpdatePreparedStatement](#list_athena-action-UpdatePreparedStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkGroup  **
  - **IAM action:**  [athena:UpdateWorkGroup](#list_athena-action-UpdateWorkGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** athena.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Athena
<a name="list_athena-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetNamedQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetNamedQuery.html)  **
  - **Description:** Grants permission to get information about one or more named queries
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetPreparedStatement](https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetPreparedStatement.html)  **
  - **Description:** Grants permission to get information about one or more prepared statements
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetQueryExecution.html)  **
  - **Description:** Grants permission to get information about one or more query executions
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CancelCapacityReservation](https://docs.aws.amazon.com/athena/latest/APIReference/API_CancelCapacityReservation.html)  **
  - **Description:** Grants permission to cancel a capacity reservation
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StopQueryExecution.html)  **
  - **Description:** Grants permission to cancel query execution. Deprecated. Applies only to AWS services and principals that use Athena JDBC driver earlier than 1.1.0. Use StopQueryExecution otherwise
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCapacityReservation](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateCapacityReservation.html)  **
  - **Description:** Grants permission to create a capacity reservation
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateDataCatalog.html)  **
  - **Description:** Grants permission to create a datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNamedQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateNamedQuery.html)  **
  - **Description:** Grants permission to create a named query
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateNotebook](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateNotebook.html)  **
  - **Description:** Grants permission to create a notebook
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePreparedStatement](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreatePreparedStatement.html)  **
  - **Description:** Grants permission to create a prepared statement
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePresignedNotebookUrl](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreatePresignedNotebookUrl.html)  **
  - **Description:** Grants permission to create a presigned notebook url
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateWorkGroup.html)  **
  - **Description:** Grants permission to create a workgroup
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCapacityReservation](https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteCapacityReservation.html)  **
  - **Description:** Grants permission to delete a capacity reservation
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteDataCatalog.html)  **
  - **Description:** Grants permission to delete a datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNamedQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteNamedQuery.html)  **
  - **Description:** Grants permission to delete a named query specified
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotebook](https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteNotebook.html)  **
  - **Description:** Grants permission to delete a notebook
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePreparedStatement](https://docs.aws.amazon.com/athena/latest/APIReference/API_DeletePreparedStatement.html)  **
  - **Description:** Grants permission to delete a prepared statement specified
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteWorkGroup.html)  **
  - **Description:** Grants permission to delete a workgroup
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportNotebook](https://docs.aws.amazon.com/athena/latest/APIReference/API_ExportNotebook.html)  **
  - **Description:** Grants permission to export a notebook
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCalculationExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecution.html)  **
  - **Description:** Grants permission to get a calculation execution
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCalculationExecutionCode](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecutionCode.html)  **
  - **Description:** Grants permission to get a calculation execution code
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCalculationExecutionStatus](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecutionStatus.html)  **
  - **Description:** Grants permission to get a calculation execution status
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCapacityAssignmentConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCapacityAssignmentConfiguration.html)  **
  - **Description:** Grants permission to get capacity assignment information for a capacity reservation
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCapacityReservation](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCapacityReservation.html)  **
  - **Description:** Grants permission to get a capacity reservation
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCatalogs](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  **
  - **Description:** Grants permission to enable access to databases and tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetDataCatalog.html)  **
  - **Description:** Grants permission to get a datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDatabase](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetDatabase.html)  **
  - **Description:** Grants permission to get a database for a given datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExecutionEngine](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  **
  - **Description:** Grants permission to enable access to the specified database and table. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetExecutionEngines](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  **
  - **Description:** Grants permission to enable access to databases and tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNamedQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetNamedQuery.html)  **
  - **Description:** Grants permission to get information about the specified named query
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNamespace](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  **
  - **Description:** Grants permission to enable access to the specified database and table. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNamespaces](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  **
  - **Description:** Grants permission to enable access to databases and tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotebookMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetNotebookMetadata.html)  **
  - **Description:** Grants permission to get notebook metadata
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPreparedStatement](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetPreparedStatement.html)  **
  - **Description:** Grants permission to get information about the specified prepared statement
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryExecution.html)  **
  - **Description:** Grants permission to get information about the specified query execution
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryExecutions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListQueryExecutions.html)  **
  - **Description:** Grants permission to get query executions. Deprecated. Applies only to AWS services and principals that use Athena JDBC driver earlier than 1.1.0. Use ListQueryExecutions otherwise
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQueryResults](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryResults.html)  **
  - **Description:** Grants permission to get the query results
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResultsStream](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver.html#jdbc-v3-driver-download)  **
  - **Description:** Grants permission to get the query results stream
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryRuntimeStatistics](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryRuntimeStatistics.html)  **
  - **Description:** Grants permission to get runtime statistics for the specified query execution
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceDashboard](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetResourceDashboard.html)  **
  - **Description:** Grants permission to get a Live UI/Persistence UI for a session
  - **Resource types (\*required):** [session](#list_athena-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetSession.html)  **
  - **Description:** Grants permission to get a session
  - **Resource types (\*required):** [session](#list_athena-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSessionEndpoint](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetSessionEndpoint.html)  **
  - **Description:** Grants permission to get a connection endpoint and authentication token for a given session Id
  - **Resource types (\*required):** [session](#list_athena-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetSessionStatus](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetSessionStatus.html)  **
  - **Description:** Grants permission to get a session status
  - **Resource types (\*required):** [session](#list_athena-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTable](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  **
  - **Description:** Grants permission to enable access to the specified table. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTableMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetTableMetadata.html)  **
  - **Description:** Grants permission to get a metadata about a table for a given datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTables](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  **
  - **Description:** Grants permission to enable access to tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetWorkGroup.html)  **
  - **Description:** Grants permission to get a workgroup
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportNotebook](https://docs.aws.amazon.com/athena/latest/APIReference/API_ImportNotebook.html)  **
  - **Description:** Grants permission to import a notebook
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListApplicationDPUSizes](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListApplicationDPUSizes.html)  **
  - **Description:** Grants permission to return a list of ApplicationRuntimeIds
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCalculationExecutions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListCalculationExecutions.html)  **
  - **Description:** Grants permission to return a list of calculation executions
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCapacityReservations](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListCapacityReservations.html)  **
  - **Description:** Grants permission to return a list of capacity reservations for the specified AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataCatalogs](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListDataCatalogs.html)  **
  - **Description:** Grants permission to return a list of datacatalogs for the specified AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatabases](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListDatabases.html)  **
  - **Description:** Grants permission to return a list of databases for a given datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEngineVersions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListEngineVersions.html)  **
  - **Description:** Grants permission to return a list of athena engine versions for the specified AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExecutors](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListExecutors.html)  **
  - **Description:** Grants permission to return a list of executors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNamedQueries](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListNamedQueries.html)  **
  - **Description:** Grants permission to return a list of named queries in Amazon Athena for the specified AWS account
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNotebookMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListNotebookMetadata.html)  **
  - **Description:** Grants permission to return a list of notebooks for a given workgroup
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNotebookSessions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListNotebookSessions.html)  **
  - **Description:** Grants permission to return a list of sessions for a given notebook
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPreparedStatements](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListPreparedStatements.html)  **
  - **Description:** Grants permission to return a list of prepared statements for the specified workgroup
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListQueryExecutions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListQueryExecutions.html)  **
  - **Description:** Grants permission to return a list of query executions for the specified AWS account
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSessions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to return a list of sessions for a given workgroup
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTableMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListTableMetadata.html)  **
  - **Description:** Grants permission to return a list of table metadata in a database for a given datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags for a resource
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [session\*](#list_athena-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWorkGroups](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListWorkGroups.html)  **
  - **Description:** Grants permission to return a list of workgroups for the specified AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutCapacityAssignmentConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_PutCapacityAssignmentConfiguration.html)  **
  - **Description:** Grants permission to assign capacity from a capacity reservation to queries
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RunQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartQueryExecution.html)  **
  - **Description:** Grants permission to run a query. Deprecated. Applies only to AWS services and principals that use Athena JDBC driver earlier than 1.1.0. Use StartQueryExecution otherwise
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCalculationExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartCalculationExecution.html)  **
  - **Description:** Grants permission to start a calculation execution
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartQueryExecution.html)  **
  - **Description:** Grants permission to start a query execution using an SQL query provided as a string
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSession](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartSession.html)  **
  - **Description:** Grants permission to start a session
  - **Resource types (\*required):** [session](#list_athena-resource-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Access level:** Write

- **   [StopCalculationExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StopCalculationExecution.html)  **
  - **Description:** Grants permission to stop a calculation execution
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StopQueryExecution.html)  **
  - **Description:** Grants permission to stop the specified query execution
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/athena/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add a tag to a resource
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Resource types (\*required):** [session\*](#list_athena-resource-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_athena-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateSession](https://docs.aws.amazon.com/athena/latest/APIReference/API_TerminateSession.html)  **
  - **Description:** Grants permission to terminate a session
  - **Resource types (\*required):** [session](#list_athena-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/athena/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a resource
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Resource types (\*required):** [session\*](#list_athena-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_athena-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCapacityReservation](https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateCapacityReservation.html)  **
  - **Description:** Grants permission to update a capacity reservation
  - **Resource types (\*required):** [capacity-reservation\*](#list_athena-resource-capacity-reservation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateDataCatalog.html)  **
  - **Description:** Grants permission to update a datacatalog
  - **Resource types (\*required):** [datacatalog\*](#list_athena-resource-datacatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNamedQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateNamedQuery.html)  **
  - **Description:** Grants permission to update a named query specified
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNotebook](https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateNotebook.html)  **
  - **Description:** Grants permission to update a notebook
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNotebookMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateNotebookMetadata.html)  **
  - **Description:** Grants permission to update notebook metadata
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePreparedStatement](https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdatePreparedStatement.html)  **
  - **Description:** Grants permission to update a prepared statement
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateWorkGroup.html)  **
  - **Description:** Grants permission to update a workgroup
  - **Resource types (\*required):** [workgroup\*](#list_athena-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Athena
<a name="list_athena-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [capacity-reservation](https://docs.aws.amazon.com/athena/latest/ug/example-policies-capacity-reservations.html)  | arn:${Partition}:athena:${Region}:${Account}:capacity-reservation/${CapacityReservationName} | [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_) | 
|  [datacatalog](https://docs.aws.amazon.com/athena/latest/ug/datacatalogs-example-policies.html)  | arn:${Partition}:athena:${Region}:${Account}:datacatalog/${DataCatalogName} | [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_) | 
|  [session](https://docs.aws.amazon.com/athena/latest/ug/example-policies-workgroup.html)  | arn:${Partition}:athena:${Region}:${Account}:workgroup/${WorkGroupName}/session/${SessionId} | [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_) | 
|  [workgroup](https://docs.aws.amazon.com/athena/latest/ug/example-policies-workgroup.html)  | arn:${Partition}:athena:${Region}:${Account}:workgroup/${WorkGroupName} | [aws:ResourceTag/${TagKey}](#list_athena-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Athena
<a name="list_athena-policy-keys"></a>

Amazon Athena defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the the presence of tag keys in the request | ArrayOfString | 