

# Tutorial: monitor an application
<a name="omni-tutorial-monitor-an-application"></a>

Use this tutorial to instrument an application with OpenTelemetry, send its telemetry to CloudWatch Omni, and verify that you can monitor its services and requests. To work through the AI agent workflow instead, see [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md).

**Prerequisites**
+ Set up a CloudWatch Omni domain and space. See [Set up Omni](omni-set-up-omni.md).
+ An application serving traffic or requests. Use an OpenTelemetry SDK for your application language, or supported auto-instrumentation where applicable. For supported application languages, see [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md).
+ Configure credentials that allow the application to send telemetry to CloudWatch. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

**Step 1: Instrument your application**

1. Add OpenTelemetry instrumentation: Instrument your application with the OpenTelemetry SDK for your language, or with supported auto-instrumentation. For how OpenTelemetry works with CloudWatch, see [Getting started with OTLP ingestion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPGettingStarted.html).

1. Set the service and application identity: Set the OpenTelemetry service.name resource attribute for each service. You can set this value with the OTEL\\\_SERVICE\\\_NAME environment variable. Omni uses this value to identify the service. Set service.namespace on services that belong to the same application. Omni groups services with the same service.namespace value into the same application. Use consistent values across your telemetry so Omni can correlate signals from the same service.

1. Instrument outbound calls: Make sure your instrumentation covers the outbound operations that you want to see as dependencies, such as HTTP client requests, database calls, and AWS SDK calls. Omni uses spans from these calls to identify service dependencies. A call that is not instrumented might not appear as a dependency.

1. Configure service metrics: Add the CloudWatch plugin for OpenTelemetry to your instrumentation, following the optional OpenTelemetry instrumentation step in [Send application telemetry](omni-send-application-telemetry.md). The plugin generates request, error, and duration (RED) metrics from your application's spans, and Omni uses those metrics for service request, latency, and errors. For the package to install for your language and its documentation, see [Monitor a service](omni-monitor-a-service.md). The plugin derives these metrics from your spans but does not export them itself. The metrics exporter in your OpenTelemetry configuration sends them, so configure a metrics exporter alongside your trace exporter.

**Step 2: Send telemetry to CloudWatch**

1. Configure the OpenTelemetry (OTLP) exporter to send traces to the CloudWatch endpoint for your Region, authenticated with AWS Signature Version 4 (SigV4). For the endpoint, the exporter configuration, and the permissions your application's role needs, follow [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

1. Run your application and send several requests through it. These requests generate telemetry that CloudWatch makes available to your Omni space. If telemetry does not appear, verify the exporter endpoint, Region, credentials, and signing configuration. See the troubleshooting guidance in [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

**Step 3: See your application on the map**

1. Open Application map in Omni. Set the time range to include the requests that you generated. The application map reflects telemetry observed during the selected period. Find the application identified by the service.namespace value that you configured in step 1. The application contains the services that share that namespace. Each service is identified by its service.name.

1. Open the application to review its services and dependencies. Each service appears as a service node named with the service name you set in step 1. For more information, see [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md).

**Step 4: Examine service health**

1. Select a service from the application map. Review the available request, latency, and error information for the selected time range. You can also inspect the services and resources connected to it. For more information about finding and monitoring services, see [Monitor a service](omni-monitor-a-service.md).

1. From the service, pivot into its traces to follow one request across your services, span by span. For the application traces, see [Application traces](omni-application-traces.md).

**Next steps**
+ Query the telemetry behind the map with SQL. See [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).
+ Put your application's telemetry on a dashboard. See [Dashboards](omni-dashboards.md).
+ Create alerts on your application's telemetry. See [Alerts](omni-alerts.md).
+ If your system includes AI agents, monitor them alongside your application. See [Monitor AI agents](omni-monitor-ai-agents.md).