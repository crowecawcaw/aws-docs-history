# AWS Cloud Map service health check

configuration

Health checks help determine whether service instances are healthy or not. If you
don't configure a health check during service creation, traffic will be routed to
service instances regardless of the instances' health status. When you configure a
health check, AWS Cloud Map returns healthy resources by default. You can use the `HealthStatus` parameter of the `DiscoverInstances` API
to filter resources by health status and get a list of unhealthy resources. You can also
use the `GetInstancesHealthStatus` API to retrieve the health status of a
particular service instance.

You can either configure a Route 53 health check or a custom, third-party health check
when you create an AWS Cloud Map service.

## Route 53 health checks

If you specify settings for an Amazon Route 53 health check, AWS Cloud Map creates a Route 53
health check whenever you register an instance and deletes the health check when you
deregister the instance.

For public DNS namespaces, AWS Cloud Map associates the health check with the Route 53
record that AWS Cloud Map creates when you register an instance.If you specify both
`A` and `AAAA` record types in a service's DNS
configuration, AWS Cloud Map creates a health check that uses the IPv4 address to check the
health of the resource. If the endpoint that's specified by the IPv4 address is
unhealthy, Route 53 considers both the `A` and `AAAA` records to
be unhealthy. If you specify a `CNAME` record type in a service's DNS
configuration, you can't configure a Route 53 health check.

For namespaces that you use API calls to discover instances for, AWS Cloud Map
creates a Route 53 health check. However, there's no DNS record for AWS Cloud Map to
associate the health check with. To determine whether a health check is healthy, you
can configure monitoring using either the Route 53 console or using Amazon CloudWatch. For more
information about using the Route 53 console, see [Get Notified When a Health Check Fails](../../../Route53/latest/DeveloperGuide/health-checks-creating-values.md#health-checks-creating-values-alarm "../../../Route53/latest/DeveloperGuide/health-checks-creating-values.md#health-checks-creating-values-alarm") in the
_Amazon Route 53 Developer Guide_. For more information about using CloudWatch, see
[PutMetricAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md") in the
_Amazon CloudWatch API Reference_.

###### Note

- You can't configure an Amazon Route 53 health check for a service created in
  a private DNS namespace.
- A Route 53 health checker in each health-checking AWS Region sends a
  health check request to an endpoint every 30 seconds. On average, your
  endpoint receives a health check request about every two seconds.
  However, health checkers don't coordinate with one another. Therefore,
  you might sometimes see several requests in one second that's followed
  by a few seconds with no health checks at all. For a list of
  health-checking regions, see [Regions](../../../Route53/latest/APIReference/API_HealthCheckConfig.md#Route53-Type-HealthCheckConfig-Regions "../../../Route53/latest/APIReference/API_HealthCheckConfig.md#Route53-Type-HealthCheckConfig-Regions").

For information about the charges for Route 53 health checks, see [Route 53 Pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

## Custom health checks

If you configure AWS Cloud Map to use a custom health check when you register an
instance, you must use a third-party health checker to evaluate the health of your
resources. Custom health checks are useful in the following circumstances:

- You can't use a Route 53 health check because the resource isn't available
  over the internet. For example, suppose that you have an instance that's
  located in an Amazon VPC. You can use a custom health check for this instance.
  However, for the health check to work,your health checker must also be in
  the same VPC as your instance.
- You want to use a third-party health checker regardless of where your
  resources are.

When you use a custom health checks, AWS Cloud Map doesn't check the health of a given
resource directly. Instead, the third-party health checker checks the health of the
resource and returns a status to your application. Your application will then need
to submit a `UpdateInstanceCustomHealthStatus` request that relays this
status to AWS Cloud Map. If the initial status relayed is `UNHEALTHY`, and if
there isn't another `UpdateInstanceCustomHealthStatus` within 30 seconds that
relays a status of `HEALTHY`, the resource is confirmed to be unhealthy.
AWS Cloud Map stops routing traffic to that resource.
