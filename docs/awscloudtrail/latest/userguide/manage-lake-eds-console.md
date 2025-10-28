# Create, update, and manage event data stores with the console

You can use the CloudTrail console to create, update, delete, and restore event data stores.

You can update the following settings using the CloudTrail console:

- You can change the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") from
  **Seven-year retention pricing** to **One-year extendable retention pricing**.
- You can update the retention period for the event data store. The retention
  period determines how long event data is kept in the event data store.
- You can convert a multi-Region event data store to a single-Region event data store,
  or convert a single-Region event data store to a multi-Region event data store.
- The management account for an AWS Organizations organization can convert an
  account-level event data store to an organization event data store, or can
  convert an organization event data store to an account-level event data
  store. This setting is not available on event data stores that collect events outside of AWS.
- You can enable or disable [Lake query federation](query-federation.md "query-federation.md").
  Federating an event data store allows you to query your event data from Amazon Athena.
- You can add or edit the resource-based policy for an event
  data store to provide cross-account access to your event data store. For more information, see [Resource-based policy examples for event data stores](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds").
- You can [stop event ingestion](query-eds-stop-ingestion.md "query-eds-stop-ingestion.md") and restart event ingestion on event data stores
  that collect management events, data events, or AWS Config configuration items.
- You can enable or disable [termination protection](query-eds-termination-protection.md "query-eds-termination-protection.md"). Enabling termination protection protects an event data store from being accidentally deleted.
  Termination protection is enabled by default.
- You can [restore](query-eds-restore.md "query-eds-restore.md") an event data store that is pending deletion.
- You can add or remove tags. You can add up to 50 tag key pairs to help you identify, sort, and control
  access to your event data store.
- You can add a KMS key to encrypt your event data store. You can’t remove a KMS key from an event data store.
  Using the CloudTrail console to create or update a event data stores provides the following advantages:

- If you're configuring an event data store to collect data events, using the CloudTrail
  console allows you to view the available data event resource types. For more
  information, see [Logging data events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md").
- If you're configuring an event data store to collect network activity events, using the CloudTrail
  console allows you to view the event sources for which you can log network activity events. For more
  information, see [Logging network activity
  events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").
- If you're configuring a event data store to collect events outside of AWS,
  using the CloudTrail console lets you view information about available partners. For more information, see
  [Create an event data store for events outside of AWS with the console](event-data-store-integration-events.md "event-data-store-integration-events.md").

###### Topics

- [Create an event data store for CloudTrail
  events with the console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md")
- [Create an event data store for Insights events with the console](query-event-data-store-insights.md "query-event-data-store-insights.md")
- [Create an event data store for
  configuration items with the console](query-event-data-store-config.md "query-event-data-store-config.md")
- [Create an event data store for events outside of AWS with the console](event-data-store-integration-events.md "event-data-store-integration-events.md")
- [Update an event data store with the console](query-event-data-store-update.md "query-event-data-store-update.md")
- [Stop and start event ingestion with the console](query-eds-stop-ingestion.md "query-eds-stop-ingestion.md")
- [Change termination protection
  with the console](query-eds-termination-protection.md "query-eds-termination-protection.md")
- [Delete an event data store with the console](query-event-data-store-delete.md "query-event-data-store-delete.md")
- [Restore an event data store with the console](query-eds-restore.md "query-eds-restore.md")
