

# IAM Execution roles
<a name="execution-roles"></a>

Jobs API operations use an AWS Identity and Access Management (IAM) role to access your Amazon S3 buckets securely. The role you specify in your API requests using the `ExecutionRoleArn` parameter must have permissions to read from your input bucket and write to your output bucket. Amazon Location Service assumes this role on your behalf when running jobs, ensuring secure access to your data without requiring long-term credentials.

For more information, see [Configure IAM permissions](https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html).