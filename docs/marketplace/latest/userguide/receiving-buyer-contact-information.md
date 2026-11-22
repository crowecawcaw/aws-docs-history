

# Receiving buyer contact information

When a buyer subscribes to your product in AWS Marketplace, the buyer shares their contact information in the **Deployment contact information** section of the procurement page. You can retrieve this information for the agreement and use it to set up the buyer's account, send deployment guides and setup instructions, provide technical support, and send product updates.

AWS Marketplace shares buyer contact information with you automatically. To retrieve it, call the [GetAgreementContacts](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementContacts.html) API or view it on the agreement details page. If your account uses an AWS managed policy such as `AWSMarketplaceSellerFullAccess`, you already have the required permission. If you use a custom IAM policy, add the `aws-marketplace:GetAgreementContacts` permission before calling the API.

An agreement might not include contact information, because only public SaaS offers require buyers to share it, and buyers can choose not to share it for all other product and offer types. Agreements created before AWS Marketplace launched this feature also don't include it.

## Required permissions
<a name="buyer-contact-information-permissions"></a>

To retrieve buyer contact information through the API or the console, you need the `aws-marketplace:GetAgreementContacts` permission, and your account must be the seller or channel partner on the agreement. Grant this permission only to the roles that handle fulfillment or onboarding.

The following AWS managed policies include this permission: `AWSMarketplaceFullAccess`, `AWSMarketplaceSellerFullAccess`, and `AWSMarketplaceSellerOfferManagement`. For more information, see [AWS managed policies for AWS Marketplace sellers](security-iam-awsmanpol.md).

## What you receive
<a name="buyer-contact-information-fields"></a>

The following table lists the buyer contact information fields that you receive.


| Field | Description | 
| --- | --- | 
| firstName | The buyer's first name. | 
| lastName | The buyer's last name. | 
| emailAddress | The email address that the buyer entered. It might be a team distribution list. | 
| companyName | The buyer's company or organization name. | 
| countryCode | The ISO 3166-1 alpha-2 code for the country or Region where the buyer's company is located, for example US. | 
+ The information reflects what the buyer entered at subscription. It doesn't update if the buyer's details change later.
+ AWS Marketplace doesn't verify this information, including the email address. If your onboarding requires a verified email address, verify it yourself.
+ You can retrieve the information only while the agreement is active.

## Retrieving buyer contact information
<a name="buyer-contact-information-retrieve"></a>

To retrieve buyer contact information, call [GetAgreementContacts](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementContacts.html) with the agreement ID. How you get the agreement ID depends on your product:
+ **SaaS products** – When the buyer is redirected to your registration page, call [ResolveCustomer](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_ResolveCustomer.html) with the registration token. The response includes the agreement ID. Use the contact information to fill in your registration form so that the buyer confirms it instead of entering it again.
+ **All products** – Get the agreement ID from the `Purchase Agreement Created - Proposer` event that AWS Marketplace sends to Amazon EventBridge. The ID is in `detail.agreement.id`. You can also find agreement IDs with `SearchAgreements`.

The following example uses the AWS CLI to retrieve buyer contact information.

```bash
aws marketplace-agreement get-agreement-contacts \
    --agreement-id agmt-1111111111111111111111111
```

The following is an example JSON response.

```json
{
    "acceptorContact": {
        "firstName": "Richard",
        "lastName": "Roe",
        "emailAddress": "richard.roe@example.com",
        "companyName": "Example Organization",
        "countryCode": "US"
    }
}
```

If the buyer didn't share their contact information, or the agreement was created before this feature was available, `GetAgreementContacts` returns `null`. This is an expected result. Continue your fulfillment flow without contact information.

**To view buyer contact information in the console**

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home) and open the **Agreements** page.

1. Choose the agreement ID.

1. Review the **Deployment contact information** section. If the buyer didn't share their contact information, the section doesn't appear.

## Handling buyer contact information
<a name="buyer-contact-information-handling"></a>
+ Treat buyer contact information as personal data. Store it securely and in line with applicable data protection laws.
+ Don't write raw contact information to shared logs.
+ Because the information doesn't update, give buyers a way to update their contact details with you after onboarding.
+ Follow the security policies for your delivery method. For more information, see [SaaS security policies](saas-guidelines.md#saas-security-policies), [AMI security policies](product-and-ami-policies.md#ami-security), and [container security policies](container-product-policies.md#container-security-requirements).