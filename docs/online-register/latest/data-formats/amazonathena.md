

# Data retrieval APIs for Amazon Athena
<a name="amazonathena"></a>

Amazon Athena provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="athena-BatchGetNamedQuery"></a>[BatchGetNamedQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetNamedQuery.html) | Get information about one or more named queries | Read | 
| <a name="athena-BatchGetPreparedStatement"></a>[BatchGetPreparedStatement](https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetPreparedStatement.html) | Get information about one or more prepared statements | Read | 
| <a name="athena-BatchGetQueryExecution"></a>[BatchGetQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetQueryExecution.html) | Get information about one or more query executions | Read | 
| <a name="athena-GetCalculationExecution"></a>[GetCalculationExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecution.html) | Get a calculation execution | Read | 
| <a name="athena-GetCalculationExecutionCode"></a>[GetCalculationExecutionCode](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecutionCode.html) | Get a calculation execution code | Read | 
| <a name="athena-GetCalculationExecutionStatus"></a>[GetCalculationExecutionStatus](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCalculationExecutionStatus.html) | Get a calculation execution status | Read | 
| <a name="athena-GetCapacityAssignmentConfiguration"></a>[GetCapacityAssignmentConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCapacityAssignmentConfiguration.html) | Get capacity assignment information for a capacity reservation | Read | 
| <a name="athena-GetCapacityReservation"></a>[GetCapacityReservation](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetCapacityReservation.html) | Get a capacity reservation | Read | 
| <a name="athena-GetCatalogs"></a>[GetCatalogs](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies) | Enable access to databases and tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0 | Read | 
| <a name="athena-GetDataCatalog"></a>[GetDataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetDataCatalog.html) | Get a datacatalog | Read | 
| <a name="athena-GetDatabase"></a>[GetDatabase](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetDatabase.html) | Get a database for a given datacatalog | Read | 
| <a name="athena-GetExecutionEngine"></a>[GetExecutionEngine](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies) | Enable access to the specified database and table. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0 | Read | 
| <a name="athena-GetExecutionEngines"></a>[GetExecutionEngines](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies) | Enable access to databases and tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0 | Read | 
| <a name="athena-GetNamedQuery"></a>[GetNamedQuery](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetNamedQuery.html) | Get information about the specified named query | Read | 
| <a name="athena-GetNamespace"></a>[GetNamespace](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies) | Enable access to the specified database and table. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0 | Read | 
| <a name="athena-GetNamespaces"></a>[GetNamespaces](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies) | Enable access to databases and tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0 | Read | 
| <a name="athena-GetNotebookMetadata"></a>[GetNotebookMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetNotebookMetadata.html) | Get notebook metadata | Read | 
| <a name="athena-GetPreparedStatement"></a>[GetPreparedStatement](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetPreparedStatement.html) | Get information about the specified prepared statement | Read | 
| <a name="athena-GetQueryExecution"></a>[GetQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryExecution.html) | Get information about the specified query execution | Read | 
| <a name="athena-GetQueryExecutions"></a>[GetQueryExecutions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListQueryExecutions.html) | Get query executions. Deprecated. Applies only to AWS services and principals that use Athena JDBC driver earlier than 1.1.0. Use ListQueryExecutions otherwise | Read | 
| <a name="athena-GetQueryResults"></a>[GetQueryResults](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryResults.html) | Get the query results | Read | 
| <a name="athena-GetQueryResultsStream"></a>[GetQueryResultsStream](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver.html#jdbc-v3-driver-download) | Get the query results stream | Read | 
| <a name="athena-GetQueryRuntimeStatistics"></a>[GetQueryRuntimeStatistics](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryRuntimeStatistics.html) | Get runtime statistics for the specified query execution | Read | 
| <a name="athena-GetResourceDashboard"></a>[GetResourceDashboard](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetResourceDashboard.html) | Get a Live UI/Persistence UI for a session | Read | 
| <a name="athena-GetSession"></a>[GetSession](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetSession.html) | Get a session | Read | 
| <a name="athena-GetSessionStatus"></a>[GetSessionStatus](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetSessionStatus.html) | Get a session status | Read | 
| <a name="athena-GetTable"></a>[GetTable](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies) | Enable access to the specified table. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0 | Read | 
| <a name="athena-GetTableMetadata"></a>[GetTableMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetTableMetadata.html) | Get a metadata about a table for a given datacatalog | Read | 
| <a name="athena-GetTables"></a>[GetTables](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies) | Enable access to tables. Applies only to AWS services managed policy and principals that use an Athena JDBC driver version 1.1.0 | Read | 
| <a name="athena-GetWorkGroup"></a>[GetWorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetWorkGroup.html) | Get a workgroup | Read | 
| <a name="athena-ListApplicationDPUSizes"></a>[ListApplicationDPUSizes](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListApplicationDPUSizes.html) | Return a list of ApplicationRuntimeIds | List | 
| <a name="athena-ListCalculationExecutions"></a>[ListCalculationExecutions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListCalculationExecutions.html) | Return a list of calculation executions | List | 
| <a name="athena-ListCapacityReservations"></a>[ListCapacityReservations](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListCapacityReservations.html) | Return a list of capacity reservations for the specified AWS account | List | 
| <a name="athena-ListDataCatalogs"></a>[ListDataCatalogs](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListDataCatalogs.html) | Return a list of datacatalogs for the specified AWS account | List | 
| <a name="athena-ListDatabases"></a>[ListDatabases](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListDatabases.html) | Return a list of databases for a given datacatalog | List | 
| <a name="athena-ListEngineVersions"></a>[ListEngineVersions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListEngineVersions.html) | Return a list of athena engine versions for the specified AWS account | Read | 
| <a name="athena-ListExecutors"></a>[ListExecutors](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListExecutors.html) | Return a list of executors | List | 
| <a name="athena-ListNamedQueries"></a>[ListNamedQueries](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListNamedQueries.html) | Return a list of named queries in Amazon Athena for the specified AWS account | List | 
| <a name="athena-ListNotebookMetadata"></a>[ListNotebookMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListNotebookMetadata.html) | Return a list of notebooks for a given workgroup | List | 
| <a name="athena-ListNotebookSessions"></a>[ListNotebookSessions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListNotebookSessions.html) | Return a list of sessions for a given notebook | List | 
| <a name="athena-ListPreparedStatements"></a>[ListPreparedStatements](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListPreparedStatements.html) | Return a list of prepared statements for the specified workgroup | List | 
| <a name="athena-ListQueryExecutions"></a>[ListQueryExecutions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListQueryExecutions.html) | Return a list of query executions for the specified AWS account | Read | 
| <a name="athena-ListSessions"></a>[ListSessions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListSessions.html) | Return a list of sessions for a given workgroup | List | 
| <a name="athena-ListTableMetadata"></a>[ListTableMetadata](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListTableMetadata.html) | Return a list of table metadata in a database for a given datacatalog | Read | 
| <a name="athena-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListTagsForResource.html) | Return a list of tags for a resource | Read | 
| <a name="athena-ListWorkGroups"></a>[ListWorkGroups](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListWorkGroups.html) | Return a list of workgroups for the specified AWS account | List | 