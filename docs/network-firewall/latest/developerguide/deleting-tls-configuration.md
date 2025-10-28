# Deleting a TLS inspection configuration in Network Firewall

To delete a TLS inspection configuration, perform the following procedure.

###### Deleting a TLS inspection configuration

When you delete a TLS inspection configuration, AWS Network Firewall checks to see if it's currently being referenced in a firewall policy. If
it is, Network Firewall sends you a warning, and doesn't delete the TLS inspection configuration. Network Firewall is almost always able to determine whether a
resource is being referenced, however, in rare cases it might not be able to do so. To be sure that the resource
that you want to delete isn't in use, check all of your firewall policies before deleting it. TLS inspection configurations referenced in firewall policies can't be deleted.

###### To delete a TLS inspection configuration

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **TLS inspection configurations**.
3. In the **TLS inspection configuration** page, select the TLS inspection configuration that you want to
   delete.
4. Choose **Delete**, and confirm your request.
   Your TLS inspection configuration is removed from the list in the **TLS inspection configuration**
   page.
