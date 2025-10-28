# Modify a prefix list reference in AWS Transit Gateway

You can modify a prefix list reference by changing the attachment that the traffic is
routed to, or indicating whether to drop traffic that matches the route.

You cannot modify the individual routes for a prefix list in the
**Routes** tab. To modify the entries in the prefix list, use the
**Managed Prefix Lists** screen. For more information, see [Modifying a
prefix list](../userguide/managed-prefix-lists.md#modify-managed-prefix-list "../userguide/managed-prefix-lists.md#modify-managed-prefix-list") in the _Amazon VPC User Guide_.

###### To modify a prefix list reference using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the transit gateway route table.
4. In the lower pane, choose **Prefix list references**.
5. Choose the prefix list reference, and choose **Modify
   references**.
6. For **Type**, choose if traffic to this prefix list should
   be allowed (**Active**) or dropped
   (**Blackhole**).
7. For **Transit gateway attachment ID**, choose the ID of the
   attachment to which to route traffic.
8. Choose **Modify prefix list reference**.

###### To modify a prefix list reference using the AWS CLI

Use the [modify-transit-gateway-prefix-list-reference](../../../cli/latest/reference/ec2/modify-transit-gateway-prefix-list-reference.md "../../../cli/latest/reference/ec2/modify-transit-gateway-prefix-list-reference.md") command.
