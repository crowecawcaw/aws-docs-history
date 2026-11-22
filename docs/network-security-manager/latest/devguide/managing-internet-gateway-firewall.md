

# Automated Internet Firewall in AWS Network Security Manager

Automated internet firewall protects all internet traffic that enters or leaves your VPCs through their internet gateways. You don't need to change your architecture or routes. AWS Network Security Manager is where you set it up, configure its policy, deploy it, and manage it. You can apply it to a single account, to organizational units (OUs), or to your whole organization in AWS Organizations. NSM creates the firewall in each VPC in scope and keeps it up to date. It also protects VPCs and subnets that you create later.

**Note**  
Automated internet firewall is available in public preview in all AWS commercial Regions. During the preview, it doesn't work with Regional NAT, **noNAT** ingress routing, or ingress-only VPC Block Public Access. During the preview, it also does not perform NAT64 for IPv6 traffic that is destined for an IPv4 destination. It also does not support Amazon EC2 [Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) or the following machine learning instance types: p4d, p4de, p6-b200, p6-b300, p6e-gb200, trn2, trn2u, and g7e.

## How the AWS Network Security Manager resources fit together
<a name="managing-igw-firewall-resources"></a>

To understand how AWS Network Security Manager resources fit together, see [Concepts](https://docs.aws.amazon.com/network-security-manager/latest/devguide/concepts.html) in the *AWS Network Security Manager Developer Guide*.

To set up automated internet firewall, you create the following resources in order.

1. **Rules** define the firewall's configuration or inspection settings, for example, the enforcement mode or logging. Each rule contains one setting.

1. **Templates** (optional) group rules so that you can reuse them.

1. **Policies** combine your templates and rules, and set the default subnet connectivity type. We recommend flexible.

1. **Scopes** select the accounts, OUs, or VPCs to protect, by tag, by ARN, or by including all VPCs.

1. **Deployments** combine a policy with a scope, and then execute firewall creation or synchronization.

Creating the deployment provisions the firewall. AWS Network Security Manager then creates an automated internet firewall for each VPC in scope. Provisioning can take several minutes. Until the firewall is in place, the VPC shows as Out of sync in synchronization status. A deployment status of Active doesn't mean that provisioning is finished.

## Where you manage Automated Internet Firewall
<a name="managing-igw-firewall-where"></a>

You configure and manage everything in AWS Network Security Manager. After deployment, the firewall appears in AWS Network Firewall as read-only, so you can check its status and logs there.

The following table shows where you perform each task when setting up and working with your automated internet firewall.


| Task | AWS Network Security Manager | Network Firewall | 
| --- | --- | --- | 
| Create rules, templates, and policies which reference Network Firewall policy constructs.<br />Create scopes where the target assets are defined.<br />Create deployments, where policies and scopes are combined and implemented. | Yes | No | 
| Create a Network Firewall rule group | No | Yes | 
| Set enforcement mode (monitor or enforce) | Yes | No | 
| Set subnet connectivity (flexible, bidirectional, outbound-only) and overrides | Yes | No | 
| Synchronize Network Security Manager policy with the deployed policy for each in-scope VPC. | Yes | No | 
| View the firewall on the Internet firewalls tab | No | Yes | 
| Describe the firewall and its firewall policy | No | Yes | 
| View firewall logs | No | Yes | 
| Change or delete the firewall | Yes (through the deployment, policy, or scope) | No | 

Use AWS Network Security Manager to change or remove an automated internet firewall or alter associated policy, scope, and deployment objects. If you try to change or delete the firewall in Network Firewall, the request fails.

## Next steps
<a name="managing-igw-firewall-next-steps"></a>

To learn more about automated internet firewall, see the following topics in the AWS Network Firewall Developer Guide.
+ To set up your first automated internet firewall, see [Getting started with Automated Internet Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/internet-gateway-firewall-getting-started.html).
+ To learn about connectivity types, NAT behavior, and traffic inspection, see [How Automated Internet Firewall works](https://docs.aws.amazon.com/network-firewall/latest/developerguide/internet-gateway-firewall-how-it-works.html).
+ To learn about each AWS Network Security Manager resource, see the rules, templates, policies, scopes, and deployments topics in this guide.