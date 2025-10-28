# Create a route table prefix list reference in AWS Transit Gateway

You can reference a prefix list in your transit gateway route table. A prefix list is
a set of one or more CIDR block entries that you define and manage. You can use a prefix
list to simplify the management of the IP addresses that you reference in your resources
to route network traffic. For example, if you frequently specify the same destination
CIDRs across multiple transit gateway route tables, you can manage those CIDRs in a
single prefix list, instead of repeatedly referencing the same CIDRs in each route
table. If you need to remove a destination CIDR block, you can remove its entry from the
prefix list instead of removing the route from every affected route table.

When you create a prefix list reference in your transit gateway route table, each entry in
the prefix list is represented as a route in your transit gateway route table.

For more information about prefix lists, see [Prefix lists](../userguide/managed-prefix-lists.md "../userguide/managed-prefix-lists.md") in the
_Amazon VPC User Guide_.

###### To create a prefix list reference using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the transit gateway route table.
4. Choose **Actions**, **Create prefix list
   reference**.
5. For **Prefix list ID**, choose the ID of the prefix
   list.
6. For **Type**, choose if traffic to this prefix list should be
   allowed (**Active**) or dropped
   (**Blackhole**).
7. For **Transit gateway attachment ID**, choose the ID of the
   attachment to which to route traffic.
8. Choose **Create prefix list reference**.

###### To create a prefix list reference using the AWS CLI

Use the [create-transit-gateway-prefix-list-reference](../../../cli/latest/reference/ec2/create-transit-gateway-prefix-list-reference.md "../../../cli/latest/reference/ec2/create-transit-gateway-prefix-list-reference.md") command.
