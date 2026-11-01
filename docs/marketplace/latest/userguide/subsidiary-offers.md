

# Creating private offers as a subsidiary account
<a name="subsidiary-offers"></a>

Many AWS partners operate through more than one legal entity. For example, you might have one entity per country, one per region, or one that you inherited through an acquisition.

In eligible jurisdictions, you can register each entity as a separate AWS Marketplace seller account. Each account is then the seller of record in its own market. It holds the customer contract, invoices in local currency, and pays the AWS Marketplace listing and transaction fees on its own sales. It's also paid into its own bank account. Registering local entities separately keeps AWS Marketplace consistent with your regional structure and simplifies local financial reconciliation.

With subsidiary authorization, you support that structure without managing your product portfolio in each seller account. You maintain a product in one AWS Marketplace seller account and authorize your other seller accounts to sell it. The account that owns the product is the *primary account*. An account authorized to sell it is a *subsidiary account*. Each subsidiary account transacts on its own terms. The primary account can see transactions across all of its connected accounts in one place.

**Note**  
A subsidiary authorization is different from a resale authorization. With a *resale authorization*, a third-party AWS Marketplace Channel Partner resells your product and marks up a wholesale cost that you set. With a *subsidiary authorization*, another of your own seller accounts sells your product and sets its own prices. For more information about Channel Partner resale, see [Creating private offers as an AWS Marketplace Channel Partner](channel-partner-offers.md).

## How subsidiary authorization works
<a name="how-subsidiary-authorization-works"></a>

Subsidiary authorization takes two steps. Nothing is shared between your accounts by default.

**Step 1: Connect the accounts.** From AWS Partner Central, the primary account sends a subsidiary connection request to another of your seller accounts. The connection becomes effective after an administrator in that account signs in and accepts the request. Acceptance establishes the connection. It also records that account's consent to share its partner attributed revenue and its AWS Marketplace insights reports with the primary account. For more information about connecting accounts, see [Managing subsidiary account connections](https://docs.aws.amazon.com/partner-central/latest/getting-started/manage-subsidiary.html) in the *AWS Partner Central Getting Started Guide*.

**Step 2: Authorize the subsidiary account to sell a product.** The primary account creates a separate authorization for each product that a connected subsidiary account can sell. The subsidiary account can create private offers for a product only after it receives an authorization for it. Each authorization names the following:
+ The product
+ The subsidiary account that can sell it
+ The countries in which that account can sell it
+ The offer types that account can create (in this release, private offers only)

The subsidiary account then creates private offers for that product. The subsidiary account doesn't need to accept the authorization. After the primary account submits it, the authorization becomes active within a few minutes.

The following diagram shows this relationship between a primary account, a subsidiary account, and a buyer.

 ![Seven-step flow from a primary account authorization to a subsidiary private offer, buyer payment, and disbursement.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/subsidiary-authorization-flow.png) 

The diagram shows the following flow:

1. The primary account authorizes the subsidiary account to sell a listing, and sets the countries, offer type, and dimensions it can use to create offers.

1. The subsidiary account creates a direct private offer for the buyer.

1. The buyer accepts the offer.

1. AWS invoices the buyer.

1. The buyer pays the invoice.

1. AWS disburses to the subsidiary account, in the currency and to the local bank account configured on that account.

1. The primary account sees consolidated offer, agreement, and renewal data for all connected subsidiary accounts in AWS Marketplace insights reports. This step is reporting visibility only and moves no funds.

## Primary and subsidiary account responsibilities
<a name="subsidiary-account-responsibilities"></a>

Product ownership stays with the primary account, and money stays in each account. The following table shows what each account is responsible for.


| Area | Primary account | Subsidiary account | 
| --- | --- | --- | 
| Owns and maintains the product listing | Yes. Creates the listing, its content, and its pricing dimensions. | No. Can sell the product but can't change listing content. | 
| Creates the authorization | Yes, to accounts it is already connected to. | No. Can't grant itself an authorization or pass one on to another account. | 
| Seller of record | On its own offers only. | Yes, on every offer it creates. Sets its own pricing and payment terms, and owns the customer agreement. | 
| Currency | Its own. | Its own. Offer currencies come from the currencies configured in the subsidiary account's AWS Marketplace payment setup. | 
| Tax interview and Know Your Customer (KYC) verification | For its own account only. | For its own account. A primary account can't complete these on a subsidiary account's behalf. | 
| AWS Marketplace listing and transaction fees | On its own transactions only. | Yes, on the transactions it makes. Fees stay with each account and aren't pooled, netted, or rebilled. | 
| Disbursement | For its own transactions only. | Yes, to its own bank account in its own currency. Funds go directly to the subsidiary account. | 

## Prerequisites for authorizing a subsidiary account
<a name="subsidiary-authorization-prerequisites"></a>

