# App Mesh troubleshooting best practices

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

We recommend that you follow the best practices in this topic to troubleshoot issues when using
App Mesh.

## Enable the Envoy proxy administration interface

The Envoy proxy ships with an administration interface that you can use to discover configuration
and statistics and to perform other administrative functions such as connection draining. For more
information, see [Administration interface](https://www.envoyproxy.io/docs/envoy/latest/operations/admin "https://www.envoyproxy.io/docs/envoy/latest/operations/admin") in the Envoy documentation.

If you use the managed [Envoy image](envoy.md "envoy.md"), the administration endpoint
is enabled by default on port 9901. Examples provided in [App Mesh setup troubleshooting](troubleshooting-setup.md "troubleshooting-setup.md") display the example administration endpoint URL as
`http://my-app.default.svc.cluster.local:9901/`.

###### Note

The administration endpoint should never be exposed to the public internet. Additionally, we
recommend monitoring the administration endpoint logs, which are set by the
`ENVOY_ADMIN_ACCESS_LOG_FILE` environment variable to
`/tmp/envoy_admin_access.log` by default.

## Enable Envoy DogStatsD integration for metric offload

The Envoy proxy can be configured to offload statistics for OSI Layer 4 and Layer 7 traffic and
for internal process health. While this topic shows how to use these statistics without offloading
the metrics to sinks like CloudWatch metrics and Prometheus., having these statistics in a
centralized location for all of your applications can help you diagnose issues and confirm behavior
more quickly. For more information, see [Using Amazon CloudWatch
Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") and the [Prometheus documentation](https://prometheus.io/docs/introduction/overview/ "https://prometheus.io/docs/introduction/overview/").

You can configure DogStatsD metrics by setting the parameters defined in [DogStatsD variables](envoy-config.md#envoy-dogstatsd-config "envoy-config.md#envoy-dogstatsd-config"). For more information
about DogStatsD, see the [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/?tab=hostagent "https://docs.datadoghq.com/developers/dogstatsd/?tab=hostagent")
documentation. You can find a demonstration of metric offload to AWS CloudWatch metrics in the [App Mesh with Amazon ECS basics walk-through](https://github.com/aws/aws-app-mesh-examples/tree/main/walkthroughs/howto-ecs-basics "https://github.com/aws/aws-app-mesh-examples/tree/main/walkthroughs/howto-ecs-basics") on GitHub.

## Enable access logs

We recommend enabling access logs on your [Virtual nodes](virtual_nodes.md "virtual_nodes.md") and [Virtual gateways](virtual_gateways.md "virtual_gateways.md") to discover details about traffic transiting between your
applications. For more information, see [Access logging](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/observability/access_logging "https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/observability/access_logging") in the Envoy documentation. The logs provide detailed information on
OSI Layer 4 and Layer 7 traffic behavior. When you use Envoy’s default format, you can analyze the
access logs with [CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") using the
following parse statement.

```
`parse @message "[*] \"* * *\" * * * * * * * * * * *" as StartTime, Method, Path, Protocol, ResponseCode, ResponseFlags, BytesReceived, BytesSent, DurationMillis, UpstreamServiceTimeMillis, ForwardedFor, UserAgent, RequestId, Authority, UpstreamHost`
```

## Enable Envoy debug logging in pre-production environments

We recommend setting the Envoy proxy’s log level to `debug` in a pre-production
environment. Debug logs can help you identify issues before you graduate the associated App Mesh
configuration to your production environment.

If you’re using the [Envoy image](envoy.md "envoy.md"), you can set the log level to
`debug` through the `ENVOY_LOG_LEVEL` environment variable.

###### Note

We do not recommend using the `debug` level in production environments. Setting
the level to `debug` increases the logging and may affect performance and the
overall cost of logs offloaded to solutions like [CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

When you use Envoy’s default format, you can analyze the process logs with [CloudWatch Logs
Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") using the following parse statement:

```
`parse @message "[*][*][*][*] [*] *" as Time, Thread, Level, Name, Source, Message`
```

## Monitor the Envoy Proxy Connectivity with App Mesh control plane

We recommend you monitor the Envoy metrics `control_plane.connected_state` to make
sure that the Envoy proxy communicates with the App Mesh control plane to fetch the dynamic
configuration resources. For more information, see [Management Server](https://www.envoyproxy.io/docs/envoy/latest/configuration/overview/mgmt_server.html "https://www.envoyproxy.io/docs/envoy/latest/configuration/overview/mgmt_server.html").
