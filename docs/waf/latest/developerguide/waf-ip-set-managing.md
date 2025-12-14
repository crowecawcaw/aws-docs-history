**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating and managing an IP set in AWS WAF

An IP set provides a collection of IP addresses and IP address ranges that you want to use together in a rule statement. IP sets are AWS resources.

To use an IP set in a protection pack (web ACL) or rule group, you first create an AWS resource,
`IPSet` with your address specifications. Then you reference the set when
you add an IP set rule statement to a protection pack (web ACL) or rule group.

## Creating an IP set

Follow the procedure in this section to create a new IP set.

###### Note

In addition to the procedure in this section, you have the option to add a new
IP set when you add an IP match rule to your protection pack (web ACL) or rule group. Choosing
that option requires you to provide the same settings as those required by this
procedure.

###### To create an IP set

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **IP sets** and then
   **Create IP set**.
3. Enter a name and description for the IP set. You'll use these to identify the set when you
   want to use it.

###### Note

You can't change the name after you create the IP set. 4. For **Region**, choose Global (CloudFront) or choose the Region where you want to store the IP set.
You can use regional IP sets only in protection packs (web ACLs) that protect regional resources. To use
an IP set in protection packs (web ACLs) that protect Amazon CloudFront distributions, you must use Global (CloudFront). 5. For **IP version**, select the version you want to use. 6. In the **IP addresses** text box, enter one IP address or IP address range
per line, in CIDR notation. AWS WAF supports all IPv4 and IPv6 CIDR ranges except for `/0`.
For more information about CIDR notation, see the Wikipedia article [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing "https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing").

Here are some examples:

    * To specify the IPv4 address 192.0.2.44, type
     **192.0.2.44/32**.
    * To specify the IPv6 address 2620:0:2d0:200:0:0:0:0,
     type **2620:0:2d0:200:0:0:0:0/128**.
    * To specify the range of IPv4 addresses from 192.0.2.0 to
     192.0.2.255, type **192.0.2.0/24**.
    * To specify the range of IPv6 addresses from 2620:0:2d0:200:0:0:0:0
     to 2620:0:2d0:200:ffff:ffff:ffff:ffff, enter
     **2620:0:2d0:200::/64**.

7. Review the settings for the IP set, and choose **Create IP set**.

## Deleting an IP set

Follow the guidance in this section to delete a referenced set.

###### Deleting referenced sets and rule groups

When you delete an entity that you can use in a protection pack (web ACL), like an IP set, regex
pattern set, or rule group, AWS WAF checks to see if the entity is currently being
used in a protection pack (web ACL). If it finds that it is in use, AWS WAF warns you. AWS WAF is almost
always able to determine if an entity is being referenced by a protection pack (web ACL). However, in
rare cases it might not be able to do so. If you need to be sure that nothing is
currently using the entity, check for it in your protection packs (web ACLs) before deleting
it. If the entity is a referenced set, also check that no rule groups are using it.

###### To delete an IP set

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **IP sets**.
3. Select the IP set that you want to delete and choose **Delete**.
