

# Best practices
<a name="jobs-best-practices"></a>

We recommend the following best practices to optimize costs for bulk address validation jobs:
+ Implement data quality checks before submitting jobs to avoid processing addresses that are easily identifiable as invalid. Pre-filtering can reduce the number of addresses requiring validation and improve overall cost efficiency.
+ Use the appropriate additional features for your use case rather than requesting all available features by default. Only request position coordinates or country-specific attributes when your application specifically needs this enhanced data.
+ Plan job schedules to bulk address updates efficiently rather than processing small numbers of addresses frequently. Regular batch processing is typically more cost-effective than frequent small jobs.

## Optimizing batch sizes
<a name="optimizing-batch-sizes"></a>

Follow these additional recommendations to group addresses and size job batches optimally:
+ Balance batch size against processing time and cost efficiency. Larger batches typically provide better cost efficiency but may take longer to process. Consider your application's tolerance for processing delays when determining optimal batch sizes.
+ Group addresses by geographic region or validation requirements to optimize processing efficiency. Addresses from the same country or region may process more efficiently together, and you can apply different additional features based on regional requirements.

## Tracking costs
<a name="tracking-costs"></a>

Use the following recommendations to track costs and usage for Amazon Location Jobs APIs:
+ Track your Jobs API usage through AWS billing and cost management tools. Monitor the number of addresses processed, job frequency, and feature usage to understand your validation patterns and costs.
+ Set up billing alerts to notify you when usage exceeds expected thresholds, helping you manage costs proactively.