# Deleting a firewall policy in AWS Network Firewall

To delete a firewall policy, perform the following procedure.

###### Deleting a rule group, TLS inspection configuration, or firewall policy

When you delete a rule group, TLS inspection configuration, or a firewall policy, AWS Network Firewall checks to see if it's currently being referenced.
A rule group and TLS inspection configuration can be referenced by a firewall policy, and a firewall policy can be referenced by a firewall. If Network Firewall
determines that the resource is being referenced, it warns you. Network Firewall is almost always able to determine whether a
resource is being referenced. However, in rare cases, it might not be able to do so. If you need to be sure that the resource
that you want to delete isn't in use, check all of your firewalls or firewall policies before deleting it. Note that policies
that have associations can't be deleted.

###### To delete a firewall policy

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.
3. In the **Firewall policies** page, select firewall policy that you want
   to delete.
4. Choose **Delete**, and confirm your request.
   Your firewall policy is removed from the list in the **Firewall policies**
   page.
