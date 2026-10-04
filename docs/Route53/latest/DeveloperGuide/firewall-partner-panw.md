

# Using partner managed DNS threat protection with Palo Alto Networks in DNS Firewall
<a name="firewall-partner-panw"></a>

This topic covers how to subscribe to, configure, and manage Palo Alto Networks (PANW) DNS threat protection rules within Amazon Route 53 Resolver DNS Firewall rule groups.

Palo Alto Networks Advanced DNS Security for Route 53 delivers cloud-native DNS threat protection for your Amazon Virtual Private Cloud instances by integrating Palo Alto Networks threat intelligence directly into DNS Firewall. This integration eliminates the need to deploy separate firewalls, manage Amazon VPC routing configurations, or forward DNS traffic to external inspection points. You enforce Palo Alto Networks DNS protections through the same DNS Firewall rules and rule groups you already use to manage DNS security in AWS.

The integration helps you in two key ways:

1. It provides access to 30\+ DNS threat detections from Palo Alto Networks Advanced DNS Security. Examples include fast flux detection, DNS hijacking, domain generation algorithm (DGA) detection, and identification of newly registered domains.

1. It eliminates the infrastructure overhead of deploying Palo Alto Networks firewalls across multiple VPCs and accounts solely for DNS inspection. This helps to reduce both cost and operational complexity while maintaining the same threat efficacy.

**Availability**  
Partner managed DNS threat protection with Palo Alto Networks is generally available in all commercial AWS Regions where DNS Firewall is available.

**Prerequisites**  
Before you can use partner managed DNS threat protection with Palo Alto Networks, you must have the following:
+ An AWS account with appropriate IAM permissions for DNS Firewall and AWS Marketplace.
+ A DNS Firewall rule group already created (or create one during the workflow).
+ The Advanced plan pricing option selected for your rule group (required for partner managed DNS threat protection). You can select this during DNS Firewall rule creation.