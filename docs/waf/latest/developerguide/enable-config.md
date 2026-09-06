

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Enabling AWS Config for using Firewall Manager
<a name="enable-config"></a>

To use Firewall Manager, you must enable AWS Config. 

**Note**  
You incur charges for your AWS Config settings, according to AWS Config pricing. For more information, see [Getting Started with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html).

**Note**  
In order for Firewall Manager to monitor policy compliance, AWS Config must continuously record configuration changes for protected resources. In your AWS Config configuration, the recording frequency must be set to **Continuous**, which is the default setting. 

**To enable AWS Config for Firewall Manager**

1. Enable AWS Config for each of your AWS Organizations member accounts, including the Firewall Manager administrator account. For more information, see [Getting Started with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html).

1. Enable AWS Config for each AWS Region that contains the resources that you want to protect. You can enable AWS Config manually, or you can use the CloudFormation template "Enable AWS Config" at [AWS CloudFormation StackSets Sample Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.html). 

   If you don't want to enable AWS Config for all resources, then you must enable the following according to the type of Firewall Manager policies that you use: 
   + **WAF policy** – Enable Config for the resource types CloudFront Distribution, Application Load Balancer (choose **ElasticLoadBalancingV2** from the list), API Gateway, WAF WebACL, WAF Regional WebACL, and WAFv2 WebACL. To enable AWS Config to protect a CloudFront distribution, you must be in the US East (N. Virginia) Region. Other Regions don't have CloudFront as an option. 
   + **Shield policy** – Enable Config for the resource types Shield Protection, ShieldRegional Protection, Application Load Balancer, EC2 EIP, WAF WebACL, WAF Regional WebACL, and WAFv2 WebACL. 
   + **Common security group policy** – Enable Config for the resource types Amazon EC2 SecurityGroup and Amazon EC2 VPC, plus the resource types in the policy's resource type list (typically Amazon EC2 Instance and Amazon EC2 NetworkInterface). If you enable security group references distribution on the policy, also enable Amazon EC2 VPCPeeringConnection.
   + **Security group content audit policy** – Enable Config for the resource types Amazon EC2 SecurityGroup, Amazon EC2 NetworkInterface, and Amazon EC2 Instance.
   + **Security group usage audit policy** – Enable Config for the resource type Amazon EC2 SecurityGroup.
   + **Network ACL policy** – Enable Config for the resource types Amazon EC2 Subnet and Amazon EC2 network ACL.
   + **Network Firewall policy** – Enable Config for the resource types NetworkFirewall FirewallPolicy, NetworkFirewall RuleGroup, EC2 VPC, EC2 InternetGateway, EC2 RouteTable, and EC2 Subnet. 
   + **DNS Firewall policy** – Enable Config for the resource type EC2 VPC and Amazon Route 53 FirewallRuleGroupAssociation. 
   + **Third-party firewall policy** – Enable Config for the resource types Amazon EC2 VPC, Amazon EC2 InternetGateway, Amazon EC2 RouteTable, Amazon EC2 Subnet, and Amazon EC2 VPCEndpoint.
**Note**  
If you configure your AWS Config recorder to use a custom IAM role, you need to make sure the IAM policy has the proper permissions to record the Firewall Manager policy's required resource types. Without the proper permissions, the required resources may not be recorded which prevents Firewall Manager from properly protecting your resources. Firewall Manager doesn't have visibility into these permission misconfigurations. For information about using IAM with AWS Config, see [IAM for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/security-iam.html).