Before a primary account can authorize a subsidiary account to sell one of its products, all of the following must be true:
+ Both accounts are registered as paid sellers in AWS Marketplace.
+ The subsidiary account has completed its own tax interview and KYC verification. It also has its own AWS Marketplace payment setup, including a bank account and at least one disbursement currency. The subsidiary account needs a completed payment setup to create an offer.
+ The two accounts have an accepted subsidiary connection in AWS Partner Central, as described in [How subsidiary authorization works](#how-subsidiary-authorization-works).
+ Both accounts have the `AWSMarketplaceSubsidiaryAuthorizationServiceRole` service role. AWS uses this role to share the authorization with the subsidiary account. For more information, see [Subsidiary authorization service role](using-roles-for-subsidiary-authorization.md).

**Sellers in India**  
Sellers in India have specific registration requirements and can only set INR for disbursement. For more information, see [Getting started as a seller in India](getting-started-seller-india.md).

### Required permissions
<a name="subsidiary-offer-permissions"></a>

The AWS Identity and Access Management (IAM) identity you sign in with must have permissions for the action you're taking. These are identity-based policies for the users in each account. They're separate from the `AWSMarketplaceSubsidiaryAuthorizationServiceRole` service role described earlier. You need both.

**Primary account.** To create a subsidiary authorization, use either the `AWSMarketplaceSellerFullAccess` or the `AWSMarketplaceSellerProductsFullAccess` managed policy.

**Subsidiary account.** To create a private offer from a subsidiary authorization, the policy you need depends on where you start the offer:
+ From the **Private offers** page, use the `AWSMarketplaceSellerOfferManagement` managed policy.
+ From the subsidiary connection details page, by selecting a subsidiary authorization, use either the `AWSMarketplaceSellerFullAccess` or the `AWSMarketplaceSellerProductsFullAccess` managed policy.

## Authorizing a subsidiary account to sell your product
<a name="authorize-a-subsidiary"></a>

Authorize a connected subsidiary account so that it can create private offers for a product that your primary account owns. Before you begin, make sure that both accounts meet the [Prerequisites for authorizing a subsidiary account](#subsidiary-authorization-prerequisites). Do the following in the primary account.

**To authorize a subsidiary account to sell your product**

1. Sign in to the primary account and open the [Subsidiary account connections](https://console.aws.amazon.com/partnercentral/account-connections/subsidiary-connections) page in AWS Partner Central.

1. Choose the connected subsidiary account you want to authorize. On its connection details page, in the **Subsidiary account authorizations** section, choose **Add authorization**.

1. For **Product**, select the product type and the product you want to authorize. The list shows only products that the primary account owns.

1. In the **Authorization details** section, enter a name. The subsidiary account selects this authorization by name when it creates an offer. Choose a name its team will recognize, such as the product and regions the authorization covers. (Optional) Enter a description.

1. For **Pricing dimensions**, select the dimensions the subsidiary account can price in its offers. For **Countries**, select the countries where the subsidiary account can sell the product. The subsidiary account can price only the selected dimensions and sell only to buyers located in the selected countries.

1. (Optional) To authorize this subsidiary account for another product, choose **Add additional authorization**, and then repeat steps 3 through 5.

1. Choose **Submit**.

The authorization becomes active within a few minutes. After it's active, the subsidiary account can create private offers from it. For instructions, see [Creating a private offer as a subsidiary account](#create-subsidiary-private-offer).

**Note**  
Each authorization covers one product. Each authorization for the same product and subsidiary account must cover different countries and pricing dimensions. Authorize as many of your products to an account as you want, and submit up to 10 products at a time.

For instructions on doing this programmatically, see [Work with subsidiary authorizations](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-subsidiary-authorizations.html) in the *AWS Marketplace Seller Guide API Reference*.

## Creating a private offer as a subsidiary account
<a name="create-subsidiary-private-offer"></a>

Create a private offer for a product that your primary account owns, so that you can sell it to buyers in your market as the seller of record. Do the following in the subsidiary account.

**To create a private offer as a subsidiary account**

1. Sign in to the subsidiary account in [AWS Partner Central](https://console.aws.amazon.com/partnercentral/home). On the navigation pane, under **Sell**, choose **Private offers**, and then choose **Create private offer**.

1. For **Offer type**, choose **Subsidiary private offer**. Use this offer type for products that your primary account owns and has authorized you to sell.

1. For **Product**, select the product you want to create the offer for. The list shows only the products your primary account has authorized you to sell.

1. Select the authorization you want to use for this offer, and then choose **Continue offer details**.

1. In **Configure offer pricing and duration**, set your prices. The page shows only the pricing dimensions that your authorization covers.

1. In **Add buyer**, select the buyer. Under **Buyer region availability**, the page shows only the countries that your authorization covers.

1. Complete the remaining offer terms, review the offer, and then choose **Publish offer**.

Your account is the seller of record. When the buyer accepts, the agreement is between the buyer and your account. AWS Marketplace charges your account the listing and transaction fees. It disburses the proceeds according to your own disbursement preferences.

**Note**  
Your primary account might revoke the authorization, or remove a country or pricing dimension you used, after you start an offer. If this happens, publishing fails and the offer stays in draft. Contact your primary account's AWS Marketplace administrator to restore the authorization.

For instructions on doing this programmatically, see [Create an offer using a subsidiary authorization](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-private-offers.html#create-offer-using-subsidiary-authorization) in the *AWS Marketplace Seller Guide API Reference*.

### Renewing a subsidiary offer
<a name="renew-subsidiary-offer"></a>

To offer refreshed terms to a buyer who has already accepted one of your offers, create a replacement offer against the buyer's existing agreement. The original offer stays unchanged. Both offers exist at the same time, and the buyer chooses which to act on. Your prices carry over from the original offer, and you can change them.

For instructions on using the API, see [Create a replacement offer using a subsidiary authorization](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-private-offers.html#create-replacement-offer-using-subsidiary-authorization) in the *AWS Marketplace Seller Guide API Reference*.

## Updating an authorization
<a name="update-subsidiary-authorization"></a>

A primary account can change the following for an active authorization at any time:
+ Name
+ Description
+ Authorized countries
+ Covered pricing dimensions

Changes apply to the offers the subsidiary account creates from then on. They don't change offers it has already published or agreements already in place with buyers.

When you extend an authorization, for example by adding a country, the change takes effect within a few minutes. If you narrow an authorization, publishing can fail for a draft offer that the subsidiary account already started. Before you narrow an authorization, consider telling the subsidiary account's team.

Product changes don't reach authorized subsidiary accounts automatically. When you change a product you've already authorized, update the existing authorization to cover the change. You can also add another authorization for the product that covers different countries and pricing dimensions.

Only the primary account that issued an authorization can update it. Do the following in that account.

**To update an authorization**

1. Sign in to the primary account and open the [Subsidiary account connections](https://console.aws.amazon.com/partnercentral/account-connections/subsidiary-connections) page in AWS Partner Central.

1. Choose the active connection whose authorization you want to update.

1. On the connection details page, in the **Subsidiary account authorizations** section, select the authorization you want to update. Then choose **Update authorization**.

1. Make your changes, and then choose **Save changes**.

## Revoking an authorization
<a name="revoke-subsidiary-authorization-ug"></a>

A primary account can revoke an authorization at any time. After you revoke an authorization, the subsidiary account can't create new private offers for that product.

**Warning**  
Revoking an authorization is permanent. To authorize the product again, you must create a new authorization.

**Important**  
Revoking an authorization doesn't cancel offers the subsidiary account has already published. It also doesn't end or change agreements already in place with buyers.  
The buyer can still accept an offer published before you revoked the authorization. Existing agreements continue according to their agreed terms. This includes their renewals and their disbursements to the subsidiary account.

AWS Marketplace notifies both the subsidiary account and the primary account when you revoke an authorization. If you end the underlying subsidiary connection in AWS Partner Central, the authorizations between those two accounts also end.

Only the primary account that issued an authorization can revoke it. Do the following in that account.

**To revoke an authorization**

1. Sign in to the primary account and open the [Subsidiary account connections](https://console.aws.amazon.com/partnercentral/account-connections/subsidiary-connections) page in AWS Partner Central.

1. Choose the active connection whose authorizations you want to revoke.

1. On the connection details page, in the **Subsidiary account authorizations** section, select the authorizations you want to revoke.
**Warning**  
Revoking is permanent and can't be undone. To authorize the product again, you must create a new authorization.

1. Choose **Revoke**.

1. In the confirmation dialog box, confirm the revocation.

## Consolidated insights for subsidiary accounts
<a name="subsidiary-consolidated-reporting"></a>

After a subsidiary connection is accepted, the primary account can see partner attributed revenue and AWS Marketplace insights reports for all of its connected subsidiary accounts in one place. These reports are in the **Marketplace insights** section of AWS Partner Central, so you don't need to sign in to each account separately.

## Considerations
<a name="subsidiary-offer-limitations-ug"></a>

Consider the following before you use subsidiary authorization.


| Area | Behavior | 
| --- | --- | 
| Offer types | A subsidiary account can create direct private offers from an authorized product. Public offers aren't supported. | 
| Resale authorizations | A subsidiary account can create resale authorizations for products that its own account owns. It can't create a resale authorization for a product that its primary account authorized to it. For more information, see [Creating a selling authorization for an AWS Marketplace Channel Partner as an ISV](channel-partner-isv-info.md). | 
| Product changes | An authorization covers one product. To authorize a different product, create another authorization for it. If you change a product you've already authorized, such as by adding a pricing dimension, update the existing authorization. The subsidiary account can then sell the latest version. | 
| Overlapping authorizations | Each authorization for the same product and subsidiary account must cover different countries and pricing dimensions. | 
| Geographic granularity | You set authorized countries at the country level. Authorizations don't support states or regions within a country. | 
| Pricing | A subsidiary authorization carries no pricing terms. The subsidiary account sets its own prices on the offers it creates. | 
| Fees and disbursement | AWS Marketplace charges listing and transaction fees to the transacting subsidiary account. It disburses proceeds to that account's bank account. | 
| Existing listings and agreements | A subsidiary account might already have its own duplicate listing with live agreements. Those agreements remain on that listing and can't be moved to the primary account's product. | 
| Offer creation | Each account creates its own offers. A primary account can't create an offer in a subsidiary account's name. | 
| Connection requests | Send a subsidiary connection request from an account that has both a partner registration and a seller registration. | 