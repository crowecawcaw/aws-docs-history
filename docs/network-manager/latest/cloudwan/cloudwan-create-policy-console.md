# Create an AWS Cloud WAN core network policy version

using the console

Use the Network Manager console to create a core network policy version. The console provides
separate tabs for you to configure a network policy version, including the new routing policy capabilities. The following steps describe
the high-level process.

1. [Configure the core network settings in an AWS Cloud WAN policy
   version](cloudwan-core-network-config.md "cloudwan-core-network-config.md").

You'll first set the network configuration parameters, including adding ASN
ranges, CIDR blocks, and the edge locations to include in the policy. 2. [Add a segment to an AWS Cloud WAN core network policy version](cloudwan-policy-segments.md "cloudwan-policy-segments.md").

After defining the network configuration parameters, you'll add network segments
and define the behavior for those segments. For example, you might want to include a
segment that requires attachment acceptance. 3. [Create a network function group in
an AWS Cloud WAN policy version](cloudwan-policy-network-function-groups.md "cloudwan-policy-network-function-groups.md").

The network function group provides an added level of security if you want to
first steer specific segments to a third-party security device or an Inspection VPC.
A network function group is the parent object for the segments you want to route to
security appliances. 4. [Create an AWS Cloud WAN route policy and rule](cloudwan-route-policy.md "cloudwan-route-policy.md").

Create routing policies with rules that define how routes are filtered, summarized, or modified based on specific conditions and actions. 5. [Add segment actions in an AWS Cloud WAN
core network policy version](cloudwan-policy-network-actions-routes.md "cloudwan-policy-network-actions-routes.md").

Define segment actions, such as sharing a segment, creating a segment route, edge location route policy associations, or
creating a service insertion action for the network function group. 6. [Create an AWS Cloud WAN attachment routing policy](cloudwan-policy-attachment-routing.md "cloudwan-policy-attachment-routing.md").

Create attachment routing policies with rules that define how attachments are associated to routing policies. 7. [Create an attachment policy in an AWS Cloud WAN core
network policy version](cloudwan-policy-attachments.md "cloudwan-policy-attachments.md").

Finally, you'll create an attachment policy that defines the order when segments or
network function groups should be run in the core network policy.

###### Topics

- [Configure the core network settings](cloudwan-core-network-config.md "cloudwan-core-network-config.md")
- [Add a segment](cloudwan-policy-segments.md "cloudwan-policy-segments.md")
- [Create a network function group](cloudwan-policy-network-function-groups.md "cloudwan-policy-network-function-groups.md")
- [Add a segment action](cloudwan-policy-network-actions-routes.md "cloudwan-policy-network-actions-routes.md")
- [Create a core network attachment policy](cloudwan-policy-attachments.md "cloudwan-policy-attachments.md")
- [Create a route policy and
  rule](cloudwan-route-policy.md "cloudwan-route-policy.md")
- [Create an attachment routing policy](cloudwan-policy-attachment-routing.md "cloudwan-policy-attachment-routing.md")
