# Configuring user background sessions for AWS Glue

###### Warning

When user background sessions is enabled for AWS Glue, Amazon SageMaker Unified Studio will not terminate interactive sessions.
All interactive sessions will be only terminated once all queries are completed.

User background sessions in AWS Glue must be enabled for the entire account.
AWS Glue requires additional actions to enable user background sessions for the entire account.

```
aws glue update-glue-identity-center-configuration \
  --user-background-sessions-enabled
```

For more information, see [User background sessions for AWS Glue ETL](../../../glue/latest/dg/user-background-sessions.md "../../../glue/latest/dg/user-background-sessions.md")
in the AWS Glue management guide.
