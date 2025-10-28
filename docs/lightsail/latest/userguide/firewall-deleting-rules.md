# Delete firewall rules

In addition to adding and editing firewall rules, you might also want to delete existing
rules for your Amazon Lightsail instances. Removing firewall rules can be necessary if you no
longer require certain inbound traffic to be allowed to your instance. The process for
deleting IPv4 and IPv6 firewall rules is straightforward and can be done directly through the
Lightsail console. Complete the following steps to delete instance firewalls rule in the
Lightsail console.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. In the left navigation pane, choose **Instances**.
3. Choose the name of the instance for which you want to delete a firewall rule.
4. Choose the **Networking** tab on your instance's management
   page.
5. Complete one of the following steps depending on whether the source IP for the rule is
   an IPv4 or IPv6 address:
   - To delete an IPv4 firewall rule, scroll down to the **IPv4
     Firewall** section of the page, and choose **Delete** (the
     trash icon) next to an existing rule to delete it.
   - To delete an IPv6 firewall rule, scroll down to the **IPv6
     Firewall** section of the page, and choose **Delete** (the
     trash icon) next to an existing rule to delete it.

###### Important

Firewall rules affect only traffic that flows in through the public IP address of an
instance. It does not affect traffic that flows in through the private IP address of an
instance, which can originate from Lightsail resources in your account, in the same
AWS Region, or resources in a peered virtual private cloud (VPC), in the same
AWS Region. For example, if you delete the SSH rule (TCP port 22) from the instance
firewall, other instances in the same Lightsail account, and in the same AWS Region,
can continue to connect to it using SSH by specifying the private IP address of the
instance.

The firewall rule is deleted after a few moments.
