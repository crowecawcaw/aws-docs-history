# Target groups for your Gateway Load Balancers

Each _target group_ is used to route requests to one or more registered
targets. When you create a listener, you specify a target group for its default action.
Traffic is forwarded to the target group that's specified in the listener rule. You can
create different target groups for different types of requests.

You define health check settings for your Gateway Load Balancer on a per target group basis. Each target
group uses the default health check settings, unless you override them when you create the
target group or modify them later on. After you specify a target group in a rule for a
listener, the Gateway Load Balancer continually monitors the health of all targets registered with the
target group that are in an Availability Zone enabled for the Gateway Load Balancer. The Gateway Load Balancer routes
requests to the registered targets that are healthy. For more information, see [Health checks for Gateway Load Balancer target groups](health-checks.md "health-checks.md").

###### Contents

- [Routing configuration](#target-group-routing-configuration "#target-group-routing-configuration")
- [Target type](#target-type "#target-type")
- [Registered targets](#registered-targets "#registered-targets")
- [Target group attributes](#target-group-attributes "#target-group-attributes")
- [Create a target group](create-target-group.md "create-target-group.md")
- [Configure health checks](health-checks.md "health-checks.md")
- [Edit target group attributes](edit-target-group-attributes.md "edit-target-group-attributes.md")
- [Register targets](target-group-register-targets.md "target-group-register-targets.md")
- [Tag a target group](target-group-tags.md "target-group-tags.md")
- [Delete a target group](delete-target-group.md "delete-target-group.md")

## Routing configuration

Target groups for Gateway Load Balancers support the following protocol and port:

- **Protocol**: GENEVE
- **Port**: 6081

The Gateway Load Balancer encapsulates the original packets using GENEVE. The GENEVE header
uses a Type-Length-Value (TLV) format to store information, using Option Class
0x0108. Appliances must decapsulate the TLV pairs to process the original packets.
For more information, see the following blog post: [Integrate your appliance with a Gateway Load Balancers](https://aws.amazon.com/blogs/networking-and-content-delivery/integrate-your-custom-logic-or-appliance-with-aws-gateway-load-balancer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/integrate-your-custom-logic-or-appliance-with-aws-gateway-load-balancer/").

## Target type

When you create a target group, you specify its target type, which determines how you
specify its targets. After you create a target group, you cannot change its target
type.

The following are the possible target types:

`instance`

The targets are specified by instance ID.

`ip`

The targets are specified by IP address.

When the target type is `ip`, you can specify IP addresses from one of the
following CIDR blocks:

- The subnets of the VPC for the target group
- 10.0.0.0/8 ([RFC
  1918](https://tools.ietf.org/html/rfc1918 "https://tools.ietf.org/html/rfc1918"))
- 100.64.0.0/10 ([RFC
  6598](https://tools.ietf.org/html/rfc6598 "https://tools.ietf.org/html/rfc6598"))
- 172.16.0.0/12 (RFC 1918)
- 192.168.0.0/16 (RFC 1918)

###### Important

You can't specify publicly routable IP addresses.

## Registered targets

Your Gateway Load Balancer serves as a single point of contact for clients, and distributes incoming
traffic across its healthy registered targets. Each target group must have at least one
registered target in each Availability Zone that is enabled for the Gateway Load Balancer. You can
register each target with one or more target groups.

If demand increases, you can register additional targets with one or more target
groups in order to handle the demand. The Gateway Load Balancer starts routing traffic to a newly
registered target as soon as the registration process completes.

If demand decreases, or you need to service your targets, you can deregister targets
from your target groups. Deregistering a target removes it from your target group, but
does not affect the target otherwise. The Gateway Load Balancer stops routing traffic to a target as
soon as it is deregistered. The target enters the `draining` state until
in-flight requests have completed. You can register the target with the target group
again when you are ready for it to resume receiving traffic.

## Target group attributes

You can use the following attributes with target groups:

`deregistration_delay.timeout_seconds`

The amount of time for ELB to wait before changing the state of a
deregistering target from `draining` to `unused`. The
range is 0-3600 seconds. The default value is 300 seconds.

`stickiness.enabled`

Indicates whether configurable flow stickiness is enabled for the target
group. The possible values are `true` or `false`. The
default is false. When the attribute is set to `false`, 5_tuple
is used.

`stickiness.type`

Indicates the type of the flow stickiness. The possible values for target
groups associated to Gateway Load Balancers are:

- `source_ip_dest_ip`
- `source_ip_dest_ip_proto`

`target_failover.on_deregistration`

Indicates how the Gateway Load Balancer handles existing flows when a target is
deregistered. The possible values are `rebalance` and
`no_rebalance`. The default is `no_rebalance`. The
two attributes (`target_failover.on_deregistration` and
`target_failover.on_unhealthy`) can't be set independently.
The value you set for both attributes must be the same.

`target_failover.on_unhealthy`

Indicates how the Gateway Load Balancer handles existing flows when a target is unhealthy.
The possible values are `rebalance` and
`no_rebalance`. The default is `no_rebalance`. The two
attributes (`target_failover.on_deregistration` and
`target_failover.on_unhealthy`) cannot be set independently.
The value you set for both attributes must be the same.

For more information, see [Edit target group attributes](edit-target-group-attributes.md "edit-target-group-attributes.md").
