# Deleting a firewall in AWS Network Firewall

The procedure for deleting a firewall has the following prerequisites:

- You must disassociate the firewall from any other AWS resources, including VPC endpoint associations.
  If your firewall has a VPC endpoint association you don't own, ask the owner to delete that VPC endpoint association.
- You must remove the firewall from any VPC route tables that mention it.
- You must disable the firewall's logging configuration. For information about updating a firewall's logging configuration, see [Updating a AWS Network Firewall logging configuration](firewall-update-logging-configuration.md "firewall-update-logging-configuration.md").

###### To delete a firewall in the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. In the **Firewalls** page, select the firewall that you want to delete.
4. Choose **Delete**, and then confirm your request.
   Your firewall is removed from the list in the **Firewalls** page. The
   removal can take a few minutes to complete.
