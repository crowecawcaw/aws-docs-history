

# Working with existing architectures

Automated internet firewall works with your existing architecture on day one, without requiring route changes. The default filtering policy is the same for all connectivity paths.

## Day one behavior with flexible connectivity
<a name="internet-gateway-firewall-day-one-behavior"></a>

When you deploy automated internet firewall with flexible connectivity, it handles existing resources based on their current IP configuration:


**Day one behavior with flexible connectivity**  

| Resource type | Day one behavior | 
| --- | --- | 
| Has a public IP address (EIP) | Automated internet firewall filters this traffic. The resource retains its public IP address and has bidirectional connectivity. | 
| Behind an existing NAT gateway | Automated internet firewall filters this traffic and does not re-NAT it. The resource retains the NAT gateway IP address as its source. | 
| No public IP address, no NAT gateway | The resource gets new outbound-only connectivity through the native NAT of automated internet firewall. See the following important note. | 

**Important**  
In flexible mode, the firewall provides outbound-only connectivity through its native NAT to resources that have no public IP address. As a result, a subnet whose route table already sends internet traffic to the internet gateway gains outbound internet access even if its resources have no public IP address and there is no NAT gateway. A subnet that has no route to the internet gateway stays isolated and is unaffected. If you have subnets that are intentionally isolated and you do not want this, set their connectivity type to exclude before you create the deployment. For more information about connectivity types, see [Subnet connectivity types](internet-gateway-firewall-how-it-works.md#internet-gateway-firewall-connectivity-types).

## Optional route updates
<a name="internet-gateway-firewall-optional-route-updates"></a>

Nothing is required at launch. You can make route updates later, at your own pace, to simplify your architecture. Route updates can provide the following benefits:

1. **Remove redundant NAT gateways.** After you remove a NAT gateway from the path, traffic from those resources shifts to the native NAT of automated internet firewall. Update the subnet route table to remove the NAT gateway route; automated internet firewall handles egress automatically. The NAT IP address changes from your NAT gateway IP address to an IP address that automated internet firewall assigns (or one from your IPAM pool, if you configured one).

1. **Remove redundant inline firewalls.** If you have existing Network Firewall endpoints attached to a transit gateway for internet traffic inspection, automated internet firewall can replace that function. You can remove the transit gateway-attached Network Firewall endpoints and the associated routing after you validate equivalent rule coverage in your automated internet firewall policy.

1. **Enable source IP address preservation.** Removing NAT gateways from the path preserves the original source IP address on traffic from resources that have a public IP address (bidirectional connectivity). This is useful for custom rules that match on source IP address. Outbound-only traffic still undergoes NAT, so source preservation applies only to the bidirectional path.