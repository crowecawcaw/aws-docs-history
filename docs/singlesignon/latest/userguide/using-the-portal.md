

# Setting up and using the AWS access portal
<a name="using-the-portal"></a>

The AWS access portal connects your workforce to AWS accounts and cloud applications through IAM Identity Center. Administrators configure the portal and manage user access, while end users sign in once to seamlessly access all their authorized resources.

The AWS access portal provides single sign-on access to:
+ AWS accounts in your organization.
+ AWS managed applications such as Amazon Quick and Kiro.
+ Cloud applications like Office 365, Concur, Salesforce, and others.

When users sign in to the portal, they find the AWS accounts and applications they're authorized to access without additional sign-in.

The AWS access portal also provides access to the AWS account access application — where users can view and access IAM roles assigned to them through [account access manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/account-access-manager.html).

## Getting started with the AWS access portal
<a name="getting-started-access-portal"></a>

**For administrators:**

You need administrative access to your [organization instance](organization-instances-identity-center.md) or [account instance](account-instances-identity-center.md) of IAM Identity Center to configure the AWS access portal and manage user access.

1. Optionally customize the AWS access portal URL.

1. Assign user access to AWS accounts and applications. Assigned AWS resources display in the portal.

**For end users:**

Your administrator must have completed the AWS access portal setup and provided you with your portal URL and sign-in credentials.

1. Get your portal URL from your administrator (typically `https://your-company.awsapps.com/start`).

1. Sign in using the credentials provided by your administrator.

1. Access your resources in your portal.