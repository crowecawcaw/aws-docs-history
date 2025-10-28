# Release: App Runner launches built-in X-Ray support on April 12, 2022

Your AWS App Runner service can now stream request traces to AWS X-Ray.

**Release date:** April 12, 2022

## Changes

Starting today, you can opt in to add AWS X-Ray tracing to your AWS App Runner service. App Runner streams all request traces to X-Ray. For more information,
see [Tracing for your App Runner application with X-Ray](../dg/monitor-xray.md "../dg/monitor-xray.md") in the _AWS App Runner Developer Guide_.

X-Ray is a service that collects data about requests that your application serves. X-Ray provides tools that you can use to view, filter, and gain
insights into that data to identify issues and opportunities for optimization. X-Ray uses trace data from the AWS resources that power your cloud
applications to generate a detailed service graph. The service graph shows the client, your frontend service, and backend services that your frontend
service calls to process requests and persist data. Use the service graph to identify bottlenecks, latency spikes, and other issues to solve to improve
the performance of your applications. For more information about X-Ray, see the [AWS X-Ray Developer Guide](../../../xray/latest/devguide.md "../../../xray/latest/devguide.md").
