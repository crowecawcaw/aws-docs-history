**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Query Amazon Pinpoint analytics data for campaigns

In addition to using the analytics pages on the Amazon Pinpoint console, you can use Amazon Pinpoint
Analytics APIs to query analytics data for a subset of standard metrics that provide insight
into delivery and engagement trends for campaigns.

Each of these metrics is a measurable value, also referred to as a _key performance indicator (KPI)_, that can help you monitor and assess the
performance of one or more campaigns. For example, you can use a metric to find out how many
endpoints a campaign message was sent to, or how many of those messages were delivered to the
intended endpoints.

Amazon Pinpoint automatically collects and aggregates this data for all of your campaigns. It stores
the data for 90 days. If you integrated a mobile app with Amazon Pinpoint by using an AWS Mobile SDK,
Amazon Pinpoint extends this support to include additional metrics, such as the percentage of push
notifications that were opened by recipients. For information about integrating a mobile app,
see [Integrate Amazon Pinpoint with your application](integrate.md "integrate.md").

If you use Amazon Pinpoint Analytics APIs to query data, you can choose various options that define
the scope, data, grouping, and filters for your query. You do this by using parameters that
specify the project, campaign, and metric that you want to query, in addition to any date-based
filters that you want to apply.

This topic explains and provides examples of how to choose these options and query the data
for one or more campaigns.

## Prerequisites

Before you query analytics data for one or more campaigns, it helps to gather the
following information, which you use to define your query:

- **Project ID** – The unique identifier for the
  project that’s associated with the campaign or campaigns. In the Amazon Pinpoint API, this value is
  stored in the `application-id` property. On the Amazon Pinpoint console, this value is
  displayed as the **Project ID** on the **All projects**
  page.
- **Campaign ID** – The unique identifier for the
  campaign, if you want to query the data for only one campaign. In the Amazon Pinpoint API, this
  value is stored in the `campaign-id` property. This value is not displayed on
  the console.
- **Date range** – Optionally, the first and last
  date and time of the date range to query data for. Date ranges are inclusive and must be
  limited to 31 or fewer calendar days. In addition, they must start fewer than 90 days from
  the current day. If you don’t specify a date range, Amazon Pinpoint automatically queries the data
  for the preceding 31 calendar days.
- **Metric type** – The type of metric to query.
  There are two types, _application metrics_ and _campaign metrics_. An _application
  metric_ provides data for all the campaigns that are associated with a
  project, also referred to as an _application_. A
  _campaign metric_ provides data for only one
  campaign.
- **Metric** – The name of the metric to query—more
  specifically, the `kpi-name` value for the metric. For a complete list of
  supported metrics and the `kpi-name` value for each one, see [Standard metrics for projects, campaigns, and journeys](analytics-standard-metrics.md "analytics-standard-metrics.md").

It also helps to determine whether you want to group the data by a relevant field. If you
do, you can simplify your analysis and reporting by choosing a metric that’s designed to group
data for you automatically. For example, Amazon Pinpoint provides several standard metrics that report
the percentage of messages that were delivered to recipients of a campaign. One of these
metrics automatically groups the data by date
(`successful-delivery-rate-grouped-by-date`). Another metric automatically groups
the data by campaign run (`successful-delivery-rate-grouped-by-campaign-activity`).
A third metric simply returns a single value—the percentage of messages that were
delivered to recipients by all campaign runs (`successful-delivery-rate`).

If you can't find a standard metric that groups data the way that you want, you can
develop a series of queries that return the data that you want. You can then manually break
down or combine the query results into custom groups that you design.

Finally, it’s important to verify that you’re authorized to access the data that you want
to query. For more information, see [IAM policies for querying Amazon Pinpoint analytics
data](analytics-permissions.md "analytics-permissions.md").
