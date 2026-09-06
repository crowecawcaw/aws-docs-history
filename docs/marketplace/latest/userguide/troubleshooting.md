

# Troubleshooting
<a name="troubleshooting"></a>

The topics in the following section provide solutions to common errors you may encounter when using AWS Marketplace. 

**Topics**
+ [Common error messages](#common-error-messages)
+ [Common seller registration error messages](#common-seller-registration-errors)

## Common error messages
<a name="common-error-messages"></a>

The following sections explain the causes of common error messages, and the resolutions and preventative measures for them. Expand the sections as needed.

### Agreement creation failed due to seller compliance issues or an unsupported offer currency in your region. Contact the seller to ensure the correct offer is extended to you.
<a name="ts-self-purchase"></a>

#### Common cause
<a name="ts-self-purchase-cause"></a>

Sellers see this error message when they try to buy their own products.

#### Resolution
<a name="ts-self-purchase-resolution"></a>

By design, AWS Marketplace prevents sellers from buying their own products.

## Common seller registration error messages
<a name="common-seller-registration-errors"></a>

The following table describes common seller registration error messages and their solutions.


| Error message | Solution | 
| --- | --- | 
| Your compliance requirements are not complete | For all Japanese sellers, we're required to collect additional information for regulatory purposes before they can publish paid products. If you're a Japan-based seller and interested in listing on AWS Marketplace, contact the Japanese seller onboarding team at aws-jp-marketplace@amazon.co.jp for additional details. For more information, see [JP SOR FAQ](https://aws.amazon.com/jp/legal/awsjp/). | 
| AWS Marketplace can't process your request right now because of an internal issue. Try again later. If the problem persists, contact us for assistance. | Clear your browser's cache and try again. If the issue persists, contact the [AWS Marketplace Seller Operations team](https://aws.amazon.com/marketplace/management/contact-us/). | 
| Before you can update your product to public, you need to add a public profile to your seller account. | Add a public profile to your seller account before updating the product to public. In [AWS Partner Central](https://aws.amazon.com/marketplace/management/seller-settings/account), go to **Settings**, then **Public profile**. | 
| Update your payment settings to be compatible with the CurrencyCode. | Update the currency code in your payment settings. Make sure to add USD, because consumption pricing only supports that code. For more information, see [Currency restrictions and available currencies](managing-disbursements.md#currency-restrictions-and-options).  | 
| VAT/GST information is required to remain a paid seller. | You have two options:1.  Update the tax settings in the main account. Review the [tax inheritance documentation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-account-payment.html#manage-account-tax-linked-accounts) to understand the effect this will have on all linked accounts. <br />2.  Remove this account from the organization and have it as a standalone account. This means that you'll need to manually add the VAT/GST settings in the [tax settings](https://console.aws.amazon.com/billing/home?#/tax-settings) page in Billing.  | 
| Tax interview location does not match the business location | To check current location settings:1.  Tax interview location:   In AWS Partner Central, go to **Settings**, then **Tax information**.   Choose **Update tax information**, followed by **Retake**.   Once you choose **Update tax profile**, scroll down and check the country you have provided.   <br />2.  Business location:   In [AWS Partner Central](https://aws.amazon.com/marketplace/management/seller-settings/account), check the **Business location** provided in **Account summary** on the **Settings** tab.   <br />If locations don't match:+  Update tax information in [Billing](https://console.aws.amazon.com/billing/home?#/tax): For more information, see [Account location](https://aws.amazon.com/tax-help/location/) <br />+  Update tax interview in [AMMP settings](https://aws.amazon.com/marketplace/management/seller-settings/account): Retake tax interview from **Tax information** <br />Ensure both locations are identical to avoid payment processing issues. | 
| To start using AWS Marketplace, complete AWS Account Registration | Complete your [AWS Account Registration](https://portal.aws.amazon.com/billing/signup/incomplete#/account/).<br />For more information on seller registration, see [Registering as a seller on AWS Marketplace](seller-account-registering.md).  | 
| Your public profile is being reviewed. You cannot add a disbursement method until your public profile is verified. Check again in 2 business days. You can currently publish only free products. | Your public profile is being reviewed. You can't add a disbursement method and complete KYC until your public profile is verified. It will take two to three business days to approve. You can currently publish only free products. Once your profile is approved, you'll receive an email to your root email address.<br />If you still can't add payment information after three business days, contact the [AWS Marketplace Seller Operations team](https://aws.amazon.com/marketplace/management/contact-us/). | 
| Your business location is in a non-supported jurisdiction. You are not eligible to publish paid products. | Your business location is in a non-supported jurisdiction. You aren't eligible to publish paid products. For more information on eligible jurisdictions, see [Eligible jurisdictions for paid products](seller-eligibility.md#eligible-jurisdictions).  | 
| AWS account is not registered as a seller in AWS Marketplace. | You aren't registered as a seller in AWS Marketplace. Complete registration from [AWS Partner Central](https://aws.amazon.com/marketplace/management/seller-settings/register). | 
| Seller must have a public profile to be able to become a paid seller. | Your seller public profile must be completed and approved. Complete it and check your account status in [AWS Partner Central](https://aws.amazon.com/marketplace/management/seller-settings). | 