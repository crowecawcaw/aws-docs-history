# Create a shared VPC attachment in an AWS Cloud WAN core network

 Use the AWS Network Manager console to create a shared VPC attachment that can be used across
 accounts.

###### To create a shared VPC attachment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, under **Shared by me**, choose
 **Attachments**.
5. Choose **Create attachment**.
6. Enter a `name` to identify the attachment.
7. From the **Core network** dropdown list, choose the core network
 that is shared with you and that is where you want to create the VPC
 attachment.
8. From the **Edge location** dropdown list, choose the location
 where the attachment is located.
9. From the **Attachment type** dropdown list, choose
 **VPC**.
10. Optionally choose any of the following:




	* Choose **Appliance mode support** if appliance mode is
	 supported. For more information about appliance mode, see [Appliance mode](cloudwan-vpc-attachment.md#cloudwan-appliancemode "cloudwan-vpc-attachment.md#cloudwan-appliancemode").
	* Choose **IPv6 support** if the attachment supports
	 IPv6.
	* By default, **DNS support**  is enabled. This allows
	 domain name system resolution for the attachment. Clear the check box if you
	 don't want to enable DNS support. For more information, see [DNS support](cloudwan-vpc-attachment.md#cloudwan-dns-support "cloudwan-vpc-attachment.md#cloudwan-dns-support").
	* By default **Security Group Referencing support** is
	 enabled. When you create a VPC attachment, Cloud WAN automatically enables
	 security group referencing for VPCs attached to the same core network edge.
	 This allows you to reference security groups across VPCs in your security
	 group rules. Clear the check box if you don't want to enable security group
	 referencing. For more information, see [Security group referencing](cloudwan-vpc-attachment.md#cloudwan-sg-referencing "cloudwan-vpc-attachment.md#cloudwan-sg-referencing").
11. Choose the **VPC ID**. You're then prompted to choose the
 **Availability Zone** and **Subnet Id** in
 which to create the core network VPC attachment. The Availability Zones that are
 listed are those edge locations that you chose when you created your core network.
 You must choose at least one Availability Zone and subnet ID.
12. (Optional) In the **Tags** section, add **Key**
 and **Value** pairs to help identify this resource. You can
 add multiple tags by choosing **Add tag**, or remove any tag by
 choosing **Remove tag**.
13. Choose **Create attachment**.
14. The **Attachment** page displays the following information about
 your shared attachments:




	* **Attachment ID**
	* **Name**
	* **Edge location**
	* **Resource Type**
	* **Resource ID**
	* **State**
	* **Core network**
	* **Core network status**
15. Choose **Create attachment** to create a new shared VPC
 attachment.
