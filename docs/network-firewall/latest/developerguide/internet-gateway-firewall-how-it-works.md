

# How Automated Internet Firewall works

Automated internet firewall allows you to configure Network Firewall with native NAT functionality at the internet gateway of all the VPCs in your environment. You can use automated internet firewall to centrally define Network Firewall policy and enforce it across the internet gateway of every VPC in your environment. You do not have to make any routing or architectural changes to deploy it, and it automatically expands across new VPCs and subnets. Because it is configured at the internet gateway, individual VPC owners who do not have the proper privileges cannot bypass these controls by manipulating routes.

## How traffic is inspected
<a name="internet-gateway-firewall-traffic-inspection"></a>

Every connection into or out of an in-scope VPC passes through the firewall before it reaches the internet or one of your resources. The firewall sits inline at the internet gateway, so the traffic itself flows through it rather than past a copy or a sample of it.

The firewall checks each connection against the Network Firewall rules in the policy that applies to that VPC, then acts based on the policy's mode:
+ In enforce mode, the firewall drops traffic that matches a block or drop rule and lets the rest continue to its destination.
+ In monitor mode, the firewall still evaluates every connection and logs it, but it doesn't block anything. This lets you observe the impact of a policy before you turn on enforcement.

Outbound traffic gets one extra step. For subnets that use outbound-only or flexible connectivity, the firewall performs network address translation (NAT) on IPv4 traffic after it finishes inspection. A subnet's connectivity type decides both whether its resources can receive inbound connections and whether their outbound traffic is translated this way.

Because inspection happens at the internet gateway rather than at a hop reached through a route table, no change to a subnet or gateway route entry inside the VPC can route traffic around the firewall. This ensures that all intended internet traffic is inspected.

## Important concepts
<a name="internet-gateway-firewall-scope-policy-deployment"></a>

Automated internet firewall uses five resource types that fit together in a hierarchy: *NSM rules* and *NSM templates* are combined into *NSM policies*, and a *deployment* joins an NSM policy to a *scope*. The following definitions describe each resource type.

**NSM rule** – The atomic unit of configuration. Each NSM rule carries one setting, and there are two kinds. A traffic inspection rule sets the Network Firewall rule groups the firewall uses to inspect traffic; you reference one of the AWS managed rule groups or a rule group you create. A firewall configuration rule sets an operational property instead, such as the policy mode (monitor or enforce), the default action, or the logging configuration. A Network Firewall rule group is referenced only inside a traffic inspection rule; the NSM rule is the managed object that carries that configuration into a policy.

**NSM template** – A reusable group of *NSM rules* that you can share across multiple *NSM policies*. Templates are optional.

**NSM policy** – A combination of *NSM templates* and *NSM rules* that automated internet firewall applies at the internet gateway. A policy also sets the default subnet connectivity type — bidirectional, outbound-only, or flexible. To apply different rules to different VPCs, create separate policies.

**Scope** – A declarative selection of the VPCs to protect. A scope can be your entire organization, specific organizational units (OUs), an account, or specific VPCs.

**Deployment** – A binding of an *NSM policy* to a *scope*. When you create a deployment, Network Security Manager creates and maintains a per-VPC firewall for each in-scope VPC, and extends protection to new VPCs that match the scope automatically.

## Subnet connectivity types
<a name="internet-gateway-firewall-connectivity-types"></a>

A subnet's connectivity type is the single setting that decides how the resources in that subnet reach the internet, and how the internet can reach them. It controls two things at once: whether resources in the subnet can accept inbound connections from the internet, and whether automated internet firewall applies NAT to their outbound traffic. You set one default connectivity type in your policy, and you can override it for specific subnets, which you identify by ARN or by tags. When a subnet matches more than one override, the override listed first applies.

Automated internet firewall offers three connectivity types for everyday use — outbound-only, bidirectional, and flexible. We recommend flexible, because it adapts to each resource and works for all kinds of workloads. Two more types complete the set: exclude, which you choose to leave a subnet out of inspection, and az-unsupported, which automated internet firewall assigns on its own. The following table explains each one.


**Automated Internet Firewall connectivity types**  

