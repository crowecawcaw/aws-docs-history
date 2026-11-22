

# How a NAT/Proxy firewall works

A NAT/Proxy firewall has one Amazon Resource Name (ARN) and one proxy hostname, and runs in one or more Availability Zones of a single VPC. In each Availability Zone, the firewall has one firewall endpoint and one NAT gateway that Network Firewall created for it. Network Firewall also creates Route 53 private hosted zones so that the proxy hostname resolves inside the VPC.

![The diagram shows a NAT/Proxy firewall that comes attached with a NAT gateway, with firewall endpoints created in VPCs that send traffic to the firewall, which filters the traffic and sends it out through the attached NAT gateway.](https://docs.aws.amazon.com/network-firewall/latest/developerguide/images/nfw-proxy-architecture.png)


**Explicit proxy traffic**  
A client sends an HTTP or HTTPS proxy request to the proxy hostname on a listener port. The hostname resolves to the firewall endpoint in the client's own Availability Zone. The firewall evaluates the request against the firewall policy. If the policy allows the request, the firewall opens a connection to the destination through the NAT gateway in the same Availability Zone. The destination sees the NAT gateway's IP address, not the client's.

**Non-proxy traffic**  
Traffic that your VPC route tables send to the firewall endpoint, and that isn't addressed to a proxy listener, is inspected the same way that a routed firewall inspects traffic. What happens after inspection depends on the firewall's **Enable NAT on non-proxy traffic** setting:
+ **Enabled** (default) – The firewall sends allowed traffic out through the Availability Zone's NAT gateway, which replaces the source IP address. In the API, this is the `TransparentFilteringNatScope` value `NAT_ALL`.
+ **Disabled** – The firewall returns allowed traffic to the firewall endpoint without address translation, and your VPC route tables deliver it. In the API, this is the `TransparentFilteringNatScope` value `NAT_NONE`.

You set this option when you create the firewall, and you can't change it afterward.

**Firewall policies and rules**  
A NAT/Proxy firewall can use either a Next Generation policy or a Classic Network Firewall policy, including custom, AWS managed, and partner rule groups. For a comparison of the policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).
+ With a Classic Network Firewall policy, the stateful rules engine evaluates explicit proxy traffic (HTTP `CONNECT` requests). Stateless rules don't inspect explicit proxy traffic. Stateless rules still apply to non-proxy traffic.
+ With a Next Generation policy, the firewall engine and the IPS engine evaluate explicit proxy traffic the same way they evaluate other traffic.
+ TLS inspection works with proxy traffic. For information about TLS inspection, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md).
+ A NAT/Proxy firewall supports TLS inspection across multiple firewall endpoints within the same account. For information about TLS inspection across multiple endpoints, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md).
+ A NAT/Proxy firewall supports TLS inspection on selected domains. For information about TLS inspection on selected domains, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md).
+ A NAT/Proxy firewall keeps the client's endpoint for proxied traffic, so you can filter traffic by the VPC that contains the firewall endpoint it entered through. For more information, see [Filtering traffic by firewall endpoint VPC](stateful-rule-groups-endpoint-vpc.md).

**Differences from routed firewall**  
The following are the main differences between a NAT/Proxy firewall and a routed firewall.


| Area | Routed firewall | NAT/Proxy firewall | 
| --- | --- | --- | 
| Client source IP address | Preserved | Replaced by the NAT gateway's IP address for proxy traffic, and for non-proxy traffic when NAT on non-proxy traffic is enabled | 
| NAT gateways | You create and route through your own NAT gateways or internet gateway | Network Firewall creates one NAT gateway in each Availability Zone | 
| How traffic reaches the firewall | VPC route tables | Proxy settings on the client for explicit proxy traffic; VPC route tables for non-proxy traffic | 
| Proxy hostname | None | One hostname per firewall | 
| Attachment | VPC or transit gateway | VPC only | 

**When to use a NAT/Proxy firewall**  
Use a NAT/Proxy firewall when you want the firewall to act as an explicit proxy that terminates and re-establishes connections on behalf of clients, when you want a single managed component for filtering and network address translation, or when you want to simplify routing for HTTP and HTTPS traffic. If you need to preserve the client source IP address, or if you want to attach the firewall to a transit gateway, use a routed firewall.