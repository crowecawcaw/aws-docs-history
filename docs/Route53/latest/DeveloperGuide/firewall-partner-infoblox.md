

# Using partner managed DNS threat protection with Infoblox in DNS Firewall

This topic covers how to subscribe to, configure, and manage Infoblox DNS threat protection rules within Amazon Route 53 Resolver DNS Firewall rule groups.

Infoblox DNS threat protection for Route 53 brings Infoblox threat intelligence directly into DNS Firewall for your Amazon Virtual Private Cloud instances. You don't need to deploy separate DNS security appliances, change Amazon VPC routing, or forward DNS traffic to an external inspection point. You enforce Infoblox protections through the same DNS Firewall rules and rule groups that you already use to manage DNS security in AWS.

The integration helps you in two key ways:

1. It gives you Infoblox DNS threat intelligence feeds, grouped by threat level (informational through critical).

1. It removes the infrastructure overhead of running separate DNS security infrastructure across multiple VPCs and accounts. This helps reduce both cost and operational complexity.

**Availability**  
Partner managed DNS threat protection with Infoblox is available in preview in all commercial AWS Regions where DNS Firewall is available.

**Prerequisites**  
Before you can use partner managed DNS threat protection with Infoblox, you must have the following:
+ An AWS account with appropriate IAM permissions for DNS Firewall and AWS Marketplace.
+ A DNS Firewall rule group already created (or create one during the workflow).
+ The Advanced plan pricing option selected for your rule (required for partner managed DNS threat protection). You can select this during DNS Firewall rule creation.