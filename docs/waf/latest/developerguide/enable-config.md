**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Enabling AWS Config for using Firewall Manager

To use Firewall Manager, you must enable AWS Config.

###### Note

You incur charges for your AWS Config settings, according to AWS Config pricing. For more
information, see [Getting Started with AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md").

###### Note

In order for Firewall Manager to monitor policy compliance, AWS Config must continuously record configuration changes for protected resources. In your AWS Config configuration, the recording frequency must be set to **Continuous**, which is the default setting.

###### To enable AWS Config for Firewall Manager

1. Enable AWS Config for each of your AWS Organizations member accounts, including the Firewall Manager administrator account. For more information,
   see [Getting Started with AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md").
2. Enable AWS Config for each AWS Region that contains the resources that you want to protect.
   You can enable AWS Config manually, or you can use the AWS CloudFormation template "Enable AWS Config" at
   [AWS CloudFormation StackSets Sample Templates](../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md").

If you don't want to enable AWS Config for all resources, then you must enable the
following according to the type of Firewall Manager policies that you use:

    * **WAF policy** – Enable Config for the resource
     types CloudFront Distribution, Application Load Balancer (choose
     **ElasticLoadBalancingV2** from the list), API Gateway, WAF WebACL, WAF Regional WebACL, and WAFv2 WebACL. To enable
     AWS Config to protect a CloudFront distribution, you must be in the
     US East (N. Virginia) Region. Other Regions don't have CloudFront as an option.
    * **Shield policy** – Enable Config for the resource types Shield
     Protection, ShieldRegional Protection, Application Load Balancer, EC2 EIP, WAF WebACL, WAF
     Regional WebACL, and WAFv2 WebACL.
    * **Security group policy** – Enable Config for the
     resource types EC2 SecurityGroup, EC2 Instance, and EC2
     NetworkInterface.
    * **Network ACL policy** – Enable Config for the resource types Amazon EC2 Subnet and Amazon EC2 network ACL.
    * **Network Firewall policy** – Enable Config
     for the resource types NetworkFirewall FirewallPolicy, NetworkFirewall
     RuleGroup, EC2 VPC, EC2 InternetGateway, EC2 RouteTable, and EC2 Subnet.
    * **DNS Firewall policy** – Enable
     Config for the resource type EC2 VPC and Amazon Route 53 ResolverRuleAssociation.
    * **Third-party firewall policy** – Enable Config for the resource types Amazon EC2 VPC, Amazon EC2 InternetGateway, Amazon EC2 RouteTable, Amazon EC2 Subnet, and Amazon EC2 VPCEndpoint.

###### Note

If you configure your AWS Config recorder to use a custom IAM role, you need to make sure the IAM policy has the proper permissions to record the Firewall Manager policy's required resource types. Without the proper permissions, the required resources may not be recorded which prevents Firewall Manager from properly protecting your resources. Firewall Manager doesn't have visibility into these permission misconfigurations. For information about using IAM with AWS Config, see [IAM for AWS Config](../../../config/latest/developerguide/security-iam.md "../../../config/latest/developerguide/security-iam.md").
