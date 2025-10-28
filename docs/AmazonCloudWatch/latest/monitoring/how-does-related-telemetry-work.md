# How does CloudWatch find related

telemetry?

The CloudWatch **Explore related** pane shows you metrics and logs that
are related to each other, but how does that work?

Metrics and logs that are sent to CloudWatch can include an optional
_entity_ to which they are related. Typically, the entity will be
a representation of what the telemetry is about. For example, a metric about CPU usage
is about an Amazon EC2 instance, and will use that instance as its entity. When you view that
metric in the **Explore related** pane, it shows you other
telemetry for that same instance.

The _topology map_ (map) in the **Explore
related** pane displays the currently selected resource, along with
_related resources_. For AWS resources, CloudWatch automatically
displays other resources that it knows are related. For example, if you are viewing an
Amazon EC2 instance, the map will also display any Amazon EBS volumes that are attached to the
instance. Selecting a volume shows telemetry for the volume, and the map is updated to
display resources related to the volume. It also displays resources that are part of
the same _service_.

The entity information associated with your telemetry defines the resource that the
telemetry is associated with, such as the Amazon EC2 instance. However, it can also include
contextual data about the resource. For example, if you have a website application that
includes resources such as an Amazon EC2 instance and a database, the entity information can
include the website application as a service. In this case, the topology map shows
the service as a related entity, and when you select it, it displays the instances
and database. This can make finding all the telemetry for a service simpler.

###### Note

CloudWatch must have received telemetry with entity information within the last
three hours in order to find related resources and telemetry.

## Where does the entity

data come from?

There are different ways that CloudWatch gets entities for telemetry:

- Most telemetry sent to CloudWatch from AWS services are associated with resources
  automatically. For a complete list of supported resources, see [AWS services that support related
  telemetry](services-with-related-telemetry.md "services-with-related-telemetry.md").
- The CloudWatch agent automatically adds entity information to the telemetry
  that it sends to CloudWatch.

###### Note

You may need to update your CloudWatch agent to the latest version to include
entity data. For more information, see
[Collect metrics, logs, and traces using the CloudWatch
agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md"), and [Configure CloudWatch agent
service and environment names for related entities](CloudWatch-Agent-configure-related-telemetry.md "CloudWatch-Agent-configure-related-telemetry.md").

- When you are submitting your own telemetry, you can add entity information
  to the data. For more information, see
  [How to add related information to
  custom telemetry sent to CloudWatch](adding-your-own-related-telemetry.md "adding-your-own-related-telemetry.md").
- CloudWatch makes a best effort to recognize the entity information associated with
  other telemetry (for example, custom telemetry that you send to CloudWatch without
  any entity information).

## Where does service data

come from?

Besides recognizing the natural connections between resources, such as an instance
resource and an attached volume resource, CloudWatch can also group resources by
_service_. For example, a service might be a website application.
An Amazon EC2 instance with a web server, and another with a database might both be part
of the same service, and are connected on the topology map based on that
service.

There are different ways that CloudWatch gets a service name for telemetry,
including:

- Application signals or otel instrumented telemetry use the
  `OTEL_SERVICE_NAME` environment variable used by supported
  OpenTelemetry instrumentation libraries to set the service name.
- The CloudWatch agent configuration allows configuring a service name. For more
  information, see [Configure CloudWatch agent
  service and environment names for related entities](CloudWatch-Agent-configure-related-telemetry.md "CloudWatch-Agent-configure-related-telemetry.md").
- Kubernetes workloads use a corresponding name from the cluster, such as the
  Deployment, ReplicaSet, Pod, or Container, for the service name.
- For Amazon EC2 workloads, the service can come from tags (the `service`,
  `application`, or `app` tags).

###### Note

To use tags to generate service names, you must first
[set up instance metadata](../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS") for the Amazon EC2 instance.

- When you are submitting your own telemetry, you can add service information
  to the data. For more information, see
  [How to add related information to
  custom telemetry sent to CloudWatch](adding-your-own-related-telemetry.md "adding-your-own-related-telemetry.md").
- When it cannot use the above, CloudWatch uses the name of the IAM role that sends
  the metrics as the service name. This, for example, can provide a service name
  for Amazon ECS telemetry.
