# AWS Region availability for routing control

For detailed information about Regional support and service endpoints for Amazon Application Recovery Controller (ARC),
see [Amazon Application Recovery Controller (ARC)
endpoints and quotas](../../../general/latest/gr/r53arc.md "../../../general/latest/gr/r53arc.md") in the _Amazon Web Services General Reference_.

###### Note

Routing control in Amazon Application Recovery Controller (ARC) is a global feature. However, you must specify the US West (Oregon)
Region (specify the parameter `--region us-west-2`) in Regional ARC AWS CLI commands. That is, when
you create resources such as clusters, control panels, or routing controls.

A ARC routing control is an on/off switch that changes the state of a ARC health check,
which can then be associated with a DNS record that redirects traffic, for example, from a primary to a standby deployment replica.

If there's an application failure or latency issue, you can update routing control states to shift traffic from your primary replica to, for
example, a standby replica. By using the highly reliable ARC data plane API operations to make routing control queries and routing control state
updates, you can rely on ARC for failover during disaster recovery scenarios. For more information, see [Getting and updating routing control states using the ARC API (recommended)](routing-control.update.md "routing-control.update.md").

ARC maintains routing control states in a _cluster_, which is a set of five redundant Regional endpoints. ARC
propagates routing control state changes across the cluster, which is located in an Amazon EC2 fleet, to get a quorum across five AWS Regions.
After propagation, when you query ARC for a routing control state, using the API and the highly-reliable data plane,
it returns the consensus view.

You can interact with any one of the five cluster endpoints to update the state of a routing control from, for example, `Off`
to `On`. Then ARC propagates the update across the five Regions of the cluster.

Data consistency across all five cluster endpoints is achieved within 5 seconds on average, and after no more than 15 seconds maximum.

ARC offers extreme reliability with its data plane for you to manually fail over your application across cells. ARC ensures that at
least three out of the five cluster endpoints are always accessible to you to perform routing control state changes. Note that each ARC cluster is
single-tenant, to ensure that you're not affected by "noisy neighbors" that might slow down your access patterns.

When you make changes to routing control states, you rely on the following three criteria, which are highly unlikely to fail:

- At least three of your five endpoints are available and take part in the quorum.
- You have working IAM credentials and can authenticate against a working Regional cluster endpoint.
- The Route 53 data plane is healthy (this data plane is designed to meet a 100% availability SLA).
