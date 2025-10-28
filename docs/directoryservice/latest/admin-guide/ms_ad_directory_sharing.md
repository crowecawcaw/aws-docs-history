# Share your AWS Managed Microsoft AD

AWS Managed Microsoft AD integrates tightly with AWS Organizations to allow seamless directory sharing across
multiple AWS accounts. You can share a single directory with other trusted AWS accounts
within the same organization or share the directory with other AWS accounts that are outside
your organization. You can also share your directory when your AWS account is not currently a
member of an organization.

## Key directory sharing

concepts

You will get more out of the directory sharing feature if you become familiar with the
following key concepts.

![Two AWS Managed Microsoft AD with directory sharing, domain joins, and Amazon VPC peering.](images/directory_sharing_concepts.png)

### Directory owner account

A directory owner is the AWS account holder that owns the originating directory in
the shared directory relationship. An administrator in this account initiates the
directory sharing workflow by specifying which AWS accounts to share their directory
with. Directory owners can see who they've shared a directory with using the
**Scale & Share** tab for a given directory in the AWS Directory Service
console.

### Directory consumer account

In a shared directory relationship, a directory consumer represents the AWS account
to which the directory owner shared the directory with. Depending on the sharing method
used, an administrator in this account may need to accept an invite sent from the
directory owner before they can start using the shared directory.

The directory sharing process creates a shared directory in the directory consumer
account. This shared directory contains the metadata that enables the EC2 instance to
seamlessly join the domain, which locates the originating directory in the directory
owner account. Each shared directory in the directory consumer account has a unique
identifier (**Shared directory ID**).

### Sharing methods

AWS Managed Microsoft AD provides the following two directory sharing methods:

- **AWS Organizations** – This method makes it easier to share the
  directory within your organization because you can browse and validate the
  directory consumer accounts. To use this option, your organization must have
  **All features** enabled, and your directory must be in the
  organization management account. This method of sharing simplifies your setup
  because it doesn't require the directory consumer accounts to accept your
  directory sharing request. In the console, this method is referred to as
  **Share this directory with AWS accounts inside your
  organization**.
- **Handshake** – This method enables directory sharing
  when you aren't using AWS Organizations. The handshake method requires the directory
  consumer account to accept the directory sharing request. In the console, this
  method is referred to as **Share this directory with other
  AWS accounts**.

### Network connectivity

Network connectivity is a prerequisite to use a directory sharing relationship across
AWS accounts. AWS supports many solutions to connect your VPCs, some of these include
[VPC
peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md"), [Transit
Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md"), and [VPN](../../../vpc/latest/adminguide/Welcome.md "../../../vpc/latest/adminguide/Welcome.md"). To get
started, see [Tutorial: Sharing your AWS Managed Microsoft AD
directory for seamless EC2 domain-join](ms_ad_tutorial_directory_sharing.md "ms_ad_tutorial_directory_sharing.md").

## Considerations

The following are some considerations when using directory share with your AWS Managed Microsoft AD:

###### Pricing

- AWS charges an additional fee for directory sharing. The AWS account that is using the
  shared AWS Managed Microsoft AD is the account charged the sharing fees. To learn more, see the
  [Pricing](https://aws.amazon.com/directoryservice/pricing/ "https://aws.amazon.com/directoryservice/pricing/") page on the AWS Directory Service website.
- Directory sharing makes AWS Managed Microsoft AD a more cost-effective way of integrating with Amazon EC2 in
  multiple accounts and VPCs.

###### Region availability

- Directory sharing is available in all [AWS regions
  where AWS Managed Microsoft AD](regions.md "regions.md") is offered.
- In the AWS China (Ningxia), this feature is available only when using [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") (SSM) to seamlessly
  join your Amazon EC2 instances.

For more information about directory sharing and how to extend the reach of your
AWS Managed Microsoft AD directory across AWS account boundaries, see the following topics.

###### Topics

- [Tutorial: Sharing your AWS Managed Microsoft AD
  directory for seamless EC2 domain-join](ms_ad_tutorial_directory_sharing.md "ms_ad_tutorial_directory_sharing.md")
- [Unsharing your directory](ms_ad_directory_sharing_unshare.md "ms_ad_directory_sharing_unshare.md")
  **Additional resources**

- [Use case: Share your directory to seamlessly
  join amazon EC2 instances to a domain across AWS accounts](usecase6.md "usecase6.md")
- [AWS security blog article: How to join Amazon EC2 instances from multiple accounts and
  VPCs to a single AWS Managed Microsoft AD directory](https://aws.amazon.com/blogs/security/how-to-domain-join-amazon-ec2-instances-aws-managed-microsoft-ad-directory-multiple-accounts-vpcs/ "https://aws.amazon.com/blogs/security/how-to-domain-join-amazon-ec2-instances-aws-managed-microsoft-ad-directory-multiple-accounts-vpcs/")
- [Joining your Amazon RDS DB instances across accounts to a single shared domain](https://aws.amazon.com/blogs/database/joining-your-amazon-rds-instances-across-accounts-to-a-single-shared-domain/ "https://aws.amazon.com/blogs/database/joining-your-amazon-rds-instances-across-accounts-to-a-single-shared-domain/")
