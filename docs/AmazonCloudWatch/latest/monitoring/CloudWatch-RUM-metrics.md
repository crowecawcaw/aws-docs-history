

# CloudWatch metrics that you can collect with CloudWatch RUM
<a name="CloudWatch-RUM-metrics"></a>

The tables in this section lists the metrics that you automatically collect with CloudWatch RUM from web applications, mobile applications, or both. You can see these metrics in the CloudWatch console. For more information, see [View available metrics](viewing_metrics_with_cloudwatch.md).

You can also optionally send extended metrics to CloudWatch. For more information, see [Extended metrics](CloudWatch-RUM-custom-and-extended-metrics.md#CloudWatch-RUM-vended-metrics).

These metrics are published in the metric namespace named `AWS/RUM`. All of the following metrics are published with an `application_name` dimension. The value of this dimension is the name of the app monitor. Some metrics are also published with additional dimensions, as listed in the following table.

The following table describes the web metrics.


| Metric | Unit | Description | 
| --- | --- | --- | 
| `HttpStatusCodeCount` | Count | The count of HTTP responses in the application, by their response status code.<br />Additional dimensions:+  `event_details.response.status` is the response status code, such as 200, 400, 404, and so on. <br />+  `event_type` The type of event.   | 
| `Http4xxCount` | Count | The count of HTTP responses in the application, with 4xx response status code.<br />These are calculated based on `http_event` RUM events that result in 4xx codes. | 
| `Http4xxCountPerSession` | Count | The count of HTTP responses in a session, with 4xx response status code.<br />These are calculated based on `http_event` RUM events that result in 4xx codes. | 
| `Http4xxCountPerPageView` | Count | The count of HTTP responses in a page review, with 4xx response status code.<br />These are calculated based on `http_event` RUM events that result in 4xx codes. | 
| `Http5xxCount` | Count | The count of HTTP responses in the application, with 5xx response status code.<br />These are calculated based on `http_event` RUM events that result in 5xx codes. | 
| `Http5xxCountPerSession` | Count | The count of HTTP responses in the session, with 5xx response status code.<br />These are calculated based on `http_event` RUM events that result in 5xx codes. | 
| `Http5xxCountPerPageView` | Count | The count of HTTP responses in a page review, with 5xx response status code.<br />These are calculated based on `http_event` RUM events that result in 5xx codes. | 
| `JsErrorCount` | Count | The count of JavaScript error events ingested.  | 
| `JsErrorCountPerSession` | Count | The count of JavaScript error events ingested in a session. | 
| `JsErrorCountPerPageView` | Count | The count of JavaScript error events ingested in a page review. | 
| `NavigationFrustratedTransaction` | Count | The count of navigation events with a `duration` higher than the frustrating threshold, which is 8000ms. The duration of navigation events is tracked in the `PerformanceNavigationDuration` metric. | 
| `NavigationSatisfiedTransaction` | Count | The count of navigation events with a `duration` that is less than the Apdex objective, which is 2000ms. The duration of navigation events is tracked in the `PerformanceNavigationDuration` metric. | 
| `NavigationToleratedTransaction` | Count | The count of navigation events with a `duration` between 2000ms and 8000ms. The duration of navigation events is tracked in the `PerformanceNavigationDuration` metric. | 
| `PageViewCount` | Count | The count of page view events ingested by the app monitor.<br />This is calculated by counting the `page_view_event` RUM events. | 
| `PageViewCountPerSession` | Count | The count of page view events in a session. | 
| `PerformanceResourceDuration` | Milliseconds | The `duration` of a resource event.<br />Additional dimensions:+  `event_details.file.type` is the file type of the resource event, such as a stylesheet, document, image, script, or font. <br />+  `event_type` The type of event.  | 
| `PerformanceNavigationDuration` | Milliseconds | The `duration` of a navigation event. | 
| `RumEventPayloadSize` | Bytes | The size of every event ingested by CloudWatch RUM. You can also use the `SampleCount` statistic for this metric to monitor the number of events that an app monitor is ingesting. | 
| `SessionCount` | Count | The count of session start events ingested by the app monitor. In other words, the number of new sessions started. | 
| `SessionDuration` | Milliseconds | The duration of a session. These are calculated based on the time between first and last events in a session. | 
| `TimeOnPage` | Milliseconds | The duration of a page view.<br />These are calculated based on the time until next page view, except for the final page in a session where it's the time between first and last events on that page. | 
| `WebVitalsCumulativeLayoutShift` | None | Tracks the value of the cumulative layout shift events. | 
| `WebVitalsFirstInputDelay` | Milliseconds | Tracks the value of the first input delay events. | 
| `WebVitalsLargestContentfulPaint` | Milliseconds | Tracks the value of the largest contentful paint events. | 
| `WebVitalsInteractionToNextPaint` | Milliseconds | Tracks the value of the interaction to next paint events. | 

You can configure extended metrics for your mobile application to provide additional dimensions for analysis.


| Metric | Unit | Description | 
| --- | --- | --- | 
| `ANRCount` | Count | For Android only: The number of Application Not Responding (ANR) incidents, occurring when the application is unresponsive for more than 5 seconds, resulting in application crash. | 
| `AppHangCount` | Count | For iOS only: The number of times the application became unresponsive for more than 250ms on the main loop. | 
| `ColdAppLaunchFrustratedTransaction` | Count | The number of cold app launches that took longer than 8 seconds to complete, likely causing user frustration. | 
| `ColdAppLaunchSatisfiedTransaction` | Count | The number of cold app launches that completed in less than 2 seconds, providing a satisfactory user experience. | 
| `ColdAppLaunchToleratedTransaction` | Count | The number of cold app launches that completed between 2 and 8 seconds, providing a tolerable, but not ideal, user experience. | 
| `ColdLaunchTime` | Milliseconds | Time taken to launch the application from a terminated state.<br />For Android: Time from Application `onCreate` until the first Activity finishes creating.<br />For iOS: Time from application start (determined by `sysctl` process start command) until `didBecomeActiveNotification`. | 
| `CrashCount` | Count | The number of unexpected application terminations caused by unhandled exceptions or OS termination.<br />For Android: Crashes due to unhandled exceptions or system termination.<br />For iOS: Crashes due to unhandled exceptions, fatal errors, or system termination.<br />Crash data is stored locally and reported on next app launch. | 
| `DroppedEventsCount` | Count | The number of log events that were dropped because they exceeded the maximum size limit of 30KB per event. | 
| `DroppedSpansCount` | Count | The number of spans that were dropped because they exceeded the maximum size limit of 30KB per span. | 
| `Http4xxCount` | Count | Records the number of HTTP client errors encountered by the web or mobile application during HTTP requests. | 
| `Http5xxCount` | Count | Records the number of HTTP server errors encountered by the web or mobile application during HTTP requests. | 
| `LogPayloadSize` | Bytes | The size in bytes of the log telemetry data being sent to CloudWatch RUM.<br />You can also use the `SampleCount` statistic for this metric to monitor the number of Log Events that an app monitor is ingesting. | 
| `NetworkLatency` | Milliseconds | The time taken for network requests to complete, measuring the round-trip time from request initiation to response completion. | 
| `ScreenLoadCount` | Count | The total number of screen loads. | 
| `ScreenLoadToleratedTransaction` | Count | The number of screen loads that completed between 2 and 8 seconds, providing a tolerable, but not ideal, user experience. | 
| `SessionCount` | Count | The total number of unique user sessions with the application. A session begins when the user opens the app and ends after 30 minutes of inactivity or when explicitly terminated. | 
| `SpanPayloadSize` | Bytes | The size in bytes of the span telemetry data being sent to CloudWatch RUM.<br />You can also use the `SampleCount` statistic for this metric to monitor the number of Spans that an app monitor is ingesting. | 
| `WarmAppLaunchFrustratedTransaction` | Count | The number of warm app launches that took longer than 8 seconds to complete, likely causing user frustration. | 
| `WarmAppLaunchSatisfiedTransaction` | Count | The number of warm app launches that completed in less than 2 seconds, providing a satisfactory user experience. | 
| `WarmAppLaunchToleratedTransaction` | Count | The number of warm app launches that completed between 2 and 8 seconds, providing a tolerable, but not ideal, user experience. | 
| `WarmLaunchTime` | Milliseconds | Time taken to launch the application from background state.<br />For Android: Time from Application `onCreate` until the first Activity finishes creating.<br />For iOS: Time from `UIApplicationWillEnterForegroundNotification` until `didBecomeActiveNotification`. | 