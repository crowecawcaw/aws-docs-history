# Register sources with a multicast

group in AWS Transit Gateway

###### Note

This procedure is only required when you have set the **Static sources
support** attribute to **enable**.

Use the following procedure to register sources with a multicast group. The source is the
network interface that sends multicast traffic.

You need the following information before you add a source:

- The ID of the multicast domain
- The IDs of the sources' network interfaces
- The multicast group IP address

###### To register sources using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Multicast**.
3. Select the multicast domain, and then choose **Actions**,
   **Add group sources**.
4. For **Group IP address**, enter either the IPv4 CIDR block or IPv6
   CIDR block to assign to the multicast domain.
5. Under **Choose network interfaces**, select the multicast senders'
   network interfaces.
6. Choose **Add sources**.

###### To register sources using the AWS CLI

Use the [register-transit-gateway-multicast-group-sources](../../../cli/latest/reference/ec2/register-transit-gateway-multicast-group-sources.md "../../../cli/latest/reference/ec2/register-transit-gateway-multicast-group-sources.md") command.
