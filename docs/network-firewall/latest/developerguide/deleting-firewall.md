

# Deleting a firewall in AWS Network Firewall

The procedure for deleting a firewall has the following prerequisites:
+ You must disassociate the firewall from any other AWS resources, including VPC endpoint associations. If your firewall has a VPC endpoint association you don't own, ask the owner to delete that VPC endpoint association.
+ You must remove the firewall from any VPC route tables that mention it.
+ You must disable the firewall's logging configuration. For information about updating a firewall's logging configuration, see [Updating a AWS Network Firewall logging configuration](firewall-update-logging-configuration.md).

**To delete a firewall in the console**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. In the **Firewalls** page, select the firewall that you want to delete.

1. Choose **Delete**. If delete protection is turned on, choose **Disable delete protection** first.

1. For a NAT/Proxy firewall, to delete the NAT gateways that Network Firewall created along with the firewall, select **Also delete the NAT gateways this firewall created**. If you leave this cleared, the NAT gateways keep working as regular NAT gateways, and you must delete them separately in the Amazon VPC console. For information, see [NAT gateways that Network Firewall creates for a NAT/Proxy firewall](nfw-proxy-nat-gateways.md).

1. Confirm your request.

Your firewall is removed from the list in the **Firewalls** page. The removal can take a few minutes to complete.