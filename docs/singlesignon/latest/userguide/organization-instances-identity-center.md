# Organization instances of IAM Identity Center

When you enable IAM Identity Center in conjunction with AWS Organizations, you are creating an organization
instance of IAM Identity Center. Your organization instance must be enabled in your management account and
you can centrally manage the access of users and groups with a single organization instance.
You can have only one organization instance for each management account in AWS Organizations.

If you enabled IAM Identity Center before November 15, 2023, you have an organization instance of IAM Identity Center.

To enable an organization instance of IAM Identity Center, see [To enable an instance of IAM Identity Center](enable-identity-center.md#to-enable-identity-center-instance "enable-identity-center.md#to-enable-identity-center-instance").

## When to use an organization

instance

An organization instance is the primary method of enabling IAM Identity Center and usually, an
organization instance is recommended. Organization instances offer the following
benefits:

- Support for all features of IAM Identity Center – Including
  managing permissions for multiple AWS accounts in your organization and assigning
  access to customer managed applications.
- Reduction of the number of management points –
  An organization instance has a single management point, the management account. We
  recommend that you enable an organization instance, rather than an account instance, to
  reduce the number of management points.
- Central control of the creation of account instances
  – You can control whether account instances can be created by member accounts in
  your organization as long as you haven't deployed an instance of IAM Identity Center to your
  organization in an opt-in Region (AWS Region that is disabled by default).

For instructions on enabling an organization instance of IAM Identity Center, see [To enable an instance of IAM Identity Center](enable-identity-center.md#to-enable-identity-center-instance "enable-identity-center.md#to-enable-identity-center-instance").
