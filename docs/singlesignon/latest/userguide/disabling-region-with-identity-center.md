# Disabling an AWS Region where IAM Identity Center is

enabled

If you disable an AWS Region in which IAM Identity Center is installed, IAM Identity Center is also disabled. After
IAM Identity Center is disabled in a Region, users in that Region won’t have single sign-on access to
AWS accounts and applications.

To re-enable IAM Identity Center in [opt-in AWS Regions](regions.md#manually-enabled-regions "regions.md#manually-enabled-regions"),
you must re-enable the Region. Because IAM Identity Center must reprocess all paused events, re-enabling IAM Identity Center
might take some time.

###### Note

IAM Identity Center can manage access only to the AWS accounts that are enabled for use in an
AWS Region. To manage access across all accounts in your organization, enable IAM Identity Center in the
management account in an AWS Region that is automatically activated for use with IAM Identity Center.

For more information about enabling and disabling AWS Regions, see [Managing
AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the _AWS General Reference_.
