# CloudTrail Lake concepts and terminology

This section describes the key concepts and terms to help you use AWS CloudTrail Lake.

###### Concepts and terms

- [Event data stores](#cloudtrail-lake-concepts-eds "#cloudtrail-lake-concepts-eds")
- [Integrations](#cloudtrail-lake-concepts-integrations "#cloudtrail-lake-concepts-integrations")
- [Queries](#cloudtrail-lake-concepts-queries "#cloudtrail-lake-concepts-queries")
- [Dashboards](#cloudtrail-lake-concepts-dashboard "#cloudtrail-lake-concepts-dashboard")

## Event data stores

Events are aggregated into _event data stores_, which are immutable
collections of events based on criteria that you select by applying advanced event
selectors.

You can create an event data store to log [CloudTrail events](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md") (management
events, data events, network activity events), [CloudTrail
Insights events](query-event-data-store-insights.md "query-event-data-store-insights.md"), [AWS Audit Manager evidence](../../../audit-manager/latest/userguide/evidence-finder.md#understanding-evidence-finder "../../../audit-manager/latest/userguide/evidence-finder.md#understanding-evidence-finder"), [AWS Config
configuration items](query-event-data-store-config.md "query-event-data-store-config.md"), or [events outside of AWS](event-data-store-integration-events.md "event-data-store-integration-events.md").

**Advanced event selectors**

_Advanced event selectors_ determine which events to
include in an event data store. Advanced event selectors help you control
costs by logging only those events that are important to you.

For management events, data events, and network activity events, you can use advanced event
selectors to filter events. For example, if you're creating an event data
store to collect management events, you can filter out AWS Key Management Service (AWS KMS) or
Amazon Relational Database Service (Amazon RDS) Data API events. Typically, AWS KMS actions such as
`Encrypt`, `Decrypt`, and
`GenerateDataKey` generate more than 99 percent of
events.

For AWS Config configuration items, Audit Manager evidence, or events outside of AWS,
advanced event selectors are used only to include events of that type in the
event data store.

**Federation**

_Federation_ lets you see the metadata associated with
an event data store in the AWS Glue [Data
Catalog](../../../glue/latest/dg/components-overview.md#data-catalog-intro "../../../glue/latest/dg/components-overview.md#data-catalog-intro") and run SQL queries on the event data using Amazon Athena.
The table metadata stored in the AWS Glue Data Catalog lets the Athena query
engine know how to find, read, and process the data that you want to query.

When you enable Lake query federation, CloudTrail creates the federated
resources on your behalf and registers those resources with [AWS Lake Formation](../../../lake-formation/latest/dg/how-it-works.md "../../../lake-formation/latest/dg/how-it-works.md"). After Lake federation is enabled, you can directly
query your event data in Athena without needing to perform any additional
steps. For more information, see [Federate an event data store](query-federation.md "query-federation.md").

**Pricing option**

When you create an event data store, you choose the _pricing
option_ that you want to use for the event data store. The
pricing option determines the cost for ingesting and storing events, and the
default and maximum retention periods for the event data store. For
information about pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").

**Retention period**

An event data store’s _retention period_ determines how
long event data is kept in the event data store. CloudTrail Lake determines
whether to retain an event by checking if the `eventTime` of the
event is within the specified retention period. For example, if you specify
a retention period of 90 days, CloudTrail will remove events when their
`eventTime` is older than 90 days.

**Default retention period**

An event data store’s _default retention period_ is the
default number of days that event data is kept in the event data store.
During an event data store’s default retention period, storage is included
with ingestion pricing at no additional charge. After the default retention
period, pricing for storage is pay-as-you-go.

**Maximum retention period**

An event data store’s _maximum retention period_
represents the maximum number of days that you can keep data in an event
data store.

**Termination protection**

By default, event data stores enable _termination
protection_, which protects an event data store from being
accidentally deleted. To delete an event data store with termination
protection enabled, choose **Change termination
protection** from the **Actions** menu on the
event data store’s details page. Then you can proceed with deleting the
event data store. For more information, see [Change termination protection
with the console](query-eds-termination-protection.md "query-eds-termination-protection.md").

## Integrations

You can use CloudTrail Lake _integrations_ to log and store user activity
data from the following sources:

- Outside of AWS
- Any source in your hybrid environments, such as in-house or software as a
  service (SaaS) applications hosted on premises or in the cloud, virtual
  machines, or containers

An integration requires a channel to deliver the events and an event data store to
receive the events. After you set up your integration, call the [PutAuditEvents](../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md "../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md") API operation to ingest your application activity into CloudTrail.
Then, you can use CloudTrail Lake to search, query, and analyze the data that is logged from
your applications. For more information, see [Create an integration with an event
source outside of AWS](query-event-data-store-integration.md "query-event-data-store-integration.md").

**Integration type**

There are two types of integrations: _direct_ and _solution_. With
direct integrations, the partner calls the `PutAuditEvents` API
operation to deliver events to the event data store for your AWS account.
With solution integrations, the application runs in your AWS account and
the application calls the `PutAuditEvents` API operation to
deliver events to the event data store for your AWS account.

**Channels**

Activity events from sources outside of AWS work by using
_channels_ to bring events into CloudTrail Lake from
external partners that work with CloudTrail, or from your own sources. When you
create a channel, you choose one or more event data stores to store events
that arrive from the channel source. You can change the destination event
data stores for a channel as needed, as long as the destination event data
stores are set to log `eventCategory="ActivityAuditLog"` events.
When you create a channel for events from an external partner, you provide a
channel Amazon Resource Name (ARN) to the partner or source
application.

**Resource-based policies**

_Resource-based policies_ are JSON policy documents
that you attach to a resource. The resource-based policy attached to the
channel allows the source to transmit events through the channel. If a
channel doesn't have a resource policy, only the channel owner can call the
`PutAuditEvents` API operation on the channel. For more
information, see [AWS CloudTrail resource-based policy examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").

## Queries

_Queries_ in CloudTrail Lake are authored in SQL. You can build a query
on the CloudTrail Lake **Editor** tab by writing the query in SQL from
scratch, by opening a saved or sample query and editing it, or by using the query generator
to produce a query from an English language prompt. For more
information, see [Create or edit a query with the CloudTrail console](query-create-edit-query.md "query-create-edit-query.md") and [Create CloudTrail Lake queries from natural language
prompts](lake-query-generator.md "lake-query-generator.md").

CloudTrail Lake supports all valid Trino
`SELECT` statements and functions. For more information about the supported
SQL functions and operators, see [Functions and
Operators](https://trino.io/docs/current/functions.html "https://trino.io/docs/current/functions.html") on the Trino documentation website.

## Dashboards

By using CloudTrail Lake _dashboards_, you can visualize the events in
an event data store and see events trends, such as top AWS services, users, and
errors. For more information, see [CloudTrail Lake dashboards](lake-dashboard.md "lake-dashboard.md").

**Dashboard types**

CloudTrail Lake offers the following types of dashboards:

- **Managed dashboards** – You can view a
  managed dashboard to see event trends for an event data store that collects
  management events, data events, or Insights events. These dashboards are
  automatically available to you and are managed by CloudTrail Lake.
  CloudTrail offers 14 managed dashboards to choose from. You can manually refresh managed dashboards. You cannot modify, add, or remove the widgets for these dashboards,
  however, you can save a managed dashboard as a custom dashboard
  if you want to modify the widgets or set a refresh schedule.
- **Custom dashboards** – Custom dashboards allow you to query
  events in any event data store type. You can add up to 10 widgets to a custom dashboard. You can manually refresh a custom dashboard, or you can set a refresh schedule.
- **Highlights dashboards** – Enable the Highlights dashboard to view an at-a-glance overview of the
  AWS activity collected by the event data stores in your account. The Highlights dashboard is managed by CloudTrail
  and includes widgets that are relevant to your account. The widgets shown on the Highlights
  dashboard are unique to each account. These widgets could surface detected abnormal activity or anomalies.
  For example, your Highlights dashboard could include the **Total cross-account access widget**,
  which shows if there is an increase in abnormal cross-account activity. CloudTrail updates the Highlights dashboard every 6 hours.
  The dashboard shows the last 24 hours of data from the last update.

**Widgets**

_Widgets_ are the components that make up a dashboard
and provide a visualization, such as a line chart or bar chart. Each widget
corresponds to a SQL query. When you refresh a dashboard,
CloudTrail runs a query for each widget on the dashboard
to populate the data for the widget.
