

# Getting started with Resolver DNS Firewall
<a name="resolver-dns-firewall-getting-started"></a>

The DNS Firewall console includes a wizard that guides you through the following steps for getting started with DNS Firewall:
+ Create rule groups for each set of rules that you want to use.
+ For each rule, populate the domain list that you want to inspect for. You can create your own domain lists and you can use AWS managed domain lists. 
+ Associate your rule groups with the VPCs where you want to use them.

## Resolver DNS Firewall walled garden example
<a name="dns-firewall-walled-garden-example"></a>

In this tutorial, you'll create a rule group that blocks all but a select group of domains that you trust. This is called a closed platform, or walled garden approach.

**To configure a DNS Firewall rule group using the console wizard**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

   Choose **DNS Firewall** in the navigation pane to open the DNS Firewall **Rule groups** page on the Amazon VPC console. Continue to step 3.

   - OR - 

   Sign in to the AWS Management Console and open the 

   the Amazon VPC console under [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/). 

1. In the navigation pane, under **DNS Firewall**, choose **Rule groups**.

1. On the navigation bar, choose the Region for the rule group. 

1. In the **Rule groups** page, choose **Add rule group**.

1. For the rule group name, enter **WalledGardenExample**. 

   In the **Tags** section, you can optionally enter a key-value pair for a tag. Tags help you organize and manage your AWS resources. For more information, see [Tagging Amazon Route 53 resources](tagging-resources.md). 

1. Choose **Add rule group**.

1. On the **WalledGardenExample** details page, choose the **Rules tab**, and then **Add rule**.

1. In the **Rule details** pane, enter the rule name ** BlockAll**.

1. In the **Domain list** pane, select **Add my own domain list**. 

1. Under **Choose or create a new domain list** select **Create new domain list**.

1. Enter a domain list name **AllDomains**, then in the **Enter one domain per line** text box, enter an asterisk: **\*** . 

1. For **Domain redirection setting** accept the default, and leave **Query type - optional** empty.

1. For the **Action**, select **BLOCK** and then leave the response to send at the default setting of **NODATA** . 

1. Choose **Add rule**. Your rule **BlockAll** is displayed in the **Rules** tab on the ** WalledGardenExample** page.

1. On the **WalledGardenExample** page, choose **Add rule** to add a second rule to your rule group. 

1. In the **Rule details** pane, enter the rule name ** AllowSelectDomains** .

1. In the **Domain list** pane, select **Add my own domain list**. 

1. Under **Choose or create a new domain list**, select **Create new domain list**.

1. Enter a domain list name **ExampleDomains**.

1. In the **Enter one domain per line** text box, on the first line, enter **example.com** and on the second line, enter **example.org**. 
**Note**  
If you want the rule to apply to subdomains as well, you need to add those domains to the list also. For example, to add all of the example.com's subdomains, add **\*.example.com** to the list.

1. For **Domain redirection setting** accept the default, and leave **Query type - optional** empty.

1. For the **Action**, select **ALLOW**. 

1. Choose **Add rule**. Your rules are both displayed in the ** Rules** tab on the **WalledGardenExample** page.

1. In the **Rules** tab on the **WalledGardenExample** page, you can adjust the evaluation order of the rules in your rule group by selecting the number listed in the **Priority column** and typing in a new number. DNS Firewall evaluates rules starting with the lowest priority setting, so the rule with the lowest priority is the first one evaluated. For this example, we want DNS Firewall to first identify and allow DNS queries for the select list of domains, and then block any remaining queries. 

   Adjust the rule priority so that **AllowSelectDomains** has a lower priority.

You now have a rule group that allows only specific domain queries through. To begin using it, you associate it with the VPCs where you want to use the filtering behavior. For more information, see [Managing associations between your VPC and Resolver DNS Firewall rule group](resolver-dns-firewall-vpc-associating-rule-group.md).

## Resolver DNS Firewall block list example
<a name="dns-firewall-block-list-example"></a>

In this tutorial, you'll create a rule group that blocks domains that you know to be malicious. You'll also add a DNS query type that is allowed for the domains in the blocked list. The rule group allows all other outbound DNS requests over the VPC Resolver.

**To configure a DNS Firewall block list by using the console wizard**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

   Choose **DNS Firewall** in the navigation pane to open the DNS Firewall **Rule groups** page on the Amazon VPC console. Continue to step 3.

   - OR - 

   Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **DNS Firewall**, choose **Rule groups**.

1. On the navigation bar, choose the Region for the rule group. 

1. In the **Rule groups** page, choose **Add rule group**.

1. For the rule group name, enter **BlockListExample**. 

   In the **Tags** section, you can optionally enter a key-value pair for a tag. Tags help you organize and manage your AWS resources. For more information, see [Tagging Amazon Route 53 resources](tagging-resources.md). 

1. On the **BlockListExample** details page, choose the ** Rules** tab, and then **Add rule**.

1. In the **Rule details** pane, enter the rule name ** BlockList**.

1. In the **Domain list** pane, select **Add my own domain list**. 

1. Under **Choose or create a new domain list**, select **Create new domain list**.

1. Enter a domain list name **MaliciousDomains**, then in the text box, enter the domains you want to block. For example, ** example.org**. Enter one domain per line. 
**Note**  
If you want the rule to apply to subdomains as well, you must add those domains to the list also. For example, to add all of the example.org's subdomains, add **\*.example.org** to the list.

1. For **Domain redirection setting** accept the default, and leave **Query type - optional** empty.

1. For the action, select **BLOCK** and then leave the response to send at the default setting of **NODATA**. 

1. Choose **Add rule**. Your rule is displayed in the ** Rules** tab on the **BlockListExample** page

1. in the **Rules** tab on the **BlockedListExample** page, you can adjust the evaluation order of the rules in your rule group by selecting the number listed in the **Priority column** and typing in a new number. DNS Firewall evaluates rules starting with the lowest priority setting, so the rule with the lowest priority is the first one evaluated. 

   Select and adjust the rule priority so that **BlockList** is evaluated either before or after any other rules you might have. Most of the time, known malicious domains should be blocked first. That is, the rules associated with them should have the lowest priority number.

1. To add a rule that allows MX records for the BlockList domains, on the ** BlockedListExample** details page in the **Rules** tab, choose **Add rule**.

1. In the **Rule details** pane, enter the rule name ** BlockList-allowMX**.

1. In the **Domain list** pane, select **Add my own domain list**. 

1. Under **Choose or create a new domain list**, select ** MaliciousDomains**.

1. For **Domain redirection setting** accept the default.

1. In the **DNS query type** list, select **MX: Specifies mail servers**.

1. For the action, select **ALLOW**. 

1. Choose **Add rule**. 

1. in the **Rules** tab on the **BlockedListExample** page, you can adjust the evaluation order of the rules in your rule group by selecting the number listed in the **Priority column** and typing in a new number. DNS Firewall evaluates rules starting with the lowest priority setting, so the rule with the lowest priority is the first one evaluated. 

   Select and adjust the rule priority so that **BlockList-allowMX** is evaluated either before or after any other rules you might have. Because you want to allow MX queries, make sure that the **BlockList-allowMX** rule has a lower priority than **BlockList**.

You now have a rule group that blocks specific malicious domain queries, but allows a specific DNS query type. To begin using it, you associate it with the VPCs where you want to use the filtering behavior. For more information, see [Managing associations between your VPC and Resolver DNS Firewall rule group](resolver-dns-firewall-vpc-associating-rule-group.md).