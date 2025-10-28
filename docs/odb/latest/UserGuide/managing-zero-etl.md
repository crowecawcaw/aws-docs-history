# Managing zero-ETL integrations in Oracle Database@AWS

After creating a zero-ETL integration, you can perform various management operations including monitoring, modifying, and deleting integrations. This section covers the ongoing management of your zero-ETL integrations.

## Monitoring zero-ETL integration

Regular monitoring of your zero-ETL integration ensures optimal performance and helps identify issues early.

### Integration status monitoring

Monitor the status of your zero-ETL integrations using AWS Glue APIs.

```
# Check status of a specific integration
aws glue describe-integrations \
  --integration-identifier `integration-id`

# List all integrations in your account
aws glue describe-integrations
```

Integration statuses include:

- **creating** – Integration is being set up
- **active** – Integration is running and replicating data
- **modifying** – Integration configuration is being updated
- **needs_attention** – Integration requires manual intervention
- **failed** – Integration has encountered an error
- **deleting** – Integration is being removed

### Performance monitoring

Monitor the following aspects of your zero-ETL integration performance:

- **Replication lag** – The time difference between when a change occurs in Oracle and when it appears in Amazon Redshift
- **Data throughput** – The volume of data being replicated per unit of time
- **Error rates** – The frequency of replication errors or failures
- **Resource utilization** – CPU, memory, and network usage on both source and target systems

Use Amazon CloudWatch to monitor these metrics and set up alarms for critical thresholds.

## Modifying zero-ETL integrations

You can modify certain aspects of your zero-ETL integration after you have created it.
Supported modifications include the integration name and description.

### Modifying data filters

Change which tables or schemas are replicated by modifying the data filter.

```
aws glue modify-integration \
  --integration-identifier `integration-id` \
  --data-filter "include: `pdb1.new_schema.*`" \
  --integration-name "Updated Integration Name"
```

###### Important

When you modify the data filter, the integration enters a `modifying` state
and might require a resynchronization of data. Monitor the integration status to make sure
the modification completes successfully.

### Modification limitations

You can't modify the following settings after you create a zero-ETL integration:

- **Secret ARN** – The AWS Secrets Manager secret containing database credentials
- **KMS key** – The CMK used for encryption
- **Source ARN** – The Oracle Database@AWS VM cluster
- **Target ARN** – The Amazon Amazon Redshift cluster or namespace

To change these settings, delete the existing zero-ETL integration and create a new
one.

## Deleting zero-ETL integrations

When you no longer need a zero-ETL integration, you can delete it to stop replication and clean up associated resources.

### Deletion process

Delete a zero-ETL integration using the AWS Glue API.

```
aws glue delete-integration \
  --integration-identifier `integration-id`
```

You can delete integrations in the following states:

- **active**
- **needs_attention**
- **failed**
- **syncing**

### Effects of deletion

When you delete a zero-ETL integration, consider the following effects:

**Replication stops.**

No new changes from Oracle will be replicated to Amazon Redshift.

**Existing data is preserved.**

Data already replicated to Amazon Redshift remains available.

**The target database remains.**

The Amazon Redshift database created from the integration isn't automatically deleted

###### Important

Deletion is irreversible. If you need to resume replication after deletion, create a
new integration, which will perform a full initial load.

## Best practices for zero-ETL management

Follow these best practices to ensure optimal performance, security, and cost-effectiveness of your zero-ETL integrations.

### Operational best practices

These operational practices help maintain reliable and efficient zero-ETL integrations.

**Regular monitoring**

Set up CloudWatch alarms to monitor integration health and performance metrics.

**Credential rotation**

Regularly rotate database passwords and update them in AWS Secrets Manager.

**Backup verification**

Regularly verify that your Oracle database backups include the necessary components for disaster recovery.

**Performance testing**

Test the impact of zero-ETL integration on your Oracle database performance, especially during peak usage periods.

**Schema change planning**

Plan and test schema changes in a development environment before applying them to production.

### Security best practices

Implement these security measures to protect your zero-ETL integration and data.

**Least privilege access**

Grant only the minimum necessary permissions to replication users and AWS IAM roles.

**Network security**

Use security groups and NACLs to restrict network access to only required ports and sources.

**Encryption at rest**

Ensure that both Oracle databases and Amazon Redshift clusters use encryption at rest.

**Audit logging**

Enable audit logging on both Oracle and Amazon Redshift to track data access and changes.

**Secret management**

Use AWS Secrets Manager automatic rotation features where possible.

### Cost optimization

Apply these strategies to optimize costs while maintaining effective zero-ETL integration performance.

**Data filtering**

Use precise data filters to replicate only the data you need, reducing storage and compute costs.

**Amazon Redshift optimization**

Use appropriate Amazon Redshift node types and implement data compression to optimize costs.

**Monitoring usage**

Regularly review your zero-ETL integration usage and costs through AWS Cost Explorer.

**Cleanup unused integrations**

Delete integrations that are no longer needed to avoid ongoing charges.
