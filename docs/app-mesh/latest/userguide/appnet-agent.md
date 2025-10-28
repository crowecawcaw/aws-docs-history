# Agent for Envoy

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

The Agent is a process manager within the Envoy image that's vended for App Mesh. The Agent
ensures Envoy remains running, stays healthy, and reduces downtime. It filters Envoy
statistics and ancillary data to provide a distilled view of the Envoy proxy’s operation in
App Mesh. This can help you troubleshooting related errors quicker.

You can use the Agent to configure the number of times that you want to restart the Envoy
proxy in the event that the proxy becomes unhealthy. If a failure occurs, the Agent logs the
conclusive exit status when Envoy exits. You can use this when troubleshooting the failure.
The Agent also facilitates Envoy connection draining, which helps make your applications
more resilient to failures.

Configure the Agent for Envoy using these variables:

- `APPNET_ENVOY_RESTART_COUNT` – When this variable is set to a
  non-zero value, the Agent attempts to restart the Envoy proxy process up to the
  number that you set when it deems the proxy process status unhealthy on polling.
  This helps reduce downtime by providing faster restart compared to a task or pod
  replacement by the container orchestrator in the case of proxy health check
  failures.
- `PID_POLL_INTERVAL_MS` – When configuring this variable, the
  default is kept to `100`. When set to this value, you allow for faster
  detection and restart of the Envoy process when it exits compared to task or pod
  replacement through container orchestrator health checks.
- `LISTENER_DRAIN_WAIT_TIME_S` – When configuring this variable,
  consider the container orchestrator timeout that's set for stopping the task or pod.
  For example, if this value is greater than the orchestrator timeout, the Envoy proxy
  can only drain for the duration until the orchestrator forcefully stops the task or
  pod.
- `APPNET_AGENT_ADMIN_MODE` – When this variable is set to
  `tcp` or `uds`, the Agent provides a local management
  interface. This management interface serves as a safe endpoint to interact with the
  Envoy proxy and provides the following APIs for health checks, telemetry data and
  summarizes the operating condition of the proxy.

      + `GET /status` – Queries Envoy stats and returns server
       information.
      + `POST /drain_listeners` – Drains all inbound
       listeners.
      + `POST /enableLogging?level=<desired_level>` –
       Change Envoy logging level across all loggers.
      + `GET /stats/prometheus` – Show Envoy statistics in
       Prometheus format.
      + `GET /stats/prometheus?usedonly` – Only show statistics
       that Envoy has updated.

  For more information about Agent configuration variables, see [Envoy configuration
  variables](envoy-config.md "envoy-config.md").

The new AWS App Mesh Agent is included in App Mesh-optimized Envoy images starting from
version `1.21.0.0` and requires no additional resource allocation in customer
tasks or pods.
