# Configure access to prepared statements

This topic covers IAM permissions for prepared statements in Amazon Athena.
Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

For more information about prepared statements, see [Use parameterized queries](querying-with-prepared-statements.md "querying-with-prepared-statements.md").

The following IAM permissions are required for creating, managing, and executing
prepared statements.

```
athena:CreatePreparedStatement
athena:UpdatePreparedStatement
athena:GetPreparedStatement
athena:ListPreparedStatements
athena:DeletePreparedStatement
```

Use these permissions as shown in the following table.

| To do this                                                           | Use these permissions                                            |
| -------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Run a `PREPARE` query                                                | `athena:StartQueryExecution`<br>`athena:CreatePreparedStatement` |
| Re-run a `PREPARE` query to update an existing prepared<br>statement | `athena:StartQueryExecution`<br>`athena:UpdatePreparedStatement` |
| Run an `EXECUTE` query                                               | `athena:StartQueryExecution`<br>`athena:GetPreparedStatement`    |
| Run a `DEALLOCATE PREPARE` query                                     | `athena:StartQueryExecution`<br>`athena:DeletePreparedStatement` |

## Example

The following example IAM policy grants permissions to manage and run prepared
statements on a specified account ID and workgroup.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "athena:StartQueryExecution",
 "athena:CreatePreparedStatement",
 "athena:UpdatePreparedStatement",
 "athena:GetPreparedStatement",
 "athena:DeletePreparedStatement",
 "athena:ListPreparedStatements"
 ],
 "Resource": [
 "arn:aws:athena:*:`111122223333`:workgroup/`<workgroup-name>`"
 ]
 }
 ]
}`

```
