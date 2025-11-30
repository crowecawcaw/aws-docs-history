# View CloudFront top referrers reports

The CloudFront top referrers report includes the following for any date range in the
previous 60 days:

- Top 25 referrers (domains of websites that originated the most HTTP and HTTPS
  requests for objects that CloudFront is distributing for your distribution)
- Number of requests from a referrer
- Number of requests from a referrer as a percentage of the total number of
  requests during the specified period
  Data for the top referrers report is drawn from the same source as CloudFront access logs.
  However, you don't need to enable [access logging](AccessLogs.md "AccessLogs.md") to
  view the top referrers.

Top referrers can be search engines, other websites that link directly to your
objects, or your own website. For example, if
`https://example.com/index.html` links to 10 graphics,
`example.com` is the referrer for all 10 graphics.

###### Note

If a user enters a URL directly into the address line of a browser, there is no
referrer for the requested object.

###### Topics

- [View CloudFront top referrers reports in the
  console](#top-referrers-howto "#top-referrers-howto")
- [How CloudFront calculates top referrers
  statistics](#top-referrers-calculate "#top-referrers-calculate")
- [Download data in CSV format](#top-referrers-csv "#top-referrers-csv")
- [How data in the top referrers report is related
  to data in the CloudFront standard logs (access logs)](#top-referrers-data "#top-referrers-data")

## View CloudFront top referrers reports in the

console

You can view the CloudFront top referrers report in the console.

###### To view top referrers for a CloudFront distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Top Referrers**.
3. In the **CloudFront Top Referrers Report** pane, for
   **Start Date** and **End Date**,
   select the date range for which you want to display a list of top referrers.

Dates and times are in Coordinated Universal Time (UTC). 4. In the **Distribution** list, select the distribution for
which you want to display a list of top referrers. 5. Choose **Update**.

## How CloudFront calculates top referrers

statistics

To get an accurate count of the top 25 referrers, CloudFront counts the requests for all
of your objects in 10-minute intervals and keeps a running total of the top 75
referrers. Near the bottom of the list, referrers constantly rise onto or drop off
the list, so the totals for those referrers are approximations.

The 25 referrers at the top of the list of 75 referrers might rise and fall within
the list, but they rarely drop off of the list altogether, so the totals for those
referrers typically are more reliable.

## Download data in CSV format

You can download the top referrers report in CSV format. This section explains how
to download the report and describes the values in the report.

###### To download the top referrers report

in CSV format

1. While viewing the Top Referrers report, choose
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

### Data in the top referrers

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

**Referrer**

The domain name of the referrer.

**RequestCount**

The total number of requests from the domain name in the
`Referrer` column.

**RequestsPct**

The number of requests submitted by the referrer as a percentage
of the total number of requests during the specified period.

## How data in the top referrers report is related

to data in the CloudFront standard logs (access logs)

The following list shows how values in the Top Referrers report in the CloudFront
console correspond with values in CloudFront access logs. For more information about CloudFront
access logs, see [Access logs (standard logs)](AccessLogs.md "AccessLogs.md").

**Referrer**

The domain name of the referrer. In access logs, referrers are listed
in the `cs(Referer)` column.

**Request count**

The total number of requests from the domain name in the
**Referrer** column. This value generally
corresponds closely with the number of `GET` requests from
the referrer in CloudFront access logs.

**Request %**

The number of requests submitted by the referrer as a percentage of
the total number of requests during the specified period. If you have
more than 25 referrers, then you can't calculate **Request
%** based on the data in this table because the
**request count** column doesn't include all of the
requests during the specified period.
