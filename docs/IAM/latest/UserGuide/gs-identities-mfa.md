# Use multi-factor authentication with your

identities

Using multi-factor authentication (MFA) with your identities is another IAM best
practice. MFA is an additional security layer that requires users to provide additional
authentication factors after providing their username and password to verify their identity.
It significantly enhances security by making it much harder for attackers to gain
unauthorized access, even if a user's password is compromised. MFA is widely adopted as a
best practice for securing access to online accounts, cloud services, and other sensitive
resources. AWS supports MFA for root user, IAM users, users in IAM Identity Center, Builder ID, and federated
users. For additional security, you can create policies that requires MFA be configured
before allowing a user to access resources or take specific actions and attach these
policies to your IAM roles. IAM Identity Center comes preconfigured with MFA turned on by default so
that all users in IAM Identity Center must sign in with MFA in addition to their user name and
password.

###### Note

All AWS account types (standalone, management, and members accounts) require MFA to
be configured for their root user. Users must register MFA within 35 days of their first
sign-in attempt to access the AWS Management Console if MFA is not already enabled.

For more information, see [Configure MFA in
IAM Identity Center](../../../singlesignon/latest/userguide/mfa-getting-started.md "../../../singlesignon/latest/userguide/mfa-getting-started.md") and [AWS Multi-factor authentication in IAM](id_credentials_mfa.md "id_credentials_mfa.md").
