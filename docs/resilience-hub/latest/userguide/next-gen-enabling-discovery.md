# Enabling dependency discovery for a service

You can enable dependency discovery from the console or using the AWS CLI.

**To enable dependency discovery for a single service
(console)**

Navigate to your service in the console and choose the **Assessment**
tab. Then choose **Enable dependency discovery**.

**To enable dependency discovery for a single service (CLI)**

```
aws resiliencehubv2 update-service \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123" \
  --dependency-discovery "ENABLED"
```

After you enable dependency discovery, Next generation Resilience Hub performs the following steps:

1. Queries 35 days of historical DNS data for your service's compute resources.
2. Identifies, deduplicates, and attributes dependencies to your service.
3. Continues monitoring hourly to detect new dependencies and update existing ones.
4. Displays results for your service in the console under the "Assessments" tab.
