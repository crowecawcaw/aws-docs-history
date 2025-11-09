# Managing CloudTrail Lake costs

AWS CloudTrail Lake event data stores and queries incur charges. You can configure event data stores in ways that capture the data you need
while remaining cost-effective. For information about
CloudTrail pricing, see [AWS CloudTrail
Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### Topics

- [Event data store pricing
  options](#cloudtrail-lake-manage-costs-pricing-option "#cloudtrail-lake-manage-costs-pricing-option")
- [Understanding CloudTrail Lake charges](#cloudtrail-lake-charges "#cloudtrail-lake-charges")
- [Recommendations for how you can reduce costs](#cloudtrail-lake-manage-costs-recommendations "#cloudtrail-lake-manage-costs-recommendations")
- [See also](#w33aab9c23c13 "#w33aab9c23c13")

## Event data store pricing

options

When you create an event data store, you choose the pricing
option that you want to use for the event data store. The
pricing option determines the cost for ingesting and storing events, and the default
and maximum retention periods for the event data store.

The following table describes the available pricing options. The table shows the
**Pricing option** in the console and the corresponding
`BillingMode` value for the API, and lists the default and maximum
retention period for each option.

| Pricing option (console)                  | BillingMode (API)              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **One-year extendable retention pricing** | `EXTENDABLE_RETENTION_PRICING` | Recommended if you expect to ingest less than 25 TB of event data<br>per month and want a flexible retention period of up to 10<br>years. This option is also recommended if your event data store collects AWS Config<br>configuration items, Audit Manager evidence, and events from outside of AWS.<br>For the first 366 days (the default retention period), storage is<br>included at no additional cost with ingestion pricing. After 366<br>days, extended retention is available at pay-as-you-go<br>pricing.<br>This is the default option.<br>**Default retention period:\*<br>• 366 days<br>**Maximum retention period:\*<br>• 3,653 days |
| **Seven-year retention pricing**          | `FIXED_RETENTION_PRICING`      | Recommended if expect to ingest more than 25 TB of event data per<br>month and need a retention period of up to 7 years.<br>Retention is included with ingestion pricing at no additional<br>charge.<br>**Default retention period:\*<br>• 2,557 days<br>**Maximum retention period:\*<br>• 2,557 days                                                                                                                                                                                                                                                                                                                                               |

## Understanding CloudTrail Lake charges

The following tables provides information about how CloudTrail Lake event data stores and queries incur charges. For information about
CloudTrail pricing, see [AWS CloudTrail
Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

| Charge type                                                        | How you incur charges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data ingestion (uncompressed data)                                 | For CloudTrail Lake, you pay based on the uncompressed<br>data ingested. The [pricing option](#cloudtrail-lake-manage-costs-pricing-option "#cloudtrail-lake-manage-costs-pricing-option")<br>for the event data store determines the cost of ingesting events:<br>• **One-year extendable retention pricing**: Offers ingestion pricing based on event type.<br>• **Seven-year retention pricing**: Offers ingestion pricing based on the volume of data ingested.<br>The greatest savings are achieved when the volume of data ingested monthly exceeds 25 TB.<br>**Copying trail events**<br>When you [copy trail<br>events](cloudtrail-copy-trail-to-lake-eds.md "cloudtrail-copy-trail-to-lake-eds.md") to CloudTrail Lake, CloudTrail unzips the logs that are stored in<br>gzip (compressed) format. Then CloudTrail copies the events contained in the<br>logs to your event data store. The size of the uncompressed data could<br>be greater than the actual Amazon S3 storage size. To get a general estimate<br>of the size of the uncompressed data, multiply the size of the logs in<br>the S3 bucket by 10.<br>NoteCloudTrail will not copy an event if its event time is older than<br>the specified retention period. To determine the appropriate<br>retention period, take the sum of the oldest event you want to copy in days and the number of days you<br>want to retain the events in the event data store as demonstrated<br>in this equation:\*_Retention period_<br>• =<br>`oldest-event-in-days` +<br>`number-days-to-retain`For example, if the oldest event you're copying is 45 days old<br>and you want to keep the events in the event data store for a<br>further 45 days, you would set the retention period to 90<br>days. |
| Data retention (optimized and compressed data)                     | CloudTrail Lake converts existing<br>events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/")<br>format. ORC is a columnar storage format that is optimized for fast retrieval of compressed data.<br>An event data store’s _retention period<br>• determines how<br>long event data is kept in the event data store. CloudTrail Lake determines<br>whether to retain an event by checking if an event's event time<br>is within the specified retention period. For example, if you specify<br>a retention period of 90 days, CloudTrail will remove events when their<br>event time is older than 90 days.<br>For event data stores using the \*\*Seven-year retention pricing_<br>• option,<br>storage is included with ingestion pricing at no additional<br>charge.<br>For event data stores using the **One-year extendable retention pricing**<br>option, storage is included at no charge with ingestion pricing for the<br>first 366 days (the default retention period). After 366 days, storage<br>is offered at pay-as-you-pricing and is charged based on the optimized and compressed<br>data in the event data store.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Running queries in CloudTrail Lake (optimized and compressed data) | When you run queries in CloudTrail Lake, you pay based on the amount of<br>optimized and compressed data scanned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Recommendations for how you can reduce costs

This section provides recommendations for how you can reduce costs when working with
CloudTrail Lake.

**Choose a pricing option based on the type of events your event data store will
collect and your expected monthly ingestion**

When creating an event data store, choose a pricing option based on the
type of events your event data store will collect and your expected monthly
ingestion.

If you expect to ingest less than 25 TB of event data on a monthly basis
and want a flexible retention period of up to 10 years, choose the
**One-year extendable retention pricing** option. We also generally
recommend this option for event data stores that collect AWS Config
configuration items, Audit Manager evidence, and events from outside of AWS.

If you expect to ingest more than 25 TB of event data on a monthly basis
and need a 7-year retention period, choose the
**Seven-year retention pricing** option.

**Evaluate your event data store's monthly ingestion over time**

Evaluate the historical monthly ingestion of your event data store to see
if there's a pricing option better suited to your needs.

If you have an existing event data store that uses the
**Seven-year retention pricing** option and you ingest
less than 25 TB of data on a monthly basis, consider updating the event data
store to use **One-year extendable retention pricing**. For event data
stores using the **Seven-year retention pricing** option, you
can change the pricing option using the [CloudTrail console](query-event-data-store-update.md "query-event-data-store-update.md"),
[AWS CLI](lake-cli-update-eds.md#lake-cli-update-billing-mode "lake-cli-update-eds.md#lake-cli-update-billing-mode"), or [UpdateEventDataStore](../APIReference/API_UpdateEventDataStore.md "../APIReference/API_UpdateEventDataStore.md") API operation.

If you have an existing event data store that uses the
**One-year extendable retention pricing** option and you ingest more
than 25 TB of event data on a monthly basis, consider whether
**Seven-year retention pricing** would better suit your
needs. To use the new pricing option, [stop ingestion](query-eds-stop-ingestion.md "query-eds-stop-ingestion.md") on your event
data store and create a new event data store with the
**Seven-year retention pricing** option.

**Use advanced event selectors to filter out events that aren't of
interest**

When configuring an event data store for CloudTrail management events, data events, or network activity events, you can
filter out events that aren't of interest by using advanced event
selectors.

You can filter management events on the following advanced event selector fields: `eventName`,
`eventSource`, `eventType`, `readOnly`, `sessionCredentialFromConsole`, and `userIdentity.arn`.

You can filter data events on the following advanced event selector fields: `eventName`, `eventSource`, `eventType`,
`resources.type`, `resources.ARN`,
`readOnly`, `sessionCredentialFromConsole`, and `userIdentity.arn`. For more information, see [Filtering data events by using advanced event
selectors](filtering-data-events.md "filtering-data-events.md").

You can filter network activity events on the following advanced event selector fields:
`eventName`, `errorCode`, and `vpcEndpointId`. For more information, see [Logging network activity
events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").

**Choose a narrower time range when copying trail events**

When copying trail events to CloudTrail Lake, specify a narrower start event
time and end event time to reduce the amount of data ingested.

If you are copying trail events to CloudTrail Lake for historical analysis and
do not want to ingest future events, deselect the option to ingest events so
that you do not incur charges on ingesting any additional events.

**Format queries to use a starting and ending `eventTime`**

When you run queries in Lake, you pay based upon the amount of data
scanned. You can constrain costs by specifying a starting and ending
`eventTime` for the query.

## See also

- [AWS CloudTrail
  Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/")
- [Supported CloudWatch metrics](cloudtrail-lake-cloudwatch-metrics.md "cloudtrail-lake-cloudwatch-metrics.md")
- [Managing your costs with AWS Budgets](../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md "../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md")
- [Getting started with Cost Explorer](../../../cost-management/latest/userguide/ce-getting-started.md "../../../cost-management/latest/userguide/ce-getting-started.md")
