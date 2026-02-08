# Troubleshooting Zero-ETL integration

This section provides guidance for resolving common issues with zero-ETL integration.

## Zero-ETL integration setup failures

**Authentication failures**

- Verify that the replication user exists and has the correct password in
  AWS Secrets Manager.
- Ensure that all required permissions have been granted to the replication
  user.
- Check that the secret ARN is correct and accessible by Oracle Database@AWS.
- Verify that the CMK resource policy allows access by Oracle Database@AWS service
  principal.

**Network connectivity issues**

- Make sure that your ODB network has the zero-ETL integration enabled.
- Verify that SSL is properly configured on port 2484 (Exadata only).
- Check that the Oracle database listener is running and accepting
  connections.
- Ensure that network security groups and NACLs allow traffic on port 2484.
- Verify that the service name in your secret matches the actual Oracle service
  name.

**Permission errors**

- Check that your IAM user or role has the necessary permissions for AWS Glue
  integration operations.
- Verify that the Amazon Redshift resource policy allows inbound integrations from your
  VM cluster.
- Ensure that Oracle Database@AWS has been granted access to your secrets and AWS Key Management Service key.

## Replication issues

**Initial load failures**

- Verify that the Oracle database has sufficient resources to support the full
  load operation.
- Ensure that supplemental logging is enabled on the source database.
- Check for any table-level locks or constraints that might prevent data
  extraction.

**Change data capture issues**

- Verify that the Oracle database has adequate redo log space and retention.
- Check that the replication user has access to archived redo logs.
- For ASM-enabled systems, ensure that the ASM user is properly configured.
- Monitor Oracle database performance to ensure CDC is not causing resource
  contention.

**High replication lag**

- Monitor the replication lag metrics in CloudWatch.
- Check for high transaction volumes or large transactions in the source
  database.
- Verify that the Amazon Redshift cluster has adequate capacity to handle incoming
  data.

## Data consistency issues

**Missing or incomplete data**

- Verify that the data filter includes all required schemas and tables.
- Check for unsupported data types that may be causing replication failures.
- Ensure that the replication user has SELECT permissions on all required
  tables.

**Data type conversion errors**

- Review the supported data type mappings between Oracle and Redshift.
- Check for Oracle-specific data types that may require custom handling.
- Consider modifying your Oracle schema to use more compatible data types.

## Monitoring and debugging

Use the following approaches to monitor and debug Zero-ETL integration issues:

- **Integration status monitoring** – Regularly check
  the integration status using `aws glue describe-integrations`.
- **CloudWatch metrics** – Monitor available
  CloudWatch metrics for replication performance and errors.
- **Oracle database monitoring** – Monitor Oracle
  database performance and resource utilization.
- **Redshift monitoring** – Monitor Amazon Redshift cluster
  performance and storage utilization.

For complex issues that cannot be resolved using this troubleshooting guide, contact
AWS Support with the following information:

- Integration ARN and current status.
- Error messages from integration describe operations.
- Oracle database and Amazon Redshift cluster configurations.
- Timeline of when the issue started occurring.
