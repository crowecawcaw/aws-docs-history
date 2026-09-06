

# List prepared statements using the AWS CLI
<a name="querying-with-prepared-statements-listing"></a>

To list the prepared statements for a specific workgroup, you can use the Athena [list-prepared-statements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-prepared-statements.html) AWS CLI command or the [ListPreparedStatements](https://docs.aws.amazon.com/athena/latest/APIReference/API_ListPreparedStatements.html) Athena API action. The `--work-group` parameter is required.

```
aws athena list-prepared-statements --work-group primary
```