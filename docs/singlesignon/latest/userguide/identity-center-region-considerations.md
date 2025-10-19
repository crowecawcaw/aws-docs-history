# Considerations for choosing an
 AWS Region

You can enable IAM Identity Center in a single, supported AWS Region of your choice and it is available to
 users globally. This global availability makes it easier for you to configure user access to
 multiple AWS accounts and applications. Following are key considerations for choosing an
 AWS Region.


* Geographical location of your users – When you select
 a Region that is geographically closest to the majority of your end users, they'll have lower
 latency of access to the AWS access portal and AWS managed applications, such as Amazon SageMaker AI.
* Availability of AWS managed applications – AWS
 managed applications can operate only in the AWS Regions in which they are available. Enable
 IAM Identity Center in a Region supported by the AWS managed application(s) you want to use with it. Many
 AWS managed applications can also operate only in the same Region where you enabled
 IAM Identity Center.
* Digital sovereignty – Digital sovereignty regulations
 or company policies may mandate the use of a particular AWS Region. Consult with your
 company’s legal department.
* Identity source – If you’re using [AWS Managed Microsoft AD](connectawsad.md "connectawsad.md") or your self-managed directory in [Active Directory (AD)](connectonpremad.md "connectonpremad.md") as the identity source, its home Region
 must match the AWS Region in which you enabled IAM Identity Center.
* Opt-in Regions (Regions that are disabled by default)
 – An opt-in Region is an AWS Region that is disabled by default. To use an opt-in
 Region, you must enable it. For more information, see [Managing IAM Identity Center in an opt-in Region](regions.md#manually-enabled-regions "regions.md#manually-enabled-regions").
* Cross-Region emails with Amazon Simple Email Service – In some Regions,
 IAM Identity Center may call [Amazon Simple Email Service
 (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html "https://docs.aws.amazon.com/ses/latest/dg/Welcome.html") in a different Region to send email. In these cross-Region calls, IAM Identity Center sends
 certain user attributes to the other Region. For more information, see [Cross-Region emails with Amazon SES](regions.md#cross-region-calls "regions.md#cross-region-calls").
###### Topics

* [IAM Identity Center Region data storage and operations](regions.md "regions.md")
* [Switching AWS Regions](switching-regions.md "switching-regions.md")
* [Disabling an AWS Region where IAM Identity Center is
 enabled](disabling-region-with-identity-center.md "disabling-region-with-identity-center.md")
