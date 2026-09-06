

# Keep your query history longer than 45 days
<a name="querying-keeping-query-history"></a>

If you want to keep the query history longer than 45 days, you can retrieve the query history and save it to a data store such as Amazon S3. To automate this process, you can use Athena and Amazon S3 API actions and CLI commands. The following procedure summarizes these steps.

**To retrieve and save query history programmatically**

1. Use Athena [ListQueryExecutions](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListQueryExecutions.html) API action or the [list-query-executions](https://docs.aws.amazon.com/cli/latest/reference/athena/list-query-executions.html) CLI command to retrieve the query IDs.

1. Use the Athena [GetQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryExecution.html) API action or the [get-query-execution](https://docs.aws.amazon.com/cli/latest/reference/athena/get-query-execution.html) CLI command to retrieve information about each query based on its ID.

1. Use the Amazon S3 [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) API action or the [put-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html) CLI command to save the information in Amazon S3.