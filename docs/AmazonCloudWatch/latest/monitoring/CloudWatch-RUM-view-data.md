# Viewing the CloudWatch RUM dashboard

CloudWatch RUM collects and visualizes application performance data from user sessions
through an interactive dashboard. By capturing load times, Apdex scores, device
information, geolocation, and error patterns, teams can quickly identify performance
bottlenecks, prioritize fixes based on real user impact, and ensure optimal experiences
across different browsers, devices, and geographic regions—ultimately reducing end
user frustration and improving application reliability.

To view the RUM dashboard:

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals (APM)**,
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
  loads over time. On this tab you can also toggle the view between
  **Page loads**, **Resources**, and
  **Locations** to see more details about page
  performance.

The **Page loads** view features interactive web vitals
graphs where you can see the different percentile values of core web vitals
for your pages and choose datapoints on the graph to view correlated
sessions captured by CloudWatch RUM. From there you can navigate to the Sessions
tab using one of the links in the diagnostic table to identify specific
conditions causing performance issues. The tab also features the application
performance index (**Apdex**) score which indicates end
users' level of satisfaction. Scores range from 0 (least satisfied) to 1
(most satisfied). The scores are based on application performance only. For
more information about Apdex scores, see [How CloudWatch RUM sets Apdex scores](#CloudWatch-RUM-apdex "#CloudWatch-RUM-apdex"). The table at the bottom lists
the **Top 100 page load times** based on **Page
Ids**. You can change this attribute in the dropdown next to
the table header.

![Performance tab showing the Page loads view with interactive web vitals graphs, Apdex score, and Top 100 page load times table](images/rum-web-performance-pageloads.png)

Similarly the **Resources** view shows the resource
request time and count by the resource type. The
**Locations** view has interactive map that lets you
drill down to a more granular view and investigate performance issues in a
specific region.

![Performance tab showing the Resources and Locations views](images/rum-web-performance-resources-locations.png)

The diagnostic panel on the right also has the
**Browsers** and **Devices** tab which
shows the top 5 browsers/devices contributing to the performance issue. You
can click on the bar chart to navigate to the Sessions tab to further
investigate the issue.

![Diagnostic panel showing the Browsers and Devices tabs with top 5 contributing browsers and devices](images/rum-web-performance-browsers-devices.png)

- The **JS errors** tab displays JavaScript error count
  and rate in the summary component along with the Browser and Device with the
  most errors. This tab includes a chart which shows the number of sessions
  with JS errors and the failure rate. You can click on any data point in the
  chart to view the correlated sessions in the diagnostic panel. The table at
  the bottom lists the top 100 JS errors. The error count link in the table
  can be used to navigate to the sessions tab where you can view relevant
  sessions.

![JS errors tab showing error count, failure rate chart, diagnostic panel, and top 100 JS errors table](images/rum-web-js-errors.png)

- The **Http requests** tab displays HTTP request volume
  and error information in the HTTP request summary on the top. This tab
  includes a graph with the HTTP errors, HTTP faults and Network failures. You
  can click on any data point in the chart to view the correlated sessions in
  the diagnostic panel. The table at the bottom lists the top 100 network
  routes with issues. If you expand one of the rows you can see the top error
  messages for that url. The error count link in the table can be used to
  navigate to the sessions tab where you can view relevant sessions.

![HTTP requests tab showing request summary, error graph, diagnostic panel, and top 100 network routes table](images/rum-web-http-requests.png)

- The **Sessions** tab displays a table that lists all
  sessions in descending chronological order. At the bottom, a waterfall
  visualization shows all telemetry for the selected session, helping you
  track user interactions and identify performance issues. You can click on
  the error link in the **Errors** column to filter the
  waterfall chart for the specific error event. Each row in the waterfall can
  be selected to open the diagnostic panel where you can view the raw
  event.

![Sessions tab showing session list and waterfall visualization of telemetry events](images/rum-web-sessions-waterfall.png)

For HTTP requests, you'll see a **traceId** for HTTP and
Xray events that links to the Traces console if you have tracing enabled.
For events like JS error or HTTP error events, diagnostic panel includes an
**Exception** tab with the stack trace. The
**View** button in the waterfall provides quick access
to this information.

![Sessions diagnostic panel showing traceId link and Exception tab with stack trace](images/rum-web-sessions-diagnostic.png)

- The **User Journey** tab displays the paths that your
  customers use to navigate your application. You can see where your customers
  enter your application and what page they exit your application from. You
  can also see the paths that they take and the percentage of customers that
  follow those paths. You can pause on a node to get more details about that
  page. You can choose a single path to highlight the connections for easier
  viewing. The page shows user journey till 2nd interaction by default. You
  can click on the **Add path** button to view further
  interactions.

![User Journey tab showing navigation paths with Add path button](images/rum-web-user-journey.png)

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

![Metrics tab showing default and extended CloudWatch metrics published by the app monitor](images/rum-web-metrics.png)

(Optional) On any of the first five tabs, you can filter the data based on user
ID, session ID and other event specific filters using the filter bar on the top. You
can also use the quick filter panel on the left to filter on a subset of attributes
like Page IDs, Page groups, Device, Browser, Location. These filters can be saved
using the **Save filter** option and can be reused using the
**Select filter** dropdown next to the filter bar.

![Filter bar with quick filter panel, Save filter option, and Select filter dropdown](images/rum-web-filter-bar.png)

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
performance only. For more information about Apdex scores, see [How CloudWatch RUM sets Apdex scores](#CloudWatch-RUM-apdex "#CloudWatch-RUM-apdex").

![Mobile Performance tab showing screen load times, app launch times, and Apdex scores with diagnostic panel](images/rum-mobile-performance.png)

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

![Mobile Errors tab showing Network Errors, Crashes, and ANRs/App Hangs categories with diagnostic panel](images/rum-mobile-errors.png)

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

![Mobile Sessions tab showing waterfall visualization and diagnostic panel with traceId and Exception tab](images/rum-mobile-sessions-diagnostic.png)

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
