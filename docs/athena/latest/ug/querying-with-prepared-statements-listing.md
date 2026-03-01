# List prepared statements using the AWS CLI

To list the prepared statements for a specific workgroup, you can use the
Athena [list-prepared-statements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-prepared-statements.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-prepared-statements.html") AWS CLI command or the [ListPreparedStatements](../APIReference/API_ListPreparedStatements.md "../APIReference/API_ListPreparedStatements.md") Athena API action. The
`--work-group` parameter is required.

```
aws athena list-prepared-statements --work-group primary
```
