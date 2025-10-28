# Setting up AWS Elemental MediaConnect

Before you start using AWS Elemental MediaConnect, you must sign up for AWS (if you don’t already have an
AWS account) and create IAM users and roles to allow access to MediaConnect. This
includes creating an IAM role for yourself. If you want to use encryption to protect your
content, you also must store your encryption keys in AWS Secrets Manager, and then give MediaConnect
permission to obtain the keys from your Secrets Manager account.

This section guides you through the steps required to configure users and roles to access
AWS Elemental MediaConnect. For background and additional information about identity and access
management for MediaConnect, see [Identity and access management for
AWS Elemental MediaConnect](security-iam.md "security-iam.md").

###### Topics

- [Create non-admin roles](setting-up-create-nonadmin-roles.md "setting-up-create-nonadmin-roles.md")
- [(Optional) Set up encryption](setting-up-encryption.md "setting-up-encryption.md")
