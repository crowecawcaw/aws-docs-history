

# How resolved IP validation works
<a name="route53-resolved-ip-validation-how-it-works"></a>

When a resource in your VPC resolves a domain through the Amazon Route 53 Resolver, the resolver records the resulting IP addresses for that domain. Network Firewall validates a connection's destination IP address against those recorded resolutions. The validation scope is the set of VPCs that are associated with the Amazon Route 53 Resolver DNS Firewall rule group that you reference in the policy.

The rule group defines the validation scope. Every VPC that is associated with it contributes its resolutions to a single shared pool, and the firewall validates against that whole pool. This includes VPCs that are associated with the rule group but don't send traffic through this firewall. A destination IP address that any associated VPC resolved for a domain is considered resolved for all of them. For more information about scoping the rule group, see [Recommendations for configuring resolved IP validation](route53-resolved-ip-validation-recommendations.md).

Validation happens at two levels:
+ At the **policy level**, resolved IP validation checks that the destination IP address was resolved for some domain in an associated VPC. It then applies the policy's enforcement action to connections that fail the check. This check is independent of the specific domain.
+ At the **rule level**, a rule that uses the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type or the `aws_route_53_resolved_domain` keyword matches connections whose destination IP address was resolved for specific domains.

Network Firewall evaluates resolved IP validation once for each connection, on the connection's first packet. The evaluation uses the connection's source IP address, which must be in the configured scope, and its destination IP address. The result applies for the life of the connection, in the connection's originating (client-to-server) direction.

Resolutions are recorded for each Availability Zone, and validation is scoped to the zone. A firewall endpoint validates against the resolutions recorded in its own Availability Zone. You can deploy across multiple Availability Zones, but traffic must stay within its zone. A client in one Availability Zone must reach the firewall endpoint in that same zone. A connection can cross zones to reach a firewall endpoint. In that case, the firewall can't tell that the client is in a different zone. The connection fails validation as unresolved, and Network Firewall applies your `Action` setting to it. The exception is a transit gateway-attached firewall, which carries the client's zone with the traffic. Use this approach for centralized deployments that inspect traffic from multiple zones. For more information, see [Transit gateway-attached firewalls](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall.html). For configuration recommendations, see [Recommendations for configuring resolved IP validation](route53-resolved-ip-validation-recommendations.md).

For instructions on setting up resolved IP validation, see [Getting started with resolved IP validation](route53-resolved-ip-validation-getting-started.md).