| Connectivity type | Explanation | 
| --- | --- | 
| bidirectional | Bidirectional. Resources with a public IP address can connect to filtered destinations on the internet and accept filtered connections from the internet. All traffic is inspected. Resources without a public IP address in these subnets cannot reach the internet. | 
| outbound-only | Outbound only. Unsolicited inbound traffic from the internet is dropped. All traffic is inspected. For IPv4 traffic, automated internet firewall performs NAT after inspection. For IPv6 traffic, no NAT is performed. To control which IP addresses are used for NAT, see [NAT for outbound traffic](#internet-gateway-firewall-nat-outbound). | 
| flexible (recommended default) | Per resource, based on IP assignment and routing. A resource with a public IP address gets bidirectional connectivity only when its subnet routes to the internet gateway; if the subnet routes to a NAT gateway, the resource is outbound-only even with a public IP. A resource without a public IP address gets outbound-only connectivity through the firewall's native NAT. | 
| exclude | No inspection. Traffic bypasses automated internet firewall. Use this to exclude specific subnets from inspection. | 
| az-unsupported | No inspection. Assigned automatically to subnets in Availability Zones where automated internet firewall is not supported. Automated internet firewall is not supported in Local Zones, and it is built only in the Availability Zones where AWS Network Firewall is available. | 

**Traffic flow by connectivity type**

![Traffic flow for each subnet connectivity type — bidirectional, outbound-only, flexible, and exclude — through automated internet firewall at the internet gateway.](https://docs.aws.amazon.com/network-firewall/latest/developerguide/images/aif-connectivity-types.png)


### NAT for outbound traffic
<a name="internet-gateway-firewall-nat-outbound"></a>

You just saw that outbound-only and flexible subnets have their outbound traffic translated. Here is how that translation works, and how you can control the addresses it uses.

Automated internet firewall performs network address translation (NAT) natively, so you don't configure a separate NAT gateway for it. By default, AWS allocates the public IPv4 addresses used for NAT automatically. If you'd rather control those addresses, you can bring your own IP address range (BYOIP), or request a contiguous IP block from AWS, and have automated internet firewall use addresses from that range for outbound communications. This native NAT applies to flexible and outbound-only subnets. IPv4 traffic is translated with NAT. In preview, automated internet firewall does not perform NAT64. To provide NAT64 functionality for IPv6 traffic that is destined for IPv4 servers, you must use a NAT gateway separately.

Automated internet firewall configures separate NAT IP addresses for each VPC, so traffic from different VPCs might leave with different NAT IP addresses.

Flexible connectivity has a deliberate exception. The firewall always filters the traffic, but it does not always perform NAT. If a resource already has a public IP address, or if its traffic comes from a NAT gateway, the firewall leaves the addressing alone, and the traffic keeps the NAT gateway IP address as its source. This is the day-one behavior for existing architectures, so nothing breaks when you first deploy. Later, at your own pace, you can remove the NAT gateway from the path and let the native NAT of automated internet firewall take over. You can defer those route updates until you're ready.

If your destinations only accept specific allowlisted IP addresses, you can use an IPAM policy to pin down which addresses automated internet firewall uses. Set up the IPAM policy in Amazon VPC IPAM, and add `igw-firewall` as the resource type. We recommend a single contiguous CIDR block, because it is easier for destinations to allowlist, although an IPAM pool can contain multiple ranges. For the workflow, see [Define public IPv4 allocation strategy with IPAM policies](https://docs.aws.amazon.com/vpc/latest/ipam/define-public-ipv4-allocation-strategy-with-ipam-policies.html#add-allocation-rules) in the Amazon VPC IPAM User Guide. Standard IPAM limits apply.

## Default behavior and subnet exclusions
<a name="internet-gateway-firewall-default-behavior"></a>

By default, automated internet firewall inspects every subnet in your VPC, whatever connectivity type applies. That default is deliberate: coverage should be complete unless you decide otherwise. When a subnet shouldn't be inspected — one that is intentionally isolated from the internet, for example — you can leave it out.

You exclude a subnet by overriding its connectivity type to exclude. For the full list of connectivity types, including exclude, and how overrides are matched, see [Subnet connectivity types](#internet-gateway-firewall-connectivity-types).

## Monitor mode
<a name="internet-gateway-firewall-enforcement-modes"></a>

Finally, monitor mode lets you turn on a new policy without risk. Automated internet firewall offers monitor mode for safe rollout of your security policy. In monitor mode, the firewall does not drop or reject traffic that your rules deny; it only logs it. You can review the access logs or alert logs to see the impact of your policy on your traffic before you move to enforce mode.