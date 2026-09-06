

# Using AWS Marketplace rule groups
<a name="aws-marketplace-rule-groups"></a>

AWS Marketplace rule groups provide managed security rules from AWS Partners that you can integrate with AWS Network Firewall.

AWS Marketplace rule groups are available by subscription through the AWS Marketplace console at [AWS Marketplace](https://aws.amazon.com/marketplace/) or through the AWS Management console. After you subscribe to an AWS Marketplace rule group, to enable the functionality in AWS Network Firewall, you can apply it to a firewall policy and associate it to a firewall to have these rules take effect.

**Note**  
Some AWS Marketplace managed rule groups use a `stateful-domain-rulegroup` resource type that is available only with managed rules. You will see this resource type identified in the Amazon Resource Name (ARN) for the rule group. This resource type consumes capacity from your firewall policy's total available domain capacity. Only AWS Marketplace managed rule groups can use this capacity. For more information about domain capacity, see [Firewall policy settings](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-settings.html).

## Pricing
<a name="aws-marketplace-rule-group-pricing"></a>

AWS Marketplace rule groups are available with no long-term contracts or minimal commitments. When you subscribe to a managed rule group provided by an AWS Marketplace seller, you will be charged additional fees based on the price set by the seller, which will be based on per GB traffic inspected by the firewall. For more information, see [AWS Network Firewall Pricing](https://aws.amazon.com/network-firewall/pricing/) and the description for each AWS Marketplace rule group at AWS Marketplace.

## Information and support
<a name="aws-marketplace-rule-group-information-support"></a>

To find additional information about an AWS Marketplace managed rule group or to contact the seller's support team, visit the individual seller's marketplace listing on AWS Marketplace. You can navigate directly to the seller's product listing from the rule group details page in AWS Network Firewall.

## Subscribe to AWS Marketplace rule groups
<a name="subscribing-aws-marketplace-rule-groups"></a>

You can subscribe to and unsubscribe from AWS Marketplace rule groups on the AWS Network Firewall console or the AWS Marketplace.

**To subscribe to an AWS Marketplace rule group**

1. Sign in to the AWS Management Console and open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. In the **AWS Marketplace** section, choose the name of a rule group to view the details and pricing information.

1. To subscribe to an AWS Marketplace rule group, navigate to a rule group, then choose **View Subscription Options**. From there you can subscribe.

**Note**  
If you decide not to subscribe to the rule group, simply close the pop-up.

After you're subscribed to an AWS Marketplace rule group, you can associate it onto your AWS Network Firewall policy as you do other managed rule groups. For information, see [Adding AWS managed rule groups to your firewall policy using the console](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-add-to-policy.html).

## Unsubscribe from AWS Marketplace rule groups
<a name="unsubscribing-aws-marketplace-rule-groups"></a>

You can unsubscribe from AWS Marketplace rule groups on the AWS Network Firewall console and the AWS Marketplace.

**Important**  
To stop the subscription charges for an AWS Marketplace rule group, you must remove it from all AWS Network Firewall policies in AWS Network Firewall, in addition to unsubscribing from it. If you unsubscribe from an AWS Marketplace rule group but don't remove it from your AWS Network Firewall policy, you will continue to be charged for the subscription until the rule group is removed from the policy.

**To unsubscribe from an AWS Marketplace rule group**

1. Open the [AWS Marketplace console](https://console.aws.amazon.com/marketplace).

1. Navigate to the **Manage subscriptions** page.

1. Open the **Delivery method** list and choose **SaaS**.

1. Under **Agreement**, open the **Actions list** and choose **Cancel subscription** next to the name of the AWS Marketplace product that you want to unsubscribe from.

1. In the **Cancel subscription** dialog box, enter `confirm`, then choose **Yes, cancel subscription**.

## Add AWS Marketplace managed rule groups
<a name="adding-aws-marketplace-managed-rule-groups"></a>

Once you subscribe to an AWS Marketplace managed rule, add them to one or more Network Firewall policies. The policy automatically implements the built-in protection across your firewall when you associate the rule group to the firewall policy. You can add AWS Marketplace managed rule groups either through the Network Firewall rule groups page or from your firewall policy's detail page.

**To add one or more AWS Marketplace managed rule groups to your firewall policy from the details page**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.

1. Select the policy that you'd like to add one or more AWS Marketplace managed rule groups to.

1. In the **Stateful rule groups** section, in the **Actions** drop-down menu, select **Add Partner managed stateful rule groups**.

1. Select the AWS Marketplace managed rule groups to add to your policy.

1. Choose **Add to policy**.

## View managed rules groups
<a name="viewing-managed-rules-groups"></a>

You can view available AWS Marketplace rule groups for your firewall policy.

**To view the list of AWS Marketplace managed rule groups**  
You can view the list of managed rule groups using the following methods:
+ **AWS console** – You can view the list of managed rule groups either in the **Network Firewall rule groups** page in the **AWS Marketplace** tab, or in the policy details page. When you add AWS Marketplace managed rule groups to a policy, you'll see only the managed rule groups that fit your policy type. For example, if your policy type is strict ordered, you'll see only the managed rule groups that have a type of strict ordered.
+ **Network Firewall API** – [ListRuleGroups](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListRuleGroups.html) with the parameter `Scope`.
+ **AWS CLI** – [aws network-firewall list-rule-groups](https://docs.aws.amazon.com/cli/latest/reference/network-firewall/list-rule-groups.html) `--scope MANAGED` and `--managed-type PARTNER_MANAGED`.

## AWS Marketplace rule group sync states
<a name="aws-marketplace-rule-group-sync-states"></a>

AWS Marketplace rule groups can have different sync states that indicate their current status and availability:

DEPRECATED  
The rule group has been deprecated by the seller. While the rule group will still be sent to the firewall, AWS Network Firewall does not have control over whether these rules are being updated or removed by the seller. It is recommended to remove this rule group from your firewall policy and use the recommended approach from the owner of the product.

NOT\_SUBSCRIBED  
You have a rule group configured in your firewall policy that does not have an active subscription to the product in AWS Marketplace. When this occurs, the rule group will not be sent to the firewall and will be effectively inactive. To resolve this, you need to either:  
+ Subscribe to the product in AWS Marketplace, or
+ Remove the rule group from your firewall policy
You can check your subscription status in the AWS Marketplace console under **Manage subscriptions**.

## Troubleshoot AWS Marketplace managed rule groups in Network Firewall
<a name="troubleshooting-aws-marketplace-managed-rule-groups"></a>

As a best practice, before using a rule group in production, with logging enabled, run the AWS Marketplace managed rule group in a specific mode depending on the intention of the firewall. You can use **alert mode** if you're using the firewall as an intrusion detection system (IDS) or you can use **drop mode** if you use the firewall as an intrusion prevention system (IPS) in a non-production environment. Either mode sends alert messages to the logs for traffic that doesn't pass inspection. For more information, see [Logging network traffic from AWS Network Firewall.](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html)

Running a managed rule group in either alert mode or drop mode allows you to do a dry run with alert logs that show you what the resulting behavior would be before you commit to making changes to your traffic. Evaluate the rule group using Network Firewall logs. When you're satisfied that the rule group does what you want it to do, disable test mode on the group.

For more information about a rule in an AWS Marketplace managed rule group, see the provider's listing at AWS Marketplace or contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## Considerations while using AWS Marketplace managed rule groups in AWS Network Firewall
<a name="considerations-aws-marketplace-managed-rule-groups"></a>

You can subscribe to AWS Marketplace managed rule groups either by visiting the product page in the Marketplace console or via Network Firewall console. While the experience is similar, you would be automatically redirected to the Seller's home page while subscribing to the product from Marketplace console, however you would not be redirected to this page if you attempted to subscribe via NFW console. If you would like to use NFW console to subscribe to a AWS Marketplace managed rule group, we recommend visiting the seller's home page and enter your details separately.