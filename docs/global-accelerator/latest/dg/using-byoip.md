

# Bring your own IP addresses (BYOIP) in Global Accelerator
<a name="using-byoip"></a>

You can bring part or all of your public IPv4 address ranges from your on-premises network to your AWS account to use with AWS Global Accelerator. You continue to own the address ranges, but AWS advertises them on the internet. BYOIP with IPv6 is not supported at this time.

Global Accelerator uses static IP addresses as entry points for your accelerators. These IP addresses are anycast from AWS edge locations. By default, Global Accelerator provides static IP addresses from the [Amazon IP address pool](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html). Instead of using the IP addresses that Global Accelerator provides, you can configure these entry points to be IPv4 addresses from your own address ranges. This topic explains how to use your own IP address ranges with Global Accelerator.

You can't use the IP addresses that you bring to AWS for one AWS service with another service. The steps in this chapter describe how to bring your own IP address range for use in AWS Global Accelerator only. For steps to bring your own IP address range for use in Amazon EC2, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html) in the Amazon EC2 User Guide.

**Important**  
You must stop advertising your IP address range from other locations before you advertise it through AWS. If an IP address range is multihomed (that is, the range is advertised by multiple service providers at the same time), we can't guarantee that traffic to the address range will enter our network or that your BYOIP advertising workflow will complete successfully.

After you bring an address range to AWS, it appears in your account as an address pool. When you create an accelerator, you can assign one IP address from your range to it. Global Accelerator assigns you a second static IP address from an Amazon IP address range. If you bring two IP address ranges to AWS, you can assign one IP address from each range to your accelerator. This restriction is because Global Accelerator assigns each address range to a different network zone, for high availability.

To use your own IP address range with Global Accelerator, review the requirements, and then follow the steps provided in this topic.

**Topics**
+ [Requirements](using-byoip.requirements.md)
+ [Prepare to bring your IP address range to your AWS account: Authorization](using-byoip.prepare.md)
+ [Provision the address range for use with Global Accelerator](using-byoip.provision.md)
+ [Advertise the address range through AWS](using-byoip.advertise.md)
+ [Deprovision the address range](using-byoip.deprovision.md)
+ [Use your BYOIP address with an accelerator in Global Accelerator](using-byoip.create-accelerator.md)
+ [Update an accelerator to change your IP addresses](using-byoip.update-accelerator.md)