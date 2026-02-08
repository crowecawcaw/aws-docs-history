# Considerations for choosing an

AWS Region

You can enable IAM Identity Center in a single, supported AWS Region of your choice and it is available to
users globally. This global availability makes it easier for you to configure user access to
multiple AWS accounts and applications. Following are key considerations for choosing an
AWS Region.

- Geographical location of your users – When you select
  a Region that is geographically closest to the majority of your end users, they'll have lower
  latency of access to the AWS access portal and AWS managed applications, such as Amazon SageMaker AI.
- Opt-in Regions (Regions that are disabled by default)
  – An opt-in Region is an AWS Region that is disabled by default. To use an opt-in
  Region, you must enable it. For more information, see [Managing IAM Identity Center in an opt-in Region](regions.md#manually-enabled-regions "regions.md#manually-enabled-regions").
- Replicating IAM Identity Center to additional Regions – If you
  plan to replicate IAM Identity Center to additional AWS Regions, you must choose a Region enabled by
  default. For more information, see [Using IAM Identity Center across multiple
  AWS Regions](multi-region-iam-identity-center.md "multi-region-iam-identity-center.md").
- Choosing deployment Regions for AWS managed applications – AWS
  managed applications can operate only in the AWS Regions in which they are available. Many
  AWS managed applications can also operate only in a Region where IAM Identity Center is enabled or
  replicated to (primary or additional Region). To confirm if your IAM Identity Center instance supports
  replication to additional Regions, see [Using IAM Identity Center across multiple
  AWS Regions](multi-region-iam-identity-center.md "multi-region-iam-identity-center.md").
  If replication is not an option, consider enabling IAM Identity Center in the Region where you plan to
  use AWS managed applications.
- Digital sovereignty – Digital sovereignty regulations
  or company policies may mandate the use of a particular AWS Region. Consult with your
  company’s legal department.
- Identity source – If you’re using [AWS Managed Microsoft AD](connectawsad.md "connectawsad.md") or your self-managed directory in [Active Directory (AD)](connectonpremad.md "connectonpremad.md") as the identity source, its home Region
  must match the AWS Region in which you enabled IAM Identity Center.
- Cross-Region emails with Amazon Simple Email Service – In some Regions,
  IAM Identity Center may call [Amazon Simple Email Service
  (Amazon SES)](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md") in a different Region to send email. In these cross-Region calls, IAM Identity Center sends
  certain user attributes to the other Region. For more information, see [Cross-Region emails with Amazon SES](regions.md#cross-region-calls "regions.md#cross-region-calls").
- AWS Control Tower – If you’re enabling an organization instance of
  IAM Identity Center from AWS Control Tower, the instance will be created in the same Region as the AWS Control Tower landing zone.

###### Topics

- [IAM Identity Center Region data storage and operations](regions.md "regions.md")
- [Switching AWS Regions](switching-regions.md "switching-regions.md")
- [Disabling an AWS Region where IAM Identity Center is
  enabled](disabling-region-with-identity-center.md "disabling-region-with-identity-center.md")
