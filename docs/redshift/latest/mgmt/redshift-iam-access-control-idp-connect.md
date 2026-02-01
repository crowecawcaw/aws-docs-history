Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connect Redshift with AWS IAM Identity Center

for a single sign-on experience

You can manage user and group access to Amazon Redshift data warehouses through trusted-identity
propagation.

[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") is an AWS IAM Identity Center feature that administrators of connected AWS services can use to grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators. For more information, see [Prerequisites and considerations](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md").

To illustrate one end-to-end case, you can use an Amazon Quick Suite dashboard or
Amazon Redshift query editor v2 to access Redshift. Access in this case is based on AWS IAM Identity Center groups.
Redshift can determine who a user is and their group memberships. AWS IAM Identity Center also makes it
possible to connect and manage identities through a third-party identity provider (IdP) like
Okta or PingOne.

After your administrator sets up the connection between Redshift and AWS IAM Identity Center, they
can configure fine-grained access based on identity-provider groups to authorize user access
to data.

###### Important

When you delete a user from an AWS IAM Identity Center or a connected identity provider (IdP)
directory, the user is not automatically deleted from the Amazon Redshift catalog.

To manually delete the user from the Amazon Redshift catalog, run the `DROP USER` command to
fully delete the user that was removed from an AWS IAM Identity Center or IdP. For more information
about how to drop a user, see [DROP USER](../dg/r_DROP_USER.md "../dg/r_DROP_USER.md") in the
_Amazon Redshift Database Developer Guide_.

## Benefits of Redshift

integration with AWS IAM Identity Center

Using AWS IAM Identity Center with Redshift can benefit your organization in the following
ways:

- Dashboard authors in Amazon Quick Suite can connect to Redshift data
  sources without having to re-enter passwords or requiring an administrator to set up
  IAM roles with complex permissions.
- AWS IAM Identity Center provides a central location for your workforce users in AWS. You can
  create users and groups directly in AWS IAM Identity Center or connect existing users and groups
  that you manage in a standards-based identity provider like Okta, PingOne, or Microsoft
  Entra ID (Azure AD). AWS IAM Identity Center directs authentication to your chosen source of truth
  for users and groups, and it maintains a directory of users and groups for access by
  Redshift. For more information, see [Manage your identity
  source](../../../singlesignon/latest/userguide/manage-your-identity-source.md "../../../singlesignon/latest/userguide/manage-your-identity-source.md") and [Supported identity
  providers](../../../singlesignon/latest/userguide/supported-idps.md "../../../singlesignon/latest/userguide/supported-idps.md") in the _AWS IAM Identity Center User Guide_.
- You can share one AWS IAM Identity Center instance with multiple Redshift clusters and
  workgroups with a simple auto-discovery and connect capability. This makes it fast to
  add clusters without the extra effort of configuring the AWS IAM Identity Center connection for
  each, and it ensures that all clusters and workgroups have a consistent view of users,
  their attributes, and groups. Note that your organization's AWS IAM Identity Center instance must be
  in the same region as any Redshift datashares you're connecting to.
- Because user identities are known and logged along with data access, it's easier for
  you to meet compliance regulations through auditing user access in
  AWS CloudTrail.

## Administrator personas for connecting

applications

The following are personas that are key to connecting analytics applications to the
AWS IAM Identity Center managed application for Redshift:

- **Application administrator** – Creates an
  application and configures which services it will enable identity-token exchanges with.
  This administrator also specifies which users or groups have access to the
  application.
- **Data administrator** – Configures fine-grained
  access to data. Users and groups in AWS IAM Identity Center can map to specific permissions.

## Connecting to Amazon Redshift with AWS IAM Identity Center

through Amazon Quick Suite

The following shows how to use Quick Suite to authenticate with Redshift when it's connected
to and access is managed through AWS IAM Identity Center: [Authorizing connections from Quick Suite to Amazon Redshift
clusters](../../../quicksuite/latest/user/enabling-access-redshift.md "../../../quicksuite/latest/user/enabling-access-redshift.md"). These steps apply to Amazon Redshift Serverless too.

## Connecting to Amazon Redshift with AWS IAM Identity Center

through Amazon Redshift query editor v2

Upon completing the steps to set up an AWS IAM Identity Center connection with Redshift, the user
can access the database and appropriate objects in the database through their AWS
IAM Identity Center-based, namespace-prefixed identity. For more information about connecting to Redshift
databases with query editor v2 sign-in, see [Querying a database using the query editor v2](query-editor-v2.md "query-editor-v2.md").

## Limitations for connecting to Amazon Redshift with AWS IAM Identity Center

When using AWS IAM Identity Center single sign-on, consider the following limitation:

- **No support for enhanced VPC** – Enhanced VPC
  isn't supported when you use AWS IAM Identity Center single sign-on for Amazon Redshift.
  For more information about enhanced VPC, see [Enhanced VPC routing in
  Amazon Redshift](enhanced-vpc-routing.md "enhanced-vpc-routing.md").
