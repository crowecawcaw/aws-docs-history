

# Modify a prefix list reference in AWS Transit Gateway
<a name="modify-prefix-list-reference"></a>

You can modify a prefix list reference by changing the attachment that the traffic is routed to, or indicating whether to drop traffic that matches the route.

You cannot modify the individual routes for a prefix list in the **Routes** tab. To modify the entries in the prefix list, use the **Managed Prefix Lists** screen. For more information, see [Modifying a prefix list](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html#modify-managed-prefix-list) in the *Amazon VPC User Guide*.

**To modify a prefix list reference using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the transit gateway route table.

1. In the lower pane, choose **Prefix list references**.

1. Choose the prefix list reference, and choose **Modify references**. 

1.  For **Type**, choose if traffic to this prefix list should be allowed (**Active**) or dropped (**Blackhole**). 

1. For **Transit gateway attachment ID**, choose the ID of the attachment to which to route traffic.

1. Choose **Modify prefix list reference**.

**To modify a prefix list reference using the AWS CLI**  
Use the [modify-transit-gateway-prefix-list-reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-transit-gateway-prefix-list-reference.html) command.