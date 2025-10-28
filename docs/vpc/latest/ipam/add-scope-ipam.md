# Create additional scopes

Follow the steps in this section to create an additional scope.

A scope is the highest-level container within IPAM. When you create an IPAM, IPAM creates two default scopes for you. Each scope represents the IP space for a single network. The private scope is intended for all private space. The public scope is intended for all public space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.

When you create an IPAM, default scopes (one private and one public) are created for you.
You can create additional private scopes. You cannot create additional public scopes.

You can create additional private scopes if you require support for multiple disconnected
private networks. Additional private scopes allow you to create pools and manage resources
that use the same IP space.

###### Important

If IPAM discovers resources with private IPv4 or private IPv6 CIDRs, the resource
CIDRs are imported into the default private scope and do not appear in any additional
private scopes you create. You can move CIDRs from the default private scope to another
private scope. For information, see [Move VPC CIDRs between scopes](move-resource-ipam.md "move-resource-ipam.md").

AWS Management Console

###### To create an additional private scope

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Scopes**.
3. Choose **Create scope**.
4. Choose the IPAM that you want to add the scope to.
5. Add a description for the scope.
6. Choose **Create scope**.
7. You can view the scope in IPAM by choosing **Scopes**
   in the navigation pane.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to create an additional private scope:

1. View your current scopes: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")
2. Create a new private scope: [create-ipam-scope](../../../cli/latest/reference/ec2/create-ipam-scope.md "../../../cli/latest/reference/ec2/create-ipam-scope.md")
3. View your current scopes to view the new scope: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")
