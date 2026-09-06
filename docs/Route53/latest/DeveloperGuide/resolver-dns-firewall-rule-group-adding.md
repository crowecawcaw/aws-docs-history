

# Creating a rule group and rules
<a name="resolver-dns-firewall-rule-group-adding"></a>

To create a rule group and add rules to it, follow the steps in this procedure.

**To create a rule group and its rules**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

   Choose **DNS Firewall** in the navigation pane to open the DNS Firewall **Rule groups** page on the Amazon VPC console. Continue to step 3.

   - OR - 

   Sign in to the AWS Management Console and open the 

   the Amazon VPC console under [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/). 

1. In the navigation pane, under **DNS Firewall**, choose **Rule groups**.

1. On the navigation bar, choose the Region for the rule group. 

1. Choose **Add rule group**, then follow the wizard guidance to specify your rule group and rule settings.

   When you add rules to a rule group, first select the rule type: **Foundation** or **Advanced**.
   + **Foundation** – Select a rule protection to create rules with your own custom domain lists or AWS essential managed domain lists.

     For more information about custom domain lists, see [Managing your own domain lists](resolver-dns-firewall-user-managed-domain-lists.md).

     For more information about managed domain lists, see [Managed Domain Lists](resolver-dns-firewall-managed-domain-lists.md).
   + **Advanced** – Select one or more advanced managed domain lists (threat and content categories) or an advanced protection (Domain Generation Algorithms, Dictionary DGA, or DNS tunneling).

     For more information about advanced managed domain lists, see [Advanced Managed Domain Lists](firewall-advanced-managed-domain-lists.md).

     For more information about advanced protections, see [Advanced DNS Protections](firewall-advanced-protections.md).

1. With each rule, you can select one or more rule settings.

   For information about the values for rule groups, see [Rule group settings in DNS Firewall](resolver-dns-firewall-rule-group-settings.md).

   For information about the values for rules, see [Rule settings in DNS Firewall](resolver-dns-firewall-rule-settings.md).