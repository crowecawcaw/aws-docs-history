# Viewing your CloudTrail cost and usage with AWS Cost Explorer

This section describes how you can view your CloudTrail costs and usage using [AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md"). Cost Explorer gives you the ability to visualize,
understand, and manage your AWS costs and usage over time.

For details about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### To view CloudTrail cost and usage with Cost Explorer

1. Sign in to the AWS Management Console and open the Cost Explorer console
   at [https://console.aws.amazon.com/cost-management/home#/custom](https://console.aws.amazon.com/https://console.aws.amazon.com/cost-management/home#/custom "https://console.aws.amazon.com/https://console.aws.amazon.com/cost-management/home#/custom").
2. Under **Time**, choose the date range you want to analyze.
3. Under **Group by**, for **Dimension**, choose **Usage type**.
4. Under **Filters**, for **Service**, choose **CloudTrail**.
   The following image shows an example of a cost report filtered for CloudTrail and grouped by **Usage type**.

![The Cost Explorer report grouped by Usage type and filtered for the CloudTrail service](images/cost-explorer-cloudtrail-usage.png)
Review the **Usage type** to see which CloudTrail features generated the most cost. Each
**Usage type** begins with the code for the AWS Region where the
charge was incurred.

The following table describes the CloudTrail usage types for each CloudTrail feature.

| CloudTrail feature  | Usage type                                                 | Description                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CloudTrail trails   | ``region`-FreeEventsRecorded`                              | The first copy of management events delivered free of charge to an AWS Region.                                                                                                                                                                                                                                                                          |
| CloudTrail trails   | ``region`-PaidEventsRecorded`                              | The charge for additional copies of management events delivered to an AWS Region.                                                                                                                                                                                                                                                                       |
| CloudTrail trails   | ``region`-DataEventsRecorded`                              | The charge for delivery of data events to an AWS Region. Data events always incur charges.                                                                                                                                                                                                                                                              |
| CloudTrail trails   | ``region`-NetworkEventsRecorded`                           | The charge for delivery of network activity events to an AWS Region. Network activity events always incur charges.                                                                                                                                                                                                                                      |
| CloudTrail Lake     | ``region`-Ingestion-Bytes`                                 | The charge for ingesting events into a CloudTrail Lake event data store using the **Seven-year retention pricing** option. Ingestion pricing is based on the volume of data ingested and is the same for all event types.                                                                                                                               |
| CloudTrail Lake     | ``region`-Ingestion-Bytes-1yearstore-Live-CloudTrail-Logs` | The charge for ingesting CloudTrail data events, network activity events, and management events into a CloudTrail Lake event data store using the **One-year extendable retention pricing** option.                                                                                                                                                     |
| CloudTrail Lake     | ``region`-Ingestion-Bytes-1yearstore-Other-data-sources`   | The charge for ingesting other event sources into a CloudTrail Lake event data store using the **One-year extendable retention pricing** option. This includes CloudTrail Insights events, configuration items from AWS Config, evidence from AWS Audit Manager, (uncompressed) historical CloudTrail logs imported from S3, and events outside of AWS. |
| CloudTrail Lake     | ``region`-QueryScanned-Bytes`                              | The charge for running CloudTrail Lake queries. When you run queries in CloudTrail Lake, you incur charges based on the amount of optimized and compressed data scanned.                                                                                                                                                                                |
| CloudTrail Insights | ``region`-InsightsEvents`                                  | The charge for CloudTrail Insights events. For Insights events, you incur charges based on the number of management events analyzed per Insight type. For more information, see [Costs for Insights events](insights-events-costs.md "insights-events-costs.md").                                                                                       |
