# Monitoring zero-ETL integration

Regular monitoring of your zero-ETL integration ensures optimal performance and helps identify issues early.

## Integration status monitoring

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

## Performance monitoring

Monitor the following aspects of your zero-ETL integration performance:

- **Replication lag** – The time difference between when a change occurs in Oracle and when it appears in Amazon Redshift
- **Data throughput** – The volume of data being replicated per unit of time
- **Error rates** – The frequency of replication errors or failures
- **Resource utilization** – CPU, memory, and network usage on both source and target systems

Use Amazon CloudWatch to monitor these metrics and set up alarms for critical thresholds.
