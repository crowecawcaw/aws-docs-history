

# Related AWS services
<a name="accounts-related-services"></a>

Depending on how you sign up for AWS, you either have access to AWS accounts or projects. Projects contain AWS accounts and the settings for sharing with other collaborators. For more information, see [Compare sign-up options](sign-up-for-aws.md). In this section, we explain how AWS accounts that you create using Sign up for AWS (advanced) work seamlessly with the following services:
+ **IAM**

  Your AWS account is closely integrated with AWS Identity and Access Management (IAM). You can use IAM with your account to ensure that other people who work in your account have as much access as they need to get their jobs done. You also use IAM to control access to all of your AWS resources, not only account specific information. It's important that you familiarize yourself with the major concepts and best practices of IAM before you get too far along with setting up the structure of your AWS account. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
+ **AWS Organizations**

  If your company is large or likely to grow, you might want to set up multiple AWS accounts that reflect your company's specific structure. AWS Organizations provides the underlying infrastructure and capabilities for you to build and manage your multi-account environments. You can combine your existing accounts into an organization that enables you to manage the accounts centrally. You can create accounts that automatically are a part of your organization, and you can invite other accounts to join your organization. You also can attach policies that affect some or all of your accounts. For more information, see [When to use AWS Organizations](using-orgs.md).

  The following account-related API actions are part of the AWS Organizations API, not the AWS Account Management API. We include them here because customers commonly look for these operations in the Account Management documentation, but they are defined in the AWS Organizations namespace.
  + [CreateAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html)
  + [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html)
  + [DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html)
+ **AWS Control Tower**

  AWS Control Tower provides a simplified way to set up and govern a secure, multi-account AWS environment. AWS Control Tower automates the creation of your multi-account environment using AWS Organizations, instantiating a set of initial accounts and with some default guardrails and configurations for the environment. You can use AWS Control Tower to provision new AWS accounts in a few steps while ensuring that the accounts conform to your organizational policies. For more information, see [When to use AWS Control Tower](when-to-use-control-tower.md).