# CloudTrail Lake event data stores

When you create an event data store in CloudTrail Lake, you choose the type of events to
include in your event data store. You can create an event data store to include CloudTrail
events (management events, data events, or network activity events), CloudTrail Insights events, AWS Config
configuration items, or events outside of AWS. Each event data store type can only
contain specific event categories (for example, AWS Config configuration items), because the
event schema is unique to the event category. You can run SQL queries across multiple
event data stores using the supported SQL JOIN keywords. For information about running
queries across multiple event data stores, see [Advanced, multi-table query
support](query-limitations.md#query-advanced-multi-table "query-limitations.md#query-advanced-multi-table").

The following table shows the supported event categories for each event data store
type. The **eventCategory** column shows the value that you would specify in the advanced event selectors to collect events of that type.

| Event type (console)       | eventCategory (API)                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CloudTrail events          | `Management`<br>`Data`<br>`NetworkActivity` | This event data store type can collect CloudTrail management events, data<br>events, and network activity events. For more information, see [Create an event data store for CloudTrail events](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md").                                                                                                                                                                                                                                                                                                                 |
| CloudTrail Insights events | `Insight`                                   | This event data store type can collect CloudTrail Insights events. To receive Insights events, you need a [source event data store](query-event-data-store-insights.md#query-event-data-store-cloudtrail-insights "query-event-data-store-insights.md#query-event-data-store-cloudtrail-insights") that<br>logs CloudTrail management events and enables Insights. For information about creating the source and destination event data stores,<br>see [Create an event data store for CloudTrail Insights events](query-event-data-store-insights.md "query-event-data-store-insights.md"). |
| Configuration items        | `ConfigurationItem`                         | This event data store type can collect AWS Config configuration items.<br>For more information, see [Create an event data store for AWS Config configuration items](query-event-data-store-config.md "query-event-data-store-config.md").                                                                                                                                                                                                                                                                                                                                                    |
| Events from integration    | `ActivityAuditLog`                          | This event data store type can collect non-AWS events from integrations. For more information,<br>see [Create an event data store for events outside of AWS](event-data-store-integration-events.md "event-data-store-integration-events.md").                                                                                                                                                                                                                                                                                                                                               |

You can also create an event data store for AWS Audit Manager evidence by using the Audit Manager console.
For more information about aggregating evidence in CloudTrail Lake using Audit Manager, see [Understanding how evidence finder works with CloudTrail Lake](../../../audit-manager/latest/userguide/evidence-finder.md#understanding-evidence-finder "../../../audit-manager/latest/userguide/evidence-finder.md#understanding-evidence-finder") in the
_AWS Audit Manager User Guide_.

CloudTrail Lake event data stores incur charges. When you create an event data store, you choose the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want
to use for the event data store. The pricing option determines the cost for ingesting and storing events, and
the default and maximum retention period for the event data store. For information
about CloudTrail pricing and managing Lake costs, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").

The sections which follow describe how to create, update, and manage event data stores.

###### Topics

- [Create, update, and manage event data stores with the console](manage-lake-eds-console.md "manage-lake-eds-console.md")
- [Create, update, and manage event data stores with the AWS CLI](lake-eds-cli.md "lake-eds-cli.md")
- [Manage event data store
  lifecycles](query-eds-disable-termination.md "query-eds-disable-termination.md")
- [Copy trail events to an event data store](cloudtrail-copy-trail-to-lake-eds.md "cloudtrail-copy-trail-to-lake-eds.md")
- [Federate an event data store](query-federation.md "query-federation.md")
- [Understanding organization event data stores](cloudtrail-lake-organizations.md "cloudtrail-lake-organizations.md")
