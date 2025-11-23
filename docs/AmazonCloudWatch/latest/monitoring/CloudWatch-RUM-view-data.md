# Viewing the CloudWatch RUM dashboard

CloudWatch RUM helps you collect data from user sessions about your application's
performance, including load times, Apdex score, device information, geolocation of user
sessions, and sessions with errors. All of this information is displayed in a
dashboard.

To view the RUM dashboard:

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**,
   **RUM**.
   The RUM console displays a list view of all your app monitors. The
   **Platform** column indicates whether each app monitor is for Web,
   Android, or iOS applications. Select an app monitor to access detailed views with
   **Performance**, **Errors**,
   **Sessions**, **Metrics** and
   **Configuration** tabs.

## Web Application Dashboard

When you select a web application monitor, you'll see the following tabs:

- The **Performance** tab displays page performance
  information including load times, request information, web vitals, and page
  loads over time. This view features interactive web vitals graphs where you
  can see the different percentile values of core web vitals for your pages
  and choose datapoints on the graph to view associated events captured by
  CloudWatch RUM. From there, you can either explore more events related to the
  metric spike or view page details for a selected event to identify specific
  conditions causing performance issues.

On this tab you can also toggle the view between **Page
loads**, **Requests**, and
**Location** to see more details about page
performance.

- The **Errors** tab displays Javascript error information
  including the error message most frequently seen by users and the devices
  and browsers with the most errors. This view includes a histogram of the
  errors and a list view of errors. You can filter the list of errors by user
  and event details. Choose an error message to see more details.
- The **HTTP requests** tab displays HTTP request
  information including the request URL with most errors and the devices and
  browsers with the most errors. This tab includes a histogram of the
  requests, a list view of requests, and a list view of network errors. You
  can filter the lists by user and event details. Choose a response code or an
  error message to see more details about the request or network error,
  respectively.
- The **Sessions** tab displays session metrics. This tab
  includes a histogram of session start events and a list view of sessions.
  You can filter the list of sessions by event type, user details, and event
  details. Choose a **sessionId** to see more details about a
  session.
- The **Events** tab displays a histogram of RUM events and
  a list view of the events. You can filter the list of events by event type,
  user details, and event details. Choose a RUM event to see the raw
  event.
- The **Browsers & Devices** tab displays information
  such as the performance and usage of different browsers and devices to
  access your application. This view includes controls to toggle the view
  between focusing on **Browsers** and
  **Devices**.

If you narrow the scope to a single browser, you see the data broken down
by browser version.

- The **User Journey** tab displays the paths that your
  customers use to navigate your application. You can see where your customers
  enter your application and what page they exit your application from. You
  can also see the paths that they take and the percentage of customers that
  follow those paths. You can pause on a node to get more details about that
  page. You can choose a single path to highlight the connections for easier
  viewing.
- The **Metrics** tab displays all default CloudWatch
  metrics published by your app monitor, including performance web vitals,
  error metrics (JavaScript errors, HTTP errors/faults), volume, user flow and
  apdex metrics. If you created extended metrics for your application, the tab
  also includes a subset of these metrics in the extended metrics section.
  This subset includes metrics of type PageViewCount,
  PerformanceNavigationDuration, Http4xxCount, Http5xxCount and JsErrorCount.
  The dashboard shows three metric variations per metric type. Since these are
  CloudWatch metrics, you can also export this tab to your own dashboard using
  the **Add to dashboard** option and update it to include
  more metrics.

(Optional) On any of the first six tabs, you can choose the
**Pages** button and select a page or page group from the list.
This narrows down the displayed data to a single page or group of pages of your
application. You can also mark pages and page groups in the list as
favorites.

## Mobile Application Dashboard

When you select a mobile application monitor, you'll see the following
tabs:

- The **Performance** tab provides insights into the
  performance of your mobile application including screen load times, app
  launch times (cold and warm), performance metrics, and Apdex scores over
  time. The detailed view breaks down performance by screen names, OS
  versions, app versions, devices, and countries. Clicking a screen load time,
  app launch time, or location datapoint in the chart will open the diagnostic
  panel on the right that provides further insights relevant to the datapoint
  consisting the most recent correlated sessions and links to the
  **Sessions** tab for troubleshooting.

