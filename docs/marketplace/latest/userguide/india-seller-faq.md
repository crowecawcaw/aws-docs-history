# Sellers in India FAQ

This FAQ addresses common questions for sellers in India who want to list products on AWS Marketplace.

###### Topics

- [Do I need a separate AWS account to sell in India?](#india-seller-separate-account "#india-seller-separate-account")
- [What information do I need to provide for seller registration?](#india-seller-registration-requirements "#india-seller-registration-requirements")
- [How do I get support and assistance as a seller in India?](#india-seller-support "#india-seller-support")
- [Can I sell to buyers outside of India as a seller in India?](#india-seller-geographic-restrictions "#india-seller-geographic-restrictions")
- [What currencies can I use for pricing my products?](#india-seller-pricing-currency "#india-seller-pricing-currency")
- [What product types can I create offers for?](#india-seller-product-types "#india-seller-product-types")
- [How do product pricing currency and seller disbursements work in detail?](#india-seller-pricing-disbursement-details "#india-seller-pricing-disbursement-details")
- [What are my GST tax obligations and liability as a seller in India?](#india-seller-tax-obligations "#india-seller-tax-obligations")
- [What banking information do I need to provide?](#india-seller-banking-requirements "#india-seller-banking-requirements")
- [How are AWS Marketplace listing fees handled for sellers in India?](#india-seller-listing-fees "#india-seller-listing-fees")
- [Do I need to withhold tax on listing fees?](#india-seller-tds-exemption "#india-seller-tds-exemption")
- [When will I receive disbursements?](#india-seller-disbursement-schedule "#india-seller-disbursement-schedule")
- [How do I migrate from selling outside India to selling in India?](#india-seller-account-migration "#india-seller-account-migration")
- [If I'm already registered as a buyer with AWS India, do I still need to create a separate account for selling?](#india-seller-buyer-account-separation "#india-seller-buyer-account-separation")
- [What are the restrictions for working with channel partners in India?](#india-seller-channel-partner-restrictions "#india-seller-channel-partner-restrictions")
- [Can non-India sellers use channel partners in India to sell to buyers in India?](#india-seller-dsor-program "#india-seller-dsor-program")
- [How do I indicate that my product is available only in India?](#india-seller-product-listing "#india-seller-product-listing")
- [Can I create private offers for buyers in India?](#india-seller-private-offers "#india-seller-private-offers")
- [What compliance requirements apply to sellers in India?](#india-seller-compliance "#india-seller-compliance")

## Do I need a separate AWS account to sell in India?

Yes. You must create a standalone AWS account that is not part of AWS Organizations. This account must be specifically configured for selling in India and cannot be used to sell to buyers outside India. You cannot use an existing buyer account for seller registration.

## What information do I need to provide for seller registration?

You must submit: GST identification number (GSTIN), Permanent Account Number (PAN) which auto-populates from GSTIN, seller signature for tax invoices, legal business name and address corresponding to your GSTIN, acknowledgements on withholding tax non-applicability and e-invoicing enablement, authorization for AWS India to raise invoices, and valid India domiciled bank account details.

## How do I get support and assistance as a seller in India?

Use the Contact Us form in AWS Marketplace Management Portal:

1. For banking or disbursement assistance, select Commercial Marketplace, then Seller Account, then Banking.
2. For private offer creation help, select Commercial Marketplace, then Private Offer, then Offer Creation.
3. For India-specific questions about tax obligations, banking, or regulatory requirements, consult with local advisors familiar with regulations in India.
4. Provide detailed information about your specific request for faster resolution.

## Can I sell to buyers outside of India as a seller in India?

No. Sellers in India can only sell to buyers in India. Buyers outside India can view your listings but cannot purchase them due to geographic restrictions.

## What currencies can I use for pricing my products?

All public offers must be priced in USD only. You have the option to publish private offers in INR or USD. However, listing fees are always deducted in INR and all disbursements are always in INR regardless of your pricing currency. There is no currency conversion or exchange rate variability for INR-priced private offers.

## What product types can I create offers for?

You can create products and offers for SaaS, AMI, Containers, Professional Services, ML and AWS Data Exchange product types.

## How do product pricing currency and seller disbursements work in detail?

For USD offers: Buyers receive invoices with USD pricing, applicable GST, and foreign exchange conversion rate to INR. The tax invoice uses the same rate as the commercial invoice. Your disbursement in INR equals the converted amount minus withholding tax (0.1%), TCS (0.5%), listing fees, and tax on listing fees. For INR private offers: Buyers receive invoices with the agreed INR amount without foreign exchange variability. Invoices show both INR and USD amounts with the fixed FX rate applied at offer acceptance. Minor rounding differences (maximum ±0.005 USD per line item) may occur due to backend USD processing.

## What are my GST tax obligations and liability as a seller in India?

Buyers are charged 18% GST which is paid to you as part of your disbursement, and you are responsible for remitting GST to tax authorities in India according to applicable tax laws. AWS India facilitates issuing GST tax invoices to buyers with you as the seller on record (SoR) and shares the tax invoice with you via email for your records and compliance purposes. You must ensure your GSTIN is enabled for e-invoicing and comply with all applicable tax laws in India including GST registration and filing requirements.

## What banking information do I need to provide?

You must provide bank account details in India including account number, Indian Financial System Code (IFSC), and name and address of the account holder. Only bank accounts domiciled in India are accepted for sellers in India. International bank accounts are not accepted. All disbursements are processed in INR to your bank account in India only.

## How are AWS Marketplace listing fees handled for sellers in India?

The fee structure follows standard AWS Marketplace rates, but all fees are calculated and charged in Indian Rupees (INR) with 18% GST applicable. AWS Marketplace provides a GST tax invoice for listing fees. Both listing fees and GST are deducted from your seller disbursement. You are not required to withhold funds toward listing fees due to TDS exemption under Section 194-O of the Income Tax Act. Refer to the AWS Marketplace Seller Terms for current fee information.

## Do I need to withhold tax on listing fees?

No. Per Section 194-O subsection 4 of the Income Tax Act, 1960, once withholding tax is processed at any point in the payment flow, sellers are exempt from Tax Deducted at Source (TDS) withholding on listing fees. AWS deducts TDS from buyer payments and remits to tax authorities. TDS certificates are shared with you for tax claiming purposes.

## When will I receive disbursements?

Disbursements follow the standard AWS Marketplace schedule but are processed in INR to your bank account in India. The timing and frequency align with standard AWS Marketplace disbursement practices. You can only receive disbursements in Indian Rupees (INR) to your bank account domiciled in India.

## How do I migrate from selling outside India to selling in India?

You have two options:

_Option 1: Create a new standalone account (recommended)_

1. Create a new standalone account for your India-based entity.
2. Re-list your offers and use `[IN]` in listing names to differentiate.
3. Buyers must cancel existing agreements and re-negotiate from your India-based entity.

_Option 2: Change your existing account location to India_

1. Update tax location in AWS Billing Console to India.
2. Ensure no linked accounts or turn off tax inheritance settings.
3. Submit GSTIN, PAN, seller signature, and bank account in India in AWS Marketplace Management Portal.
4. Upon validation, you can start listing on AWS India.
5. You'll lose ability to sell to non-India buyers.
6. Existing non-India disbursements will be blocked.
7. You must cancel all agreements with non-India buyers.
8. Existing contracts with buyers in India will be invoiced in INR from AWS India.

## If I'm already registered as a buyer with AWS India, do I still need to create a separate account for selling?

Yes. You must create a new standalone AWS Marketplace account for seller registration. This prevents incorrect tax and invoicing treatment for your seller account and avoids complications related to AWS Organizations structure changes.

## What are the restrictions for working with channel partners in India?

You can only work with channel partners located in India due to geographic restrictions. As an India-based channel partner, you can extend Channel Partner Private Offers (CPPO) authorized by India-registered ISVs to India-based buyers only. You cannot extend CPPOs to non-India buyers regardless of ISV location, and cannot extend CPPOs from non-India ISVs to India buyers.

## Can non-India sellers use channel partners in India to sell to buyers in India?

Yes, through the Designated Seller on Record (DSOR) program. The India-based channel partner lists offerings on behalf of the non-India seller. AWS Marketplace settles with the channel partner, and the non-India seller receives payment directly from the channel partner outside AWS Marketplace. Contact your AWS account representative or AWS Marketplace Seller Operations team for additional details about the DSOR program.

## How do I indicate that my product is available only in India?

Products from sellers in India are automatically restricted to buyers in India. You should include `[IN]` in your product title to clearly indicate availability to buyers in India. The geographic restriction is enforced at the platform level.

## Can I create private offers for buyers in India?

Yes. You can create private offers for buyers in India using the standard private offer process. All private offers are only available to buyers in India and can be priced in either USD or INR.

## What compliance requirements apply to sellers in India?

You must comply with all applicable laws and regulations in India, including but not limited to tax laws, data protection requirements, and software licensing regulations. AWS provides the platform, but compliance with local laws is your responsibility.
