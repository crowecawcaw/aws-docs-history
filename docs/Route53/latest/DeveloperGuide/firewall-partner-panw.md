

# Using partner managed DNS threat protection with Palo Alto Networks in DNS Firewall
<a name="firewall-partner-panw"></a>

This topic covers how to subscribe to, configure, and manage Palo Alto Networks (PANW) DNS threat protection rules within Amazon Route 53 Resolver DNS Firewall rule groups.

Palo Alto Networks Advanced DNS Security for Route 53 delivers cloud-native DNS threat protection for your Amazon Virtual Private Cloud instances by integrating Palo Alto Networks threat intelligence directly into DNS Firewall. This integration eliminates the need to deploy separate firewalls, manage Amazon VPC routing configurations, or forward DNS traffic to external inspection points. You enforce Palo Alto Networks DNS protections through the same DNS Firewall rules and rule groups you already use to manage DNS security in AWS.

The integration addresses two operational challenges:

1. It provides access to 30\+ DNS threat detections beyond what AWS Managed Domain Lists offer natively, including fast flux detection, DNS hijacking, DNS rebinding, domain generation algorithm (DGA) detection, and identification of newly registered domains.

1. It eliminates the infrastructure overhead of deploying Palo Alto Networks firewalls across multiple VPCs and accounts solely for DNS inspection. This helps to reduce both cost and operational complexity while maintaining the same threat efficacy.

**Preview availability**  
Partner managed DNS threat protection with Palo Alto Networks is in public preview. The preview is available in the following commercial AWS Regions:  
US East (N. Virginia) – us-east-1
US East (Ohio) – us-east-2
US West (N. California) – us-west-1
US West (Oregon) – us-west-2
Africa (Cape Town) – af-south-1
Asia Pacific (Hong Kong) – ap-east-1
Asia Pacific (Hyderabad) – ap-south-2
Asia Pacific (Jakarta) – ap-southeast-3
Asia Pacific (Malaysia) – ap-southeast-5
Asia Pacific (Melbourne) – ap-southeast-4
Asia Pacific (Mumbai) – ap-south-1
Asia Pacific (New Zealand) – ap-southeast-6
Asia Pacific (Osaka) – ap-northeast-3
Asia Pacific (Seoul) – ap-northeast-2
Asia Pacific (Singapore) – ap-southeast-1
Asia Pacific (Sydney) – ap-southeast-2
Asia Pacific (Taipei) – ap-east-2
Asia Pacific (Thailand) – ap-southeast-7
Asia Pacific (Tokyo) – ap-northeast-1
Canada (Central) – ca-central-1
Canada West (Calgary) – ca-west-1
Europe (Frankfurt) – eu-central-1
Europe (Ireland) – eu-west-1
Europe (London) – eu-west-2
Europe (Milan) – eu-south-1
Europe (Paris) – eu-west-3
Europe (Spain) – eu-south-2
Europe (Stockholm) – eu-north-1
Europe (Zurich) – eu-central-2
Mexico (Central) – mx-central-1
South America (São Paulo) – sa-east-1

**Prerequisites**  
Before you can use partner managed DNS threat protection with Palo Alto Networks, you must have the following:
+ An AWS account with appropriate IAM permissions for DNS Firewall and AWS Marketplace.
+ A DNS Firewall rule group already created (or create one during the workflow).
+ The Advanced plan pricing option selected for your rule group (required for partner managed DNS threat protection). You can select this during DNS Firewall rule creation.