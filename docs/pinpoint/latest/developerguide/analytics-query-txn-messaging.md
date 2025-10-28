**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Query Amazon Pinpoint analytics data for transactional

messages

In addition to using the analytics pages on the Amazon Pinpoint console, you can use Amazon Pinpoint
Analytics APIs to query analytics data for a subset of standard metrics that provide insight
into delivery and engagement trends for the transactional messages that were sent for a project.

Each of these metrics is a measurable value, also referred to as a _key performance indicator (KPI)_, that can help you monitor and assess the
performance of transactional messages. For example, you can use a metric to find out how many
transactional email or SMS messages you sent, or how many of those messages were delivered to
recipients. Amazon Pinpoint automatically collects and aggregates this data for all the transactional
email and SMS messages that you send for a project. It stores the data for 90 days.

If you use Amazon Pinpoint Analytics APIs to query data, you can choose various options that define
the scope, data, grouping, and filters for your query. You do this by using parameters that
specify the project and metric that you want to query, in addition to any date-based filters
that you want to apply.

This topic explains and provides examples of how to choose these options and query
transactional messaging data for a project.

## Prerequisites

Before you query analytics data for transactional messages, it helps to gather the
following information, which you use to define your query:

- **Project ID** – The unique identifier for the
  project that the messages were sent from. In the Amazon Pinpoint API, this value is stored in the
  `application-id` property. On the Amazon Pinpoint console, this value is displayed as
  the **Project ID** on the **All projects** page.
- **Date range** – Optionally, the first and last
  date and time of the date range to query data for. Date ranges are inclusive and must be
  limited to 31 or fewer calendar days. In addition, they must start fewer than 90 days from
  the current day. If you don’t specify a date range, Amazon Pinpoint automatically queries the data
  for the preceding 31 calendar days.
- **Metric** – The name of the metric to query—more
  specifically, the `kpi-name` value for the metric. For a complete list of
  supported metrics and the `kpi-name` value for each one, see [Standard metrics for projects, campaigns, and journeys](analytics-standard-metrics.md "analytics-standard-metrics.md").

It also helps to determine whether you want to group the data by a relevant field. If you
do, you can simplify your analysis and reporting by choosing a metric that’s designed to group
data for you automatically. For example, Amazon Pinpoint provides several standard metrics that report
the number of transactional SMS messages that were delivered to recipients. One of these
metrics automatically groups the data by date
(`txn-sms-delivered-grouped-by-date`). Another metric automatically groups the data
by country or region (`txn-sms-delivered-grouped-by-country`). A third metric
simply returns a single value—the number of messages that were delivered to recipients
(`txn-sms-delivered`). If you can't find a standard metric that groups data the
way that you want, you can develop a series of queries that return the data that you want. You
can then manually break down or combine the query results into custom groups that you
design.

Finally, it’s important to verify that you’re authorized to access the data that you want
to query. For more information, see [IAM policies for querying Amazon Pinpoint analytics
data](analytics-permissions.md "analytics-permissions.md").
