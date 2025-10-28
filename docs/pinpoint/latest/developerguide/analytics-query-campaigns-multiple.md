**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Query Amazon Pinpoint data for multiple

campaigns

There are two ways to query the data for multiple campaigns. The best way depends on
whether you want to query the data for campaigns that are all associated with the same
project. If you do, it also depends on whether you want to query the data for all or only or
subset of those campaigns.

To query the data for campaigns that are associated with different projects or for only a
subset of the campaigns that are associated with the same project, the best approach is to
create and run a series of individual queries, one for each campaign that you want to query
the data for. The preceding section explains how to query the data for only one
campaign.

To query the data for all the campaigns that are associated with the same project, you can
use the [Application
Metrics](../apireference/apps-application-id-kpis-daterange-kpi-name.md "../apireference/apps-application-id-kpis-daterange-kpi-name.md") API. Specify values for the following required parameters:

- **application-id** – The project ID, which is the
  unique identifier for the project. In Amazon Pinpoint, the terms _project_ and _application_ have the same
  meaning.
- **kpi-name** – The name of the metric to query.
  This value describes the associated metric and consists of two or more terms, which are
  comprised of lowercase alphanumeric characters, separated by a hyphen. For a complete list
  of supported metrics and the `kpi-name` value for each one, see [Standard metrics for projects, campaigns, and journeys](analytics-standard-metrics.md "analytics-standard-metrics.md").
  You can also filter the data by date range. If you don’t specify a date range, Amazon Pinpoint
  returns the data for the preceding 31 calendar days. To filter the data by different dates,
  use the supported date range parameters to specify the first and last date and time of the
  date range. The values should be in extended ISO 8601 format and use Coordinated Universal
  Time (UTC)—for example, `2019-07-19T20:00:00Z` for 8:00 PM UTC July 19,

2019. Date ranges are inclusive and must be limited to 31 or fewer calendar days. In addition,
      the first date and time must be fewer than 90 days from the current day.

The following examples show how to query analytics data for a campaign by using the Amazon Pinpoint
REST API, the AWS CLI, and the AWS SDK for Java. You can use any supported AWS SDK to query
analytics data for a campaign. The AWS CLI examples are formatted for Microsoft Windows. For
Unix, Linux, and macOS, replace the caret (^) line-continuation character with a backslash
(\).

REST API
To query analytics data for multiple campaigns by using the Amazon Pinpoint REST API, send an
HTTP(S) GET request to the [Application
Metrics](../apireference/apps-application-id-kpis-daterange-kpi-name.md "../apireference/apps-application-id-kpis-daterange-kpi-name.md") URI. In the URI, specify the appropriate values for the required path
parameters:

```
https://`endpoint`/v1/apps/`application-id`/kpis/daterange/`kpi-name`
```

Where:

- `endpoint` is the Amazon Pinpoint endpoint for the AWS Region
  that hosts the project associated with the campaigns.
- `application-id` is the unique identifier for the
  project that’s associated with the campaigns.
- `kpi-name` is the `kpi-name` value for the
  metric to query.

All the parameters should be URL encoded.

To apply a filter that retrieves the data for a specific date range, append the
`start-time` and `end-time` query parameters and values to the
URI. By using these parameters, you can specify the first and last date and time, in
extended ISO 8601 format, of an inclusive date range to retrieve the data for. Use an
ampersand (&) to separate the parameters.

For example, the following request retrieves the number of unique endpoints that
messages were delivered to, by each of a project's campaigns, from July 19, 2019 through
July 26, 2019:

```
https://pinpoint.us-east-1.amazonaws.com/v1/apps/1234567890123456789012345example/kpis/daterange/unique-deliveries-grouped-by-campaign?start-time=2019-07-19T00:00:00Z&end-time=2019-07-26T23:59:59Z
```

Where:

- `pinpoint.us-east-1.amazonaws.com` is the Amazon Pinpoint endpoint for the
  AWS Region that hosts the project.
- `1234567890123456789012345example` is the unique identifier for the
  project that’s associated with the campaigns.
- `unique-deliveries-grouped-by-campaign` is the `kpi-name`
  value for the _endpoint deliveries, grouped by campaign_
  application metric, which is the metric that returns the number of unique endpoints
  that messages were delivered to, by each campaign.
- `2019-07-19T00:00:00Z` is the first date and time to retrieve data
  for, as part of an inclusive date range.
- `2019-07-26T23:59:59Z` is the last date and time to retrieve data
  for, as part of an inclusive date range.

AWS CLI
To query analytics data for multiple campaigns by using the AWS CLI, use the
**get-application-date-range-kpi** command and specify the appropriate
values for the required parameters:

```
`C:\>` `aws pinpoint get-application-date-range-kpi ^
 --application-id `application-id` ^
 --kpi-name `kpi-name``
```

Where:

- `application-id` is the unique identifier for the
  project that’s associated with the campaigns.
- `kpi-name` is the `kpi-name` value for the
  metric to query.

To apply a filter that retrieves the data for a specific date range, include the
`start-time` and `end-time` parameters and values in your query.
By using these parameters, you can specify the first and last date and time, in extended
ISO 8601 format, of an inclusive date range to retrieve the data for. For example, the
following request retrieves the number of unique endpoints that messages were delivered
to, by each of a project's campaigns, from July 19, 2019 through July 26, 2019:

