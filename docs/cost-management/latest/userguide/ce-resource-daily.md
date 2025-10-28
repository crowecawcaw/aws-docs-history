# Resource-level data at daily granularity

In Cost Explorer, you can enable resource-level data for your chosen AWS
services at daily granularity for the past 14 days.

You can apply **Group by: Resource** to understand the cost of
services by resource ID that you have enabled resource-level data for. Costs
associated with services that you have not enabled resource-level data for appear
under **No resource ID** in Cost Explorer. If you want to focus on
resource-level costs for a specific service, choose the
**Resource** filter in Cost Explorer, select the service you
want to analyze, and then select all resources (if you don’t have a specific
resource in mind) or a specific resource ID to understand cost and usage driven by
that specific resource.

Use resource-level data to identify your cost drivers. When analyzing variances or
anomalies in your AWS costs, you can group by service to first understand which
service is causing the variance or anomaly. Then you can filter for that service in
Cost Explorer and group by resource to create a view of costs per resource in that
service. Use the Cost Explorer table and graphs to understand which specific
resource has deviated from the normal usage pattern and is contributing to the
variance or anomaly. If you want to understand how your spend on a specific resource
has evolved over time, such as your spend on an S3 bucket, you can filter for that
resource in Cost Explorer by selecting that resource ID in the
**Resource** filter. Moreover, resource-level data is useful in
order to understand which specific resources are consuming your Savings Plans and
Reservations commitments. To create this view, you can filter for “Savings Plan
Covered Usage” or “Reservation applied usage” charge types, group by resource, and
filter for specific services that you have purchased Savings Plans and Reservations
for.

Once enabled, resource-level data at daily granularity is available within 48 hours. Note
that this data is not available for Savings Plans and Reservations utilization and coverage
reports.

###### Note

We will disable resource-level data at daily granularity for your organization
if no one in the organization accesses it in three consecutive months. However,
if you need the data, you can re-enable it in Cost Management
preferences.

Cost Explorer displays the top 5,000 most costly resources per service. If
you have more than 5,000 resources, you might not see all of them in the
console. However, you can search for those resources using the resource ID.
Consider using Cost and Usage Reports (CUR) to retrieve the cost and usage
associated with all resources as a CSV file.
