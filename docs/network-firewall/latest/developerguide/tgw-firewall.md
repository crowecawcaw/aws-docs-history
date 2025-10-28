# Transit gateway-attached firewalls in Network Firewall

The AWS Network Firewall integration with AWS Transit Gateway lets you create and centrally manage firewall protective coverage
without needing to provision multiple firewall endpoints.

Firewall owners can attach a Network Firewall directly to a transit gateway as a transit gateway attachment
either within their own account or shared from a different account. For more information,
see [Create a transit gateway-attached firewall](create-tgw-firewall.md "create-tgw-firewall.md").

## Key concepts

Review the following concepts before you continue. Note that these definitions are in the context of the Network Firewall integration with AWS Transit Gateway.

###### Transit Gateway

A transit gateway works across AWS accounts, and you can use AWS RAM to share your transit gateway with other accounts.
When a transit gateway is shared, recipients can use it to create a _transit gateway attachment_.

###### Transit gateway-attached firewall

A type of transit gateway attachment. When a Network Firewall account owner uses a shared transit gateway to provision a firewall, they bypass the networking configuration
required by the standard firewall setup. The firewall a Network Firewall provisions using a shared transit gateway is a _transit gateway-attached firewall_.

###### AWS RAM sharing account

The sharing account contains the resource that is shared. In the context of the Network Firewall integration with AWS Transit Gateway,
the AWS RAM sharing account that shares the transit gateway is referred to as the _transit gateway owner._

###### Ownership scenarios

Similar to working with firewalls and firewall endpoints created in Network Firewall, different account ownership scenarios impact how you
work with a transit gateway-attached firewall.

- The transit gateway owner is the account that owns the transit gateway
- The firewall owner is the account that creates and manages the transit gateway-attached firewall

###### Note

These roles can be in the same account or in different accounts.

###### Topics

- [Considerations for transit gateway-attached firewalls](tgw-firewall-considerations.md "tgw-firewall-considerations.md")
- [Create a transit gateway-attached firewall from a shared transit gateway](create-tgw-firewall.md "create-tgw-firewall.md")
- [Working with transit gateway-attached firewalls](working-with-tgw-firewalls.md "working-with-tgw-firewalls.md")