```
`C:\>` `aws pinpoint get-application-date-range-kpi ^
 --application-id 1234567890123456789012345example ^
 --kpi-name unique-deliveries-grouped-by-campaign ^
 --start-time 2019-07-19T00:00:00Z ^
 --end-time 2019-07-26T23:59:59Z`
```

Where:

- `1234567890123456789012345example` is the unique identifier for the
  project that’s associated with the campaign.
- `unique-deliveries-grouped-by-campaign` is the `kpi-name`
  value for the _endpoint deliveries, grouped by
  campaign_ application metric, which is the metric that returns the
  number of unique endpoints that messages were delivered to, by each campaign.
- `2019-07-19T00:00:00Z` is the first date and time to retrieve data
  for, as part of an inclusive date range.
- `2019-07-26T23:59:59Z` is the last date and time to retrieve data
  for, as part of an inclusive date range.

SDK for Java
To query analytics data for multiple campaigns by using the AWS SDK for Java, use the
**GetApplicationDateRangeKpiRequest** method of the [Application
Metrics](../apireference/apps-application-id-kpis-daterange-kpi-name.md "../apireference/apps-application-id-kpis-daterange-kpi-name.md") API. Specify the appropriate values for the required
parameters:

```
GetApplicationDateRangeKpiRequest request = new GetApplicationDateRangeKpiRequest()
        .withApplicationId("`applicationId`")
        .withKpiName("`kpiName`")
```

Where:

- `applicationId` is the unique identifier for the
  project that’s associated with the campaigns.
- `kpiName` is the `kpi-name` value for the
  metric to query.

To apply a filter that retrieves the data for a specific date range, include the
`startTime` and `endTime` parameters and values in your query.
By using these parameters, you can specify the first and last date and time, in extended
ISO 8601 format, of an inclusive date range to retrieve the data for. For example, the
following request retrieves the number of unique endpoints that messages were delivered
to, by each of a project's campaigns, from July 19, 2019 through July 26, 2019:

```
GetApplicationDateRangeKpiRequest request = new GetApplicationDateRangeKpiRequest()
        .withApplicationId("1234567890123456789012345example")
        .withKpiName("unique-deliveries-grouped-by-campaign")
        .withStartTime(Date.from(Instant.parse("2019-07-19T00:00:00Z")))
        .withEndTime(Date.from(Instant.parse("2019-07-26T23:59:59Z")));
```

Where:

- `1234567890123456789012345example` is the unique identifier for the
  project that’s associated with the campaigns.
- `unique-deliveries-grouped-by-campaign` is the `kpi-name`
  value for the _endpoint deliveries, grouped by
  campaign_ application metric, which is the metric that returns the
  number of unique endpoints that messages were delivered to, by each campaign.
- `2019-07-19T00:00:00Z` is the first date and time to retrieve data
  for, as part of an inclusive date range.
- `2019-07-26T23:59:59Z` is the last date and time to retrieve data
  for, as part of an inclusive date range.

After you send your query, Amazon Pinpoint returns the query results in a JSON response. The
structure of the results varies depending on the metric that you queried. Some metrics return
only one value. Other metrics return multiple values, and those values are grouped by a
relevant field. If a metric returns multiple values, the JSON response includes a field that
indicates which field was used to group the data.

For example, the _endpoint deliveries, grouped by
campaign_ (`unique-deliveries-grouped-by-campaign`) application metric,
which is used in the preceding examples, returns multiple values—the number of unique
endpoints that messages were delivered to, for each campaign that's associated with a project.
In this case, the JSON response is the following:

```
{
    "ApplicationDateRangeKpiResponse":{
        "ApplicationId":"1234567890123456789012345example",
        "EndTime":"2019-07-26T23:59:59Z",
        "KpiName":"unique-deliveries-grouped-by-campaign",
        "KpiResult":{
            "Rows":[
                {
                    "GroupedBys":[
                        {
                            "Key":"CampaignId",
                            "Type":"String",
                            "Value":"80b8efd84042ff8d9c96ce2f8example"
                        }
                    ],
                    "Values":[
                        {
                            "Key":"UniqueDeliveries",
                            "Type":"Double",
                            "Value":"123.0"
                        }
                    ]
                },
                {
                    "GroupedBys":[
                        {
                            "Key":"CampaignId",
                            "Type":"String",
                            "Value":"810c7aab86d42fb2b56c8c966example"
                        }
                    ],
                    "Values":[
                        {
                            "Key":"UniqueDeliveries",
                            "Type":"Double",
                            "Value":"456.0"
                        }
                    ]
                },
                {
                    "GroupedBys":[
                        {
                            "Key":"CampaignId",
                            "Type":"String",
                            "Value":"42d8c7eb0990a57ba1d5476a3example"
                        }
                    ],
                    "Values":[
                        {
                            "Key":"UniqueDeliveries",
                            "Type":"Double",
                            "Value":"789.0"
                        }
                    ]
                }
            ]
        },
        "StartTime":"2019-07-19T00:00:00Z"
    }
}
```

In this case, the `GroupedBys` field indicates that the values are grouped by
campaign ID (`CampaignId`).

To learn more about the structure of query results, see [Use JSON query results](analytics-query-results.md "analytics-query-results.md").
