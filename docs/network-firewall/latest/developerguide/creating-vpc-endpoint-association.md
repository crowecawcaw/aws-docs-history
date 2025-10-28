# Creating a VPC endpoint association in AWS Network Firewall

Create VPC endpoint associations to establish new firewall endpoints in any Availability Zone where the firewall is already being used. The first use of a firewall in an Availability Zone must be defined by the firewall owner in the firewall subnet specifications. For more information about where to specify endpoints, see [Firewalls and firewall endpoints](firewalls.md "firewalls.md").

###### Important

VPC endpoint associations are available for firewalls created in Network Firewall, but not transit gateway-attached firewalls created using AWS Transit Gateway.

Before you create a VPC endpoint association, review these requirements:

- You must own the firewall that you want to use or it must be shared with you. If you don't own the firewall, ask the owner to share it with your account. For information about sharing firewalls, see [Sharing Network Firewall resources](sharing.md "sharing.md").
- VPC endpoint association can only be created in an Availability Zone where the firewall consists of primary endpoints.
- For same-account associations:
  - VPC endpoint association can be created within Firewall owner's account - for the same primary VPC within different subnets or different VPCs

- For cross-account associations:
  - VPC endpoint association can be created from another account for different VPCs, but the firewall must be shared with you

- The subnet that you want to use in the VPC must be available to host a firewall endpoint. For information, see [VPC subnets](vpc-config-subnets.md "vpc-config-subnets.md").

###### To create a VPC endpoint association through the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **VPC endpoint associations**.
3. In the **VPC endpoint associations** page, choose **Create VPC endpoint association**.
4. Choose the firewall that you want to use.
5. Choose the VPC that you want to protect.
6. Choose the Availability Zone and subnet where you want to place the firewall endpoint. The subnet should be dedicated for Network Firewall firewall use. For more information, see [VPC subnets](vpc-config-subnets.md "vpc-config-subnets.md").

###### Note

If you don't see the Availability Zone that you want, check that the firewall itself has a subnet defined there. You can only define VPC endpoint associations in Availability Zones where the firewall is already in use. If you don't own the firewall, ask the owner. 7. (Optional) Expand the **Additional configurations** and provide a description for the association and assign key-value tags to it. For information about tagging your AWS resources, see [Tagging AWS Network Firewall resources](tagging.md "tagging.md") 8. Choose **Create VPC endpoint association**.

## Next steps

After you create a VPC endpoint association, complete these steps:

1. Verify the status of your VPC endpoint association. The status should change from **Provisioning** to **Ready** when the endpoint is available to process traffic.
2. Configure your VPC route tables to direct traffic through the new firewall endpoint. For information, see [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md "vpc-config-route-tables.md").
3. If needed, update your firewall policy to accommodate the new endpoint. See [Firewall policies in AWS Network Firewall](firewall-policies.md "firewall-policies.md") for details on managing firewall policies.
4. Consider setting up logging for your firewall to track traffic through the new endpoint. For information about logging, see [Logging and monitoring in AWS Network Firewall](logging-monitoring.md "logging-monitoring.md").

Remember, changes to your network configuration can affect your security posture. Always verify that your new endpoint is functioning as expected and that it complies with your organization's security policies.
