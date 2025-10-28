# Keep your query history longer than 45

days

If you want to keep the query history longer than 45 days, you can retrieve the query
history and save it to a data store such as Amazon S3. To automate this process, you can use
Athena and Amazon S3 API actions and CLI commands. The following procedure summarizes these
steps.

###### To retrieve and save query history programmatically

1. Use Athena [ListQueryExecutions](../APIReference/API_ListQueryExecutions.md "../APIReference/API_ListQueryExecutions.md") API action or the [list-query-executions](../../../cli/latest/reference/athena/list-query-executions.md "../../../cli/latest/reference/athena/list-query-executions.md") CLI command to retrieve the query IDs.
2. Use the Athena [GetQueryExecution](../APIReference/API_GetQueryExecution.md "../APIReference/API_GetQueryExecution.md") API action or the [get-query-execution](../../../cli/latest/reference/athena/get-query-execution.md "../../../cli/latest/reference/athena/get-query-execution.md") CLI command to retrieve information about each
   query based on its ID.
3. Use the Amazon S3 [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") API
   action or the [put-object](../../../cli/latest/reference/s3api/put-object.md "../../../cli/latest/reference/s3api/put-object.md") CLI command to save the information in Amazon S3.
