**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Query Amazon Pinpoint data for transactional email

messages

To query the data for transactional email messages that were sent for a project, you use
the [Application
Metrics](../apireference/apps-application-id-kpis-daterange-kpi-name.md "../apireference/apps-application-id-kpis-daterange-kpi-name.md") API and specify values for the following required parameters:

- **application-id** – The project ID, which is the
  unique identifier for the project. In Amazon Pinpoint, the terms _project_ and _application_ have the same
  meaning.
- **kpi-name** – The name of the metric to query.
  This value describes the associated metric and consists of two or more terms, which are
  comprised of lowercase alphanumeric characters, separated by a hyphen. For a complete list
  of supported metrics and the `kpi-name` value for each one, see [Standard metrics for projects, campaigns, and journeys](analytics-standard-metrics.md "analytics-standard-metrics.md").
  You can also apply a filter that queries the data for a specific date range. If you don’t
  specify a date range, Amazon Pinpoint returns the data for the preceding 31 calendar days. To filter the
  data by different dates, use the supported date range parameters to specify the first and last
  date and time of the date range. The values should be in extended ISO 8601 format and use
  Coordinated Universal Time (UTC)—for example, `2019-09-06T20:00:00Z` for
  8:00 PM UTC September 6, 2019. Date ranges are inclusive and must be limited to 31 or fewer
  calendar days. In addition, the first date and time must be fewer than 90 days from the current
  day.

The following examples show how to query analytics data for transactional email messages
by using the Amazon Pinpoint REST API, the AWS CLI, and the AWS SDK for Java. You can use any supported AWS
SDK to query analytics data for transactional messages. The AWS CLI examples are formatted for
Microsoft Windows. For Unix, Linux, and macOS, replace the caret (^) line-continuation
character with a backslash (\).

REST API
To query analytics data for transactional email messages by using the Amazon Pinpoint REST
API, send an HTTP(S) GET request to the [Application
Metrics](../apireference/apps-application-id-kpis-daterange-kpi-name.md "../apireference/apps-application-id-kpis-daterange-kpi-name.md") URI. In the URI, specify the appropriate values for the required path
parameters:

```
https://`endpoint`/v1/apps/`application-id`/kpis/daterange/`kpi-name`
```

Where:

- `endpoint` is the Amazon Pinpoint endpoint for the AWS Region
  that hosts the project.
- `application-id` is the unique identifier for the
  project.
- `kpi-name` is the `kpi-name` value for the
  metric to query.

All the parameters should be URL encoded.

To apply a filter that queries the data for a specific date range, append the
`start-time` and `end-time` query parameters and values to the
URI. By using these parameters, you can specify the first and last date and time, in
extended ISO 8601 format, of an inclusive date range to retrieve the data for. Use an
ampersand (&) to separate the parameters.

For example, the following request retrieves the number of transactional email
messages that were sent for a project from September 6, 2019 through September 13,
2019:

```
https://pinpoint.us-east-1.amazonaws.com/v1/apps/1234567890123456789012345example/kpis/daterange/txn-emails-sent?start-time=2019-09-06T00:00:00Z&end-time=2019-09-13T23:59:59Z
```

Where:

- `pinpoint.us-east-1.amazonaws.com` is the Amazon Pinpoint endpoint for the
  AWS Region that hosts the project.
- `1234567890123456789012345example` is the unique identifier for the
  project.
- `txn-emails-sent` is the `kpi-name` value for the
  _sends_ application metric, which is the metric that reports
  the number of transactional email messages that were sent for a project.
- `2019-09-06T00:00:00Z` is the first date and time to retrieve data
  for, as part of an inclusive date range.
- `2019-09-13T23:59:59Z` is the last date and time to retrieve data
  for, as part of an inclusive date range.

AWS CLI
To query analytics data for transactional email messages by using the AWS CLI, use the
**get-application-date-range-kpi** command, and specify the appropriate
values for the required parameters:

```
`C:\>` `aws pinpoint get-application-date-range-kpi ^
 --application-id `application-id` ^
 --kpi-name `kpi-name``
```

Where:

- `application-id` is the unique identifier for the
  project.
