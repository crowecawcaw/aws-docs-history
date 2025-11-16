# About routing control

Routing control redirects traffic by using health checks in Amazon Route 53 that are configured with DNS records associated with the top-level resource
of the cells in your recovery group, such as an Elastic Load Balancing load balancer. You can redirect traffic from one cell to another, for example, by updating a
routing control state to `Off` (to stop traffic flow to one cell) and updating another routing control state to `On` (to start
traffic flow to another). The process that changes the traffic flow is the Route 53 health check associated with the routing control, after ARC
updates it to set it as healthy or unhealthy, based on the corresponding routing control state.

Routing controls support failover across any AWS service that has a DNS endpoint. You can update routing control states to fail over traffic for
disaster recovery, or when you detect latency drops for your application, or other issues.

You can also configure safety rules for routing control, to make sure that rerouting traffic by using routing controls
doesn't impair availability. For more information, see [Creating safety rules for routing control](routing-control.md "routing-control.md") .

It's important to note that routing controls are not themselves health checks that monitor the underlying health of endpoints.
For example, unlike a Route 53 health check, a routing control doesn't monitor response times or TCP connection times. A routing control is
a simple on-off switch that controls a health check. Typically, you change the state to redirect traffic, and that state change
moves the traffic to go to a particular endpoint for an entire application stack, or prevents routing to the whole application stack.
For example, in a simple scenario, when you change a routing control state from `On` to `Off`, it updates
a Route 53 health check, which you've associated with a DNS failover record to move the traffic off of an endpoint.

##

How to use routing control

To update a routing control state, so that you can reroute traffic, you must connect to one of your cluster endpoints in ARC. If the
endpoint that you try to connect to is unavailable, try changing the state with another cluster endpoint. Your process for changing
routing control states should be prepared to try each endpoint in rotation, since cluster endpoints are cycled
through available and unavailable states for regular maintenance and updates.

When you create routing controls, you configure your DNS records to associate routing control health checks with Route 53 DNS names
that front each application replica. For example, to control traffic failovers across two load balancers, one in each of
two Regions, you create two routing control health checks and associate them with two DNS records, for example, Alias records with
failover routing policies, with the domain names of the respective load balancers.

You can also set up more complex traffic failover scenarios by using ARC routing control together with Route 53 health checks and
DNS record sets, using DNS records with weighted routing policies. To see a detailed example,
see the section on failing over user traffic in the following AWS blog post:
[Building highly resilient applications using Amazon Application Recovery Controller (ARC), Part 2: Multi-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-2-multi-region-stack/ "https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-2-multi-region-stack/")

When you start a failover for an AWS Region using routing control,
because of the steps involved with traffic flow, you might not see traffic move out of the Region
immediately. It also can take a short time for existing, in-progress connections
in the Region to complete, depending on client behavior and connection reuse. Depending on
your DNS settings and other factors, existing connections can complete in just a few minutes, or might
take longer. For more information, see
[Ensuring that traffic shifts finish quickly](route53-arc-best-practices.md#arc-zonal-shift.existing-connections "route53-arc-best-practices.md#arc-zonal-shift.existing-connections").

## Benefits of routing control

A routing control in ARC has several benefits over rerouting traffic with traditional health checks. For example:

- A routing control gives you a way to fail over an entire application stack. This is in
  contrast to failing over individual components of a stack, as Amazon EC2 instances
  do, based on resource-level health checks.
- A routing control gives you a safe, simple manual override that you can use to shift traffic
  to do maintenance or to recover from failures when internal monitors don't detect an issue.
- You can use a routing control together with safety rules to prevent common side effects that can happen
  with fully automated health check-based automation, such as failing over to standby infrastructure that isn't prepared
  for failover.

Here's an example of incorporating routing controls into your failover strategy,
to improve the resilience and availability of your applications in AWS.

You can support highly available AWS applications on AWS by running multiple (typically three) redundant replicas across
Regions. Then you can use Amazon Route 53 routing control to route traffic to the appropriate replica.

For example, you can set up one application replica to be active and serve application traffic, while another is a standby replica. When
your active replica has failures, you can reroute user traffic there to restore availability to your application. You should decide whether
to fail away from or to a replica based on information from your monitoring and health check systems.

If you want to enable faster recoveries, another option that you can choose for your architecture is an active-active implementation.
With this approach, your replicas are active at the same time. This means that you can recover from failures by
moving users away from an impaired application replica by just rerouting traffic to another active replica.
