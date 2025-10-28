# IAM Identity Center and AWS Organizations

AWS Organizations is recommended, but not required, for use with IAM Identity Center. If you haven't set up an
organization, you do not have to. When you enable IAM Identity Center, you will choose whether to enable
the service with AWS Organizations. When you set up an organization, the AWS account that sets up
the organization becomes the management account of the organization. The root user of the
AWS account is now the owner of the organizational management account. Any additional
AWS accounts you invite to your organization are member accounts. The management account
creates the organizations resources, organizational units, and policies that manage the
member accounts. Permissions are delegated to member accounts by the management account.

###### Note

We recommend that you enable IAM Identity Center with AWS Organizations, which creates an organization
instance of IAM Identity Center. An organization instance is our recommended best practice because it
supports all features of IAM Identity Center and provides central management capabilities. For more
information, see [Organization instances of IAM Identity Center](organization-instances-identity-center.md "organization-instances-identity-center.md").

If you've already set up AWS Organizations and are going to add IAM Identity Center to your organization, make
sure that all AWS Organizations features are enabled. When you create an organization, enabling all
features is the default. For more information, see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the
_AWS Organizations User Guide_.

To enable an organization instance of IAM Identity Center, you must sign in to the AWS Management Console by signing
in to your AWS Organizations management account as a user that has administrative credentials or as
the root user (not recommended unless no other administrative users exist). For more
information, see [Creating and managing an AWS Organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the
_AWS Organizations User Guide_.

When signed in with administrative credentials from an AWS Organizations member account, you can
enable an account instance of IAM Identity Center. Account instances have limited capabilities and are
bound to a single AWS account.
