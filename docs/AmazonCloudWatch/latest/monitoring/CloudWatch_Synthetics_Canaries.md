# Synthetic monitoring (canaries)

You can use Amazon CloudWatch Synthetics to create _canaries_,
configurable scripts that run on a schedule, to monitor your endpoints and APIs. Canaries
follow the same routes and perform the same actions as a customer, which makes it possible for
you to continually verify your customer experience even when you don't have any customer traffic
on your applications. By using canaries, you can discover issues before your customers
do.

Canaries are scripts written in Node.js, Python, or Java. They create Lambda functions in your account that
use Node.js, Python, or Java as the runtime. Canaries work over both
HTTP and HTTPS protocols. Canaries use Lambda layers that contain the CloudWatch Synthetics library.
The library includes CloudWatch Synthetics implementations for NodeJS, Python, and Java.

Canaries in Node.js and Python runtimes offer programmatic access to headless browsers through Playwright, Puppeteer, or Selenium Webdriver. Multiple browsers are supported, including a headless Google Chrome browser, and Mozilla Firefox.
For more information about Playwright, see [Playwright](https://playwright.dev/ "https://playwright.dev/"). For more information about Puppeteer, see [Puppeteer](https://developer.chrome.com/docs/puppeteer/ "https://developer.chrome.com/docs/puppeteer/").
For more information about Selenium, see [Selenium](https://www.selenium.dev/ "https://www.selenium.dev/"). Canaries on Selenium only support Chrome browser. Canaries in Java are designed for flexibility in monitoring any type of service or application and do not contain browser support or frameworks.

Canaries check the availability and latency of your endpoints and can store load time data
and screenshots of the UI. They monitor your REST APIs, URLs, and website content, and they can
check for unauthorized changes from phishing, code injection and cross-site scripting.

CloudWatch Synthetics is integrated with [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md"),
which can discover and monitor your application services, clients, Synthetics canaries, and service dependencies.
Use Application Signals to see a list or visual map of your services, view health metrics based on your service level objectives (SLOs), and drill down
to see correlated X-Ray traces for more detailed troubleshooting. To see your canaries in Application Signals,
[turn on X-Ray active tracing](CloudWatch_Synthetics_Canaries_tracing.md "CloudWatch_Synthetics_Canaries_tracing.md").
Your canaries are displayed on the [Application Map](ServiceMap.md "ServiceMap.md") connected to your services, and in the
[Service detail](ServiceDetail.md "ServiceDetail.md") page of the services they call.

For a video demonstration of canaries, see the following:

- [Introduction to Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=MItluIsvfTo "https://www.youtube.com/watch?v=MItluIsvfTo")
- [Amazon CloudWatch Synthetics Demo](https://www.youtube.com/watch?v=hF3NM9j-u7I "https://www.youtube.com/watch?v=hF3NM9j-u7I")
- [Create Canaries Using Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=DSx65wW7lr0 "https://www.youtube.com/watch?v=DSx65wW7lr0")
- [Visual Monitoring with Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=_PCs-ucZz7E "https://www.youtube.com/watch?v=_PCs-ucZz7E")
  You can run a canary once or on a regular schedule. Canaries can run as often as once per minute.
  You can use both cron and rate expressions to schedule canaries.

For information about security issues to consider before you create and run canaries, see
[Security considerations for Synthetics canaries](servicelens_canaries_security.md "servicelens_canaries_security.md").

By default, canaries create several CloudWatch metrics in the `CloudWatchSynthetics` namespace.
These metrics have
`CanaryName` as a dimension. Canaries that use the `executeStep()`
or `executeHttpStep()`
function from the function library also have
`StepName` as a dimension. For more information about the canary
function library, see [Library functions available for canary scripts](CloudWatch_Synthetics_Canaries_Function_Library.md "CloudWatch_Synthetics_Canaries_Function_Library.md").

CloudWatch Synthetics integrates well with the X-Ray Trace Map, which uses CloudWatch with AWS X-Ray to
provide an end-to-end view of your services to help you more efficiently pinpoint performance
bottlenecks and identify impacted users. Canaries that you create with CloudWatch Synthetics appear on
the trace map. For more information, see [X-Ray Trace Map](../../../xray/latest/devguide/xray-console-servicemap.md "../../../xray/latest/devguide/xray-console-servicemap.md").

CloudWatch Synthetics is currently available in all commercial AWS Regions and the GovCloud
Regions.

###### Note

In Asia Pacific (Osaka), AWS PrivateLink is not supported. In Asia Pacific (Jakarta), AWS PrivateLink
and X-Ray are not supported.

###### Topics

- [Required roles and permissions for CloudWatch canaries](CloudWatch_Synthetics_Canaries_Roles.md "CloudWatch_Synthetics_Canaries_Roles.md")
- [Creating a canary](CloudWatch_Synthetics_Canaries_Create.md "CloudWatch_Synthetics_Canaries_Create.md")
- [Groups](CloudWatch_Synthetics_Groups.md "CloudWatch_Synthetics_Groups.md")
- [Test a canary locally](CloudWatch_Synthetics_Debug_Locally.md "CloudWatch_Synthetics_Debug_Locally.md")
- [Troubleshooting a failed canary](CloudWatch_Synthetics_Canaries_Troubleshoot.md "CloudWatch_Synthetics_Canaries_Troubleshoot.md")
- [Sample code for canary scripts](CloudWatch_Synthetics_Canaries_Samples.md "CloudWatch_Synthetics_Canaries_Samples.md")
- [Canaries and X-Ray tracing](CloudWatch_Synthetics_Canaries_tracing.md "CloudWatch_Synthetics_Canaries_tracing.md")
- [Running a canary on a VPC](CloudWatch_Synthetics_Canaries_VPC.md "CloudWatch_Synthetics_Canaries_VPC.md")
- [Encrypting canary artifacts](CloudWatch_Synthetics_artifact_encryption.md "CloudWatch_Synthetics_artifact_encryption.md")
- [Viewing canary statistics and details](CloudWatch_Synthetics_Canaries_Details.md "CloudWatch_Synthetics_Canaries_Details.md")
- [CloudWatch metrics published by canaries](CloudWatch_Synthetics_Canaries_metrics.md "CloudWatch_Synthetics_Canaries_metrics.md")
- [Edit or delete a canary](synthetics_canaries_deletion.md "synthetics_canaries_deletion.md")
- [Start, stop, delete, or update runtime for multiple canaries](synthetics_canaries_multi-action.md "synthetics_canaries_multi-action.md")
- [Monitoring canary events with Amazon EventBridge](monitoring-events-eventbridge.md "monitoring-events-eventbridge.md")
- [Performing safe canary updates](performing-safe-canary-upgrades.md "performing-safe-canary-upgrades.md")
