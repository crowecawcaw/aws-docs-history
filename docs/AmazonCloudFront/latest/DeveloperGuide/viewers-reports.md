# View CloudFront viewers reports

The CloudFront viewers reports include the following information for any date range in the
previous 60 days:

- **Devices** – The types of devices most
  frequently used to access your content (such as Desktop or Mobile)
- **Browsers** – The top 10 browsers most
  frequently used to access your content (such as Chrome or Firefox)
- **Operating systems** – The top 10
  operating systems most frequently used when accessing your content (such as
  Linux, macOS, or Windows)
- **Locations** – The top 50 locations
  (countries or U.S. states/territories) of the viewers that most frequently
  access your content
  - You can also view locations with hourly data points for any date range
    of up to 14 days in the previous 60 days

###### Note

You don't need to enable [access logging](AccessLogs.md "AccessLogs.md") to see
viewers charts and reports.

###### Topics

- [View viewers charts and reports in the
  console](#viewers-reports-displaying "#viewers-reports-displaying")
- [Download data in CSV format](#viewer-csv "#viewer-csv")
- [Data included in the viewers reports](#viewer-csv-header "#viewer-csv-header")
- [How data in the locations report is related
  to data in the CloudFront standard logs (access logs)](#viewers-reports-data "#viewers-reports-data")

## View viewers charts and reports in the

console

You can view CloudFront viewers charts and reports in the console.

###### To view CloudFront viewers charts and

reports

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Viewers**.
3. In the **CloudFront Viewers** pane, for **Start
   Date** and **End Date**, select the date range
   for which you want to display viewer charts and reports.

For the Locations chart, available ranges depend on the value that you
select for **Granularity**:

    * **Daily** – To display charts
     with one data point per day, select any date range in the previous
     60 days.
    * **Hourly** – To display charts
     with one data point every hour, select any date range of up to 14
     days within the previous 60 days.

Dates and times are in Coordinated Universal Time (UTC). 4. (Browsers and Operating Systems charts only) For
**Grouping**, specify whether you want to group
browsers and operating systems by name (Chrome, Firefox) or by name and
version (Chrome 40.0, Firefox 35.0). 5. (Locations chart only) For **Granularity**, specify
whether to display one data point per day or one data point per hour in the
charts. If you specify a date range greater than 14 days, the option to
specify one data point per hour is not available. 6. (Locations chart only) For **Details**, specify whether
to display the top locations by countries or by U.S. states. 7. In the **Distribution** list, select the distribution for
which you want to display data in the usage charts:

    * **An individual distribution**
     – The charts display data for the selected CloudFront distribution.
     The **Distribution** list displays the distribution
     ID and an alternate domain name (CNAME) for the distribution, if
     any. If a distribution has no alternate domain names, the list
     includes an origin domain name for the distribution.
    * **All distributions (excludes
     deleted)** – The charts display summed data for
     all distributions that are associated with the current AWS
     account, excluding distributions that you have deleted.

8. Choose **Update**.

To view data for a daily or hourly data point within a chart, hover over the data
point.

## Download data in CSV format

You can download each of the viewer reports in CSV format. This section explains
how to download the reports and describes the values in the report.

###### To download the viewer reports in CSV

format

1. While viewing the Viewer report, choose **CSV**.
2. Choose the data that you want to download, for example,
   **Devices** or **Devices
   Trends**.
3. In the **Opening _file
   name_** dialog box, choose whether to open or save
   the file.

## Data included in the viewers reports

The first few rows of each report include the following information:

**Version**

The version of the format for this CSV file.

**Report**

The name of the report.

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all distributions.

**StartDateUTC**

The beginning of the date range for which you ran the report, in
Coordinated Universal Time (UTC).

**EndDateUTC**

The end of the date range for which you ran the report, in Coordinated
Universal Time (UTC).

**GeneratedTimeUTC**

The date and time on which you ran the report, in Coordinated
Universal Time (UTC).

**Grouping (browsers and operating systems reports only)**

Whether the data is grouped by the name or by the name and version of
the browser or operating system.

**Granularity**

Whether each row in the report represents one hour or one day.

**Details (locations report only)**

Whether requests are listed by country or by U.S. state.

The following topics describe the information in the different viewers
reports.

###### Topics

- [Devices report](#viewer-devices-csv-data "#viewer-devices-csv-data")
- [Device trends report](#viewer-device-trends-csv-data "#viewer-device-trends-csv-data")
- [Browsers report](#viewer-browsers-csv-data "#viewer-browsers-csv-data")
- [Browser trends report](#viewer-browser-trends-csv-data "#viewer-browser-trends-csv-data")
- [Operating systems
  report](#viewer-operating-system-csv-data "#viewer-operating-system-csv-data")
- [Operating system
  trends report](#viewer-operating-system-trends-csv-data "#viewer-operating-system-trends-csv-data")
- [Locations report](#viewer-locations-csv-data "#viewer-locations-csv-data")
- [Location trends report](#viewer-location-trends-csv-data "#viewer-location-trends-csv-data")

### Devices report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all
distributions.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**Requests**

The number of requests that CloudFront received from each type of
device.

**RequestsPct**

The number of requests that CloudFront received from each type of device
as a percentage of the total number of requests that CloudFront received
from all devices.

**Custom**

Requests for which the value of the `User-Agent` HTTP
header was not associated with one of the standard device types, for
example, `Desktop` or `Mobile`.

### Device trends report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all
distributions.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**TimeBucket**

The hour or the day that the data applies to, in Coordinated
Universal Time (UTC).

**Desktop**

The number of requests that CloudFront received from desktop computers
during the period.

**Mobile**

The number of requests that CloudFront received from mobile devices
during the period. Mobile devices can include both tablets and
mobile phones. If CloudFront can't determine whether a request originated
from a mobile device or a tablet, it's counted in the
`Mobile` column.

**Smart-TV**

The number of requests that CloudFront received from smart TVs during
the period.

**Tablet**

The number of requests that CloudFront received from tablets during the
period. If CloudFront can't determine whether a request originated from a
mobile device or a tablet, it's counted in the `Mobile`
column.

**Unknown**

Requests for which the value of the `User-Agent` HTTP
header was not associated with one of the standard device types, for
example, `Desktop` or `Mobile`.

**Empty**

The number of requests that CloudFront received that didn't include a
value in the HTTP `User-Agent` header during the
period.

### Browsers report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all
distributions.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**Group**

The browser or the browser and version that CloudFront received requests
from, depending on the value of `Grouping`. In addition
to browser names, possible values include the following:

- **Bot/Crawler** –
  primarily requests from search engines that are indexing
  your content.
- **Empty** – requests
  for which the value of the `User-Agent` HTTP
  header was empty.
- **Other** – browsers
  that CloudFront identified but that aren't among the most popular.
  If `Bot/Crawler`, `Empty`, and/or
  `Unknown` don't appear among the first nine
  values, then they're also included in
  `Other`.
- **Unknown** – requests
  for which the value of the `User-Agent` HTTP
  header was not associated with a standard browser. Most
  requests in this category come from custom applications or
  scripts.

**Requests**

The number of requests that CloudFront received from each type of
browser.

**RequestsPct**

The number of requests that CloudFront received from each type of
browser as a percentage of the total number of requests that CloudFront
received during the time period.

### Browser trends report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all
distributions.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**TimeBucket**

The hour or the day that the data applies to, in Coordinated
Universal Time (UTC).

**(Browsers)**

The remaining columns in the report list the browsers or the
browsers and their versions, depending on the value of
`Grouping`. In addition to browser names, possible
values include the following:

- **Bot/Crawler** –
  primarily requests from search engines that are indexing
  your content.
- **Empty** – requests
  for which the value of the `User-Agent` HTTP
  header was empty.
- **Other** – browsers
  that CloudFront identified but that aren't among the most popular.
  If `Bot/Crawler`, `Empty`, and/or
  `Unknown` don't appear among the first nine
  values, then they're also included in
  `Other`.
- **Unknown** – requests
  for which the value of the `User-Agent` HTTP
  header was not associated with a standard browser. Most
  requests in this category come from custom applications or
  scripts.

### Operating systems

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

**Group**

The operating system or the operating system and version that CloudFront
received requests from, depending on the value of
`Grouping`. In addition to operating system names,
possible values include the following:

- **Bot/Crawler** –
  primarily requests from search engines that are indexing
  your content.
- **Empty** – requests
  for which the value of the `User-Agent` HTTP
  header was empty.
- **Other** – operating
  systems that CloudFront identified but that aren't among the most
  popular. If `Bot/Crawler`, `Empty`,
  and/or `Unknown` don't appear among the first
  nine values, then they're also included in
  `Other`.
- **Unknown** – requests
  for which the value of the `User-Agent` HTTP
  header was not associated with a standard browser. Most
  requests in this category come from custom applications or
  scripts.

**Requests**

The number of requests that CloudFront received from each type of
operating system.

**RequestsPct**

The number of requests that CloudFront received from each type of
operating system as a percentage of the total number of requests
that CloudFront received during the time period.

### Operating system

trends report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all
distributions.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**TimeBucket**

The hour or the day that the data applies to, in Coordinated
Universal Time (UTC).

**(Operating systems)**

The remaining columns in the report list the operating systems or
the operating systems and their versions, depending on the value of
`Grouping`. In addition to operating system names,
possible values include the following:

- **Bot/Crawler** –
  primarily requests from search engines that are indexing
  your content.
- **Empty** – requests
  for which the value of the `User-Agent` HTTP
  header was empty.
- **Other** – operating
  systems that CloudFront identified but that aren't among the most
  popular. If `Bot/Crawler`, `Empty`,
  and/or `Unknown` don't appear among the first
  nine values, then they're also included in
  `Other`.
- **Unknown** – requests
  for which the operating system isn't specified in the
  `User-Agent` HTTP header.

### Locations report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all
distributions.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**LocationCode**

The abbreviation for the location that CloudFront received requests
from. For more information about possible values, see the
description of Location in [How data in the locations report is related
to data in the CloudFront standard logs (access logs)](#viewers-reports-data "#viewers-reports-data").

**LocationName**

The name of the location that CloudFront received requests from.

**Requests**

The number of requests that CloudFront received from each
location.

**RequestsPct**

The number of requests that CloudFront received from each location as a
percentage of the total number of requests that CloudFront received from
all locations during the time period.

**TotalBytes**

The number of bytes that CloudFront served to viewers in this country or
state, for the specified distribution and period.

### Location trends report

The report includes the following values:

**DistributionID**

The ID of the distribution that you ran the report for, or
`ALL` if you ran the report for all
distributions.

**FriendlyName**

An alternate domain name (CNAME) for the distribution, if any. If
a distribution has no alternate domain names, the list includes an
origin domain name for the distribution.

**TimeBucket**

The hour or the day that the data applies to, in Coordinated
Universal Time (UTC).

**(Locations)**

The remaining columns in the report list the locations that CloudFront
received requests from. For more information about possible values,
see the description of Location in [How data in the locations report is related
to data in the CloudFront standard logs (access logs)](#viewers-reports-data "#viewers-reports-data").

## How data in the locations report is related

to data in the CloudFront standard logs (access logs)

The following list shows how data in the Locations report in the CloudFront console
corresponds with values in CloudFront access logs. For more information about CloudFront access
logs, see [Access logs (standard logs)](AccessLogs.md "AccessLogs.md").

**Location**

The country or U.S. state that the viewer is in. In access logs, the
`c-ip` column contains the IP address of the device that
the viewer is running on. We use geolocation data to identify the
geographic location of the device based on the IP address.

If you're displaying the **Locations** report by
country, the country list is based on [ISO 3166-2,
_Codes for the representation of names of countries and
their subdivisions – Part 2: Country subdivision
code_](https://en.wikipedia.org/wiki/ISO_3166-2 "https://en.wikipedia.org/wiki/ISO_3166-2"). The country list includes the following
additional values:

- **Anonymous Proxy** – The request
  originated from an anonymous proxy.
- **Satellite Provider** – The request
  originated from a satellite provider that provides internet
  service to multiple countries. Viewers might be in countries
  with a high risk of fraud.
- **Europe (Unknown)** – The request
  originated from an IP in a block that is used by multiple
  European countries. The country that the request originated from
  can't be determined. CloudFront uses **Europe
  (Unknown)** as the default.
- **Asia/Pacific (Unknown)** – The
  request originated from an IP in a block that is used by
  multiple countries in the Asia/Pacific region. The country that
  the request originated from can't be determined. CloudFront uses
  **Asia/Pacific (Unknown)** as the default.

If you display the **Locations** report by U.S.
state, note that the report can include U.S. territories and U.S. Armed
Forces regions.

###### Note

If CloudFront can't determine a user's location, the location will
appear as Unknown in viewer reports.

**Request Count**

The total number of requests from the country or U.S. state that the
viewer is in, for the specified distribution and period. This value
generally corresponds closely with the number of `GET`
requests from IP addresses in that country or state in CloudFront access logs.

**Request %**

One of the following, depending on the value that you selected for
**Details**:

- **Countries** – The
  requests from this country as a percentage of the total number
  of requests.
- **U.S. States** – The
  requests from this state as a percentage of the total number of
  requests from the United States.

If requests came from more than 50 countries, then you can't calculate
**Request %** based on the data in this table
because the **Request Count** column doesn't include
all of the requests during the specified period.

**Bytes**

The number of bytes that CloudFront served to viewers in this country or
state, for the specified distribution and period. To change the display
of data in this column to KB, MB, or GB, choose the link in the column
heading.
