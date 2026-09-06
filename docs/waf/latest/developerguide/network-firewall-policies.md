

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Using AWS Network Firewall policies in Firewall Manager
<a name="network-firewall-policies"></a>

This section explains how to use AWS Network Firewall policies with Firewall Manager.

You can use AWS Firewall Manager Network Firewall *policies* to manage AWS Network Firewall *firewalls* for your Amazon Virtual Private Cloud *VPCs* across your *organization* in AWS Organizations. You can apply centrally controlled firewalls to your entire organization or to a select subset of your accounts and VPCs. 

Network Firewall provides network traffic filtering protections for the public subnets in your VPCs. Firewall Manager creates and manages your firewalls based on the *firewall management type* defined by your policy. Firewall Manager provides the following firewall management models:
+ **Distributed** - For each account and VPC that's within policy scope, Firewall Manager creates a Network Firewall firewall and deploys firewall endpoints to VPC subnets, to filter network traffic.
+ **Centralized** - Firewall Manager creates a single Network Firewall firewall in a single Amazon VPC.
+ **Import existing firewalls** - Firewall Manager imports existing firewalls for management in a single Firewall Manager policy. You can apply additional rules to the imported firewalls managed by your policy to ensure that your firewalls meet your security standards.

**Note**  
Firewall Manager Network Firewall policies are Firewall Manager policies that you use to manage Network Firewall protections for your VPCs across your organization.   
The Network Firewall protections are specified in resources in the Network Firewall service that are called firewall policies. 

For information about using Network Firewall, see the [AWS Network Firewall Developer Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html).

The following sections cover requirements for using Firewall Manager Network Firewall policies and describe how the policies work. For the procedure for creating the policy, see [Creating an AWS Firewall Manager policy for AWS Network Firewall](create-policy.md#creating-firewall-manager-policy-for-network-firewall). 

**Important**  
**You must enable resource sharing.** A Network Firewall policy shares Network Firewall rule groups across the accounts in your organization. For this to work, you must have resource sharing enabled for AWS Organizations. For information about how to enable resource sharing, see [Resource sharing for Network Firewall and DNS Firewall policies](resource-sharing.md).

**Important**  
**You must have your Network Firewall rule groups defined. ** When you specify a new Network Firewall policy, you define the firewall policy the same as you do when you're using AWS Network Firewall directly. You specify the stateless rule groups to add, default stateless actions, and stateful rule groups. Your rule groups must already exist in the Firewall Manager administrator account for you to include them in the policy. For information about creating Network Firewall rule groups, see [AWS Network Firewall rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups.html).

**Topics**
+ [How Firewall Manager creates firewall endpoints](fms-create-firewall-endpoints.md)
+ [How Firewall Manager manages your firewall subnets](fms-manage-firewall-subnets.md)
+ [How Firewall Manager manages your Network Firewall resources](fms-manage-network-firewall.md)
+ [How Firewall Manager manages and monitors VPC route tables for your policy](fms-manage-vpc-route-tables.md)
+ [Configuring logging for an AWS Network Firewall policy](nwfw-policies-logging-config.md)