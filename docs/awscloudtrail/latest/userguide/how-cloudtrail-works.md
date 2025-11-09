# How CloudTrail works

You automatically have access to the CloudTrail **Event history** when you
create your AWS account. The **Event history** provides a viewable,
searchable, downloadable, and immutable record of the past 90 days of recorded management
events in an AWS Region.

For an ongoing record of events in your AWS account past 90 days,
create a trail or a CloudTrail Lake event data store.

###### Topics

- [CloudTrail Event history](#how-cloudtrail-works-eventhistory "#how-cloudtrail-works-eventhistory")
- [CloudTrail Lake and event data stores](#how-cloudtrail-works-lake "#how-cloudtrail-works-lake")
- [CloudTrail Lake dashboards](#how-cloudtrail-works-lake-dashboards "#how-cloudtrail-works-lake-dashboards")
- [CloudTrail trails](#how-cloudtrail-works-trails "#how-cloudtrail-works-trails")
- [CloudTrail Insights events](#how-cloudtrail-works-insights "#how-cloudtrail-works-insights")
- [CloudTrail channels](#how-cloudtrail-works-channels "#how-cloudtrail-works-channels")

## CloudTrail Event history

You can easily view the last 90 days of management events in the CloudTrail console by going
to the **Event history** page. You can also view the event history by
running the [**aws cloudtrail
lookup-events**](../../../cli/latest/reference/cloudtrail/lookup-events.md "../../../cli/latest/reference/cloudtrail/lookup-events.md") command, or the [`LookupEvents`](../APIReference/API_LookupEvents.md "../APIReference/API_LookupEvents.md") API operation. You can search events in
**Event history** by filtering for events on a single attribute.
For more information, see [Working with CloudTrail event history](view-cloudtrail-events.md "view-cloudtrail-events.md").

The **Event history** is not connected to any trails
or event data stores that exist in your account and is not affected by configuration
changes you make to your trails and event data stores.

There are no CloudTrail charges for viewing the **Event
history** page or running the `lookup-events` command.

## CloudTrail Lake and event data stores

You can create an event data store to log [CloudTrail events](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md") (management
events, data events, network activity events), [CloudTrail
Insights events](query-event-data-store-insights.md "query-event-data-store-insights.md"), [AWS Audit Manager evidence](../../../audit-manager/latest/userguide/evidence-finder.md#understanding-evidence-finder "../../../audit-manager/latest/userguide/evidence-finder.md#understanding-evidence-finder"), [AWS Config
configuration items](query-event-data-store-config.md "query-event-data-store-config.md"), or [events outside of AWS](event-data-store-integration-events.md "event-data-store-integration-events.md").

Event data stores can log events from the current AWS Region, or from all
AWS Regions in your AWS account. Event data stores that you are using to log
**Integration** events from outside AWS must be for a single
Region only; they cannot be multi-Region event data stores.

If you have created an organization in AWS Organizations, you can create an
_organization event data store_ that logs all events for all
AWS accounts in that organization. Organization event data stores can apply to all
AWS Regions, or the current Region. Organization event data stores must be created
using the management account or delegated administrator account, and when specified as
applying to an organization, are automatically applied to all member accounts in the
organization. Member accounts cannot see the organization event data store, nor can they
modify or delete it. Organization event data stores cannot be used to collect events
from outside of AWS. For more information, see [Understanding organization event data stores](cloudtrail-lake-organizations.md "cloudtrail-lake-organizations.md").

By default, all events in an event data store are encrypted by CloudTrail. When you
configure an event data store, you can choose to use your own AWS KMS key. Using your
own KMS key incurs AWS KMS costs for encryption and decryption. After you associate an
event data store with a KMS key, the KMS key cannot be removed or changed. For more
information, see [Encrypting CloudTrail log files, digest files, and event data stores with AWS KMS keys (SSE-KMS)](encrypting-cloudtrail-log-files-with-aws-kms.md "encrypting-cloudtrail-log-files-with-aws-kms.md").

The following table provides information about tasks you can perform on event data
stores.

| Task                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [View and create dashboards](lake-dashboard.md "lake-dashboard.md")                                                                                                                                              | You can use CloudTrail Lake dashboards to see event trends for the event data stores in your account. You can view managed dashboards,<br>create custom dashboards, and enable the \*_Highlights_<br>• dashboard<br>to see highlights for your event data curated and managed by CloudTrail Lake.                                                                                                                                                                                                                                                                                                                   |
| [Log<br>management events](logging-management-events-with-cloudtrail.md "logging-management-events-with-cloudtrail.md")                                                                                          | Configure your event data store to log read-only, write-only, or<br>all management events. By default, event data stores log management<br>events.<br>You can filter management events on the following advanced event selector fields: `eventName`,<br>`eventSource`, `eventType`, `readOnly`, `sessionCredentialFromConsole`, and `userIdentity.arn`.                                                                                                                                                                                                                                                             |
| [Log data<br>events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md")                                                                                                            | You can use [advanced event selectors](../APIReference/API_AdvancedEventSelector.md "../APIReference/API_AdvancedEventSelector.md") to create fine-grained<br>selectors to log only those data events of interest. For example, you can filter on the<br>`eventName` field to include or exclude logging of<br>specific API calls, which can help control costs. For more information,<br>see [Filtering data events by using advanced event<br>selectors](filtering-data-events.md "filtering-data-events.md").                                                                                                    |
| [Log network activity<br>events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md")                                                                                          | Configure your event data store to log network activity events. You can use<br>advanced event selectors to filter on the `eventName`, `errorCode`, and `vpcEndpointId` fields to<br>log only those events of interest.                                                                                                                                                                                                                                                                                                                                                                                              |
| [Log<br>Insights events](query-event-data-store-insights.md "query-event-data-store-insights.md")                                                                                                                | Configure your event data stores to log Insights events to help you<br>identify and respond to unusual activity associated with management<br>API calls. For more information, see [Working with CloudTrail Insights](logging-insights-events-with-cloudtrail.md "logging-insights-events-with-cloudtrail.md").<br>Additional charges apply for Insights events. You will be charged<br>separately if you enable Insights for both trails and event data<br>stores. For more information, see [AWS CloudTrail<br>Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). |
| [Copy trail<br>events](cloudtrail-copy-trail-to-lake-eds.md "cloudtrail-copy-trail-to-lake-eds.md")                                                                                                              | You can copy trail events to a [new](scenario-lake-import.md "scenario-lake-import.md") or [existing](cloudtrail-copy-trail-events-lake.md "cloudtrail-copy-trail-events-lake.md")<br>event data store to create a point-in-time snapshot of events logged<br>to the trail.                                                                                                                                                                                                                                                                                                                                         |
| [Enable federation on an event<br>data store](query-federation.md "query-federation.md")                                                                                                                         | You can federate an event data store to see the metadata<br>associated with the event data store in the AWS Glue [Data Catalog](../../../glue/latest/dg/components-overview.md#data-catalog-intro "../../../glue/latest/dg/components-overview.md#data-catalog-intro") and run SQL queries on the event data<br>using Amazon Athena. The table metadata stored in the AWS Glue Data Catalog<br>lets the Athena query engine know how to find, read, and process the<br>data that you want to query.                                                                                                                 |
| [Stop or start event<br>ingestion on an event data store](query-eds-stop-ingestion.md "query-eds-stop-ingestion.md")                                                                                             | You can stop and start event ingestion on event data stores<br>that collect CloudTrail management and data events, or AWS Config<br>configuration items.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Create an<br>integration with an event source outside of<br>AWS](query-event-data-store-integration.md "query-event-data-store-integration.md")                                                                 | You can use CloudTrail Lake \*integrations<br>• to log<br>and store user activity data from outside of AWS; from any source<br>in your hybrid environments, such as in-house or SaaS applications<br>hosted on-premises or in the cloud, virtual machines, or containers.<br>For information about available integration partners, see [AWS CloudTrail Lake<br>Integrations](https://aws.amazon.com/cloudtrail/partners/ "https://aws.amazon.com/cloudtrail/partners/").                                                                                                                                            |
| [View Lake sample queries<br>in the CloudTrail console](lake-console-queries.md "lake-console-queries.md")                                                                                                       | The CloudTrail console provides a number of sample queries that can<br>help you get started writing your own queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Create or edit a<br>query](query-create-edit-query.md "query-create-edit-query.md")                                                                                                                             | Queries in CloudTrail are authored in SQL. You can build a query on<br>the CloudTrail Lake \*_Editor_<br>• tab by writing the query<br>in SQL from scratch, or by opening a saved or sample query and<br>editing it.                                                                                                                                                                                                                                                                                                                                                                                                |
| [Save query results<br>to an S3 bucket](query-run-query.md#scenario-lake-save-queries "query-run-query.md#scenario-lake-save-queries")                                                                           | When you run a query, you can save the query results to an S3<br>bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Download<br>saved query results](view-download-cloudtrail-lake-query-results.md#cloudtrail-download-lake-query-results "view-download-cloudtrail-lake-query-results.md#cloudtrail-download-lake-query-results") | You can download a CSV file containing your saved CloudTrail Lake<br>query results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Validate<br>saved query results](cloudtrail-query-results-validation.md "cloudtrail-query-results-validation.md")                                                                                               | You can use CloudTrail query results integrity validation to<br>determine whether the query results were modified, deleted, or<br>unchanged after CloudTrail delivered the query results to the S3<br>bucket.                                                                                                                                                                                                                                                                                                                                                                                                       |

For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](cloudtrail-lake.md "cloudtrail-lake.md").

CloudTrail Lake event data stores and queries incur charges. When you create an event
data store, you choose the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you
want to use for the event data store. The pricing option determines the cost for
ingesting and storing events, and the default and maximum retention period for the
event data store. When you run queries in Lake, you pay based upon the amount of
data scanned. For information about CloudTrail pricing and managing Lake costs, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").

## CloudTrail Lake dashboards

You can use CloudTrail Lake dashboards to see event trends for the event data stores in your account. CloudTrail Lake
offers the following types of dashboards:

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

Each dashboard consists of one or more widgets and each widget represents a SQL
query.

For more information, see [CloudTrail Lake dashboards](lake-dashboard.md "lake-dashboard.md").

## CloudTrail trails

A _trail_ is a configuration that enables delivery of events to an
Amazon S3 bucket that you specify. You can also deliver and analyze events in a trail with
[Amazon CloudWatch Logs](send-cloudtrail-events-to-cloudwatch-logs.md "send-cloudtrail-events-to-cloudwatch-logs.md") and [Amazon EventBridge](cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-eventbridge "cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-eventbridge").

Trails can log CloudTrail management events, data events, network activity events, and Insights
events.

You can create both multi-Region and single-Region trails for your AWS account.

**Multi-Region trails**

When you create a multi-Region trail, CloudTrail records events
in all AWS Regions that are [enabled](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone") in your AWS account and delivers the CloudTrail event log files to an
S3 bucket that you specify. As a best practice, we recommend creating a
multi-Region trail because it captures activity in all enabled Regions. All trails created
using the CloudTrail console are multi-Region trails. You can convert a single-Region trail
to a multi-Region trail by using the AWS CLI. For
more information, see [Understanding multi-Region trails and
opt-in Regions](cloudtrail-multi-region-trails.md "cloudtrail-multi-region-trails.md"), [Creating a trail with the console](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console"), and [Converting a single-Region trail to a multi-Region trail](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-convert "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-convert").

**Single-Region trails**

When you create a single-Region trail, CloudTrail records the
events in that Region only. It then delivers the CloudTrail event log files to an
Amazon S3 bucket that you specify. You can only create a single-Region trail by
using the AWS CLI. If you create additional single trails, you can have those
trails deliver CloudTrail event log files to the same S3 bucket or to separate
buckets. This is the default option when you create a trail using the AWS CLI
or the CloudTrail API. For more information, see [Creating, updating, and managing trails with the AWS CLI](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.md").

###### Note

For both types of trails, you can specify an Amazon S3 bucket from any Region.

If you have created an organization in AWS Organizations, you can create an
_organization trail_ that logs all events for all AWS accounts
in that organization. Organization trails can apply to all AWS Regions, or the current
Region. Organization trails must be created using the management account or delegated
administrator account, and when specified as applying to an organization, are
automatically applied to all member accounts in the organization. Member accounts can
see the organization trail, but cannot modify or delete it. By default, member accounts
do not have access to the log files for an organization trail in the Amazon S3 bucket.

By default, when you create a trail in the CloudTrail console, your event log files and digest files are
encrypted with a KMS key. If you choose not to enable **SSE-KMS
encryption**, your event log files and digest files are encrypted using Amazon S3 server-side
encryption (SSE). You can store your log files in your bucket for as long as you want.
You can also define Amazon S3 lifecycle rules to archive or delete log files automatically.
If you want notifications about log file delivery and validation, you can set up Amazon SNS
notifications.

CloudTrail publishes log files multiple times an hour, about every 5 minutes. These log
files contain API calls from services in the account that support CloudTrail. For more
information, see [CloudTrail supported services and integrations](cloudtrail-aws-service-specific-topics.md "cloudtrail-aws-service-specific-topics.md").

###### Note

CloudTrail typically delivers logs within an average of about 5 minutes
of an API call. This time is not guaranteed. Review the [AWS CloudTrail Service Level Agreement](https://aws.amazon.com/cloudtrail/sla "https://aws.amazon.com/cloudtrail/sla") for more
information.

If you misconfigure your trail (for example, the S3 bucket is unreachable), CloudTrail
will attempt to redeliver the log files to your S3 bucket for 30 days, and these
attempted-to-deliver events will be subject to standard CloudTrail charges. To avoid
charges on a misconfigured trail, you need to delete the trail.

CloudTrail captures actions made directly by the user or on behalf of the user by an
AWS service. For example, an AWS CloudFormation `CreateStack` call can result in
additional API calls to Amazon EC2, Amazon RDS, Amazon EBS, or other services as required by the
AWS CloudFormation template. This behavior is normal and expected. You can identify if the action
was taken by an AWS service with the `invokedby` field in the CloudTrail
event.

The following table provides information about tasks you can perform on trails.

| Task                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Logging<br>management events](logging-management-events-with-cloudtrail.md "logging-management-events-with-cloudtrail.md")                              | Configure your trails to log read-only, write-only, or all<br>management events.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Log data<br>events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md")                                                    | You can use [advanced event selectors](../APIReference/API_AdvancedEventSelector.md "../APIReference/API_AdvancedEventSelector.md") to create fine-grained<br>selectors to log only those data events of interest. For example, you can filter on the<br>`eventName` field to include or exclude logging of<br>specific API calls, which can help control costs. For more information,<br>see [Filtering data events by using advanced event<br>selectors](filtering-data-events.md "filtering-data-events.md").                             |
| [Log network activity<br>events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md")                                  | Configure your trails to log network activity events. You can configure<br>advanced event selectors to filter on the `eventName`,<br>`errorCode`, and `vpcEndpointId` fields to<br>log only those events of interest.                                                                                                                                                                                                                                                                                                                        |
| [Log<br>Insights events](logging-insights-events-with-cloudtrail.md "logging-insights-events-with-cloudtrail.md")                                        | Configure your trails to log Insights events to help you identify and<br>respond to unusual activity associated with management API<br>calls.<br>Additional charges apply for Insights events. You will be charged<br>separately if you enable Insights for both trails and event data<br>stores. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").                                                                                               |
| [View Insights events](view-insights-events.md "view-insights-events.md")                                                                                | After you enable CloudTrail Insights on a trail, you can view up to 90 days of<br>Insights events by using the CloudTrail console or the AWS CLI.                                                                                                                                                                                                                                                                                                                                                                                            |
| [Download<br>Insights events](view-insights-events-console.md#downloading-insights-events "view-insights-events-console.md#downloading-insights-events") | After you enable CloudTrail Insights on a trail, you can download a CSV or JSON<br>file containing up to the past 90 days of Insights events for your<br>trail.                                                                                                                                                                                                                                                                                                                                                                              |
| [Copy trail events to<br>CloudTrail Lake](cloudtrail-copy-trail-to-lake.md "cloudtrail-copy-trail-to-lake.md")                                           | You can copy existing trail events to a CloudTrail Lake event data store<br>to create a point-in-time snapshot of events logged to the<br>trail.                                                                                                                                                                                                                                                                                                                                                                                             |
| [Create<br>and subscribe to an Amazon SNS topic](configure-sns-notifications-for-cloudtrail.md "configure-sns-notifications-for-cloudtrail.md")          | Subscribe to a topic to receive notifications about log file<br>delivery to your bucket. Amazon SNS can notify you in multiple ways,<br>including programmatically with Amazon Simple Queue Service.<br>NoteIf you want to receive SNS notifications about log file<br>deliveries from all Regions, specify only one SNS topic for your<br>trail. If you want to programmatically process all events, see<br>[Using the CloudTrail Processing Library](use-the-cloudtrail-processing-library.md "use-the-cloudtrail-processing-library.md"). |
| [View your log<br>files](get-and-view-cloudtrail-log-files.md "get-and-view-cloudtrail-log-files.md")                                                    | Find and download your log files from the S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Monitor events with CloudWatch Logs](monitor-cloudtrail-log-files-with-cloudwatch-logs.md "monitor-cloudtrail-log-files-with-cloudwatch-logs.md")       | You can configure your trail to send events to CloudWatch Logs. You can then<br>use CloudWatch Logs to monitor your account for specific API calls and<br>events.<br>NoteIf you configure a multi-Region trail to send<br>events to a CloudWatch Logs log group, CloudTrail sends events from all Regions<br>to a single log group.                                                                                                                                                                                                          |
| [Enable SSE-KMS encryption](encrypting-cloudtrail-log-files-with-aws-kms.md "encrypting-cloudtrail-log-files-with-aws-kms.md")                           | Encrypting your log files and digest files with a KMS key provides an extra layer of security for your<br>CloudTrail data.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Enable log<br>file integrity](cloudtrail-log-file-validation-intro.md "cloudtrail-log-file-validation-intro.md")                                        | Log file integrity validation helps you verify that log files have<br>remained unchanged since CloudTrail delivered them.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Share log files with other<br>AWS accounts](cloudtrail-sharing-logs.md "cloudtrail-sharing-logs.md")                                                    | You can share log files between accounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Aggregate logs from multiple accounts](cloudtrail-receive-logs-from-multiple-accounts.md "cloudtrail-receive-logs-from-multiple-accounts.md")           | You can aggregate log files from multiple accounts to a single<br>bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Work with<br>partner solutions](https://aws.amazon.com/cloudtrail/partners/ "https://aws.amazon.com/cloudtrail/partners/")                              | Analyze your CloudTrail output with a partner solution that integrates<br>with CloudTrail. Partner solutions offer a broad set of capabilities, such<br>as change tracking, troubleshooting, and security analysis.                                                                                                                                                                                                                                                                                                                          |

You can deliver one copy of your ongoing management events to your S3 bucket at no
charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For
more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3
pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## CloudTrail Insights events

AWS CloudTrail Insights help AWS users identify and respond to unusual activity associated with API call rates and API error rates by continuously analyzing CloudTrail management events. CloudTrail Insights
analyzes your normal patterns of API call volume and API error rates, also called the
_baseline_, and generates Insights events when the call volume or error
rates are outside normal patterns. Insights events on API call rate are generated for
`write` management APIs, and Insights events on API error rate are generated for
both `read` and `write` management APIs.

By default, CloudTrail trails and event data stores don't log Insights events. You must configure
your trail or event data store to log Insights events. For more information, see [Logging Insights events with the CloudTrail console](insights-events-enable.md "insights-events-enable.md") and [Logging Insights events with the AWS CLI](insights-events-CLI-enable.md "insights-events-CLI-enable.md").

Additional charges apply for Insights events. You will be charged separately if you enable
Insights for both trails and event data stores. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

### Viewing Insights events for trails

and event data stores

CloudTrail supports Insights events for both trails and event data stores, however, there are
some differences in how you view and access Insights events.

**Viewing Insights events for trails**

If you have Insights events enabled on a trail, and CloudTrail detects unusual activity, Insights events
are logged to a different folder or prefix in the destination S3 bucket for your
trail. You can also see the type of insight and the incident time period when you
view Insights events on the CloudTrail console. For more information, see [Viewing Insights events for trails with the console](view-insights-events-console.md "view-insights-events-console.md").

After you enable CloudTrail Insights for the first time on a trail,
CloudTrail may take up to 36 hours to begin delivering Insights events after you enable Insights events on a trail,
provided that unusual activity is detected during that time.

**Viewing Insights events for event data stores**

To log Insights events in CloudTrail Lake, you need a destination event data store
that logs Insights events and a source event data store that enables Insights and
logs management events. For more information, see [Create an event data store for Insights events with the console](query-event-data-store-insights.md "query-event-data-store-insights.md").

After you enable CloudTrail Insights for the first time on the source event data
store, CloudTrail may take up to 7 days to begin delivering Insights events,
provided that unusual activity is detected during that time.

If you have CloudTrail Insights enabled on a source event data store and CloudTrail detects
unusual activity, CloudTrail delivers Insights events to your destination event data
store. You can then query your destination event data store to get information about
your Insights events and can optionally save the query results to an S3 bucket. For more
information, see [Create or edit a query with the CloudTrail console](query-create-edit-query.md "query-create-edit-query.md") and [View sample queries with the CloudTrail console](lake-console-queries.md "lake-console-queries.md").

You can view the **Insights events** dashboard to visualize the
Insights events in your destination event data store. For more information about Lake
dashboards, see [CloudTrail Lake dashboards](lake-dashboard.md "lake-dashboard.md").

## CloudTrail channels

CloudTrail supports two types of _channels_:

**Channels for CloudTrail Lake integrations with event sources outside of AWS**

CloudTrail Lake uses _channels_ to bring events from outside
of AWS into CloudTrail Lake from external partners that work with CloudTrail, or from
your own sources. When you create a channel, you choose one or more event
data stores to store events that arrive from the channel source. You can
change the destination event data stores for a channel as needed, as long as
the destination event data stores are set to log activity events. When you
create a channel for events from an external partner, you provide a channel
ARN to the partner or source application. The resource policy attached to
the channel allows the source to transmit events through the channel. For
more information, see [Create an integration with an event
source outside of AWS](query-event-data-store-integration.md "query-event-data-store-integration.md") and [`CreateChannel`](../APIReference/API_CreateChannel.md "../APIReference/API_CreateChannel.md") in the _AWS CloudTrail API
Reference_.

**Service-linked channels**

AWS services can create a service-linked channel to receive CloudTrail events
on your behalf. The AWS service creating the service-linked channel
configures advanced event selectors for the channel and specifies whether
the channel applies to all Regions, or the current Region.

You can use the [CloudTrail console](cloudtrail-service-linked-channels.md#viewing-service-linked-channels-console "cloudtrail-service-linked-channels.md#viewing-service-linked-channels-console") or [AWS CLI](cloudtrail-service-linked-channels.md#viewing-service-linked-channels-cli "cloudtrail-service-linked-channels.md#viewing-service-linked-channels-cli") to view
information about any CloudTrail service-linked channels created by
AWS services.
