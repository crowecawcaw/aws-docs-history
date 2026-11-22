

# What is AWS Network Firewall?

AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for your virtual private cloud (VPC). With Network Firewall, you can filter traffic at the perimeter of your VPC. This includes traffic entering or leaving your VPC through an internet gateway, NAT gateway, transit gateway, Cloud WAN, or virtual private gateway, or over a VPN or Direct Connect connection, as long as the traffic is routed to a firewall endpoint. You can also filter traffic between subnets. 

Network Firewall offers two kinds of firewall policy. We recommend **Next Generation** policies for new firewalls. A Next Generation policy is a single policy that inspects your traffic in two sequential stages—first a *firewall engine* for access control (drop by default), then an *IPS engine* for threat detection and prevention—and provides a simplified rule-authoring model and dynamic rule capacity. **Classic Network Firewall** policies, which filter traffic with a stateless rules engine and a stateful rules engine, remain fully supported for existing firewalls. You can associate either a Classic Network Firewall policy or a Next Generation policy with a firewall, but not both. For a comparison, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md); for details, see [Next Generation policies](firewall-policies-v2.md).

**Note**  
You can use Network Firewall to automatically protect the internet traffic that enters and leaves your VPCs by enabling automated internet firewall. Automated internet firewall applies a managed firewall at your internet gateway and is managed centrally through Network Security Manager, with no changes to your routes. For more information, see [Automated Internet Firewall](internet-gateway-firewall.md).

Network Firewall uses the open source intrusion prevention system (IPS), Suricata, for stateful inspection, and supports Suricata compatible rules. For more information, see [Working with stateful rule groups in AWS Network Firewall](stateful-rule-groups-ips.md).

