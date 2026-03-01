# View CloudFront popular objects reports

View the Amazon CloudFront popular objects report to see the 50 most popular objects for a
distribution during a specified date range in the previous 60 days. You can also view
statistics about those objects, including the following:

- Number of requests for the object
- Number of hits and misses
- Hit ratio
- Number of bytes served for misses
- Total bytes served
- Number of incomplete downloads
- Number of requests by HTTP status code (2xx, 3xx, 4xx, and 5xx)
  Data for these statistics is drawn from the same source as CloudFront access logs. However,
  you don't need to enable [access logging](AccessLogs.md "AccessLogs.md") to view
  popular objects.

###### Topics

- [View CloudFront popular objects reports in the console](#popular-objects-howto "#popular-objects-howto")
- [How CloudFront calculates popular objects statistics](#popular-objects-calculate "#popular-objects-calculate")
- [Download data in CSV format](#popular-objects-csv "#popular-objects-csv")
- [How data in the popular objects report is related to data in the CloudFront standard logs (access logs)](#popular-objects-data "#popular-objects-data")

## View CloudFront popular objects reports in the console

You can view the CloudFront popular objects report in the console.

###### To view popular objects for a CloudFront distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Popular
   Objects**.
3. In the **CloudFront Popular Objects Report** pane, for
   **Start Date** and **End Date**,
   select the date range for which you want to display a list of popular
   objects. You can choose any date range in the previous 60 days.

Dates and times are in Coordinated Universal Time (UTC). 4. In the **Distribution** list, select the distribution for
which you want to display a list of popular objects. 5. Choose **Update**.

## How CloudFront calculates popular objects statistics

To get an accurate count of the top 50 objects in your distribution, CloudFront counts
the requests for all of your objects in 10-minute intervals beginning at midnight
and keeps a running total of the top 150 objects for the next 24 hours. (CloudFront also
retains daily totals for the top 150 objects for 60 days.)

Near the bottom of the list, objects constantly rise onto or drop off the list, so
the totals for those objects are approximations. The 50 objects at the top of the
list of 150 objects might rise and fall within the list, but they rarely drop off
the list altogether, so the totals for those objects are more reliable.

When an object drops off the list of the top 150 objects and then rises onto the
list again over the course of a day, CloudFront adds an estimated number of requests for
the period that the object was missing from the list. The estimate is based on the
number of requests received by whichever object was at the bottom of the list during
that time period.

If the object rises into the top 50 objects later in the day, the estimates of the
number of requests that CloudFront received while the object was out of the top 150
objects usually causes the number of requests in the popular objects report to
exceed the number of requests that appear in the access logs for that object.

## Download data in CSV format

You can download the popular objects report in CSV format. This section explains
how to download the report and describes the values in the report.

###### To download the popular objects report in CSV format

1. While viewing the popular objects report, choose
   **CSV**.
2. In the **Opening _file
   name_** dialog box, choose whether to open or save
   the file.

### Information about the report

The first few rows of the report include the following information:

**Version**

The version of the format for this CSV file.

**Report**

The name of the report.

**DistributionID**

The ID of the distribution that you ran the report for.

**StartDateUTC**

The beginning of the date range for which you ran the report, in
Coordinated Universal Time (UTC).

**EndDateUTC**

The end of the date range for which you ran the report, in
Coordinated Universal Time (UTC).

**GeneratedTimeUTC**

The date and time on which you ran the report, in Coordinated
Universal Time (UTC).

### Data in the popular objects report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**Object**

The last 500 characters of the URL for the object.

**RequestCount**

The total number of requests for this object.

**HitCount**

The number of viewer requests for which the object is served from
a CloudFront edge cache.

**MissCount**

The number of viewer requests for which the object isn't currently
in an edge cache, so CloudFront must get the object from your
origin.

**HitCountPct**

The value of `HitCount` as a percentage of the value of
`RequestCount`.

**BytesFromMisses**

The number of bytes served to viewers for this object when the
object was not in the edge cache at the time of the request.

**TotalBytes**

The total number of bytes served to viewers by CloudFront for this
object in response to all requests for all HTTP methods.

**IncompleteDownloadCount**

The number of viewer requests for this object for which the viewer
started but didn't finish downloading the object.

**HTTP2xx**

The number of viewer requests for which the HTTP status code was a
2xx value (succeeded).

**HTTP3xx**

The number of viewer requests for which the HTTP status code was a
3xx value (additional action is required).

**HTTP4xx**

The number of viewer requests for which the HTTP status code was a
4xx value (client error).

**HTTP5xx**

The number of viewer requests for which the HTTP status code was a
5xx value (server error).

## How data in the popular objects report is related to data in the CloudFront standard logs (access logs)

The following list shows how values in the popular objects report in the CloudFront
console correspond with values in CloudFront access logs. For more information about CloudFront
access logs, see [Access logs (standard logs)](AccessLogs.md "AccessLogs.md").

**URL**

The last 500 characters of the URL that viewers use to access the
object.

**Requests**

The total number of requests for the object. This value generally
corresponds closely with the number of `GET` requests for the
object in CloudFront access logs.

**Hits**

The number of viewer requests for which the object was served from a
CloudFront edge cache. In access logs, these are requests for which the value
of `x-edge-response-result-type` is `Hit`.

**Misses**

The number of viewer requests for which the object wasn't in an edge
cache, so CloudFront retrieved the object from your origin. In access logs,
these are requests for which the value of
`x-edge-response-result-type` is
`Miss`.

**Hit ratio**

The value of the **Hits** column as a percentage of
the value of the **Requests** column.

**Bytes from misses**

The number of bytes served to viewers for objects that were not in the
edge cache at the time of the request. In CloudFront access logs,
**bytes from misses** is the sum of the values in
the `sc-bytes` column for requests for which the value of
`x-edge-result-type` is `Miss`.

**Total bytes**

The total number of bytes that CloudFront served to viewers in response to
all requests for the object for all HTTP methods. In CloudFront access logs,
**total bytes** is the sum of the values in the
`sc-bytes` column for all of the requests during the same
time period.

**Incomplete downloads**

The number of viewer requests that did not finish downloading the
requested object. Typically, the reason that a download doesn't complete
is that the viewer canceled it, for example, by clicking a different
link or by closing the browser. In CloudFront access logs, these requests have
a value of `200` in the `sc-status` column and a
value of `Error` in the `x-edge-result-type`
column.

**2xx**

The number of requests for which the HTTP status code is
`2xx`, `Successful`. In CloudFront access logs,
status codes appear in the `sc-status` column.

**3xx**

The number of requests for which the HTTP status code is
`3xx`, `Redirection`. `3xx` status
codes indicate that additional action is required. For example, 301
(Moved Permanently) means that the requested object has moved to a
different location.

**4xx**

The number of requests for which the HTTP status code is
`4xx`, `Client Error`. `4xx` status
codes indicate that the client apparently made an error. For example,
404 (Not Found) means that the client requested an object that could not
be found.

**5xx**

The number of requests for which the HTTP status code is
`5xx`, `Server Error`. `5xx` status
codes indicate that the origin server didn't fill the request. For
example, 503 (Service Unavailable) means that the origin server is
currently unavailable.
