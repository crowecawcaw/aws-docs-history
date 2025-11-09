# Organization and account instances of IAM Identity Center

An instance is a single deployment of IAM Identity Center. There are two types of instances available for
IAM Identity Center: _organization instances_ and _account
instances_.

- Organization instance (recommended)

An instance of IAM Identity Center that you enable in the AWS Organizations management account. Organization
instances support all features of IAM Identity Center. We recommend that you deploy an organization
instance rather than account instances to minimize the number of management points.

- Account instance

An instance of IAM Identity Center that is bound to a single AWS account, and that is visible only
within the AWS account and AWS Region in which it is enabled. Use an account instance for
simpler, single-account scenarios. You can enable an account instance from either of the
following:

    + An AWS account that isn't managed by AWS Organizations
    + A member account in AWS Organizations

## AWS account types that can enable IAM Identity Center

To enable IAM Identity Center, sign in to the AWS Management Console by using one of the following credentials,
depending on the instance type you want to create:

- Your AWS Organizations management account (recommended) –
  Required to create an [organization
  instance](organization-instances-identity-center.md "organization-instances-identity-center.md") of IAM Identity Center. Use an organization instance for multi-account permissions and
  application assignments across the organization.
- Your AWS Organizations member account – Use to create an
  [account instance](account-instances-identity-center.md "account-instances-identity-center.md") of IAM Identity Center to
  enable application assignments within that member account. One or more accounts with a
  member level instance can exist in an organization.
- A standalone AWS account – Use to create an
  [organization instance](organization-instances-identity-center.md "organization-instances-identity-center.md") or
  [account instance](account-instances-identity-center.md "account-instances-identity-center.md") of IAM Identity Center. The
  standalone AWS account isn't managed by AWS Organizations. You can associate only one instance of
  IAM Identity Center with a standalone AWS account and use that instance for application assignments
  within that standalone AWS account.

Use the following table to compare the capabilities provided by the instance type:

| Capability                                                                   | Instance in the AWS Organizations management account (recommended) | Instance in a member account | Instance in a standalone AWS account |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------- | ------------------------------------ |
| Manage users                                                                 | Yes                                                                | Yes                          | Yes                                  |
| AWS access portal for single-sign on access to your AWS managed applications | Yes                                                                | Yes                          | Yes                                  |
| OAuth 2.0 (OIDC) customer managed applications                               | Yes                                                                | Yes                          | Yes                                  |
| Multi-account permissions                                                    | Yes                                                                | No                           | No                                   |
| AWS access portal for single-sign on access to your AWS accounts             | Yes                                                                | No                           | No                                   |
| SAML 2.0 customer managed applications                                       | Yes                                                                | No                           | No                                   |
| Delegated administrator can manage instance                                  | Yes                                                                | No                           | No                                   |

For more information about AWS managed applications and IAM Identity Center, see [AWS managed applications
that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md").

###### Topics

- [Organization instances of IAM Identity Center](organization-instances-identity-center.md "organization-instances-identity-center.md")
- [Account instances of IAM Identity Center](account-instances-identity-center.md "account-instances-identity-center.md")
- [Delete your IAM Identity Center instance](delete-config.md "delete-config.md")