**Note**  
This section and others that describe Suricata-based concepts are not intended to replace or duplicate information from the Suricata documentation. For more Suricata-specific information, see the [Suricata documentation](https://docs.suricata.io/en/suricata-8.0.3/).

You can use Network Firewall to monitor and protect your Amazon VPC traffic in a number of ways, including the following: 
+ Allowlist only trusted destinations, such as AWS service domains or IP address endpoints (for example, Amazon S3).
+ deny custom or managed lists of known malicious destinations.
+ Inspect the full contents of packets (not just headers) entering or leaving your VPC.
+ Use stateful protocol detection to filter protocols like HTTPS, independent of the port used.

When you create a firewall, you choose one of the following firewall capabilities:
+ **Routed firewall** – The firewall receives traffic from the firewall endpoint, filters it, and sends the filtered traffic back through the firewall endpoint to its destination. The original source and destination IP addresses are preserved throughout inspection. You steer traffic to the firewall through VPC route tables, and you can route outbound traffic through your own NAT gateway or internet gateway. This capability supports all protocols (TCP, UDP, and ICMP), supports VPC and transit gateway attachments, and is designed for general network security use cases like intrusion prevention, domain-based filtering, and east-west or north-south traffic inspection.
+ **NAT/Proxy firewall** – Network Firewall creates a NAT gateway and a firewall endpoint in each Availability Zone that you add. The firewall endpoint receives traffic, the firewall filters it, and the filtered traffic exits through the NAT gateway, which uses the NAT gateway's IP address as the source in place of the client source IP address. The firewall also acts as an explicit forward proxy: clients send HTTP and HTTPS requests directly to the firewall's proxy hostname, without route table changes. Other traffic reaches the firewall endpoint through your VPC route tables. For more information, see [NAT/Proxy firewall](nfw-proxy.md).

Both capabilities support Next Generation policies and Classic Network Firewall policies.

To configure Network Firewall inside a VPC, you perform steps in both Amazon VPC and in Network Firewall. For information about managing your Amazon Virtual Private Cloud VPC, see the [Amazon Virtual Private Cloud User Guide](https://docs.aws.amazon.com/vpc/latest/userguide). For more information about how Network Firewall works, see [How AWS Network Firewall works](how-it-works.md). 

You can use AWS Firewall Manager (Firewall Manager) to centrally configure and manage your firewalls across your accounts and applications in AWS Organizations. You can manage firewalls for multiple accounts using a single account in Firewall Manager. For more information, see [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

**Topics**
+ [AWS Network Firewall​ AWS resources](#aws-resources)
+ [AWS Network Firewall concepts](#concepts)
+ [AWS Network Firewall firewall policy versions](firewall-policy-versions.md)
+ [Accessing AWS Network Firewall](#accessing)
+ [Regions and endpoints for AWS Network Firewall](#regions-and-endpoints)
+ [Pricing for AWS Network Firewall](#pricing)
+ [AWS Network Firewall quotas](#what-it-is-quotas)
+ [AWS Network Firewall additional resources](#info-resources)

## AWS Network Firewall​ AWS resources
<a name="aws-resources"></a>

Network Firewall manages the following AWS resource types: 
+ **Firewall** – An AWS resource that holds the traffic-filtering logic for a VPC. A firewall is associated with a single firewall policy, and defines the VPC that it protects and a firewall endpoint subnet in each Availability Zone. 
+ **VpcEndpointAssociation** – Provides additional firewall endpoints across other VPCs so that your workloads in other VPCs can access the Firewall.
+ **RuleGroup** – Defines a set of rules to match against VPC traffic, and the actions to take when Network Firewall finds a match. Network Firewall uses stateless and stateful rule group types, each with its own Amazon Resource Name (ARN). A referenced rule group is a reusable resource that you can share across multiple policies and whose capacity is pre-allocated when you create it; embedded rules are authored directly in a policy (native to the policy) and don't require an upfront capacity allocation.
+ **FirewallPolicy** – It is a top level container where you can stack your rule groups in order of priority. Your traffic is filtered against the rules in your policy.

## AWS Network Firewall concepts
<a name="concepts"></a>

AWS Network Firewall is a firewall service for Amazon Virtual Private Cloud (Amazon VPC). For information about managing your Amazon Virtual Private Cloud VPC, see the [Amazon Virtual Private Cloud User Guide](https://docs.aws.amazon.com/vpc/latest/userguide). 

The following are the key concepts for Network Firewall. For the Network Firewall resource types—firewall, VPC endpoint association, firewall policy, and rule group—see [AWS Network Firewall​ AWS resources](#aws-resources). 
+ **Virtual private cloud (VPC)** – A virtual network dedicated to your AWS account. 
+ **Internet gateway** – A gateway that you attach to a VPC to enable communication between resources in the VPC and the internet.
+ **Subnet** – It is a subnetwork containing a specific contiguous and immutable range of IP addresses inside your VPC where you provision your AWS resources. Network Firewall creates firewall endpoints in subnets inside your VPC, to filter network traffic.
+ **Firewall subnet** – A subnet that you've designated for exclusive use by Network Firewall for a firewall endpoint. A firewall endpoint cannot filter traffic coming into or going out of the firewall endpoint subnet in which it resides, so do not use your firewall subnets for anything other than Network Firewall.
+ **Route table** – A set of rules, called routes, that are used to determine where network traffic is directed. You modify your VPC route tables in Amazon VPC to direct traffic through your firewalls for filtering.
+ **Stateless rules** – Criteria for inspecting a single network traffic packet, without the context of the other packets in the traffic flow, the direction of flow, or any other information that's not provided by the packet itself. Stateless rules apply to Classic Network Firewall policies only; Next Generation policies don't use stateless rule groups. 
+ **Firewall rule groups** – Access-control rules that a Next Generation policy's firewall engine evaluates. 
+ **IPS rule groups** – Intrusion prevention rules that a Next Generation policy's IPS engine evaluates. 
+ **Stateful rules** – Criteria for inspecting network traffic packets in the context of their traffic flow. 
+ **Flows** – Network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort with other traffic. Flows that are processed by the firewall are tracked in the firewall state table and are visible in flow logs.
+ **Firewall state table** – Table where Network Firewall tracks and maintains information about network traffic flows. The firewall state table tracks flows that are processed by stateful rules—or, for a Next Generation policy, by firewall engine and IPS engine rules. When traffic matches the criteria in one of these rules, the firewall creates a flow entry in the firewall state table. These entries persist until they are either removed using a flow flush operation, naturally terminate, or time out due to inactivity. You can manage the firewall state table using specific operations. This is also known as the firewall table or state table.

  For information, see [Flow operations in your firewall](firewall-flow-operations.md).

## Accessing AWS Network Firewall
<a name="accessing"></a>

You can create, access, and manage your firewall, firewall policy, and rule group resources in Network Firewall using any of the following methods:
+ **AWS Management Console** – Provides a web interface for managing the service. The procedures throughout this guide explain how to use the AWS Management Console to perform tasks for Network Firewall. You can access the AWS Management Console at [https://aws.amazon.com/console](https://aws.amazon.com/console/). To access Network Firewall using the console:

  ```
  https://{{<region>}}.console.aws.amazon.com/network-firewall/home
  ```
+ **AWS Command Line Interface (AWS CLI)** – Provides commands for a broad set of AWS services, including Network Firewall. The CLI is supported on Windows, macOS, and Linux. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). To access Network Firewall using the CLI endpoint:

  ```
  aws network-firewall
  ```
+ **AWS Network Firewall API** – Provides a RESTful API. The REST API requires you to handle connection details, such as calculating signatures, handling request retries, and handling errors. For more information, see [AWS APIs](https://docs.aws.amazon.com/general/latest/gr/aws-apis.html) and the [AWS Network Firewall API Reference](https://docs.aws.amazon.com/network-firewall/latest/APIReference/). To access Network Firewall, use the following REST API endpoint:

  ```
  https://network-firewall.{{<region>}}.amazonaws.com 
  ```
+ **AWS SDKs** – Provide language-specific APIs. If you're using a programming language that AWS provides an SDK for, you can use the SDK to access AWS Network Firewall. The SDKs handle many of the connection details, such as calculating signatures, handling request retries, and handling errors. They integrate easily with your development environment, and provide easy access to Network Firewall commands. For more information, see [Tools for Amazon Web Services](https://aws.amazon.com/tools).
+ **AWS CloudFormation** – Helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want and CloudFormation takes care of provisioning and configuring those resources for you. For more information, see [Network Firewall resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkFirewall.html) in the *AWS CloudFormation User Guide*.
+ **AWS Tools for Windows PowerShell** – Let developers and administrators manage their AWS services and resources in the PowerShell scripting environment. For more information, see the [AWS Tools for PowerShell User Guide](https://docs.aws.amazon.com/powershell/latest/userguide/).

## Regions and endpoints for AWS Network Firewall
<a name="regions-and-endpoints"></a>

To view the complete list of AWS Regions where Network Firewall is available, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/network-firewall.html) in the *AWS General Reference*. 

 **IPv4 endpoints** 

```
https://network-firewall.{{<region>}}.amazonaws.com
```

 **Dual-stack (IPv4 and IPv6) endpoints** 

Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request to a dual-stack endpoint, the endpoint URL resolves to an IPv6 or IPv4 address, depending on the protocol used by your network and client.

```
https://network-firewall.{{<region>}}.api.aws
```

## Pricing for AWS Network Firewall
<a name="pricing"></a>

For detailed information about pricing for Network Firewall, see [AWS Network Firewall pricing](https://aws.amazon.com/network-firewall/pricing/).

Some configurations can incur additional costs, on top of the basic costs for using Network Firewall. For example, if you use a firewall endpoint in one Availability Zone to filter traffic from another zone, you can incur cross-zone traffic charges. If you enable logging, you incur additional charges according to factors such as the logging destination that you use and the amount of traffic that you choose to log. 

## AWS Network Firewall quotas
<a name="what-it-is-quotas"></a>

AWS Network Firewall defines maximum settings and other quotas on the number of Network Firewall resources that you can use. You can request an increase for some of these quotas. A Next Generation policy has its own quotas—for firewall rules, IPS rules, embedded rules, and the rule groups per section—that are distinct from the Classic Network Firewall policy quotas. For more information, see [AWS Network Firewall quotas](quotas.md).

## AWS Network Firewall additional resources
<a name="info-resources"></a>

To get a hands-on introduction to AWS Network Firewall, complete [Getting started with AWS Network Firewall](getting-started.md). 

Use the following resources to get additional information and guidance for using AWS Network Firewall. 
+ **[AWS discussion forums](https://forums.aws.amazon.com/)** – A community-based forum for discussing technical questions related to this and other AWS services. 
+ **[Getting started resource center](https://aws.amazon.com/getting-started/)** – Information to help you get started building on AWS.
+ **[Support center](https://console.aws.amazon.com/support/home#/)** – The home page for AWS Support.
+ **[Contact Us](https://aws.amazon.com/contact-us/)** – A central contact point for inquiries concerning billing, accounts, and events.