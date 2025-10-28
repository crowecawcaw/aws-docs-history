# Associating VPC attachments and subnets with

a multicast domain in AWS Transit Gateway

Use the following procedure to associate a VPC attachment with a multicast domain. When
you create an association, you can then select the subnets to include in the multicast
domain.

Before you begin, you must create a VPC attachment on your transit gateway. For more
information, see [Amazon VPC attachments in AWS Transit Gateway](tgw-vpc-attachments.md "tgw-vpc-attachments.md").

###### To associate VPC attachments with a multicast domain using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Multicast**.
3. Select the multicast domain, and then choose **Actions**,
   **Create association**.
4. For **Choose attachment to associate**, select the transit gateway attachment.
5. For **Choose subnets to associate**, select the subnets to include in
   the multicast domain.
6. Choose **Create association**.

###### To associate VPC attachments with a multicast domain using the AWS CLI

Use the [associate-transit-gateway-multicast-domain](../../../cli/latest/reference/ec2/associate-transit-gateway-multicast-domain.md "../../../cli/latest/reference/ec2/associate-transit-gateway-multicast-domain.md") command.
