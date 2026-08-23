Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Using AWS IAM Identity Center authentication with enhanced VPC routing

When [enhanced VPC routing](enhanced-vpc-routing.md "enhanced-vpc-routing.md") is
turned on, Redshift routes traffic through your virtual private cloud (VPC) instead of over
the internet. This includes the calls that Redshift makes to authenticate an AWS IAM Identity Center
user. This applies whether the user signs in interactively or connects with an
AWS IAM Identity Center token obtained through trusted identity propagation. For these connections to
succeed, Redshift must be able to reach AWS IAM Identity Center from your VPC. Interface VPC endpoints
are the recommended way to provide this connectivity. They let your provisioned cluster or
Amazon Redshift Serverless workgroup reach AWS IAM Identity Center over the AWS network.

###### Important

These requirements apply to any connection authenticated through AWS IAM Identity Center. IAM
users and local database users authenticate through different mechanisms and aren't
affected. If enhanced VPC routing is turned off, these endpoints aren't required.

###### Note

Changing enhanced VPC routing restarts a provisioned cluster. For more information
about turning on enhanced VPC routing, see [Turning on enhanced VPC
routing](enhanced-vpc-enabling-cluster.md "enhanced-vpc-enabling-cluster.md").

## Interface VPC endpoints

Create the following interface VPC endpoints (AWS PrivateLink) in the VPC where your
cluster or workgroup resides. Both endpoints are required. If either endpoint is missing or
unreachable, AWS IAM Identity Center sign-in fails.

`com.amazonaws.`region`.sso-oauth`

Validates the AWS IAM Identity Center access token that the user presents at sign-in and
exchanges it for a token scoped to your Redshift session.

`com.amazonaws.`region`.identitystore`

Resolves the user and their AWS IAM Identity Center group memberships from the AWS IAM Identity Center
identity store.

For information about creating an interface VPC endpoint, see [Create a VPC
endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Before you create the endpoints, confirm that the `DNS hostnames` and
`DNS resolution` attributes are turned on for the VPC where your cluster or
workgroup runs. Private DNS names depend on both attributes. For more information, see
[DNS
attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") in the _Amazon VPC User Guide_.

Enhanced VPC routing requires that your provisioned cluster or Redshift Serverless workgroup is not
publicly accessible.

When you create each endpoint, do the following:

- **Turn on private DNS names** – Redshift
  connects to these services using their standard DNS names. Without private DNS names,
  those names continue to resolve to public addresses and the calls don't route to your
  endpoints.
- **Create the endpoints in the AWS IAM Identity Center Region**
  – AWS IAM Identity Center is a Regional service. Create these endpoints in the Region where
  your AWS IAM Identity Center instance runs. If your cluster or workgroup runs in a different Region
  and you don't use AWS IAM Identity Center multi-Region replication, use the cross-Region endpoint
  option so that the endpoints reach the AWS IAM Identity Center Region.
- **Choose subnets in the same Availability Zones**
  – Select subnets in the Availability Zones that your cluster or workgroup
  uses.
- **Allow inbound HTTPS** – The security group
  attached to each endpoint must allow inbound traffic on TCP port 443 from your cluster
  or workgroup subnets.
- **Keep the default endpoint policy** – The
  default policy allows full access. If your organization requires a restrictive endpoint
  policy, scope it by principal rather than by a list of actions. Then verify that
  sign-in still succeeds.

## Using AWS Network Firewall

AWS Network Firewall is optional. If you filter outbound traffic with AWS Network
Firewall instead of using interface VPC endpoints, the firewall policy must allow the AWS
IAM Identity Center service domains. Otherwise sign-in fails when Redshift can't reach them. Add the
following domains to your firewall's allow list, replacing
`region` with your AWS IAM Identity Center Region:

`oidc.`region`.amazonaws.com`

Validates the AWS IAM Identity Center access token and exchanges it for a token scoped to
your Redshift session.

`.sso.`region`.amazonaws.com`

Reaches the AWS IAM Identity Center service to resolve the AWS IAM Identity Center application and its
assignments.

`identitystore.`region`.amazonaws.com`

Resolves the user and their AWS IAM Identity Center group memberships.

If your firewall uses a deny-by-default policy, it must also allow the domains that
Redshift uses for general operation under enhanced VPC routing, such as Amazon S3 and, if you
query a data lake, AWS Glue. For more information, see [Enhanced VPC routing in Amazon Redshift](enhanced-vpc-routing.md "enhanced-vpc-routing.md").

Using interface VPC endpoints, as described in [Interface VPC endpoints](#redshift-iam-access-control-idp-connect-evr-endpoints "#redshift-iam-access-control-idp-connect-evr-endpoints"), keeps this
traffic on the AWS network and doesn't require firewall allow-listing.