On this tab you can also toggle the view between **Screen
loads**, **App launches**, and
**Location** to see more details about application
performance.

The tab also features the application performance index (Apdex) score
which indicates end users' level of satisfaction. Scores range from 0 (least
satisfied) to 1 (most satisfied). The scores are based on application
performance only. For more information about Apdex scores, see .

- The **Errors** tab breaks down application issues in
  three categories: Network Errors, Crashes, and ANRs (Android)/App Hangs
  (iOS). The **Network Errors** tab has a line chart showing
  network latency, client errors (4xx status code), and server errors (5xx
  status code). Clicking on a data point for any of these lines in the chart
  will open the diagnostic panel. The bottom table lists the 100 most common
  network routes. Clicking on a radio button will filter the line chart by the
  network route selected.

Similarly, the **Crashes** and **ANRs/App
Hangs** tabs show a line series for the count of each error,
and these are intractable. The bottom table displays the most common top
crash message or ANR/App Hang stack trace. Clicking on a radio button will
filter the chart, and clicking the error message will show the complete
stack trace.

- The **Sessions** tab displays a table that lists all
  sessions in descending chronological order. At the bottom, a waterfall
  visualization shows all telemetry for the selected session, helping you
  track user interactions and identify performance issues. Each row in the
  waterfall can be selected to open the diagnostic panel. For HTTP requests,
  you'll see a **traceId** that links to the Traces
  console.

For HTTP requests with non-2xx status codes, crashes, or ANRs (Android)/
App Hangs (iOS), the diagnostic panel includes an
**Exception** tab with the stack trace. The
**View** button in the waterfall provides quick access
to this information.

- The **Metrics** tab displays all default CloudWatch
  metrics published by your app monitor, including performance metrics (screen
  load times, cold app launch times), error metrics (crashes, ANRs/App Hangs,
  HTTP errors/faults), volume and apdex metrics. If you created extended
  metrics for your application, the tab also includes a subset of these
  metrics in the extended metrics section. This subset includes metrics of
  type ScreenLoadTime, ScreenLoadCount, CrashCount, Http4xxCount,
  Http5xxCount, ANRCount/AppHangCount, ColdLaunchTime and WarmLaunchTime. The
  dashboard shows three metric variations per metric type. Since these are
  CloudWatch metrics, you can also export this tab to your own dashboard using
  the **Add to dashboard** option and update it to include
  more metrics.
- The **Configuration** tab provides access to your app monitor's general
  settings and configuration details. You can also access the **Code snippets**
  tab which contains instructions for instrumenting your mobile application
  with the ADOT SDK, including both Manual and Zero-Code instrumentation
  options.

### How CloudWatch RUM sets Apdex scores

Apdex (Application Performance Index) is an open standard that defines a
method to report, benchmark, and rate application response time. An Apdex score
helps you understand and identify the impact on application performance over
time.

The Apdex score indicates the end users' level of satisfaction. Scores range
from 0 (least satisfied) to 1 (most satisfied). The scores are based on
application performance only. Users are not asked to rate the
application.

Each individual Apdex score falls into one of three thresholds. Based on the
Apdex threshold and actual application response time, there are three kinds of
performance, as follows:

- **Satisfied**— The actual
  application response time is less than or equal to the Apdex threshold.
  For CloudWatch RUM, this threshold is 2000 ms or less.
- **Tolerable**— The actual
  application response time is greater than the Apdex threshold, but less
  than or equal to four times the Apdex threshold. For CloudWatch RUM, this
  range is 2000—8000 ms.
- **Frustrating**— The actual
  application response time is greater than four times the Apdex
  threshold. For CloudWatch RUM, this range is over 8000 ms.

The total 0-1 Apdex score is calculated using the following formula:

`(positive scores + tolerable scores/2)/total scores * 100`
