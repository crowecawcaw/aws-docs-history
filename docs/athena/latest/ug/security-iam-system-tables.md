

# Configure access to system tables
<a name="security-iam-system-tables"></a>

System tables add the `system-table` resource type, with the ARN `arn:{partition}:athena:{region}:{account}:system-table/{tableName}`. They also add five actions: `athena:CreateSystemTableConfiguration`, `athena:UpdateSystemTableConfiguration`, `athena:DeleteSystemTableConfiguration`, `athena:GetSystemTableConfiguration`, and `athena:ListSystemTableStatuses`. Grant the permissions to manage system tables separately from the permissions to query them. For least-privilege example policies, see [IAM permissions](athena-system-tables.md#athena-system-tables-iam-permissions).

When you enable system tables, the Athena system tables service principal (`systemtables.athena.amazonaws.com`) writes query history to the `aws-athena` Amazon S3 Tables bucket in your account. The bucket policy that S3 Tables attaches grants access only to that service principal, and only for requests made on behalf of your account (`aws:SourceAccount`). S3 Tables denies writes to system tables from all principals in your account. You can read and delete system tables, but you can't modify their data.