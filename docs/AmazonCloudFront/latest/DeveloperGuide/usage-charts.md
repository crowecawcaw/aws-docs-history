# View CloudFront usage reports

The CloudFront usage reports include the following information:


* **Number of requests** – Shows the total
 number of requests that CloudFront responds to from edge locations in the selected
 region during each time interval for the specified CloudFront distribution.
* **Data transferred by protocol** and **data transferred by destination** – Both show
 the total amount of data transferred from CloudFront edge locations in the selected
 region during each time interval for the specified CloudFront distribution. They
 separate the data differently, as follows:




	+ **By protocol** – Separates the data by
	 protocol: HTTP or HTTPS.
	+ **By destination** – Separates the data
	 by destination: to your viewers or to your origin.
The CloudFront usage report is based on the AWS usage report for CloudFront. This report doesn't
 require any additional configuration. For more information, see [View the AWS usage report for CloudFront](reports-billing.md#usage-report "reports-billing.md#usage-report").

You can view reports for a specified date range in the last 60 days, with data points
 every hour or every day. You can usually view data about requests that CloudFront received as
 recently as four hours ago, but data can occasionally be delayed by as much as 24
 hours.

For more information, see [How the usage charts are related to data in the
 CloudFront usage report](#usage-charts-table "#usage-charts-table").

###### Topics

* [View CloudFront usage reports in the console](#usage-charts-howto "#usage-charts-howto")
* [Download data in CSV format](#usage-csv "#usage-csv")
* [How the usage charts are related to data in the
 CloudFront usage report](#usage-charts-table "#usage-charts-table")

## View CloudFront usage reports in the console


You can view the CloudFront usage report in the console.


###### To view CloudFront usage reports

1. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Usage Reports**.
3. In the **CloudFront Usage Reports** pane, for **Start
 Date** and **End Date**, select the date range
 for which you want to display usage charts. Available ranges depend on the
 value that you select for **Granularity**:




	* **Daily** — To display charts with one
	 data point per day, select any date range in the previous 60 days.
	* **Hourly** — To display charts with one
	 data point every hour, select any date range of up to 14 days within
	 the previous 60 days.
Dates and times are in Coordinated Universal Time (UTC).
4. For **Granularity**, specify whether to display one data
 point per day or one data point per hour in the charts. If you specify a
 date range greater than 14 days, the option to specify one data point per
 hour is not available.
5. For **Billing Region**, choose the CloudFront billing region
 that has the data you want to view, or choose **All
 Regions**. Usage charts include data for requests that CloudFront
 processes in edge locations in the specified region. The region where CloudFront
 processes requests might or might not correspond with the location of your
 viewers. 


Select only Regions that are included in the price class for your
 distribution. Otherwise, the usage charts probably won't contain any data.
 For example, if you chose Price Class 200 for your distribution, the South
 America and Australia billing regions are not included, so CloudFront generally
 won't process your requests from those regions. For more information about
 price classes, see [CloudFront
 pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").
6. In the **Distribution** list, select the distributions
 for which you want to display data in the usage charts: 




	* **An individual distribution**
	 — The charts display data for the selected CloudFront distribution.
	 The **Distribution** list displays the distribution
	 ID and alternate domain names (CNAMEs) for the distribution, if any.
	 If a distribution has no alternate domain names, the list includes
	 origin domain names for the distribution.
	* **All distributions (excludes deleted)** —
	 The charts display summed data for all distributions that are
	 associated with the current AWS account, excluding distributions
	 that you have deleted.
	* **All Deleted Distributions** — The charts
	 display summed data for all distributions that are associated with
	 the current AWS account and that were deleted in the last 60
	 days.
7. Choose **Update Graphs**.

###### Tip


* To view data for a daily or hourly data point within a chart, hover
 over the data point.
* For charts that show data transferred, note that you can change the
 vertical scale to gigabytes, megabytes, or kilobytes.

## Download data in CSV format


You can download the usage report in CSV format. This section explains how to
 download the report and describes the values in the report.


###### To download the usage report in CSV
 format

1. While viewing the Usage report, choose **CSV**.
2. In the **Opening *file
 name*** dialog box, choose whether to open or save
 the file.

### Information about the report


The first few rows of the report include the following information:




**Version**

The version of the format for this CSV file.



**Report**

The name of the report.



**DistributionID**

The ID of the distribution that you ran the report for,
 `ALL` if you ran the report for all distributions, or
 `ALL_DELETED` if you ran the report for all deleted
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
 



**BillingRegion**

The continent that viewer requests originated from, or
 `ALL`, if you chose to download the report for all
 billing regions.




### Data in the usage report


The report includes the following values:




**DistributionID**

The ID of the distribution that you ran the report for,
 `ALL` if you ran the report for all distributions, or
 `ALL_DELETED` if you ran the report for all deleted
 distributions.



**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
 a distribution has no alternate domain names, the list includes an
 origin domain name for the distribution.



**BillingRegion**

The CloudFront billing region that you ran the report for, or
 `ALL`.



**TimeBucket**

The hour or the day that data applies to, in Coordinated Universal
 Time (UTC).



**HTTP**

The number of HTTP requests that CloudFront responded to from edge
 locations in the selected region during each time interval for the
 specified CloudFront distribution. Values include:



* The number of `GET` and `HEAD`
 requests, which cause CloudFront to transfer data to your
 viewers
* The number of `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests, which cause CloudFront to transfer
 data to your origin


**HTTPS**

The number of HTTPS requests that CloudFront responded to from edge
 locations in the selected region during each time interval for the
 specified CloudFront distribution. Values include:



* The number of `GET` and `HEAD`
 requests, which cause CloudFront to transfer data to your
 viewers
* The number of `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests, which cause CloudFront to transfer
 data to your origin


**HTTPBytes**

The total amount of data transferred over HTTP from CloudFront edge
 locations in the selected billing region during the time period for
 the specified CloudFront distribution. Values include:



* Data transferred from CloudFront to your viewers in response to
 `GET` and `HEAD` requests
* Data transferred from your viewers to CloudFront for
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests
* Data transferred from CloudFront to your viewers in response to
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests


**HTTPSBytes**

The total amount of data transferred over HTTPS from CloudFront edge
 locations in the selected billing region during the time period for
 the specified CloudFront distribution. Values include:



* Data transferred from CloudFront to your viewers in response to
 `GET` and `HEAD` requests
* Data transferred from your viewers to CloudFront for
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests
* Data transferred from CloudFront to your viewers in response to
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests


**BytesIn**

The total amount of data transferred from CloudFront to your origin for
 `DELETE`, `OPTIONS`, `PATCH`,
 `POST`, and `PUT` requests in the selected
 region during each time interval for the specified CloudFront
 distribution. 



**BytesOut**

The total amount of data transferred over HTTP and HTTPS from CloudFront
 to your viewers in the selected region during each time interval for
 the specified CloudFront distribution. Values include:



* Data transferred from CloudFront to your viewers in response to
 `GET` and `HEAD` requests
* Data transferred from CloudFront to your viewers in response to
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests



## How the usage charts are related to data in the
 CloudFront usage report


The following list shows how the usage charts in the CloudFront console correspond with
 values in the **Usage Type** column in the CloudFront usage
 report.


###### Topics

* [Number of requests](#usage-charts-requests "#usage-charts-requests")
* [Data transferred by
 protocol](#usage-charts-data-transferred-by-protocol "#usage-charts-data-transferred-by-protocol")
* [Data transferred
 by destination](#usage-charts-data-transferred-by-destination "#usage-charts-data-transferred-by-destination")

### Number of requests


This chart shows the total number of requests that CloudFront responds to from edge
 locations in the selected region during each time interval for the specified
 CloudFront distribution, separated by protocol (HTTP or HTTPS) and type (static,
 dynamic, or proxy).




**Number of HTTP requests**


* `region`**-Requests-HTTP-Static:** Number of HTTP
 `GET` and `HEAD` requests served
 for objects with TTL ≥ 3600 seconds
* `region`**-Requests-HTTP-Dynamic:** Number of HTTP
 `GET` and `HEAD` requests served
 for objects with TTL < 3600 seconds
* `region`**-Requests-HTTP-Proxy:** Number of HTTP
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests that CloudFront forwards to your
 origin


**Number of HTTPS requests**


* `region`**-Requests-HTTPS-Static:** Number of HTTPS
 `GET` and `HEAD` requests served
 for objects with TTL ≥ 3600 seconds
* `region`**-Requests-HTTPS-Dynamic:** Number of HTTPS
 `GET` and `HEAD` requests served
 for objects with TTL < 3600 seconds
* `region`**-Requests-HTTPS-Proxy:** Number of HTTPS
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests that CloudFront forwards to your
 origin



### Data transferred by
 protocol


This chart shows the total amount of data transferred from CloudFront edge locations
 in the selected region during each time interval for the specified CloudFront
 distribution, separated by protocol (HTTP or HTTPS), type (static, dynamic, or
 proxy), and destination (viewers or origin).




**Data transferred over HTTP**


* `region`**-Out-Bytes-HTTP-Static:** Bytes served via
 HTTP for objects with TTL ≥ 3600 seconds
* `region`**-Out-Bytes-HTTP-Dynamic:** Bytes served via
 HTTP for objects with TTL < 3600 seconds
* `region`**-Out-Bytes-HTTP-Proxy:** Bytes returned from
 CloudFront to viewers via HTTP in response to `DELETE`,
 `OPTIONS`, `PATCH`,
 `POST`, and `PUT` requests
* `region`**-Out-OBytes-HTTP-Proxy:** Total bytes
 transferred via HTTP from CloudFront edge locations to your origin
 in response to `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests


**Data transferred over HTTPS**


* `region`**-Out-Bytes-HTTPS-Static:** Bytes served via
 HTTPS for objects with TTL ≥ 3600 seconds
* `region`**-Out-Bytes-HTTPS-Dynamic:** Bytes served via
 HTTPS for objects with TTL < 3600 seconds
* `region`**-Out-Bytes-HTTPS-Proxy:** Bytes returned from
 CloudFront to viewers via HTTPS in response to
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests
* `region`**-Out-OBytes-HTTPS-Proxy:** Total bytes
 transferred via HTTPS from CloudFront edge locations to your
 origin in response to `DELETE`,
 `OPTIONS`, `PATCH`,
 `POST`, and `PUT` requests



### Data transferred
 by destination


This chart shows the total amount of data transferred from CloudFront edge locations
 in the selected region during each time interval for the specified CloudFront
 distribution, separated by destination (viewers or origin), protocol (HTTP or
 HTTPS), and type (static, dynamic, or proxy).




**Data transferred from CloudFront to your viewers**


* `region`**-Out-Bytes-HTTP-Static:** Bytes served via
 HTTP for objects with TTL ≥ 3600 seconds
* `region`**-Out-Bytes-HTTPS-Static:** Bytes served via
 HTTPS for objects with TTL ≥ 3600 seconds
* `region`**-Out-Bytes-HTTP-Dynamic:** Bytes served via
 HTTP for objects with TTL < 3600 seconds
* `region`**-Out-Bytes-HTTPS-Dynamic:** Bytes served via
 HTTPS for objects with TTL < 3600 seconds
* `region`**-Out-Bytes-HTTP-Proxy:** Bytes returned from
 CloudFront to viewers via HTTP in response to `DELETE`,
 `OPTIONS`, `PATCH`,
 `POST`, and `PUT` requests
* `region`**-Out-Bytes-HTTPS-Proxy:** Bytes returned from
 CloudFront to viewers via HTTPS in response to
 `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests


**Data transferred from CloudFront to your origin**


* `region`**-Out-OBytes-HTTP-Proxy:** Total bytes
 transferred via HTTP from CloudFront edge locations to your origin
 in response to `DELETE`, `OPTIONS`,
 `PATCH`, `POST`, and
 `PUT` requests
* `region`**-Out-OBytes-HTTPS-Proxy:** Total bytes
 transferred via HTTPS from CloudFront edge locations to your
 origin in response to `DELETE`,
 `OPTIONS`, `PATCH`,
 `POST`, and `PUT` requests
