

# Sharing your contact information at subscription

When you subscribe to a product in AWS Marketplace, you share your contact information with the seller in the **Deployment contact information** section of the procurement page. The seller can use it to send deployment guides and setup instructions, provide technical support, and send product updates. For SaaS products, the seller can also use it to set up your account.

AWS Marketplace fills in this section where it can, so that you review your information instead of entering it for each subscription. You can edit any field before you subscribe.

## What information is shared
<a name="buyer-contact-information-shared"></a>

AWS Marketplace shares the following fields with the seller:
+ **First name** and **Last name** – Your name.
+ **Email address** – The email address that the seller uses to contact you. You can enter a team distribution list instead of a personal email address.
+ **Company name** – The name of your organization.
+ **Country or Region** – Where your company or organization is located.

**Note**  
The seller receives your information as it appears when you subscribe. You can't change it after you subscribe, and later changes to your AWS Profile or AWS account aren't sent to the seller.

## How your information is filled in
<a name="buyer-contact-information-autofill"></a>

The procurement page can fill in your contact information from multiple sources. The source appears under **Autofilled source**. If more than one source has information, you can choose which one to use.
+ **Your last purchase of this product** – The contact information from the most recent AWS Marketplace purchase of this product on this AWS account.
+ **Your last purchase on this AWS account** – The contact information from the most recent AWS Marketplace purchase on this AWS account. AWS accounts are often shared, so if someone else from your organization made that purchase, their details appear.
+ **AWS Profile** – Your AWS Profile is where you manage your personal information and preferences for AWS. You sign in to it with AWS Builder ID. To use it, choose **Sign in to AWS Profile** on the procurement page. AWS Marketplace uses your name, email address, company, and country or region from your AWS Profile. For more information, see [AWS Profile](https://aws.amazon.com/profile/).
+ **AWS account details** – Your details from IAM Identity Center, or the contact information for your AWS account. Your administrator manages this information.

To autofill your deployment contact information from past purchases, you need the `aws-marketplace:GetAgreementContacts` permission. If no source is available, enter your contact information manually.

Changes that you make on the procurement page apply only to this subscription. They don't update your AWS Profile or your AWS account details.

## Providing your contact information when you subscribe
<a name="buyer-contact-information-provide"></a>

**To provide your contact information when you subscribe**

1. Sign in to [AWS Marketplace](https://aws.amazon.com/marketplace/) and open the page for the product that you want to subscribe to.

1. Choose **View purchase options**. For a free trial, choose **Try for free**.

1. In the **Deployment contact information** section, review or enter your contact information.

1. To fill in your information from your AWS Profile, choose **Sign in to AWS Profile**.

1. Choose **Subscribe**.

Public SaaS offers require you to share your contact information. For all other product and offer types, you can choose not to provide it.

## After you subscribe
<a name="buyer-contact-information-after-subscribe"></a>

The contact information that you shared appears in the **Deployment contact information** section on the subscription confirmation page and on the agreement details page in the AWS Marketplace console.
+ You can't change this information after you subscribe. To update your contact details with the seller, contact the seller.
+ The seller can access this information only while the agreement is active.
+ The seller can't access your AWS Profile.

**Note**  
To view the **Deployment contact information** section on the agreement details page, you need the `aws-marketplace:GetAgreementContacts` permission.

The following AWS managed policies include this permission: `AWSMarketplaceFullAccess`, `AWSMarketplaceManageSubscriptions`, and `AWSMarketplaceRead-only`. For more information, see [AWS managed policies for AWS Marketplace buyers](buyer-security-iam-awsmanpol.md).