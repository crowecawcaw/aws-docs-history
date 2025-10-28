**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Working with IP match conditions

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

If you want to allow or block web requests based on the IP addresses that the requests
originate from, create one or more IP match conditions. An IP match condition lists up
to 10,000 IP addresses or IP address ranges that your requests originate from. Later in
the process, when you create a web ACL, you specify whether to allow or block requests
from those IP addresses.

###### Topics

- [Creating an IP Match Condition](#classic-web-acl-ip-conditions-creating "#classic-web-acl-ip-conditions-creating")
- [Editing IP match conditions](#classic-web-acl-ip-conditions-editing "#classic-web-acl-ip-conditions-editing")
- [Deleting IP match conditions](#classic-web-acl-ip-conditions-deleting "#classic-web-acl-ip-conditions-deleting")

## Creating an IP Match Condition

If you want to allow some web requests and block others based on the IP addresses that the
requests originate from, create an IP match condition for the IP addresses that you want to allow
and another IP match condition for the IP addresses that you want to block.

###### Note

When you add an IP match condition to a rule, you also can configure AWS WAF Classic to allow or block
web requests that _do not_ originate from the IP addresses
that you specify in the condition.

###### To create an IP match condition

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. In the navigation pane, choose **IP addresses**. 3. Choose **Create condition**. 4. Enter a name in the **Name** field.

The name can contain only
alphanumeric characters (A-Z, a-z, 0-9) or the following special characters: \_-!"#`+\*},./ . You can't change the name of a condition after you create it. 5. Select the correct IP version and specify an IP address or range of IP addresses by using CIDR notation. Here are some examples:

    * To specify the IPv4 address 192.0.2.44, type **192.0.2.44/32**.
    * To specify the IPv6 address 0:0:0:0:0:ffff:c000:22c, type **0:0:0:0:0:ffff:c000:22c/128**.
    * To specify the range of IPv4 addresses from 192.0.2.0 to 192.0.2.255, type
     **192.0.2.0/24**.
    * To specify the range of IPv6 addresses from 2620:0:2d0:200:0:0:0:0 to
     2620:0:2d0:200:ffff:ffff:ffff:ffff, enter
     **2620:0:2d0:200::/64**.

AWS WAF Classic supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF Classic supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128. For more information about CIDR notation, see
the Wikipedia entry
[Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing "https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing"). 6. Choose **Add another IP address or range**. 7. If you want to add another IP address or range, repeat steps 5 and 6. 8. When you're finished adding values, choose **Create IP match condition**.

## Editing IP match conditions

You can add an IP address range to an IP match condition or delete a range. To change a range, add a new one and
delete the old one.

###### To edit an IP match condition

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. In the navigation pane, choose **IP addresses**. 3. In the **IP match conditions** pane, choose the IP match condition that you want to edit. 4. To add an IP address range:

    1. In the right pane, choose **Add IP address or range**.
    2. Select the correct IP version and enter an IP address range by using CIDR notation. Here are
     some examples:




    	* To specify the IPv4 address 192.0.2.44, enter **192.0.2.44/32**.
    	* To specify the IPv6 address 0:0:0:0:0:ffff:c000:22c, enter
    	 **0:0:0:0:0:ffff:c000:22c/128**.
    	* To specify the range of IPv4 addresses from 192.0.2.0 to 192.0.2.255, enter
    	 **192.0.2.0/24**.
    	* To specify the range of IPv6 addresses from 2620:0:2d0:200:0:0:0:0 to
    	 2620:0:2d0:200:ffff:ffff:ffff:ffff, enter
    	 **2620:0:2d0:200::/64**.
    AWS WAF Classic supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF Classic supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128. For more information about CIDR notation, see
     the Wikipedia entry
     [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing "https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing").
    3. To add more IP addresses, choose **Add another IP address** and enter the
     value.
    4. Choose **Add**.

5. To delete an IP address or range:
   1. In the right pane, select the values that you want to delete.
   2. Choose **Delete IP address or range**.

## Deleting IP match conditions

If you want to delete an IP match condition, you must first delete all IP addresses and
ranges in the condition and remove the condition from all the rules that are using
it, as described in the following procedure.

###### To delete an IP match condition

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. In the navigation pane, choose **IP addresses**. 3. In the **IP match conditions** pane, choose the IP match condition that you want to delete. 4. In the right pane, choose the **Rules** tab.

If the list of rules using this IP match condition is empty, go to step 6. If the list contains
any rules, make note of the rules, and continue with step 5. 5. To remove the IP match condition from the rules that are using it, perform the following steps:

    1. In the navigation pane, choose **Rules**.
    2. Choose the name of a rule that is using the IP match condition that you want to delete.
    3. In the right pane, select the IP match condition that you want to remove from the rule,
     and choose **Remove selected condition**.
    4. Repeat steps b and c for all the remaining rules that are using the IP match condition that
     you want to delete.
    5. In the navigation pane, choose **IP match conditions**.
    6. In the **IP match conditions** pane, choose the IP match condition that you want to delete.

6. Choose **Delete** to delete the selected condition.
