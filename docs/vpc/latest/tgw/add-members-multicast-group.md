

# Register members with a multicast group in AWS Transit Gateway
<a name="add-members-multicast-group"></a>

Use the following procedure to register group members with a multicast group. 

You need the following information before you add members:
+ The ID of the multicast domain
+ The IDs of the group members' network interfaces
+ The multicast group IP address

**To register members using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain, and then choose **Actions**, **Add group members**.

1. For **Group IP address**, enter either the IPv4 CIDR block or IPv6 CIDR block to assign to the multicast domain.

1. Under **Choose network interfaces**, select the multicast receivers' network interfaces.

1. Choose **Add members**.

**To register members using the AWS CLI**  
Use the [register-transit-gateway-multicast-group-members](https://docs.aws.amazon.com/cli/latest/reference/ec2/register-transit-gateway-multicast-group-members.html) command.