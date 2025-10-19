# IAM Identity Center prerequisites and
 considerations

You can use IAM Identity Center for access to AWS managed applications only, AWS accounts only, or
 both. If you are using IAM federation to manage access to AWS accounts, you can
 continue to do so while using IAM Identity Center for application access.

Before enabling IAM Identity Center, consider the following:


* AWS Region


You can enable IAM Identity Center in a single, [supported](regions.md "regions.md") Region
 for each instance of IAM Identity Center. If you want to use IAM Identity Center for single-sign on access to
 AWS accounts, the Region must be accessible by all of the users in your
 organization. If you plan to use IAM Identity Center for application access, be aware that some
 AWS managed applications, such as Amazon SageMaker AI, can operate only in the Regions they
 support. Make sure that you enable IAM Identity Center in a Region supported by the AWS managed
 application(s) you want to use with it. Additionally, many AWS managed
 applications can operate only in the same Region where you enabled IAM Identity Center. For these
 reasons, make sure to choose the appropriate Region when enabling IAM Identity Center. For more
 information, see [Considerations for choosing an
 AWS Region](identity-center-region-considerations.md "identity-center-region-considerations.md").
* Application access only


You can use IAM Identity Center only for user access to applications such as Amazon Q Developer, using
 your existing identity provider. For more information, see [Using IAM Identity Center for user access to applications
 only](identity-center-for-apps-only.md "identity-center-for-apps-only.md").


###### Note

Access to application resources is managed independently by the application
 owner.
* Quota for IAM roles


IAM Identity Center creates IAM roles to give users permissions to account resources. For more
 information, see [IAM roles created by IAM Identity Center](identity-center-and-iam-roles.md "identity-center-and-iam-roles.md").
* IAM Identity Center and AWS Organizations


AWS Organizations is recommended, but not required, for use with IAM Identity Center. If you haven't set up
 an organization, you do not have to. If you've already set up AWS Organizations and are going to
 add IAM Identity Center to your organization, make sure that all AWS Organizations features are enabled. For
 more information, see [IAM Identity Center and AWS Organizations](identity-center-and-orgs.md "identity-center-and-orgs.md").
