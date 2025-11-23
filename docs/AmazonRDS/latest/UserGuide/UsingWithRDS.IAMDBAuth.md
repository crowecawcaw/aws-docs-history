# Troubleshooting for IAM DB authentication

Following, you can find troubleshooting ideas for some common IAM DB authentication
issues and information on CloudWatch logs and metrics for IAM DB authentication.

## Exporting IAM DB authentication error logs to CloudWatch Logs

IAM DB authentication error logs are stored on the database host,
and you can export these logs your CloudWatch Logs account. Use the logs and
remediation methods in this page to troubleshoot IAM DB authentication issues.

You can enable log exports to CloudWatch Logs from the console, AWS CLI, and RDS API. For console instructions, see
[Publishing database logs to Amazon CloudWatch Logs](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md").

To export your IAM DB authentication error logs to CloudWatch Logs when creating a
DB instance from the AWS CLI, use the following command:

```
aws rds create-db-instance --db-instance-identifier `mydbinstance` \
--region `us-east-1` \
--db-instance-class `db.t3.large` \
--allocated-storage `50` \
--engine `postgres` \
--engine-version `16` \
--port `5432` \
--master-username `master` \
--master-user-password `password` \
--publicly-accessible \
--enable-iam-database-authentication \
*--enable-cloudwatch-logs-exports=iam-db-auth-error*
```

To export your IAM DB authentication error logs to CloudWatch Logs when modifying a DB instance
from the AWS CLI, use the following command:

```
aws rds modify-db-instance --db-instance-identifier `mydbinstance` \
--region `us-east-1` \
*--cloudwatch-logs-export-configuration '{"EnableLogTypes":["iam-db-auth-error"]}'*
```

To verify if your DB instance
is exporting IAM DB authentication logs to CloudWatch Logs, check if the `EnabledCloudwatchLogsExports`
parameter is set to `iam-db-auth-error` in the output for the `describe-db-instances` command.

```
aws rds describe-db-instances --region us-east-1 --db-instance-identifier `mydbinstance`
            ...

             "EnabledCloudwatchLogsExports": [
                "iam-db-auth-error"
            ],
            ...

```

## IAM DB authentication CloudWatch metrics

Amazon RDS delivers near-real time metrics
about IAM DB authentication to your Amazon CloudWatch account.
The following table lists the IAM DB authentication metrics available using CloudWatch:

| Metric                                              | Description                                                                                                                       |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `IamDbAuthConnectionRequests`                       | Total number of connection requests made with IAM DB<br>authentication.                                                           |
| `IamDbAuthConnectionSuccess`                        | Total number of successful IAM DB authentication<br>requests.                                                                     |
| `IamDbAuthConnectionFailure`                        | Total number of failed IAM DB authentication<br>requests.                                                                         |
| `IamDbAuthConnectionFailureInvalidToken`            | Total number of failed IAM DB authentication requests due to<br>invalid token.                                                    |
| `IamDbAuthConnectionFailureInsufficientPermissions` | Total number of failed IAM DB authentication requests due to<br>incorrect policies or permissions.                                |
| `IamDbAuthConnectionFailureThrottling`              | Total number of failed IAM DB authentication requests due to<br>IAM DB authentication throttling.                                 |
| `IamDbAuthConnectionFailureServerError`             | Total number of failed IAM DB authentication requests due to<br>an internal server error in the IAM DB authentication<br>feature. |

## Common issues and solutions

You might encounter the following issues when using IAM DB authention. Use the remediation steps
in the table to solve the issues:

| Error                                                                                                                                                                                                                                                                                                                  | Metric(s)                                                                           | Cause                                                                                                                                                                                                                                                                                                                                                                 | Solution                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[ERROR] Failed to authenticate the connection request for<br>user `db_user` because the provided<br>token is malformed or otherwise invalid. (Status Code: 400,<br>Error Code: InvalidToken)`                                                                                                                         | `IamDbAuthConnectionFailure`<br>`IamDbAuthConnectionFailureInvalidToken`            | The IAM DB authentiation token in the connection request is<br>either not a valid SigV4a token, or it is not formatted<br>correctly.                                                                                                                                                                                                                                  | Check your token generation strategy in your application. In some<br>cases, make sure you are passing the token with valid formatting.<br>Truncating the token (or incorrect string formatting) will make the<br>token invalid. |
| `[ERROR] Failed to authenticate the connection request for<br>user `db_user` because the token age is<br>longer than 15 minutes. (Status Code: 400, Error<br>Code:ExpiredToken)`                                                                                                                                       | `IamDbAuthConnectionFailure`<br>`IamDbAuthConnectionFailureInvalidToken`            | The IAM DB authentication token has expired. Tokens are only<br>valid for 15 minutes.                                                                                                                                                                                                                                                                                 | Check your token caching and/or token re-use logic in your<br>application. You should not re-use tokens that are older than 15<br>minutes.                                                                                      |
| `[ERROR] Failed to authorize the connection request for user<br>`db_user` because the IAM policy<br>assumed by the caller 'arn:aws:sts::123456789012:assumed-role/<br><RoleName>/ <RoleSession>' is not authorized to perform<br>`rds-db:connect` on the DB instance. (Status Code: 403, Error<br>Code:NotAuthorized)` | `IamDbAuthConnectionFailure`<br>`IamDbAuthConnectionFailureInsufficientPermissions` | This error might be due to the following reasons:<br>• The IAM policy assumed by the application does not<br>authorize the `rds-db:connect` action.<br>• You are assuming the incorrect role/policy for<br>`db_user` to connect to the<br>database.<br>• You are assuming the correct policy for<br>`db_user`, but you are not<br>connecting to the correct database. | Verify that the IAM role and/or policy you are assuming in your<br>application. Make sure you assume the same policy to generate the<br>token as to connect to the DB.                                                          |
| `[ERROR] Failed to authorize the connection request for user<br>`db_user` due to IAM DB<br>authentication throttling. (Status Code: 429, Error Code:<br>ThrottlingException)`                                                                                                                                          | `IamDbAuthConnectionFailure`<br>`IamDbAuthConnectionFailureThrottling`              | You are making too many connection requests to your DB in a short<br>amount of time. IAM DB authentication throttling limit is 200<br>connections per second.                                                                                                                                                                                                         | Reduce the rate of establishing new connections with IAM<br>authentication. Consider implementing connection pooling using RDS Proxy in<br>order to reuse established connections in your application.                          |
| `[ERROR] Failed to authorize the connection request for user<br>`db_user` due to an internal IAM<br>DB authentication error. (Status Code: 500, Error Code: InternalError)`                                                                                                                                            | `IamDbAuthConnectionFailure`<br>`IamDbAuthConnectionFailureThrottling`              | There was an internal error while authorizing the<br>DB conneciton with IAM DB authentication.                                                                                                                                                                                                                                                                        | Reach out to https://aws.amazon.com/premiumsupport/ to investigate the issue.                                                                                                                                                   |
