# Registration FAQs

## Our organization has multiple AWS account IDs. How do I know which AWS account ID to use?

Use an AWS account that can serve as the primary account for managing AWS-related partnership activities. All AWS Partner Central users will be provisioned access to the AWS account. AWS recommends not using a Management/Payer account but instead setting up a Member account within your AWS Organizations structure. Contact your organization's IAM Administrator if unsure of which AWS account to use, or if a new AWS account must be created.

## How do I know if my company has a AWS Partner Central account?

During the registration process, your registration business validation will fail if a company with the same legal business name and details exists in our database. Contact [Partner Central Support](https://www.apn-portal.com/knowledgebase/?cu=1&fs=ContactUs&l=en_US "https://www.apn-portal.com/knowledgebase/?cu=1&fs=ContactUs&l=en_US") if you need to merge or consolidate APN accounts.

## How do I know if I am a root user?

You are a root user if you created the AWS account and sign in using the email address and password used to create the account, rather than IAM credentials. AWS recommends not logging in as a root user. More information can be found [here](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md").

## Can the alliance lead contact information be updated after registering?

Yes, the alliance lead contact information can be updated at any time. For more information, see [Partner Central settings](https://us-east-1.console.aws.amazon.com/partnercentral/settings "https://us-east-1.console.aws.amazon.com/partnercentral/settings").

## Who should complete the identity verification process?

An individual authorized to register a AWS Partner Central account can complete this.

## What are you doing with the identity verification data?

The data is used to verify identity, establish partner credentials, and maintain partner program compliance.

## What happens if I register the AWS Partner Central Account and then change roles or leave my company? What happens to my personal data?

Your organization's account administrator can transfer account management to another person. Personal data acquired in registration can be updated or removed upon request through [AWS Partner Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support").

## Are all international IDs valid?

AWS accepts most government-issued IDs, but some restrictions may apply based on country-specific regulations.

## How do I cancel?

Contact [Partner Central Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support") to deactivate an existing account.

## Why does my account summary on the dashboard of AWS Partner Central show "Not Registered" even though I've already registered with the APN?

If you have an AWS Marketplace account and see a "Not Registered" message in AWS Partner Central in the Console, this means you haven't completed your migration from the legacy Partner Central experience.

###### Important

Do not create a new profile or register again. Creating a new registration will replace all of your historical partner data.

**What should I do?** Work with your IT administrator to schedule your migration from legacy Partner Central to the new AWS Partner Central in the Console. This will preserve all of your existing partner history and data.

## I cannot start the identity verification process. It shows "Access denied. You do not have permission to AWS Partner Central."

Contact your IAM administrator to provision you the permissions to access AWS Partner Central. You will need [AWSPartnerCentralFullAccess](../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md") and [AWSMarketplaceSellerFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.md"). Work with your IAM administrator and review the registration prerequisites.

## I cannot pass identity verification. It shows "Failed to verify your Identity. Refresh to get a new code." How do I fix it?

Ensure you use a government ID that shows your face. If you use a government ID without a photo, the system cannot match it with your selfie. Also ensure your photo ID has a recent picture.

## Why do I need to complete identity verification?

To maintain the security and integrity of the AWS Partner Network and AWS customers.

## Why am I seeing the error "Partner Registration requires a paid AWS account in good standing. Please ensure your account meets these requirements to continue"?

To register as an AWS Partner, your AWS account must be on a paid plan rather than the AWS Free Tier, and your account must be in good standing with AWS. Upgrading to a paid plan does not incur additional costs beyond your actual AWS usage.

If you are currently on the AWS Free Tier, log into the AWS Management Console and [upgrade your account to a paid plan](https://console.aws.amazon.com/billing/home?#/freetier/upgrade "https://console.aws.amazon.com/billing/home?#/freetier/upgrade"). If your account is already on a paid plan and the error persists, sign in to the AWS Management Console and contact APN support through [this external link](https://www.apn-portal.com/knowledgebase/?cu=1&fs=ContactUs&l=en_US "https://www.apn-portal.com/knowledgebase/?cu=1&fs=ContactUs&l=en_US") and specify the issue.

## When I enter the Alliance Lead email address in the registration form, I see "domain in use" error. How do I resolve this?

This error means your company already has a AWS Partner Central account. Your company hasn't yet migrated that account to the new Partner Central in the AWS Management Console. You don't need to create a new account.

To resolve this error, return to [legacy Partner Central](https://partnercentral.awspartner.com/partnercentral2/s/login "https://partnercentral.awspartner.com/partnercentral2/s/login"), sign in as an existing AWS Partner, and complete the migration.
