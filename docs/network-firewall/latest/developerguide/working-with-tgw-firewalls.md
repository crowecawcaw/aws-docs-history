

# Working with transit gateway-attached firewalls
<a name="working-with-tgw-firewalls"></a>

After you accept a shared transit gateway attachment, the firewall you create appears in the **Firewalls** page of the Network Firewall console with one of the following statuses, depending on what state it is in:
+ `Pending` — the process to create a transit gateway-attached firewall has been initiated. The transit gateway owner must next accept the firewall from the transit gateway console. For more information, see [Accept a shared attachment using Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/acccept-tgw-attach.html) in the *Amazon VPC Developer Guide*.

  The transit gateway-attached firewall cannot monitor network traffic while pending, but the firewall owner can adjust the firewall's configuration using the steps in but [Updating a firewall in AWS Network Firewall](firewall-updating.md).
+ `Rejected` — the transit gateway owner has rejected the transit gateway-attached firewall. For more information, see [Accept a shared attachment using Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/acccept-tgw-attach.html) in the *Amazon VPC Developer Guide*.
+ `Ready` — the transit gateway-attached firewall has finished provisioning and has begun monitoring traffic according to the network configuration set in transit gateway.

As the transit gateway-attached firewall owner, you maintain control of the firewall configuration, while the transit gateway owner controls the routing of your traffic through the firewall through the networking configuration managed in the AWS Transit Gateway console and CLI.