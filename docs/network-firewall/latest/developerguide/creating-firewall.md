# Creating a firewall in AWS Network Firewall

You can create a firewall in Network Firewall to start using the protections you've defined in a firewall policy to protect a VPC.

There are two ways you can create a firewall:

- Create a VPC-attached firewall to protect a VPC
- Create a transit gateway-attached firewall to enable centralized network inspection

###### Note

To create a transit gateway-attached firewall, you can accept a transit gateway that has been shared with you through AWS RAM or a transit gateway that you own.

###### Important

Before you begin, make sure your VPC has at least one subnet that can host a firewall endpoint. The subnet must be dedicated to Network Firewall use and cannot be used for other resources. For information about subnet requirements and configuration, see [VPC subnets](vpc-config-subnets.md "vpc-config-subnets.md").

###### To create a firewall through the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. Choose **Create firewall**.
4. Enter a **Name** to identify this firewall.

###### Note

You can't change the name after you create the firewall. 5. (Optional) Enter a **Description** for the firewall to help you identify it among your other resources. 6. Choose **Next**. 7. Choose your **VPC** from the dropdown list.

###### Note

You can't change the VPC after you create the firewall. 8. For **Firewall subnets**, choose the Availability Zones and subnets that you want to use for your primary firewall endpoints. You can choose up to one subnet for each Availability Zone that your VPC spans, and you must specify a subnet in any Availability Zone where you want to create endpoints using VPC endpoint associations.

The subnets that you specify should be dedicated for Network Firewall firewall use. For more information, see [VPC subnets](vpc-config-subnets.md "vpc-config-subnets.md"). 9. Choose **Next**. 10. For **Attachment type**, choose either:

    * **VPC** - Create a firewall in subnets in a VPC
    * **Transit Gateway** - Create a firewall that automatically provisions networking components

11. Based on your attachment type selection:
    1.  If you selected **VPC**:
        1. Choose your **VPC** from the dropdown list.

        ###### Note

        You can't change the VPC after you create the firewall. 2. For **Firewall subnets**, choose the Availability Zones and subnets that you want to use for your firewall endpoints.

    2.  If you selected **Transit Gateway**:
        1. For **Transit Gateway**, choose an existing transit gateway from the dropdown list. The list includes:
           - Any transit gateway attachment in your account (marked as "this account")
           - AWS Transit Gateways shared with you from other accounts (showing the owner account ID)

        ###### Note

        If you need to create a new transit gateway, open the Transit Gateway console in a new tab. After creating the transit gateway, return to this page and refresh the Transit Gateway selector. 2. For **Availability Zones**, select the Availability Zones for your firewall. Consider:

            * To maintain Availability Zone isolation, enable the firewall in every Availability Zone where you have workloads
            * You must select at least one Availability Zone
            * You can modify Availability Zones later, but this may briefly disrupt traffic

12. (Optional) Under **Protection against changes**, optionally enable **Deletion protection** and **Subnet change protection** to protect your firewall against accidental changes.
13. (Optional) Under **Customer managed key**, optionally toggle **Customize encryption settings** to use a AWS Key Management Service customer managed key to encrypt your resources. For more information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md "kms-encryption-at-rest.md").
14. Choose **Next**.

(Optional) Under **Traffic analysis mode** optionally select **Enable traffic analysis mode** to enable access to HTTP and HTTPS traffic reporting.

###### Note

Enabling traffic analysis mode does not automatically generate a report when you finish creating your firewall. See [Reporting on network traffic in Network Firewall](reporting.md "reporting.md") for more information on report generation.

###### Important

Network Firewall only starts collecting traffic analysis metrics when you enable **Traffic analysis mode** on your firewall.
Traffic observed before you enable **Traffic analysis mode** is not included in reporting. 15. For the **Associate firewall policy** section, choose the firewall policy that you want to associate with the firewall. 16. Choose **Create firewall**.

## Next steps

After you create your firewall, it appears in the **Firewalls** page. As the firewall owner, you have full control over its configuration and management.

Complete these tasks to start using your firewall:

1. Required: Configure your firewall policy to define how traffic is filtered. For information, see [Firewall policies in AWS Network Firewall](firewall-policies.md "firewall-policies.md").
2. Required: Configure your VPC route tables to direct traffic through your firewall endpoints. For information, see [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md "vpc-config-route-tables.md").

You can also enhance your firewall's capabilities with these optional tasks:

- Set up logging to monitor network traffic through your firewall. For information, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").
- Create VPC endpoint associations to extend your firewall's protection to additional VPCs or to create multiple endpoints in a single Availability Zone. For information, see [Creating a VPC endpoint association](creating-vpc-endpoint-association.md "creating-vpc-endpoint-association.md").
