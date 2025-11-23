# CloudWatch RUM

With CloudWatch RUM, you can perform real user monitoring to collect and view client-side data
about your web and mobile application performance from actual user sessions in near real
time. For Web applications, you can analyze page load times, client-side errors, and user
behavior. For Mobile applications, you can monitor screen load times, app launch times,
network errors, crashes, and platform-specific issues such as Android Application Not
Responding (ANR) and iOS App Hangs. When you view this data, you can see it all aggregated
together and also see breakdowns by device types, operating systems, and other
characteristics of your application usage.

You can use the collected data to quickly identify and debug client-side performance
issues. CloudWatch RUM helps you visualize anomalies in your application performance and find
relevant debugging data such as error messages, stack traces, and user sessions. You can
also use RUM to understand the range of end user impact including the number of users,
geolocations, and browsers/devices used.

End user data that you collect for CloudWatch RUM is retained for 30 days and then automatically
deleted. If you want to keep the RUM telemetry data for a longer time, you can choose to
have the app monitor send copies of the telemetry to CloudWatch Logs in your account. Then, you can
adjust the retention period for that log group.

To use RUM, you create an _app monitor_ and provide some information.
RUM generates a code snippet that you can use to add a dependency injection into your
application. The snippet pulls in the RUM client code as needed. The RUM client captures
data from a percentage of your application's user sessions, which is displayed in a
pre-built dashboard. You can specify what percentage of user sessions to gather data
from.

CloudWatch RUM is integrated with [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md"), which can discover and monitor your application services,
clients, Synthetics canaries, and service dependencies. Use Application Signals to see a
list or visual map of your services, view health metrics based on your service level
objectives (SLOs), and drill down to see correlated X-Ray traces for more detailed
troubleshooting. To see RUM client page requests in Application Signals, turn on X-Ray
active tracing when [creating
an app monitor](CloudWatch-RUM-get-started-create-app-monitor.md "CloudWatch-RUM-get-started-create-app-monitor.md"). For web applications, you can also enable this by [manually configuring the RUM web
client](CloudWatch-RUM-configure-client.md "CloudWatch-RUM-configure-client.md"). Your RUM clients are displayed on the [Application
Map](ServiceMap.md "ServiceMap.md") connected to your services, and in the [Service
detail](ServiceDetail.md "ServiceDetail.md") page of the services they call.

The RUM clients are open source. For more information, see [CloudWatch RUM web client](https://github.com/aws-observability/aws-rum-web "https://github.com/aws-observability/aws-rum-web"), the
[AWS Distro for
OpenTelemetry (ADOT) Android SDK](https://github.com/aws-observability/aws-otel-android "https://github.com/aws-observability/aws-otel-android"), and [AWS Distro for
OpenTelemetry (ADOT) iOS SDK](https://github.com/aws-observability/aws-otel-swift "https://github.com/aws-observability/aws-otel-swift").

**RUM Pricing**

For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

**Region availability**

CloudWatch RUM is currently available in the following Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
- Asia Pacific (Mumbai)
- Asia Pacific (Hyderabad)
- Asia Pacific (Melbourne)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Jakarta)
- Asia Pacific (Malaysia)
- Asia Pacific (Thailand)
- Asia Pacific (Tokyo)
- Asia Pacific (Hong Kong)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- Europe (Zurich)
- Middle East (Bahrain)
- Middle East (UAE)
- Mexico (Central)
- South America (São Paulo)
- Israel (Tel Aviv)
- Canada West (Calgary)
