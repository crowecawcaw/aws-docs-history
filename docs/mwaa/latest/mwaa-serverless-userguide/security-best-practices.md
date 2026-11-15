

# Security best practices on Amazon MWAA Serverless
<a name="security-best-practices"></a>

Amazon MWAA Serverless provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your workflow, treat them as helpful considerations rather than prescriptions.
+ Use least-permissive permission policies. Grant permissions to only the resources or actions that users need to perform tasks.
+ Use AWS CloudTrail to monitor user activity in your account.

## Security best practices in Apache Airflow
<a name="security-best-practices-for-airflow"></a>

To implement security boundaries for your workflows:
+ Store secrets in AWS Secrets Manager. Although this doesn't prevent users who can write workflow definitions from reading secrets, it prevents them from modifying the secrets that your workflow uses. For more information about configuring a secrets backend, see [Managing connections and variables](connections.md).
+ Don't store secrets in workflow environment variables, because `GetWorkflow` returns them in plain text. For more information, see [Using environment variables in Amazon MWAA Serverless workflows](workflows-environment-variables.md).

## Security best practices for the Apache Airflow UI
<a name="security-best-practices-airflow-ui"></a>

The Apache Airflow UI runs with the permissions of the IAM identity that opens it. For more information, refer to [Access the Airflow UI](workflows-airflow-ui.md).
+ Allow `airflow-serverless:CreateAirflowUiUrl` only for identities that need the UI. To give an identity read-only access to the UI, don't allow `airflow-serverless:StartWorkflowRun`.
+ Treat the launch URL like a password until it is used or expires, and don't share it. Set `--expires-in-seconds` to the shortest time you need to open the URL.
+ Set `--session-duration-in-seconds` to the shortest session you need, and sign out from the UI when you're done.
+ Use AWS CloudTrail to monitor `CreateAirflowUiUrl` events and the calls that the UI makes on your behalf.