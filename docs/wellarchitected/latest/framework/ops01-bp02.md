

# OPS01-BP02 Develop user experience telemetry

 User experience telemetry measures how real people experience your application. *Real user monitoring* captures what happens in the sessions of actual users, and *synthetic monitoring* runs scripted interactions on a schedule to test critical paths. Together they show what users experience now and whether important functionality still works when traffic is low. 

 **Desired outcome:** 
+  You see application performance from the user's perspective, including load times across devices, browsers, and geographies. 
+  You test critical user journeys on a schedule, so you catch broken paths even when no real user is exercising them. 
+  You detect client-side problems from real session data before users report them. 
+  You can compare the experience of real users against scripted test results to isolate where a problem originates. 

 **Common anti-patterns:** 
+  Teams monitor server-side metrics only, so they learn about a slow page from customer complaints rather than data. 
+  Applications run without real user monitoring, discarding the client-side data that shows how users actually interact with the interface. 
+  Critical but less frequently used paths, such as password reset or checkout, go untested, so failures reach users. 
+  Organizations test only during business hours, missing failures that occur when real traffic is low. 

 **Benefits of establishing this best practice:** 
+  Client-side issues are identified and addressed before they affect a large share of users. 
+  Continuous feedback from real sessions guides interface and performance improvements. 
+  Scripted tests confirm that core functions stay available at all times. 
+  Performance data segmented by device and browser shows where optimization pays off. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Server-side telemetry stops at what your services returned. A page can render slowly because of slow DNS resolution, a third-party script, the application's client-side code, a large image, or a slow network on the user's device, none of which appear in backend metrics. User experience telemetry addresses this problem by measuring the experience in the browser or client. Client-side RED metrics (rate, errors, and duration) describe what the user experienced: errors and duration include every contribution between your services and the user, and rate shows how many users an issue touches. 

 Real user monitoring (RUM) collects performance and error data from actual user sessions, capturing the devices and networks your users bring. RUM only reports on paths users happen to exercise. Synthetic monitoring covers the paths you choose by running scripted interactions, often called *canaries*, on a fixed schedule. Canaries test critical functionality continually, even when no real user is active, but they only exercise the scenarios you script. RUM covers mobile applications as well as the browser, with SDKs for iOS and Android. For web applications, session replay records sessions so you can play back what a user experienced without reconstructing it from logs. 

 The RED metrics of your services ([OPS01-BP01 Develop application telemetry](ops01-bp01.md)) describe the experience you delivered, but nothing beyond it. [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) measures the internet paths between your users and the workload and shows when a provider event is degrading the experience. This is dependency telemetry, as covered in [OPS01-BP03 Develop dependency telemetry](ops01-bp03.md). Real user monitoring records what users experienced on their devices, and synthetic canaries probe even when no real users are active. If service metrics are healthy but real-user data shows degradation, the problem lies between your service and the user. 

 Both techniques have costs. RUM collects data from client sessions that may include information you are not permitted to store, so configure sampling and data handling before you deploy. Session replay captures more, so it masks all text input and on-page text by default. Synthetic canaries are code, and they drift out of date as the application changes. An unmaintained canary produces false alarms or passes while the user experience is broken. Treat canaries as part of the application, versioned and reviewed like any other test. 

 [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) collects and visualizes client-side performance and error data from a snippet embedded in your pages. [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) runs canaries that script and monitor the paths you define. Because both services publish into the same monitoring service as your application metrics and logs, you can correlate a drop in real-user performance or a failed canary with the backend telemetry that explains it. Integrate these services with [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) to see client pages and canaries alongside the service they exercise, its traces, logs, and service-level objectives (SLOs). The mobile SDKs are AWS Distro for OpenTelemetry SDKs, so mobile sessions are recorded as OpenTelemetry data with the same standards and semantic conventions as the rest of your workload's telemetry. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy real user monitoring:** Add [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to your application, using its web client for browser applications or its [mobile SDKs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-web-mobile.html) for iOS and Android applications, to collect client-side performance and error data. A single app monitor can consolidate telemetry across multiple domains and subdomains. Build dashboards that show real-user metrics by page, device, and geography, and for web applications enable [session replay](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-session-replay.html) where visual playback would shorten diagnosis. 

1.  **Identify critical user journeys:** Work with product and front-end teams to list the paths that matter most, such as sign-in, search, and checkout. Prioritize journeys by business impact and by how damaging a silent failure would be. 

1.  **Create and schedule synthetic canaries:** Script those journeys as canaries with [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) and run them at fixed intervals for consistent coverage. Version and review canaries alongside application code so they stay accurate as the interface changes. 

1.  **Alert and correlate:** Configure alarms on RUM and canary results, and correlate both with backend telemetry to locate where a problem originates. Route each alert to the team that owns the affected journey. Turn on [X-Ray tracing of user sessions](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-RUM.html) so client-side requests carry a trace context. To follow a session into your backend traces, configure the RUM web client to add the trace header to allowed requests. Where a journey has a service level objective, alarm on the SLO rather than on raw thresholds, so alerts fire when the user experience is actually at risk. Following a slow or failing session through the services behind it is the practice of distributed tracing. See [OPS01-BP04 Develop distributed tracing](ops01-bp04.md), where Amazon CloudWatch Application Signals connects these client sessions to the backend service map. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 
+  [OPS01-BP04 Develop distributed tracing](ops01-bp04.md) 
+  [OPS01-BP03 Develop dependency telemetry](ops01-bp03.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 

 **Related documents:** 
+  [Amazon CloudWatch RUM guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) 
+  [Amazon CloudWatch Synthetics guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) 
+  [CloudWatch RUM and AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-RUM.html) 
+  [Set up a mobile application to use CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-web-mobile.html) 
+  [CloudWatch RUM session replay](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-session-replay.html) 
+  [Using Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Comprehensive observability with Mobile RUM and Application Map (COP364)](https://www.youtube.com/watch?v=z1qnPTUZZ9M) 

 **Related examples:** 
+  [Amazon CloudWatch RUM web client repository](https://github.com/aws-observability/aws-rum-web) 
+  [Using Amazon CloudWatch Synthetics to measure page load time](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance) 
+  [AWS Distro for OpenTelemetry Android SDK](https://github.com/aws-observability/aws-otel-android) 
+  [AWS Distro for OpenTelemetry Swift SDK](https://github.com/aws-observability/aws-otel-swift) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability) 