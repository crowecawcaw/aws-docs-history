# View CloudFront cache statistics reports

The Amazon CloudFront cache statistics report shows the following information:


* **Total requests** – The total number of
 requests for all HTTP status codes (for example, 200 or 404) and all methods
 (for example, GET, HEAD, or POST)
* **Percentage of viewer requests by result type**
 – Hits, misses, and errors as a percentage of total viewer requests for
 the selected CloudFront distribution
* **Bytes transferred to viewers** – Total
 bytes and bytes from misses
* **HTTP status codes** – Viewer requests by
 HTTP status code
* **Percentage of GET requests that didn't finish
 downloading** – Viewer GET requests that didn't finish
 downloading the requested object as a percentage of total requests
Data for these statistics is drawn from the same source as CloudFront access logs. However,
 you don't need to enable [access logging](AccessLogs.md "AccessLogs.md") to view cache
 statistics.

You can display charts for a specified date range in the last 60 days, with data
 points every hour or every day. You can usually view data about requests that CloudFront
 received as recently as an hour ago, but data can occasionally be delayed by as much as
 24 hours. 

###### Topics

* [View CloudFront cache statistics reports in the
 console](#cache-statistics-howto "#cache-statistics-howto")
* [Download data in CSV format](#cache-statistics-csv "#cache-statistics-csv")
* [How cache statistics charts are related to
 data in the CloudFront standard logs (access logs)](#cache-statistics-data "#cache-statistics-data")

## View CloudFront cache statistics reports in the
 console


You can view the CloudFront cache statistics report in the console.


###### To view the CloudFront cache statistics
 report

1. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Cache
 Statistics**.
3. In the **CloudFront Cache Statistics Reports** pane, for
 **Start Date** and **End Date**,
 select the date range for which you want to display cache statistics charts.
 Available ranges depend on the value that you select for
 **Granularity**:




	* **Daily** – To display charts
	 with one data point per day, select any date range in the previous
	 60 days.
	* **Hourly** – To display charts
	 with one data point every hour, select any date range of up to 14
	 days within the previous 60 days.
Dates and times are in Coordinated Universal Time (UTC).
4. For **Granularity**, specify whether to display one data
 point per day or one data point per hour in the charts. If you specify a
 date range greater than 14 days, the option to specify one data point per
 hour is not available.
5. For **Viewer Location**, choose the continent from which
 viewer requests originated, or choose **All Locations**.
 Cache statistics charts include data for requests that CloudFront received from
 the specified location.
6. In the **Distribution** list, select the distributions
 for which you want to display data in the usage charts:




	* **An individual distribution**
	 – The charts display data for the selected CloudFront distribution.
	 The **Distribution** list displays the distribution
	 ID and alternate domain names (CNAMEs) for the distribution, if any.
	 If a distribution doesn't have alternate domain names, the list
	 includes origin domain names for the distribution.
	* **All distributions** – The
	 charts display summed data for all distributions that are associated
	 with the current AWS account, excluding distributions that you
	 have deleted.
7. Choose **Update**.

###### Tip


* To view data for a daily or hourly data point within a chart, hover
 over the data point.
* For charts that show data transferred, you can change the vertical
 scale to gigabytes, megabytes, or kilobytes.

## Download data in CSV format


You can download the cache statistics report in CSV format. This section explains
 how to download the report and describes the values in the report.


###### To download the cache statistics
 report in CSV format

1. While viewing the cache statistics report, choose
 **CSV**.
2. In the **Opening *file
 name*** dialog box, choose whether to open or save
 the file.

### Information about the
 report


The first few rows of the report include the following information:




**Version**

The version of the format for this CSV file.



**Report**

The name of the report.



**DistributionID**

The ID of the distribution that you ran the report for, or
 `ALL` if you ran the report for all
 distributions.



**StartDateUTC**

The beginning of the date range for which you ran the report, in
 Coordinated Universal Time (UTC).



**EndDateUTC**

The end of the date range for which you ran the report, in
 Coordinated Universal Time (UTC).



**GeneratedTimeUTC**

The date and time on which you ran the report, in Coordinated
 Universal Time (UTC).



**Granularity**

Whether each row in the report represents one hour or one day.
 



**ViewerLocation**

The continent that viewer requests originated from, or
 `ALL`, if you chose to download the report for all
 locations.




### Data in the cache statistics
 report


The report includes the following values:




**DistributionID**

The ID of the distribution that you ran the report for, or
 `ALL` if you ran the report for all
 distributions.



**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
 a distribution has no alternate domain names, the list includes an
 origin domain name for the distribution.



**ViewerLocation**

The continent that viewer requests originated from, or
 `ALL`, if you chose to download the report for all
 locations.



**TimeBucket**

The hour or the day that data applies to, in Coordinated Universal
 Time (UTC).



**RequestCount**

The total number of requests for all HTTP status codes (for
 example, 200 or 404) and all methods (for example, GET, HEAD, or
 POST).



**HitCount**

The number of viewer requests for which the object is served from
 a CloudFront edge cache.



**MissCount**

The number of viewer requests for which the object isn't currently
 in an edge cache, so CloudFront must get the object from your
 origin.



**ErrorCount**

The number of viewer requests that resulted in an error, so CloudFront
 didn't serve the object.



**IncompleteDownloadCount**

The number of viewer requests for which the viewer started but
 didn't finish downloading the object.



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



**TotalBytes**

The total number of bytes served to viewers by CloudFront in response to
 all requests for all HTTP methods.



**BytesFromMisses**

The number of bytes served to viewers for objects that were not in
 the edge cache at the time of the request. This value is a good
 approximation of bytes transferred from your origin to CloudFront edge
 caches. However, it excludes requests for objects that are already
 in the edge cache but that have expired.




## How cache statistics charts are related to
 data in the CloudFront standard logs (access logs)


The following table shows how cache statistics charts in the CloudFront console
 correspond with values in CloudFront access logs. For more information about CloudFront access
 logs, see [Standard logging (access logs)](AccessLogs.md "AccessLogs.md").




**Total requests**

This chart shows the total number of requests for all HTTP status
 codes (for example, 200 or 404) and all methods (for example,
 `GET`, `HEAD`, or `POST`). Total
 requests shown in this chart equal the total number of requests in the
 access log files for the same time period.



**Percentage of viewer requests by result type**

This chart shows hits, misses, and errors as a percentage of total
 viewer requests for the selected CloudFront distribution:



* **Hit** – A viewer request
 for which the object is served from a CloudFront edge cache. In access
 logs, these are requests for which the value of
 `x-edge-response-result-type` is
 `Hit`.
* **Miss** – A viewer
 request for which the object isn't currently in an edge cache,
 so CloudFront must get the object from your origin. In access logs,
 these are requests for which the value of
 `x-edge-response-result-type` is
 `Miss`.
* **Error** – A viewer
 request that resulted in an error, so CloudFront didn't serve the
 object. In access logs, these are requests for which the value
 of `x-edge-response-result-type` is
 `Error`, `LimitExceeded`, or
 `CapacityExceeded`.

The chart does not include refresh hits—requests for objects
 that are in the edge cache but that have expired. In access logs,
 refresh hits are requests for which the value of
 `x-edge-response-result-type` is
 `RefreshHit`.



**Bytes transferred to viewers**

This chart shows two values:



* **Total bytes** – The
 total number of bytes served to viewers by CloudFront in response to
 all requests for all HTTP methods. In CloudFront access logs,
 **Total Bytes** is the sum of the values in
 the `sc-bytes` column for all of the requests during
 the same time period.
* **Bytes from misses** –
 The number of bytes served to viewers for objects that were not
 in the edge cache at the time of the request. In CloudFront access
 logs, **bytes from misses** is the sum of the
 values in the `sc-bytes` column for requests for
 which the value of `x-edge-result-type` is
 `Miss`. This value is a good approximation of
 bytes transferred from your origin to CloudFront edge caches. However,
 it excludes requests for objects that are already in the edge
 cache but that have expired.


**HTTP status codes**

This chart shows viewer requests by HTTP status code. In CloudFront access
 logs, status codes appear in the `sc-status` column:



* **2xx** – The request
 succeeded.
* **3xx** – Additional
 action is required. For example, 301 (Moved Permanently) means
 that the requested object has moved to a different
 location.
* **4xx** – The client
 apparently made an error. For example, 404 (Not Found) means
 that the client requested an object that could not be
 found.
* **5xx** – The origin
 server didn't fill the request. For example, 503 (Service
 Unavailable) means that the origin server is currently
 unavailable.


**Percentage of GET requests that didn't finish downloading**

This chart shows viewer `GET` requests that didn't finish
 downloading the requested object as a percentage of total requests.
 Typically, downloading an object doesn't complete because the viewer
 canceled the download, for example, by clicking a different link or by
 closing the browser. In CloudFront access logs, these requests have a value of
 `200` in the `sc-status` column and a value of
 `Error` in the `x-edge-result-type`
 column.
