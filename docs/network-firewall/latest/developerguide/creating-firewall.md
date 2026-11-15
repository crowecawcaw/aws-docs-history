

# Creating a firewall in AWS Network Firewall
<a name="creating-firewall"></a>

You can create a firewall in Network Firewall to start using the protections you've defined in a firewall policy to protect a VPC.

There are two ways you can create a firewall:
+ Create a VPC-attached firewall to protect a VPC
+ Create a transit gateway-attached firewall to enable centralized network inspection

**Note**  
To create a transit gateway-attached firewall, you can accept a transit gateway that has been shared with you through AWS RAM or a transit gateway that you own.

**Important**  
Before you begin, make sure your VPC has at least one subnet that can host a firewall endpoint. The subnet must be dedicated to Network Firewall use and cannot be used for other resources. For information about subnet requirements and configuration, see [VPC subnets](vpc-config-subnets.md).

**To create a firewall through the console**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

   In the navigation pane, under **Network Firewall**, choose **Firewalls**, and then choose **Create firewall**.

1. On the **Describe firewall** page, provide the following information, and then choose **Next**:

   1. Enter a **Name** to identify this firewall.
**Note**  
You can't change the name after you create the firewall.

   1. (Optional) Enter a **Description** for the firewall to help you identify it among your other resources.

1. On the **Attachment type** page, under **Attachment Details**, select how to attach the firewall:

   1. **VPC** – Attach the firewall to subnets in a VPC. Select your **VPC** from the dropdown list, and then, for **Firewall subnets**, select the **Availability Zone**, **Subnet**, and **IP address type** for each firewall endpoint. You can add one subnet for each Availability Zone that your VPC spans, and you must specify a subnet in any Availability Zone where you want to create endpoints using VPC endpoint associations.
**Note**  
You can't change the VPC after you create the firewall.

      The subnets that you specify should be dedicated for Network Firewall firewall use. For more information, see [VPC subnets](vpc-config-subnets.md).

   1. **Transit Gateway** – Attach the firewall to a transit gateway. For **Transit gateway**, select an existing transit gateway from the dropdown list, which includes any transit gateway attachment in your account (marked as "this account") and AWS Transit Gateways shared with you from other accounts (showing the owner account ID). Then, for **Associated Availability Zone**, select the Availability Zones for your firewall. You must select at least one Availability Zone.
**Note**  
If you need to create a new transit gateway, open the Transit Gateway console in a new tab. After creating the transit gateway, return to this page and refresh the Transit Gateway selector.

   Choose **Next**.

1. (Optional) On the **Configure advanced settings** page, configure any of the following, and then choose **Next**:

   1. Under **Protection against changes**, turn on or turn off the protections that guard your firewall against accidental changes. **Delete protection** is turned on by default. For a VPC attachment, **Subnet change protection** is also turned on by default; for a transit gateway attachment, **Availability Zone change protection** is turned on by default.

   1. Under **Traffic analysis mode**, select **Enable traffic analysis mode** to turn on access to HTTP and HTTPS traffic reporting. Turning on traffic analysis mode does not automatically generate a report when you finish creating your firewall. For more information about report generation, see [Reporting on network traffic in Network Firewall](reporting.md).
**Important**  
Network Firewall only starts collecting traffic analysis metrics when you enable **Traffic analysis mode** on your firewall. Traffic observed before you enable **Traffic analysis mode** is not included in reporting. 

   1. Under **Customer managed key**, to use a AWS Key Management Service customer managed key to encrypt your resources instead of an AWS owned key, customize the encryption settings. For more information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md).

   1. Under **Logging configuration**, select the **Log type** to turn on—**Alert**, **Flow**, or **TLS**—and, for each log type that you select, select a log destination (an Amazon S3 bucket, a Amazon CloudWatch log group, or a Amazon Data Firehose stream). To view your firewall's traffic in the monitoring dashboard, under **Firewall monitoring dashboard**, select **Enable**. For more information about logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).

1. On the **Associate firewall policy** page, select one of the following:
   + **Create and associate a firewall policy** – Create a new policy to associate with this firewall. Enter a name and an optional description, and select the **Policy version** (**Next Generation**, which is recommended and selected by default, or **Classic**). For a Next Generation policy, the only inline settings are **Firewall default action**, **Policy mode**, and **Stream exception setting**. For information about these settings, see [Creating a Next Generation policy in AWS Network Firewall](firewall-policy-v2-creating.md) and [Creating a firewall policy in AWS Network Firewall](firewall-policy-creating.md).
   + **Associate an existing firewall policy** – Choose a policy that you've already created. The list includes both Classic and Next Generation policies.
**Note**  
Next Generation policies require a source-preserving firewall. You can't associate a Next Generation policy with a firewall that uses proxy mode (that is, a firewall configured with no source preservation, proxy settings, or NAT gateway mappings); the service rejects the association. For more information, see [AWS Network Firewall no-source-preservation mode](nfw-no-source-preservation.md).

   Choose **Next**.

1. (Optional) On the **Add tags** page, add any tags that you want to apply to the firewall, and then choose **Next**. For more information, see [Tagging AWS Network Firewall resources](tagging.md).

1. On the **Review and create** page, review the firewall configuration. To change a setting, choose **Edit** for that section. When you're satisfied, choose **Create firewall**.

To create a firewall with the API or AWS CLI, specify the firewall policy to associate in the `FirewallPolicyArn` parameter of the `CreateFirewall` (or `AssociateFirewallPolicy`) operation. For a Next Generation policy, use a `firewall-policy-v2` ARN, for example `arn:aws:network-firewall:{{region}}:{{account-id}}:firewall-policy-v2/{{policy-name}}`. For a Classic policy, use a `firewall-policy` ARN.

## Next steps
<a name="new-firewall-next-steps"></a>

After you create your firewall, it appears in the **Firewalls** page. As the firewall owner, you have full control over its configuration and management.

Complete these tasks to start using your firewall:

1. Required: Configure your firewall policy to define how traffic is filtered. A Next Generation policy is recommended for new firewalls; Classic Network Firewall policies remain fully supported. For information, see [Next Generation policies](firewall-policies-v2.md) and [Firewall policies in AWS Network Firewall](firewall-policies.md). To author rules for a Next Generation policy, see [Rule groups for Next Generation policies](rule-groups-v2.md).

1. Required: Configure your VPC route tables to direct traffic through your firewall endpoints. For information, see [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md).

You can also enhance your firewall's capabilities with these optional tasks:
+ Set up logging to monitor network traffic through your firewall. For information, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).
+ Create VPC endpoint associations to extend your firewall's protection to additional VPCs or to create multiple endpoints in a single Availability Zone. For information, see [Creating a VPC endpoint association](creating-vpc-endpoint-association.md).
+ For a guided walkthrough that creates a firewall with a Next Generation policy, see [Getting started with a Next Generation policy](getting-started-v2.md).