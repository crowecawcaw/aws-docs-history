# Download metrics data in CSV format

You can download the CloudWatch metrics data for a CloudFront distribution in CSV format.

###### To download metrics data in CSV format

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Monitoring**.
3. Choose the distribution and then choose **View distribution
   metrics**.
4. Choose **Download CSV** and then choose the time period (for
   example, **For last 1 day (1 hour period)**.
5. After your file downloads, open it to view the following information.

###### Topics

- [Information about the report](#cloudwatch-csv-header "#cloudwatch-csv-header")
- [Data in the metrics report](#cloudwatch-csv-data "#cloudwatch-csv-data")

## Information about the report

The first few rows of the report include the following information:

**Version**

The CloudFront reporting version.

**Report**

The name of the report.

**DistributionID**

The ID of the distribution for which you ran the report.

**StartDateUTC**

The beginning of the date range for which you ran the report, in
Coordinated Universal Time (UTC).

**EndDateUTC**

The end of the date range for which you ran the report, in Coordinated
Universal Time (UTC).

**GeneratedTimeUTC**

The date and time on which you ran the report, in Coordinated
Universal Time (UTC).

**Granularity**

The time period for each row in the report, for example,
`ONE_MINUTE`.

## Data in the metrics report

The report includes the following values:

**DistributionID**

The ID of the distribution for which you ran the report.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If a
distribution has no alternate domain names, the list includes an origin
domain name for the distribution.

**TimeBucket**

The hour or the day that the data applies to, in Coordinated Universal
Time (UTC).

**Requests**

The total number of requests for all HTTP status codes (for example,
`200`, `404`, and so on) and all methods (for
example, `GET`, `HEAD`, `POST`, and so
on) during the time period.

**BytesDownloaded**

The number of bytes that viewers downloaded for the specified
distribution during the time period.

**BytesUploaded**

The number of bytes that viewers uploaded for the specified
distribution during the time period.

**TotalErrorRatePct**

The percentage of requests for which the HTTP status code was a
`4xx` or `5xx` error for the specified
distribution during the time period.

**4xxErrorRatePct**

The percentage of requests for which the HTTP status code was a
`4xx` error for the specified distribution during the
time period.

**5xxErrorRatePct**

The percentage of requests for which the HTTP status code was a
`5xx` error for the specified distribution during the
time period.

If you have [turned on
additional metrics](viewing-cloudfront-metrics.md#monitoring-console.distributions-additional "viewing-cloudfront-metrics.md#monitoring-console.distributions-additional") for your distribution, then the report also includes
the following additional values:

**401ErrorRatePct**

The percentage of requests for which the HTTP status code was a
`401` error for the specified distribution during the
time period.

**403ErrorRatePct**

The percentage of requests for which the HTTP status code was a
`403` error for the specified distribution during the
time period.

**404ErrorRatePct**

The percentage of requests for which the HTTP status code was a
`404` error for the specified distribution during the
time period.

**502ErrorRatePct**

The percentage of requests for which the HTTP status code was a
`502` error for the specified distribution during the
time period.

**503ErrorRatePct**

The percentage of requests for which the HTTP status code was a
`503` error for the specified distribution during the
time period.

**504ErrorRatePct**

The percentage of requests for which the HTTP status code was a
`504` error for the specified distribution during the
time period.

**OriginLatency**

The total time spent, in milliseconds, from when CloudFront received a
request to when it started providing a response to the network (not the
viewer), for requests that were served from the origin, not the CloudFront
cache. This is also known as _first byte
latency_, or _time-to-first-byte_.

**CacheHitRate**

The percentage of all cacheable requests for which CloudFront served the
content from its cache. HTTP `POST` and `PUT`
requests, and errors, are not considered cacheable requests.
