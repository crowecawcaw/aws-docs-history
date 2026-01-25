# Ensure health check access for your accelerator

Each listener for a standard accelerator routes requests only to healthy, active endpoints.
When you add an endpoint, it must pass a health check to be considered healthy.
AWS Global Accelerator also regularly sends health check requests to all endpoints on standard accelerators, to test their status.
Global Accelerator automatically runs these regular health checks. After each health check is completed, the
listener closes the connection that was established for the health check.

Note that if there aren't any healthy endpoints to route traffic to, Global Accelerator routes incoming
client requests to _all_ endpoints in the endpoint group. For more information, see
[How failover works for unhealthy endpoints](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md").

Details about how health checks work, and guidance about using health checks, depends
on the type of endpoint resource.

This topic provides information about how to work with health checks for different endpoint types, including steps
for updating health check options in Global Accelerator (applies to EC2 instance or Elastic IP address endpoints).

## Ensure access for your accelerator health checks

To ensure access for health checks to complete successfully
for EC2 instance or Elastic IP address endpoints, make sure that your router and firewall rules allow inbound
traffic from the IP addresses associated with Amazon Route 53 health checkers. To see the list of IP address ranges
associated with Route 53 health checkers, see [IP address ranges
of Route 53 servers](../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md "../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md") in the _Amazon Route 53 Developer Guide_.

Global Accelerator health checks work by receiving traffic for Route 53 health checks, which is forwarded to the
configured health check port for the endpoint group. Typically,
the ports configured for health checks match the listener configuration. If you configure a different
port for health checks instead, review your security group configuration to make sure that you don't
allow public traffic on the port.

For example, if your listener is configured on port 80, then your health check port is also 80. If you
choose to configure health ports on another port, for example, port 83, then make sure that
you configure your security groups to allow traffic on port 83 only from IP addresses that are in the
IP address range for Route 53 health checks.

## Health check guidance for different

endpoint types

Review the information in this section for guidelines about the health checks that
you specify for each endpoint type for your accelerator.

In addition, make sure that the health checks that you choose for endpoints with HTTP workloads are
representative of the overall health of your application, and that you follow the guidance for ensuring
access to health checks that is described in the preceding section,
[Ensure security and access for health checks](#GAX-HCsecurityaccessguidance "#GAX-HCsecurityaccessguidance").

The following guidelines apply to each specified endpoint type:

- For Network Load Balancer or Application Load Balancer endpoints, be aware of the following:
  - The [health check options](#GAX-HCsetoptions "#GAX-HCsetoptions")
    that you choose in Global Accelerator do not affect Network Load Balancers or Application Load Balancers that you've added as endpoints.
    That is, health check options that you specify in Global Accelerator are used for Amazon EC2 and
    Elastic IP address health checks, but not for health checks on load balancer endpoints.

  For load balancer endpoints, configure health checks by using Elastic Load Balancing configuration options.
  For more information, see [Health checks for your target groups](../../../elasticloadbalancing/latest/network/target-group-health-checks.md "../../../elasticloadbalancing/latest/network/target-group-health-checks.md").
  - Global Accelerator considers an Application Load Balancer healthy if every target group has at least one healthy target. For more information,
    see [Health checks for your target groups](../../../elasticloadbalancing/latest/network/target-group-health-checks.md "../../../elasticloadbalancing/latest/network/target-group-health-checks.md").
  - Global Accelerator considers a Network Load Balancer healthy if there is at least one healthy Availability Zone. An Availability Zone
    is healthy if it has a healthy target in all load balancer target groups that it is in.

  Be aware that when you enable cross-zone load balancing, healthy targets in Network Load Balancer target groups
  contribute to the health of the target group in all Availability Zones. This is how Global Accelerator evaluates the
  health of an AZ in a target group regardless of which AZs are actually healthy. This means that with
  cross-zone load balancing, if every target group contains a healthy target, Global Accelerator considers the Network Load Balancer to
  be healthy. However, at all times, Global Accelerator only considers a Network Load Balancer healthy if the number of healthy
  targets meets the Network Load Balancer minimum healthy target count setting, `minimum_healthy_targets`.

- For EC2 instance or Elastic IP address endpoints, be aware of the following:
  - When you add EC2 instance or Elastic IP address endpoints to a listener
    configured with TCP, you can specify the port to use for health checks. By default, if you don't
    specify a port for health checks, Global Accelerator uses the listener port that you specified for your accelerator.
  - When you add these endpoint types with a UDP listener, Global Accelerator uses the
    listener port and the TCP protocol for health checks, so you must have a TCP server on your endpoint.

  Make sure to check that the port that you've configured for the TCP server on each
  endpoint is the same as the port that you specify for the health check in Global Accelerator. If the port
  numbers aren't the same, or if you haven't set up a TCP server for the endpoint, Global Accelerator marks
  the endpoint as unhealthy, regardless of the endpoint's health.
  - Make sure to follow the [guidance for security and access](#GAX-HCsecurityaccessguidance "#GAX-HCsecurityaccessguidance")
    when you configure ports for health checks for your EC2 instance or Elastic IP address endpoints.

## Set health check options

To set health check options for your accelerator, specify one or more of
the following options when you create an accelerator or when you edit an endpoint group.

You can add the following health check options for an endpoint group.

**Health check port**
The port to use when Global Accelerator performs health checks on endpoints that are part of this endpoint group.

Note that you can't set a port override for health check ports.

**Health check protocol**
The protocol to use when Global Accelerator performs health checks on endpoints that are part of this endpoint group.

**Health check interval**
The interval, in seconds, between each health check for an endpoint.

**Threshold count**
The number of consecutive health checks required before considering an unhealthy target healthy or
a healthy target unhealthy.
