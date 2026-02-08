# Managing zero-ETL integrations in Oracle Database@AWS

After creating a zero-ETL integration, you can perform various management operations including modifying and deleting integrations. This section covers the ongoing management of your zero-ETL integrations.

## Modifying zero-ETL integrations

You can modify only the name, description, and data filtering options for a zero-ETL integration in a supported data warehouse. You can't modify the AWS Key Management Service key used to encrypt the integration, or the source or target databases.

### Prerequisites for modifying integrations

Before you modify a zero-ETL integration, ensure that you have the following:

- **Required permissions** – Your IAM user or role must
  have the `odb:UpdateOutboundIntegration` permission in addition to the
  standard AWS Glue permissions.
- **Integration in active state** – The integration must be
  in an `ACTIVE` state, not in `CREATING`, `MODIFYING`, `DELETING`, or
  `FAILED`.
- **Valid data filter syntax** – New data filters must follow
  the supported include/exclude pattern syntax.

### Modifying data filters

You can change which tables or schemas are replicated by modifying the data filter. In
this way, you can add or remove database objects from replication without recreating the
entire integration.

To modify the data filter for an integration, use the `modify-integration` command.

```
aws glue modify-integration \
  --integration-identifier `integration-id` \
  --data-filter "include: `pdb1.new_schema.*`"
```

You can also modify the integration name and description at the same time. In the
following example, you modify the integration name, descriptions, and filters for two
schemas in `pdb1`.

```
aws glue modify-integration \
  --integration-identifier `integration-id` \
  --data-filter "include: `pdb1.schema1.*, pdb1.schema2.*`" \
  --integration-name "`Updated Integration Name`" \
  --description "`Updated integration description`"
```

###### Important

When you modify the data filter, the integration enters a `modifying` state
and performs a resynchronization of data. The integration stops replication, applies the new filter settings, and resumes replication with a reload-target operation. Monitor the integration status to ensure the modification completes successfully.

### Considerations for data filter

modifications to zero-ETL integrations

Consider the following when modifying data filters:

- **Single PDB limitation** – You can only specify one
  pluggable database (PDB) per integration. Data filters like `include: pdb1.*.*,
include: pdb2.*.*` aren't supported
- **Replication interruption** – Data replication stops
  during the modification process and resumes after the new filter is applied.
- **Data reload** – The integration performs a full reload of
  data that matches the new filter criteria.
- **Performance impact** – Large data filter changes might
  take significant time to complete and can affect the source database performance during
  the reload.

### Limitations for modifications to zero-ETL

integration settings

You can't modify the following settings after you create a zero-ETL integration:

- **Secret ARN** – The AWS Secrets Manager secret containing database credentials
- **KMS key** – The customer managed key used for encryption
- **Source ARN** – The Oracle Database@AWS VM cluster
- **Target ARN** – The Amazon Redshift cluster or namespace

To change these settings, delete the existing zero-ETL integration and create a new
one.

## Deleting zero-ETL integrations

When you no longer need a zero-ETL integration, you can delete it to stop replication and clean up associated resources.

### Deletion using AWS Glue

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

Oracle Database@AWS doesn't replicate new changes from Amazon Redshift.

**Existing data is preserved.**

Data already replicated to Amazon Redshift remains available.

**The target database remains.**

The Amazon Redshift database created from the integration isn't automatically deleted.

###### Important

Deletion is irreversible. If you need to resume replication after deletion, create a
new integration, which performs a full initial load.

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
