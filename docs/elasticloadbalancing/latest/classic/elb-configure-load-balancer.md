# Configure your Classic Load Balancer

After you create a Classic Load Balancer, you can change its configuration. For example, you can update
the load balancer attributes, subnets, and security groups.

###### Load balancer attributes

[Connection draining](config-conn-drain.md "config-conn-drain.md")

If enabled, the load balancer allows existing requests to complete before the
load balancer shifts traffic away from a deregistered or unhealthy instance.

[Cross-zone load balancing](enable-disable-crosszone-lb.md "enable-disable-crosszone-lb.md")

If enabled, the load balancer routes the request traffic evenly across all instances
regardless of the Availability Zones.

[Desync migitation mode](config-desync-mitigation-mode.md "config-desync-mitigation-mode.md")

Determines how the load balancer handles requests that might pose a security
risk to your application. The possible values are `monitor`,
`defensive`, and `strictest`. The default is `defensive`.

[Idle timeout](config-idle-timeout.md "config-idle-timeout.md")

If enabled, the load balancer allows the connections to remain idle (no data
is sent over the connection) for the specified duration. The default is 60 seconds.

[Sticky sessions](elb-sticky-sessions.md "elb-sticky-sessions.md")

Classic Load Balancers support both duration-based and application-based session stickiness.

###### Load balancer details

[Security groups](elb-vpc-security-groups.md "elb-vpc-security-groups.md")

The security groups for your load balancer must allow traffic on the listener and
health check ports.

[Subnets](elb-manage-subnets.md "elb-manage-subnets.md")

You can expand the ability of your load balancer to additional subnets.

[Proxy protocol](enable-proxy-protocol.md "enable-proxy-protocol.md")

If enabled, we add a header with connection information that is sent to the instance.

[Tags](add-remove-tags.md "add-remove-tags.md")

You can add tags to categorize your load balancres.
