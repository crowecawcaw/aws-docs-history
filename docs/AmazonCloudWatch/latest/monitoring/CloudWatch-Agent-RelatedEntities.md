# Using the CloudWatch agent with related

telemetry

Metrics and logs that are sent to CloudWatch can include an optional entity to correlate
telemetry. Entities are used in the [Explore related](ExploreRelated.md "ExploreRelated.md")
pane. The CloudWatch agent sends entities with a service name and environment name included.

The agent chooses the service name and environment name from the following data.

**Service name**

The agent chooses the service name from the following options, in priority order:

- **Application Signals instrumentation** – The
  agent sends the service name used by Application Signals. This can be overwritten by
  changing the `OTEL_SERVICE_NAME` environment variable used by supported
  OpenTelemetry instrumentation libraries.
- **CloudWatch agent configuration** – You can [configure the agent](CloudWatch-Agent-configure-related-telemetry.md "CloudWatch-Agent-configure-related-telemetry.md") to use
  a specific service name. This can be configured at the agent, plugin, metrics, logs, or
  log file level.
- **Kubernetes workload name** – For Kubernetes
  workloads, the agent sends the name of the workload for the corresponding pod, in the
  following priority order.
  - Deployment name
  - ReplicaSet name
  - StatefulSet name
  - DaemonSet name
  - CronJob name
  - Job name
  - Pod name
  - Container name

- **Resource tags from instance metadata** – For
  Amazon EC2 workloads, the agent sends the a name from tags, in the following order.

      + service
      + application
      + app

  You must [setup instance metadata](../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS") for the agent to be able to access tags.

- **Default** – If no other service name is found,
  the agent will send the name `Unknown`.
  **Environment name**

The agent chooses the environment name from the following options, in priority
order:

- **Application Signals instrumentation** – The
  agent sends the environment name used by Application Signals. This can be overwritten by
  setting a `deployment.environment` environment variable used by supported
  OpenTelemetry instrumentation libraries. For example, applications may set the environment
  variable
  `OTEL_RESOURCE_ATTRIBUTES=deployment.environment=MyEnvironment`.
- **CloudWatch agent configuration** – You can [configure the agent](CloudWatch-Agent-configure-related-telemetry.md "CloudWatch-Agent-configure-related-telemetry.md") to use
  a specific environment name. This can be configured at the agent, plugin, metrics, logs,
  or log file level.
- **Cluster name and workspace** – For Amazon EKS,
  `eks:`cluster-name`/`Namespace``.
For native Kubernetes running on Amazon EC2,
`k8s:`cluster-name`/`Namespace``.
- **Resource tags from instance metadata** – For
  Amazon EC2 workloads, the agent can will use the `AutoScalingGroup` tag.

You must [setup instance metadata](../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS") for the agent to be able to access tags.

- By default, Amazon EC2 instances that aren't running Kubernetes will get the environment
  name `ec2:default`.
