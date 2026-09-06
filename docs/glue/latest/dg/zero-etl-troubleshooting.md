

# Troubleshooting zero-ETL integrations
<a name="zero-etl-troubleshooting"></a>

Use the following sections to help troubleshoot problems that you have with AWS Glue zero-ETL integrations.

**Note**  
When an integration enters the NEEDS\_ATTENTION state, it recovers automatically after you fix the underlying issue—there is no manual recovery action to perform. Recovery is not immediate: AWS Glue retries the integration automatically using an exponential backoff schedule, so the interval between retry attempts increases over time. The integration returns to a healthy state on the next successful retry after the issue is resolved.

## Troubleshooting zero-ETL integrations with Amazon DynamoDB source
<a name="zero-etl-troubleshoot-dynamodb"></a>

### Missing RBAC policy or point-in-time recovery on source DynamoDB table
<a name="zero-etl-troubleshoot-dynamodb-rbac"></a>

Before creating the integration, the source must be configured properly. If the source DynamoDB table is missing the RBAC policy with the required permissions, or if point-in-time recovery is disabled, the integration enters the NEEDS\_ATTENTION state. To resolve this issue, fix the permissions, enable point-in-time recovery, or do both. After you apply the fix, the integration recovers automatically on a subsequent retry.

## Troubleshooting zero-ETL integrations with SaaS sources (using AWS Glue connection)
<a name="zero-etl-troubleshoot-saas"></a>

### Connection not configured properly
<a name="zero-etl-troubleshoot-saas-connection"></a>

If the AWS Glue connection is not configured properly, the integration may fail to access the SaaS source. Verify that the connection credentials are valid and that the source role has the appropriate permissions to access the connection.

## Troubleshooting zero-ETL integrations with general purpose Amazon S3 target
<a name="zero-etl-troubleshoot-s3-target"></a>

### Target-role is missing permissions
<a name="zero-etl-troubleshoot-s3-target-role"></a>

If the target role is missing the required permissions or is set up incorrectly, the integration enters the NEEDS\_ATTENTION state. For instructions on configuring the target role, see [Creating a target IAM role](zero-etl-target.md#zero-etl-config-target-s3-iam-role). After you apply the fix, the integration recovers automatically on a subsequent retry.

### Target Catalog RBAC policy is incorrectly configured
<a name="zero-etl-troubleshoot-s3-target-rbac"></a>

If the target catalog resource policy is incorrectly configured, the integration enters the NEEDS\_ATTENTION state. For instructions on configuring the catalog RBAC policy, see [Providing a catalog Resource Based Access (RBAC) policy](zero-etl-target.md#zero-etl-config-target-s3-rbac-policy). After you apply the fix, the integration recovers automatically on a subsequent retry.

## Troubleshooting zero-ETL integrations with Amazon S3-Table target
<a name="zero-etl-troubleshoot-s3-tables-target"></a>

### Target-role is missing permissions
<a name="zero-etl-troubleshoot-s3-tables-target-role"></a>

If the target role is missing the required permissions or is set up incorrectly, the integration enters the NEEDS\_ATTENTION state. For instructions on configuring the target role, see [Create target IAM Role](zero-etl-target.md#zero-etl-config-target-s3-tables-iam-role). After you apply the fix, the integration recovers automatically on a subsequent retry.

### Target Catalog RBAC policy is incorrectly configured
<a name="zero-etl-troubleshoot-s3-tables-target-rbac"></a>

If the target catalog resource policy is incorrectly configured, the integration enters the NEEDS\_ATTENTION state. For instructions on configuring the catalog RBAC policy, see [Provide Catalog RBAC Policy](zero-etl-target.md#zero-etl-config-target-s3-tables-rbac). After you apply the fix, the integration recovers automatically on a subsequent retry.

## General troubleshooting guide for AWS Glue zero-ETL integration errors
<a name="zero-etl-troubleshoot-general"></a>

All integrations emit CloudWatch logs after the completion of each process e.g. full data load or change data capture. You can refer to those logs to determine the exact root cause of the failure or error.

Additionally, AWS Glue also creates system table in the target AWS Glue database or S3-Table. During the time when integration remains operational (i.e. not in FAILED or DELETED state), AWS Glue will keep appending the statuses for each individual operations on the target i.e. completion of full data load or change data capture with statistics such as number of records, number of insertions, deletions etc.