# Use the Internet Monitor query interface

An option for understanding more about internet traffic for your AWS application is to use the Internet Monitor
_query interface_. To use the query interface, you create a query with data filters that
you choose, and then run the query to return a subset of your Internet Monitor data. Exploring the data that the query
returns can give you insights into how your application is performing on the internet.

You can query and explore all the metrics that Internet Monitor captures with your monitor, including availability and performance
scores, bytes transferred, round-trip times, and time to first byte (TTFB).

Internet Monitor uses the query interface to provide the data that you can explore in the Internet Monitor console dashboard.
By using search options in the dashboard—on the **Analyze** page
or the **Optimize** page—you can query and filter internet data for your application.

If you'd like more flexibility to explore and filter your data than the dashboard provides, you can use the query interface yourself,
by using Internet Monitor API operations with the AWS Command Line Interface or with an AWS SDK. This section introduces the types of queries that you can use
with the query interface, and the filters that you can specify to create a subset of data, to get insights about internet traffic
for your application.

###### Topics

- [How to use the query interface](#CloudWatch-IM-view-cw-tools-cwim-query-use-query "#CloudWatch-IM-view-cw-tools-cwim-query-use-query")
- [Query examples](#CloudWatch-IM-view-cw-tools-cwim-query-example-queries "#CloudWatch-IM-view-cw-tools-cwim-query-example-queries")
- [Get query results](#CloudWatch-IM-view-cw-tools-cwim-query-get-data "#CloudWatch-IM-view-cw-tools-cwim-query-get-data")
- [Troubleshooting](#CloudWatch-IM-view-cw-tools-cwim-query-troubleshooting "#CloudWatch-IM-view-cw-tools-cwim-query-troubleshooting")

## How to use the query interface

You create a query with the query interface by choosing a _query type_,
and then specifying filter values, to return a specific desired subset of your log file data. Then, you can work
with the data subset, to further filter and sort, create reports, and so on.

The query process works like this:

1. When you run a query, Internet Monitor returns a `query ID` that
   is unique to the query. This section describes the query types that are available, and options for filtering data in queries.
   To understand how this works, you can also review the section on [query examples](#IMQueryInterfaceExamples "#IMQueryInterfaceExamples").
2. You specify the query ID with your monitor name with the [GetQueryResults](../../../internet-monitor/latest/api/API_GetQueryResults.md "../../../internet-monitor/latest/api/API_GetQueryResults.md") API operation to return data
   results for the query. Each query type returns a different set of data fields. To learn more, see [Get query results](#IMGetQueryData "#IMGetQueryData").

The query interface provides the following query types. Each query type returns a different set
of information about your traffic from the log files, as shown.

- **Measurements:** Provides availability score, performance score, total traffic,
  and round-trip times, at 5 minute intervals.
- **Top locations:** Provides availability score, performance score, total traffic,
  and time to first byte (TTFB) information, for the top location and ASN combinations that you're monitoring, by traffic volume.
- **Top locations details:** Provides TTFB for Amazon CloudFront, your
  current configuration, and the best performing Amazon EC2 configuration, at 1 hour intervals.
- **Overall traffic suggestions:** Provides TTFB, using a 30-day weighted average,
  for all traffic in each AWS location that is monitored.
- **Overall traffic suggestions details:** Provides TTFB, using a 30-day weighted
  average, for each top location, for a proposed AWS location.
- **Routing suggestions:** Provides the predicted average round-trip time (RTT)
  from an IP prefix toward an AWS location for a DNS resolver. The RTT is calculated at one hour intervals,
  over a one hour period.

You can filter the data more by using specific criteria. With most query types, except routing suggestions, you can filter by
specifying one or more of the following criteria:

- **AWS location:** For AWS location, you can specify CloudFront or an AWS Region, such as
  `us-east-2`.
- **ASN:** Specify the autonomous system number (ASN) of a
  DNS resolver (typically, an ISP), for example, 4225.
- **Client location:** For location, specify a city, metro, subdivision, or country.
- **Proposed AWS location:** Specify an AWS Region, such as `us-east-2`,
  or an AWS Local Zone. You can use this filter with the overall traffic suggestions details query type.
- **Geo:** Specify `geo` for some queries. This is required for queries that use
  the `Top locations` query type, but not allowed for other query types. To understand when to specify `geo`
  for filter parameters, see the [query examples](#IMQueryInterfaceExamples "#IMQueryInterfaceExamples") section.

For the routing suggestions query type, you can filter the data more by specifying one or more of the following criteria:

- **Current AWS location:** Specify an AWS Region, such as `us-east-2`.
- **Proposed AWS location:** Specify an AWS Region, such as `us-east-2`,
  or an AWS Local Zone.
- **IPv4 prefix:** Specify an IPv4 prefix in the standard format, similar to `192.0.2.0/24`.
- **Monitor ARN:** Specify the ARN for a specific monitor.
- **DNS resolver IP:** Specify the IP address of a DNS resolver.
- **DNS resolver ISP:** Specify the name of a DNS resolver (typically an ISP), for example,
  `Cloudflare`.
- **DNS resolver ASN:** Specify the autonomous system number (ASN) of a
  DNS resolver, for example, 4225.

The operators that you can use for filtering your data are `EQUALS` and `NOT_EQUALS`. For details
about filtering parameters, see the
[FilterParameter](../../../internet-monitor/latest/api/API_FilterParameter.md "../../../internet-monitor/latest/api/API_FilterParameter.md") API operation.

To see details about the query interface operations, see the following API operations in the Internet Monitor API Reference Guide:

- To create and run a query, see the
  [StartQuery](../../../internet-monitor/latest/api/API_StartQuery.md "../../../internet-monitor/latest/api/API_StartQuery.md") API operation.
- To stop a query, see the
  [StopQuery](../../../internet-monitor/latest/api/API_StopQuery.md "../../../internet-monitor/latest/api/API_StopQuery.md") API operation.
- To return data for a query that you've created, see the
  [GetQueryResults](../../../internet-monitor/latest/api/API_GetQueryResults.md "../../../internet-monitor/latest/api/API_GetQueryResults.md") API operation.
- To retrieve the status of a query, see the
  [GetQueryStatus](../../../internet-monitor/latest/api/API_GetQueryStatus.md "../../../internet-monitor/latest/api/API_GetQueryStatus.md") API operation.

## Query examples

To create a query that you can use to retrieve a filtered set of data
from your monitor's log file, you use the [StartQuery](../../../internet-monitor/latest/api/API_StartQuery.md "../../../internet-monitor/latest/api/API_StartQuery.md")
API operation. You specify a query type and filter parameters for the query. Then, when you use the Internet Monitor query
interface API operation to get query results using the query, it will retrieve the subset of your data that you want to work with.

To illustrate how query types and filter parameters work, let's look at some examples.

**Example 1**

Let's say that you want to retrieve all of your monitor's log file data for a specific country, except for one city. The following
example shows filter parameters for a query that you could create with the `StartQuery` operation for this scenario.

```
{
   MonitorName: "TestMonitor"
   StartTime: "2023-07-12T20:00:00Z"
   EndTime: "2023-07-12T21:00:00Z"
   QueryType: "MEASUREMENTS"
   FilterParameters: [
      {
       Field: "country",
       Operator: "EQUALS",
       Values: ["Germany"]
      },
      {
       Field: "city",
       Operator: "NOT_EQUALS",
       Values: ["Berlin"]
      },
    ]
}
```

**Example 2**

As another example, let's say that you want to see your top locations by metropolitan area. You could use the following
example query for this scenario.

```
{
   MonitorName: "TestMonitor"
   StartTime: "2023-07-12T20:00:00Z"
   EndTime: "2023-07-12T21:00:00Z"
   QueryType: "TOP_LOCATIONS"
   FilterParameters: [
      {
       Field: "geo",
       Operator: "EQUALS",
       Values: ["metro"]
      },
    ]
}
```

**Example 3**

Now, let's say that you want to see the top city-network combinations in the Los Angeles metro area.
To do this, specify `geo=city`, and then set `metro` to Los Angeles.
Now, the query returns the top city-networks in the Los Angeles metro area instead of the top metro+networks overall.

Here's the example query that you could use:

```
{
   MonitorName: "TestMonitor"
   StartTime: "2023-07-12T20:00:00Z"
   EndTime: "2023-07-12T21:00:00Z"
   QueryType: "TOP_LOCATIONS"
   FilterParameters: [
      {
       Field: "geo",
       Operator: "EQUALS",
       Values: ["city"]
      },
      {
       Field: "metro",
       Operator: "EQUALS",
       Values: ["Los Angeles"]
      }
    ]
}
```

**Example 4**

Next, let's say that you want to retrieve TTFB data for a specific subdivision (for example, a U.S. state).

The following is an example query for this scenario:

```
{
   MonitorName: "TestMonitor"
   StartTime: "2023-07-12T20:00:00Z"
   EndTime: "2023-07-12T21:00:00Z"
   QueryType: "TOP_LOCATION_DETAILS"
   FilterParameters: [
      {
       Field: "subdivision",
       Operator: "EQUALS",
       Values: ["California"]
      },
    ]
}
```

**Example 5**

Now, let's say that you want to retrieve TTFB data for every location where your application has client traffic.

The following is an example query for this scenario:

```
{
   MonitorName: "TestMonitor"
   StartTime: "2023-07-12T20:00:00Z"
   EndTime: "2023-07-12T21:00:00Z"
   QueryType: "OVERALL_TRAFFIC_SUGGESTIONS"
   FilterParameters: []
}

Results:
[us-east-1, 40, us-west-2, 30],
[us-east-1, 40, us-west-1, 35],
[us-east-1, 40, us-east-1, 44],
[us-east-1, 40, CloudFront, 22],
...
[us-east-2, 44, us-west-2, 30],
[us-east-2, 44, us-west-1, 35],
...
```

**Example 6**

Let's say that you want to retrieve TTFB data for a specific new AWS Region.

The following is an example query for this scenario:

```
{
   MonitorName: "TestMonitor"
   StartTime: "2023-07-12T20:00:00Z"
   EndTime: "2023-07-12T21:00:00Z"
   QueryType: "OVERALL_TRAFFIC_SUGGESTIONS_DETAILS"
   FilterParameters: [
      {
       Field: "proposed_aws_location",
       Operator: "EQUALS",
       Values: ["us-west-2"]
      },
   ]
}

Results:
[San Jose, San Jose-Santa Clara, California, United States, 7922, us-east-1, 40, 350, 350, us-west-2, 45]
[San Jose, San Jose-Santa Clara, California, United States, 7922, us-west-1, 35, 450, 450, us-west-2, 45]
```

**Example 7**

A final example is to retrieve data for specific DNS resolvers.

The following is an example query for this scenario:

```
{
   MonitorName: "TestMonitor"
   StartTime: "2023-07-12T20:00:00Z"
   EndTime: "2023-07-12T21:00:00Z"
   QueryType: "ROUTING_SUGGESTIONS"
   FilterParameters: [
      {
       Field: "proposed_aws_location",
       Operator: "EQUALS",
       Values: ["us-east-1"]
      },
   ]
}

Results:
[162.158.180.245, 13335, Cloudflare, [5.4.0.0/14], us-east-2, 200.0, us-east-1, 160.0]
[162.158.180.243, 13313, Cloudflare, [5.4.0.0/10], us-east-2, 150.0, us-east-1, 125.0]
```

## Get query results

After you define a query, you can return a set of results with the query
by running another Internet Monitor API operation, [GetQueryResults](../../../internet-monitor/latest/api/API_GetQueryResults.md "../../../internet-monitor/latest/api/API_GetQueryResults.md").
When you run `GetQueryResults`, you specify the query ID for the query that you've defined, along with the name of
your monitor. `GetQueryResults` retrieves data for the specified query into a result set.

When you run a query, make sure that the query has finished running before you use `GetQueryResults` to look at the results. You can
determine if the query has completed by using the [GetQueryStatus](../../../internet-monitor/latest/api/API_GetQueryStatus.md "../../../internet-monitor/latest/api/API_GetQueryStatus.md") API operation. When the `Status` for the query is `SUCCEEDED`, you can go ahead with reviewing the
results.

When your query completes, you can use the following information to help you review the results. Each query type that you use to create a query
includes a unique set of data fields from the log files, as described in the following list:

**Measurements**
The `measurements` query type returns the following data:

`timestamp, availability, performance, bytes_in, bytes_out, rtt_p50, rtt_p90, rtt_p95`

**Top locations**
The `top locations` query type groups data by location, and provides the data
averaged over the time period. The data that it returns includes the following:

`aws_location, city, metro, subdivision, country, asn, availability, performance,
 bytes_in, bytes_out, current_fbl, best_ec2, best_ec2_region, best_cf_fbl`

Note that `city`, `metro`, and `subdivision` are only returned if
you choose that location type for the `geo` field. The following location fields are returned,
depending on the location type that you specify for `geo`:

```
city = city, metro, subdivision, country
metro = metro, subdivision, country
subdivision = subdivision, country
country = country
```

**Top locations details**
The `top locations details` query type returns data grouped hour by hour. The
query returns the following data:

`timestamp, current_service, current_fbl, best_ec2_fbl, best_ec2_region, best_cf_fbl`

**Overall traffic suggestions**
The `overall traffic suggestions` query type returns data grouped hour by hour. The
query returns the following data:

`current_aws_location, proposed_aws_location, average_fbl, traffic, optimized_traffic_excluding_cf, 
 optimized_traffic_including_cf`

**Overall traffic suggestions details**
The `overall traffic suggestions details` query type returns data grouped hour by hour. The
query returns the following data:

`aws_location, city, metro, subdivision, country, asn, traffic, current_aws_location, fbl_data`

**Routing suggestions**
The `routing suggestions` query type returns data grouped hour by hour. The
query returns the following data:

`dns_resolver_ip, dns_resolver_asn, dns_resolver_isp, ipv4_prefixes, current_aws_location, current_latency, 
 proposed_aws_location, proposed_latency`

When you run the `GetQueryResults` API operation, Internet Monitor returns the following in the response:

- A _data string array_ that contains the results that the query returns. The information
  is returned in arrays that are aligned with the `Fields` field, also returned by the API call. Using
  the `Fields` field, you can parse the information from the `Data` repository and then further filter
  or sort it for your purposes.
- An _array of fields_ that lists the fields that the query returned data for (in the
  `Data` field response). Each item in the array is a name-datatype pair, such as `availability_score`-`float`.

## Troubleshooting

If errors are returned when you use query interface API operations, verify that you have the
required permissions to use Internet Monitor. Specifically, make sure that you have the following permissions:

```
internetmonitor:StartQuery
internetmonitor:GetQueryStatus
internetmonitor:GetQueryResults
internetmonitor:StopQuery
```

These permissions are included in the recommended AWS Identity and Access Management policy to use the Internet Monitor dashboard
in the console. For more information, see [AWS managed policies for Internet Monitor](CloudWatch-IM-permissions.md "CloudWatch-IM-permissions.md").
