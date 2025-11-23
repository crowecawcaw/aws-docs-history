# Best practices

Follow these best practices to ensure reliable and efficient scheduled query
operations:

**Query optimization**

- Test queries manually before scheduling to verify performance and
  results
- Use filter indexes early in your query to reduce data processing
- Limit time ranges to avoid timeouts with high-volume log
  groups
- Consider query complexity and execution time limits

**Schedule planning**

- Avoid overlapping executions by ensuring queries complete before
  the next scheduled run
- Consider log ingestion delays when setting time ranges
- Use cron expressions for specific times
- Spread out the schedules to ensure you do not hit query concurrency limit

**Monitoring and maintenance**

- Monitor execution history regularly to identify failures or
  performance issues
- Review and update IAM roles periodically to maintain
  security
- Test destination accessibility before deploying to
  production

**Authorization**

- All the APIs for scheduled query authorize on the scheduled query resource and not on the resources it takes in the input like log groups. Set up IAM policies accordingly
- Manage authorization of log groups using the execution role passed in the APIs
