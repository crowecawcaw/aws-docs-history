

# Sellers in India FAQ
<a name="india-seller-faq"></a>

This FAQ addresses common questions for sellers in India who want to list products on AWS Marketplace.

**Topics**
+ [Do I need a separate AWS account to sell in India?](#india-seller-separate-account)
+ [What information do I need to provide for seller registration?](#india-seller-registration-requirements)
+ [How do I get support and assistance as a seller in India?](#india-seller-support)
+ [Can I sell to buyers outside of India as a seller in India?](#india-seller-geographic-restrictions)
+ [What currencies can I use for pricing my products?](#india-seller-pricing-currency)
+ [What product types can I create offers for?](#india-seller-product-types)
+ [How do product pricing currency and seller disbursements work in detail?](#india-seller-pricing-disbursement-details)
+ [What are my GST tax obligations and liability as a seller in India?](#india-seller-tax-obligations)
+ [What banking information do I need to provide?](#india-seller-banking-requirements)
+ [How are AWS Marketplace listing fees handled for sellers in India?](#india-seller-listing-fees)
+ [Do I need to withhold tax on listing fees?](#india-seller-tds-exemption)
+ [When will I receive disbursements?](#india-seller-disbursement-schedule)
+ [How do I migrate from selling outside India to selling in India?](#india-seller-account-migration)
+ [If I'm already registered as a buyer with AWS India, do I still need to create a separate account for selling?](#india-seller-buyer-account-separation)
+ [What are the restrictions for working with channel partners in India?](#india-seller-channel-partner-restrictions)
+ [Can non-India sellers use channel partners in India to sell to buyers in India?](#india-seller-dsor-program)
+ [How do I indicate that my product is available only in India?](#india-seller-product-listing)
+ [Can I create private offers for buyers in India?](#india-seller-private-offers)
+ [What compliance requirements apply to sellers in India?](#india-seller-compliance)

## Do I need a separate AWS account to sell in India?
<a name="india-seller-separate-account"></a>

Yes. You must create a standalone AWS account that is not part of AWS Organizations. This account must be specifically configured for selling in India and cannot be used to sell to buyers outside India. You cannot use an existing buyer account for seller registration.

## What information do I need to provide for seller registration?
<a name="india-seller-registration-requirements"></a>

You must submit: GST identification number (GSTIN), Permanent Account Number (PAN) which auto-populates from GSTIN, seller signature for tax invoices, legal business name and address corresponding to your GSTIN, acknowledgements on withholding tax non-applicability and e-invoicing enablement, authorization for AWS India to raise invoices, and valid India domiciled bank account details.

## How do I get support and assistance as a seller in India?
<a name="india-seller-support"></a>

Use the Contact Us form in AWS Marketplace Management Portal:

1. For banking or disbursement assistance, select Commercial Marketplace, then Seller Account, then Banking.

1. For private offer creation help, select Commercial Marketplace, then Private Offer, then Offer Creation.

1. For India-specific questions about tax obligations, banking, or regulatory requirements, consult with local advisors familiar with regulations in India.

1. Provide detailed information about your specific request for faster resolution.

## Can I sell to buyers outside of India as a seller in India?
<a name="india-seller-geographic-restrictions"></a>

No. Sellers in India can only sell to buyers in India. Buyers outside India can view your listings but cannot purchase them due to geographic restrictions.

## What currencies can I use for pricing my products?
<a name="india-seller-pricing-currency"></a>

All public offers must be priced in USD only. You have the option to publish private offers in INR or USD. However, listing fees are always deducted in INR and all disbursements are always in INR regardless of your pricing currency. There is no currency conversion or exchange rate variability for INR-priced private offers.

## What product types can I create offers for?
<a name="india-seller-product-types"></a>

You can create products and offers for SaaS, AMI, Containers, Professional Services, ML and AWS Data Exchange product types.

## How do product pricing currency and seller disbursements work in detail?
<a name="india-seller-pricing-disbursement-details"></a>

For USD offers: Buyers receive invoices with USD pricing, applicable GST, and foreign exchange conversion rate to INR. The tax invoice uses the same rate as the commercial invoice. Your disbursement in INR equals the converted amount minus withholding tax (0.1%), TCS (0.5%), listing fees, and tax on listing fees. For INR private offers: Buyers receive invoices with the agreed INR amount without foreign exchange variability. Invoices show both INR and USD amounts with the fixed FX rate applied at offer acceptance. Minor rounding differences (maximum ±0.005 USD per line item) may occur due to backend USD processing.

## What are my GST tax obligations and liability as a seller in India?
<a name="india-seller-tax-obligations"></a>

Buyers are charged 18% GST which is paid to you as part of your disbursement, and you are responsible for remitting GST to tax authorities in India according to applicable tax laws. AWS India facilitates issuing GST tax invoices to buyers with you as the seller on record (SoR) and shares the tax invoice with you via email for your records and compliance purposes. You must ensure your GSTIN is enabled for e-invoicing and comply with all applicable tax laws in India including GST registration and filing requirements.

## What banking information do I need to provide?
<a name="india-seller-banking-requirements"></a>

You must provide bank account details in India including account number, Indian Financial System Code (IFSC), and name and address of the account holder. Only bank accounts domiciled in India are accepted for sellers in India. International bank accounts are not accepted. All disbursements are processed in INR to your bank account in India only.

## How are AWS Marketplace listing fees handled for sellers in India?
<a name="india-seller-listing-fees"></a>

The fee structure follows standard AWS Marketplace rates, but all fees are calculated and charged in Indian Rupees (INR) with 18% GST applicable. AWS Marketplace provides a GST tax invoice for listing fees. Both listing fees and GST are deducted from your seller disbursement. You are not required to withhold funds toward listing fees due to TDS exemption under Section 194-O of the Income Tax Act. Refer to the AWS Marketplace Seller Terms for current fee information.

## Do I need to withhold tax on listing fees?
<a name="india-seller-tds-exemption"></a>

No. Per Section 194-O subsection 4 of the Income Tax Act, 1960, once withholding tax is processed at any point in the payment flow, sellers are exempt from Tax Deducted at Source (TDS) withholding on listing fees. AWS deducts TDS from buyer payments and remits to tax authorities. TDS certificates are shared with you for tax claiming purposes.

## When will I receive disbursements?
<a name="india-seller-disbursement-schedule"></a>

Disbursements follow the standard AWS Marketplace schedule but are processed in INR to your bank account in India. The timing and frequency align with standard AWS Marketplace disbursement practices. You can only receive disbursements in Indian Rupees (INR) to your bank account domiciled in India.

## How do I migrate from selling outside India to selling in India?
<a name="india-seller-account-migration"></a>

To migrate from selling outside India to selling in India, create a new standalone account for your India-based entity:

1. Create a new standalone account for your India-based entity.

1. Re-list your offers and use `[IN]` in listing names to differentiate.

1. Buyers must cancel existing agreements and re-negotiate from your India-based entity.

You cannot change an existing account's country to India. Create a new standalone account instead.

## If I'm already registered as a buyer with AWS India, do I still need to create a separate account for selling?
<a name="india-seller-buyer-account-separation"></a>

Yes. You must create a new standalone AWS Marketplace account for seller registration. This prevents incorrect tax and invoicing treatment for your seller account and avoids complications related to AWS Organizations structure changes.

## What are the restrictions for working with channel partners in India?
<a name="india-seller-channel-partner-restrictions"></a>

You can only work with channel partners located in India due to geographic restrictions. As an India-based channel partner, you can extend Channel Partner Private Offers (CPPO) authorized by India-registered ISVs to India-based buyers only. You cannot extend CPPOs to non-India buyers regardless of ISV location, and cannot extend CPPOs from non-India ISVs to India buyers.

## Can non-India sellers use channel partners in India to sell to buyers in India?
<a name="india-seller-dsor-program"></a>

Yes, through the Designated Seller on Record (DSOR) program. The India-based channel partner lists offerings on behalf of the non-India seller. AWS Marketplace settles with the channel partner, and the non-India seller receives payment directly from the channel partner outside AWS Marketplace. Contact your AWS account representative or AWS Marketplace Seller Operations team for additional details about the DSOR program.

## How do I indicate that my product is available only in India?
<a name="india-seller-product-listing"></a>

Products from sellers in India are automatically restricted to buyers in India. You should include `[IN]` in your product title to clearly indicate availability to buyers in India. The geographic restriction is enforced at the platform level.

## Can I create private offers for buyers in India?
<a name="india-seller-private-offers"></a>

Yes. You can create private offers for buyers in India using the standard private offer process. All private offers are only available to buyers in India and can be priced in either USD or INR.

## What compliance requirements apply to sellers in India?
<a name="india-seller-compliance"></a>

You must comply with all applicable laws and regulations in India, including but not limited to tax laws, data protection requirements, and software licensing regulations. AWS provides the platform, but compliance with local laws is your responsibility.