- `kpi-name` is the `kpi-name` value for the
  metric to query.

To apply a filter that queries the data for a specific date range, add the
`start-time` and `end-time` parameters and values to your query.
By using these parameters, you can specify the first and last date and time, in extended
ISO 8601 format, of an inclusive date range to retrieve the data for. For example, the
following request retrieves the number of transactional email messages that were sent
for a project from September 6, 2019 through September 13, 2019:

```
`C:\>` `aws pinpoint get-application-date-range-kpi ^
 --application-id 1234567890123456789012345example ^
 --kpi-name txn-emails-sent ^
 --start-time 2019-09-06T00:00:00Z ^
 --end-time 2019-09-13T23:59:59Z`
```

Where:

- `1234567890123456789012345example` is the unique identifier for the
  project.
- `txn-emails-sent` is the `kpi-name` value for the
  _sends_ application metric, which is the metric that reports
  the number of transactional email messages that were sent for a project.
- `2019-09-06T00:00:00Z` is the first date and time to retrieve data
  for, as part of an inclusive date range.
- `2019-09-13T23:59:59Z` is the last date and time to retrieve data
  for, as part of an inclusive date range.

SDK for Java
To query analytics data for transactional email messages by using the AWS SDK for Java,
use the **GetApplicationDateRangeKpiRequest** method of the [Application
Metrics](../apireference/apps-application-id-kpis-daterange-kpi-name.md "../apireference/apps-application-id-kpis-daterange-kpi-name.md") API. Specify the appropriate values for the required
parameters:

```
GetApplicationDateRangeKpiRequest request = new GetApplicationDateRangeKpiRequest()
        .withApplicationId("`applicationId`")
        .withKpiName("`kpiName`")
```

Where:

- `applicationId` is the unique identifier for the
  project.
- `kpiName` is the `kpi-name` value for the
  metric to query.

To apply a filter that queries the data for a specific date range, include the
`startTime` and `endTime` parameters and values in your query.
By using these parameters, you can specify the first and last date and time, in extended
ISO 8601 format, of an inclusive date range to retrieve the data for. For example, the
following request retrieves the number of transactional email messages that were sent
for a project from September 6, 2019 through September 13, 2019:

```
GetApplicationDateRangeKpiRequest request = new GetApplicationDateRangeKpiRequest()
        .withApplicationId("1234567890123456789012345example")
        .withKpiName("txn-emails-sent")
        .withStartTime(Date.from(Instant.parse("2019-09-06T00:00:00Z")))
        .withEndTime(Date.from(Instant.parse("2019-09-13T23:59:59Z")));
```

Where:

- `1234567890123456789012345example` is the unique identifier for the
  project.
- `txn-emails-sent` is the `kpi-name` value for the
  _sends_ application metric, which is the metric that reports
  the number of transactional email messages that were sent for a project.
- `2019-09-06T00:00:00Z` is the first date and time to retrieve data
  for, as part of an inclusive date range.
- `2019-09-13T23:59:59Z` is the last date and time to retrieve data
  for, as part of an inclusive date range.

After you send your query, Amazon Pinpoint returns the query results in a JSON response. The
structure of the results varies depending on the metric that you queried. Some metrics return
only one value. For example, the _sends_
(`txn-emails-sent`) application metric, which is used in the preceding examples,
returns one value—the number of transactional email messages that were sent from a
project. In this case, the JSON response is the following:

```
{
    "ApplicationDateRangeKpiResponse":{
        "ApplicationId":"1234567890123456789012345example",
        "EndTime":"2019-09-13T23:59:59Z",
        "KpiName":"txn-emails-sent",
        "KpiResult":{
            "Rows":[
                {
                    "Values":[
                        {
                            "Key":"TxnEmailsSent",
                            "Type":"Double",
                            "Value":"62.0"
                        }
                    ]
                }
            ]
        },
        "StartTime":"2019-09-06T00:00:00Z"
    }
}
```

Other metrics return multiple values and group the values by a relevant field. If a metric
returns multiple values, the JSON response includes a field that indicates which field was
used to group the data.

To learn more about the structure of query results, see [Use JSON query results](analytics-query-results.md "analytics-query-results.md").
