# Understanding the differences between firewall owners and VPC endpoint association owners

If you create a firewall, you are that firewall's _firewall owner_. If you create a VPC endpoint
association for a firewall that is shared with you from another account, you are a _VPC endpoint association owner_.
For information about sharing firewalls with other accounts, see [Sharing Network Firewall resources](sharing.md "sharing.md").

The following table shows how the capabilities of firewall owners differ from those of VPC endpoint association owners.

| Capability                                                                                                                                       | Owner                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| Creates a firewall and manages the firewall's configuration and settings                                                                         | Firewall owner                 |
| Shares a firewall with other accounts to enable creation of VPC endpoint associations to their firewall                                          | Firewall owner                 |
| Creates VPC endpoint associations for their firewall, within their account                                                                       | Firewall owner                 |
| Can list any VPC endpoint association that is associated with their firewall, either from within their account or from another account           | Firewall owner                 |
| Receives a consolidated bill for their firewall's primary firewall endpoint and any additional firewall endpoints                                | Firewall owner                 |
| Has visibility into metrics for network traffic passing through their firewall's primary firewall endpoint and any additional firewall endpoints | Firewall owner                 |
| Can perform flow operations on a firewall's primary firewall endpoint and any additional firewall endpoints                                      | Firewall owner                 |
| Creates VPC endpoint associations for firewalls shared with them                                                                                 | VPC endpoint association owner |
| Uses the same configuration and settings for their VPC endpoint association as defined in the firewall                                           | VPC endpoint association owner |
| Routes network traffic through the VPC endpoint association they create                                                                          | VPC endpoint association owner |

For more information, see [Managing a firewall and firewall endpoints in AWS Network Firewall](firewall-managing.md "firewall-managing.md").

## Example ownership scenarios

Review the following examples to understand how different ownership scenarios may affect firewall and VPC endpoint association management.
These scenarios show common use cases but do not provide an exhaustive list of capabilities for either firewall owners or VPC endpoint association owners.
For a comprehensive list of capabilities, refer to the previous table.

In this scenario, one AWS account manages both the firewall and its VPC endpoint associations:

- The account creates a firewall in a production VPC
- The same account creates VPC endpoint associations to extend protection to development VPCs
- As both the firewall owner and VPC endpoint association owner, the account can:
  - Configure all firewall settings
  - Monitor traffic across all endpoints
  - Manage all VPC endpoint associations

In this scenario, two separate AWS accounts share firewall resources:

- Account A (firewall owner):
  - Creates and configures the firewall in its own VPC
  - Shares the firewall with Account B
  - Monitors traffic across all endpoints, including those in Account B

- Account B (VPC endpoint association owner):
  - Creates VPC endpoint associations in its own VPCs
  - Uses the firewall settings as configured by Account A
  - Cannot modify the firewall settings
