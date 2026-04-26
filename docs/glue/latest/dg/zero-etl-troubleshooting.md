# Troubleshooting zero-ETL integrations

Use the following sections to help troubleshoot problems that you have with AWS Glue zero-ETL integrations.

## Troubleshooting zero-ETL integrations with Amazon DynamoDB source

### Missing RBAC policy or point-in-time recovery on source DynamoDB table

Before creating the integration, source must be configured properly. If the source DynamoDB table is missing the RBAC policy with appropriate permissions or if the point-in-time recovery is disabled, then integration will go into Needs_Attention state. To resolve this issue, fix the permissions and/or enable the point-in-time recovery. The integration should automatically recover after some time once you fix the missing configurations.

## Troubleshooting zero-ETL integrations with SaaS sources (using AWS Glue connection)

### Connection not configured properly

If the AWS Glue connection is not configured properly, the integration may fail to access the SaaS source. Verify that the connection credentials are valid and that the source role has the appropriate permissions to access the connection.

## Troubleshooting zero-ETL integrations with general purpose Amazon S3 target

### Target-role is missing permissions

If the target role is missing the appropriate permissions or setup incorrectly, it will cause the integration to go into NEEDS_ATTENTION state. Please refer to the section for target role configuration to fix the issue. Integration should be automatically recovered after some time once you fix the issue.

### Target Catalog RBAC policy is incorrectly configured

If the target catalog resource policy is incorrectly configured, it will also cause the integration to go into NEEDS_ATTENTION state. Please refer to the section for target role configuration to fix the issue. Integration should be automatically recovered after some time once you fix the issue.

## Troubleshooting zero-ETL integrations with Amazon S3-Table target

### Target-role is missing permissions

If the target role is missing the appropriate permissions or setup incorrectly, it will cause the integration to go into NEEDS_ATTENTION state. Please refer to the section for target role configuration to fix the issue. Integration should be automatically recovered after some time once you fix the issue.

### Target Catalog RBAC policy is incorrectly configured

If the target catalog resource policy is incorrectly configured, it will also cause the integration to go into NEEDS_ATTENTION state. Please refer to the section for target role configuration to fix the issue. Integration should be automatically recovered after some time once you fix the issue.

## General troubleshooting guide for AWS Glue zero-ETL integration errors

All integrations emit CloudWatch logs after the completion of each process e.g. full data load or change data capture. You can refer to those logs to determine the exact root cause of the failure or error.

Additionally, AWS Glue also creates system table in the target AWS Glue database or S3-Table. During the time when integration remains operational (i.e. not in FAILED or DELETED state), AWS Glue will keep appending the statuses for each individual operations on the target i.e. completion of full data load or change data capture with statistics such as number of records, number of insertions, deletions etc.
