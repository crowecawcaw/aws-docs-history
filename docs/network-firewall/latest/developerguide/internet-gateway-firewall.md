

# Automated Internet Firewall

Automated internet firewall protects all traffic that enters or leaves your VPCs through their internet gateways.

**Note**  
Automated internet firewall is available in public preview in all AWS commercial Regions. During the preview, it doesn't work with Regional NAT, **noNAT** ingress routing, or ingress-only VPC Block Public Access. During the preview, it also does not perform NAT64 for IPv6 traffic that is destined for an IPv4 destination. It also does not support Amazon EC2 [Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) or the following machine learning instance types: p4d, p4de, p6-b200, p6-b300, p6e-gb200, trn2, trn2u, and g7e.

With automated internet firewall, you define and maintain Network Firewall security rules centrally in Network Security Manager. Automated internet firewall places Network Firewall with native NAT functionality at the internet gateway of your VPC, so that all traffic entering or leaving the VPC is always filtered by your security policies. You do not need to make any routing or architectural changes inside your VPCs to deploy automated internet firewall. Automated internet firewall performs NAT natively, so you do not need to configure NAT gateways separately. Because automated internet firewall is deployed at the internet gateway, VPC or subnet owners and compromised workloads cannot manipulate routes to bypass your security policies.

You can choose to apply automated internet firewall across your entire organization, organizational units (OUs), individual accounts, or specific VPCs. Automated internet firewall automatically protects new VPCs and subnets as you create them, so your coverage stays complete as your environment grows. If you are beginning your security journey, you can turn on automated internet firewall using the default AWS managed rule groups, with no custom configuration required. AWS security experts maintain and update these rule groups to help protect your workloads against changing security threats, and you can customize them at any time. For the list of managed rule groups, see [the list of AWS managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/create-policy.html#creating-firewall-manager-policy-for-network-firewall).

You can run automated internet firewall in monitor mode first to observe the impact on your traffic, and then enforce it. You do not need to make architectural or routing changes to implement it.

**Before automated internet firewall**

![A VPC connects to the internet through its internet gateway before automated internet firewall is applied, with no centralized inspection of internet traffic.](https://docs.aws.amazon.com/network-firewall/latest/developerguide/images/aif-before.png)


**After automated internet firewall**

![The same VPC after automated internet firewall is applied, with firewall inspection and managed NAT at the internet gateway inspecting all inbound and outbound internet traffic.](https://docs.aws.amazon.com/network-firewall/latest/developerguide/images/aif-after.png)


**Key capabilities**

Automated internet firewall provides the following key capabilities:

1. Robust security, with assurance that all traffic entering or leaving the internet gateway is inspected and that no one with insufficient privileges can bypass it.

1. Easy setup that works with your existing architecture and does not require routing or architectural updates in your VPCs.

1. Centralized policy management and visibility with distributed implementation, which improves scalability and availability while keeping management simple.

1. Coverage that automatically expands to new VPCs.

1. AWS managed rule groups that companies beginning their security journey can turn on by default.

This chapter describes the automated internet firewall deployment model for AWS Network Firewall, how it works, and how to get started.

**Topics**
+ [How Automated Internet Firewall works](internet-gateway-firewall-how-it-works.md)
+ [Getting started with Automated Internet Firewall](internet-gateway-firewall-getting-started.md)
+ [Working with existing architectures](internet-gateway-firewall-existing-architectures.md)
+ [Logging and monitoring](internet-gateway-firewall-logging-monitoring.md)
+ [Service quotas](internet-gateway-firewall-quotas.md)