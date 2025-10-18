# Working with AWS CloudTrail Lake

AWS CloudTrail Lake lets you run SQL-based queries on your events. CloudTrail Lake converts existing
 events in row-based JSON format to  [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/")
 format. ORC is a columnar storage format that is optimized for fast retrieval of data.
 Events are aggregated into event data stores, which are immutable collections of events
 based on criteria that you select by applying [advanced event selectors](cloudtrail-lake-concepts.md#adv-event-selectors "cloudtrail-lake-concepts.md#adv-event-selectors"). 
 You can keep the event data in an event data store for up to 3,653 days (about 10 years) if you choose the **One-year extendable retention pricing** option, 
 or up to 2,557 days (about 7 years) if you choose the **Seven-year retention pricing** option. The selectors that you apply to an event data store control which 
 events persist and are available for you to query. CloudTrail Lake is an auditing solution that 
 can complement your compliance stack, and assist you with near real-time troubleshooting.


## CloudTrail Lake event data stores


When you create an event data store, you choose the type of events to include in your
 event data store. You can create an event data store to include [CloudTrail events](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md") (management events, data events, network activity events), [CloudTrail Insights events](query-event-data-store-insights.md "query-event-data-store-insights.md"), [AWS Config configuration items](query-event-data-store-config.md "query-event-data-store-config.md"), [AWS Audit Manager evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder.html#understanding-evidence-finder "https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder.html#understanding-evidence-finder"), or [events from outside of AWS](event-data-store-integration-events.md "event-data-store-integration-events.md"). Each event data store can only contain a
 specific event category (for example, AWS Config configuration items), because the [event schema](query-supported-event-schemas.md "query-supported-event-schemas.md") is unique to the event
 category. You can store events from an organization in AWS Organizations in an [organization event data store](cloudtrail-lake-organizations.md "cloudtrail-lake-organizations.md"),
 including events from multiple Regions and accounts. You can also run SQL queries across
 multiple event data stores using the supported SQL JOIN keywords. For information about
 running queries across multiple event data stores, see [Advanced, multi-table query
 support](query-limitations.md#query-advanced-multi-table "query-limitations.md#query-advanced-multi-table").


You can copy trail events to a new or existing event data store to create a
 point-in-time snapshot of events logged to the trail. For more information, see
 [Copy trail events to an event data store](cloudtrail-copy-trail-to-lake-eds.md "cloudtrail-copy-trail-to-lake-eds.md").


You can federate an event data store to see the metadata associated with the event data store in the AWS Glue 
 [Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro "https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro") and run SQL queries on the event data 
 using Amazon Athena. The table metadata stored in the AWS Glue Data Catalog 
 lets the Athena query engine know how to find, read, and process the data that you want to query. For more information, see [Federate an event data store](query-federation.md "query-federation.md").


You can attach a resource-based policy to your event data store to provide
 cross-account access to selected principals. You can
 add a resource-based policy when you create or update an event data store on the CloudTrail
 console, or by running the AWS CLI `put-resource-policy` command. For more
 information, see [Resource-based policy examples for event data stores](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds").


By default, all events in an event data store are encrypted by CloudTrail. When you configure an
 event data store, you can choose to use your own AWS Key Management Service key. Using your own KMS key
 incurs AWS KMS costs for encryption and decryption. After you associate an event data store
 with a KMS key, the KMS key cannot be removed or changed.


You can control access to actions on event data stores by using authorization based on tags. For more
 information and examples, see [Examples: Denying
 access to create or delete event data stores based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags") in this guide.


CloudTrail Lake event data stores incur charges. When you create an event data store, you choose the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want
 to use for the event data store. The pricing option determines the cost for ingesting and storing events, and 
 the default and maximum retention period for the event data store. For information 
 about CloudTrail pricing and managing Lake costs, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").


CloudTrail Lake supports Amazon CloudWatch metrics, which provide information about 
 data ingested and storage bytes. For more information about supported CloudWatch metrics, see [Supported CloudWatch metrics](cloudtrail-lake-cloudwatch-metrics.md "cloudtrail-lake-cloudwatch-metrics.md").


###### Note

CloudTrail typically delivers events within an average of about 5 minutes of an API call.
 This time is not guaranteed.


## CloudTrail Lake queries


CloudTrail Lake queries offer a deeper and more customizable view of events than simple key and
 value lookups in **Event history**, or running `LookupEvents`.
 An **Event history** search is limited to a single AWS account, only
 returns events from a single AWS Region, and cannot query multiple attributes. In contrast, CloudTrail
 Lake users can run complex SQL queries across multiple event fields. 
 CloudTrail Lake supports all valid Trino `SELECT` statements and functions. For more information about the 
 supported SQL functions and operators, see [Functions and Operators](https://trino.io/docs/current/functions.html "https://trino.io/docs/current/functions.html") 
 on the Trino documentation website.


You can build a query
 on the CloudTrail Lake **Editor** tab by writing the query in SQL from
 scratch, by opening a saved or sample query and editing it, or by using the query generator 
 to produce a query from an English language prompt. For more
 information, see [Create or edit a query with the CloudTrail console](query-create-edit-query.md "query-create-edit-query.md") and [Create CloudTrail Lake queries from natural language
 prompts](lake-query-generator.md "lake-query-generator.md").


You can save CloudTrail Lake queries for future use, and view results of queries for up to seven
 days. When you run queries, you can save the query results to an Amazon S3 bucket.


The CloudTrail console provides a number of sample queries that can help you get started writing your own queries. For more information, see [View sample queries with the CloudTrail console](lake-console-queries.md "lake-console-queries.md").


CloudTrail Lake queries incur charges. When you run queries in Lake, you
 pay based upon the amount of data scanned. For information 
 about CloudTrail pricing and managing Lake costs, see
 [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").


## CloudTrail Lake dashboards


You can use CloudTrail Lake dashboards to see event trends for the event data stores in your account. CloudTrail Lake
 offers the following types of dashboards:



* **Managed dashboards** – You can view a
 managed dashboard to see event trends for an event data store that collects
 management events, data events, or Insights events. These dashboards are
 automatically available to you and are managed by CloudTrail Lake. 
 CloudTrail offers 14 managed dashboards to choose from. You can manually refresh managed dashboards. You cannot modify, add, or remove the widgets for these dashboards, 
 however, you can save a managed dashboard as a custom dashboard 
 if you want to modify the widgets or set a refresh schedule.
* **Custom dashboards** – Custom dashboards allow you to query 
 events in any event data store type. You can add up to 10 widgets to a custom dashboard. You can manually refresh a custom dashboard, or you can set a refresh schedule.
* **Highlights dashboards** – Enable the Highlights dashboard to view an at-a-glance overview of the 
AWS activity collected by the event data stores in your account. The Highlights dashboard is managed by CloudTrail 
and includes widgets that are relevant to your account. The widgets shown on the Highlights 
dashboard are unique to each account. These widgets could surface detected abnormal activity or anomalies. 
For example, your Highlights dashboard could include the **Total cross-account access widget**, 
which shows if there is an increase in abnormal cross-account activity. CloudTrail updates the Highlights dashboard every 6 hours. 
The dashboard shows the last 24 hours of data from the last update.

Each dashboard consists of one or more widgets and each widget represents a SQL
 query.


For more information, see [CloudTrail Lake dashboards](lake-dashboard.md "lake-dashboard.md").


## CloudTrail Lake integrations


You can use CloudTrail Lake *integrations* to log and store user activity
 data from outside of AWS; from any source in your hybrid environments, such as in-house or
 SaaS applications hosted on-premises or in the cloud, virtual machines, or containers. After
 you create event data stores in CloudTrail Lake and create a channel to log activity events,
 you call the `PutAuditEvents` API to ingest your application activity into CloudTrail.
 You can then use CloudTrail Lake to search, query, and analyze the data that is logged from your
 applications.


Integrations can also log events to your event data stores from over a dozen CloudTrail
 partners. In a partner integration, you create destination event data stores, a channel, and
 a resource policy. After you create the integration, you provide the channel ARN to the partner. There are 
 two types of integrations: direct and solution. With direct integrations, the partner calls the `PutAuditEvents`
 API to deliver events to the event data store for your AWS account. With solution
 integrations, the application runs in your AWS account and the application calls the
 `PutAuditEvents` API to deliver events to the event data store for your
 AWS account.


For more information about integrations, see 
 [Create an integration with an event source outside of AWS](query-event-data-store-integration.md "query-event-data-store-integration.md").


## Additional resources


The following resources can help you get a better understanding of what 
 CloudTrail Lake is and how you can use it.



* [Modernize Your Audit Log Management Using CloudTrail Lake](https://www.youtube.com/watch?v=aLkecCsHhxw "https://www.youtube.com/watch?v=aLkecCsHhxw") (YouTube video)
* [Log Activity Events from Non-AWS Sources in AWS CloudTrail Lake](https://www.youtube.com/watch?v=gF0FLdegQKM "https://www.youtube.com/watch?v=gF0FLdegQKM") (YouTube video)
* [Analyze Activity Logs with AWS CloudTrail Lake and Amazon Athena](https://www.youtube.com/watch?v=cOeZaJt_k-w "https://www.youtube.com/watch?v=cOeZaJt_k-w") (YouTube video)
* [Get visibility into the activity logs for your workforce and customer identities](https://aws.amazon.com/blogs/mt/get-visibility-into-the-activity-logs-for-your-workforce-and-customer-identities/ "https://aws.amazon.com/blogs/mt/get-visibility-into-the-activity-logs-for-your-workforce-and-customer-identities/") (AWS blog)
* [Using AWS CloudTrail Lake to identify older TLS connections to AWS service endpoints](https://aws.amazon.com/blogs/mt/using-aws-cloudtrail-lake-to-identify-older-tls-connections-to-aws-service-endpoints/ "https://aws.amazon.com/blogs/mt/using-aws-cloudtrail-lake-to-identify-older-tls-connections-to-aws-service-endpoints/") (AWS blog)
* [How Arctic Wolf uses AWS CloudTrail Lake to Simplify Security and Operations](https://aws.amazon.com/blogs/mt/how-arctic-wolf-uses-aws-cloudtrail-lake-to-simplify-security-and-operations/ "https://aws.amazon.com/blogs/mt/how-arctic-wolf-uses-aws-cloudtrail-lake-to-simplify-security-and-operations/") (AWS blog)
* [CloudTrail Lake FAQs](https://aws.amazon.com/cloudtrail/faqs/#CloudTrail_Lake "https://aws.amazon.com/cloudtrail/faqs/#CloudTrail_Lake")
* [AWS CloudTrail API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md")
* [AWS CloudTrail Data API Reference](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/Welcome.html")
* [AWS CloudTrail Partner Onboarding Guide](https://docs.aws.amazon.com/awscloudtrail/latest/partner-onboarding/cloudtrail-lake-partner-onboarding.html "https://docs.aws.amazon.com/awscloudtrail/latest/partner-onboarding/cloudtrail-lake-partner-onboarding.html")
