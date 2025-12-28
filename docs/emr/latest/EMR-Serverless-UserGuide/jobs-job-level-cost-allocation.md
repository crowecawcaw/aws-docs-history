# Enabling Job Level Cost Allocation

Job level cost allocation enables granular billing attribution for EMR Serverless at the individual job run level, rather than aggregating all costs at the application level. When enabled, you can filter and track costs in AWS Cost Explorer and Cost and Usage Reports by specific job run IDs and tags associated with job runs, providing better visibility into charges for job runs submitted.

## Default behavior

Job-level cost allocation is not enabled by default.

## How to enable or disable the feature

You can configure job-level cost allocation during application creation or update it for existing applications.

Specify the `jobLevelCostAllocation` parameter when creating a new application:

```
# Enable job-level cost allocation:
aws emr-serverless create-application \
    --name "my-application" \
    --release-label "emr-7.12.0" \
    --type "SPARK" \
    --job-level-cost-allocation-configuration '{
        "enabled": true
    }'

# Disable job-level cost allocation:
aws emr-serverless create-application \
    --name "my-application" \
    --release-label "emr-7.12.0" \
    --type "SPARK" \
    --job-level-cost-allocation-configuration '{
        "enabled": false
    }'
```

Update the `jobLevelCostAllocationConfiguration` parameter for an existing application:

```
# Enable job-level cost allocation:
aws emr-serverless update-application \
    --application-id <application-id> \
    --job-level-cost-allocation-configuration '{
        "enabled": true
    }'

# Disable job-level cost allocation:
aws emr-serverless update-application \
    --application-id <application-id> \
    --job-level-cost-allocation-configuration '{
        "enabled": false
    }'
```

## Considerations and Limitations

- Enabling job-level cost allocation does not retroactively attribute costs for job runs that completed before the feature was enabled. Job runs started after enabling the feature will have granular cost attribution.
- Job-level cost allocation parameter can only be updated when an Application is in either CREATED or STOPPED state.
- When job-level cost allocation is enabled, costs are attributed to individual job runs rather than the application. To view aggregated costs at the application level, you must apply consistent tags (such as application-name or application-id) to all job runs within that application and filter by those tags in Cost Explorer or Cost and Usage Reports.
