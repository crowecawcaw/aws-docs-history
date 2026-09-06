

# Step 2: Provide tax information
<a name="provide-tax-information"></a>

Providing tax information is a required step for sellers who plan to offer paid products on AWS Marketplace. This information ensures proper tax reporting and withholding for your sales.

## Tax information requirements
<a name="tax-information-requirements"></a>

The tax information you need to provide depends on your country or region and the types of products you plan to sell:
+ **US-based sellers** – If you're based in the United States, you need to provide a completed W-9 form, which includes your Taxpayer Identification Number (TIN).
+ **Non-US sellers** – If you're based outside the United States, you need to provide a completed W-8 form (typically W-8BEN for individuals or W-8BEN-E for entities). This does not apply to sellers in India.
+ **VAT/GST registration** – If you're required to collect Value-Added Tax (VAT) or Goods and Services Tax (GST) in your jurisdiction, you need to provide your VAT/GST registration number.
+ **Professional services providers** – If you plan to sell professional services on AWS Marketplace, you must complete the Tax Questionnaire for DAC7 in addition to the standard tax forms.

**Sellers in India**  
Sellers in India don't need to complete the W-8 form or DAC7 as they can only sell to buyers in India. If you're changing your location to outside India, you need to complete W-9 or W-8 forms (as applicable) and DAC7. For detailed information about India-specific tax requirements, see [Getting started as a seller in India](getting-started-seller-india.md).

### VAT registration requirements
<a name="vat-registration-requirements"></a>

If you're located in these countries, you must provide VAT registration information:
+ Australia
+ Bahrain
+ Colombia
+ European Union member states
+ Israel
+ New Zealand
+ Norway
+ Switzerland
+ United Arab Emirates (UAE)
+ United Kingdom (UK)

**Note**  
If you need to add supplemental tax registrations for specific localities after registration, see [Supplemental tax registrations](supplemental-tax-registrations.md) in [Managing your seller account](seller-account-management.md). 

### Tax invoicing responsibility
<a name="tax-invoicing-responsibility"></a>

In these countries, if you and your buyer are located in the same country, you may be responsible for tax invoicing, collections, and remittances. Consult with your tax advisor:
+ Bahrain
+ Colombia
+ Israel
+ Norway
+ Switzerland
+ United Arab Emirates (UAE)

### Japan tax requirements
<a name="japan-tax-requirements"></a>

From April 1, 2025, the following procedures are in effect for the collection and remittance of the 10% Japanese Consumption Tax (JCT) and the issuance of tax qualified invoice (TQI) by AWS Japan for products sold on AWS Marketplace:


| Seller and customer scenario | Tax collection and invoice procedures | 
| --- | --- | 
| **Seller – **Independent software vendor (ISV) with an address outside of Japan.<br />**Customer – **AWS account with an address in Japan. | According to the Specified Platform Taxation rule, AWS Japan will do the following:+  Collect the 10% Japanese Consumption Tax (JCT). <br />+  Issue a Tax Qualified Invoice (TQI) to the customer under AWS Japan JCT number T6011001106696. <br />+  Remit the collected Japanese Consumption Tax (JCT) to the Japan Tax Authority (JTA). <br />To avoid duplication, the ISV should cease collecting or remitting Japanese Consumption Tax (JCT) and issuing Tax Qualified Invoices (TQIs). | 
| **Seller – **Independent software vendor (ISV) with an address in Japan.<br />**Customer – **AWS account with an address in Japan. | According to the Special Agency rule, AWS Japan will do the following:+  Collect the 10% Japanese Consumption Tax (JCT). <br />+  Issue a Tax Qualified Invoice (TQI) to the customer under AWS Japan JCT number T6011001106696. <br />+  Disburse the collected JCT to the ISV. <br />The ISV must do the following:+  Enter their Japanese Corporate Number and Japanese Consumption Tax (JCT) Number in the Amazon Marketplace Management Portal. <br />+  Use the Tax Qualified Invoice (TQI) information available in the Amazon Marketplace Management Portal to remit the collected JCT to the Japanese Tax Authority (JTA).  | 
| Channel Partner Private Offer (CPPO), ISV outside Japan.1.  First transaction   **Seller – **Independent software vendor (ISV) with an address outside Japan.   **Customer – **AWS Marketplace Channel Partner with an address in Japan.   <br />2.  Second transaction   **Seller – **Same AWS Marketplace Channel Partner.   **Customer – **AWS account with an address in Japan.    | For the first transaction, the Channel Partner must report the Japanese Consumption Tax (JCT) according to the reverse-charge tax mechanism.<br />For the second transaction:+  According to the Special Agency rule, AWS Japan will do the following:   Collect the 10% Japanese Consumption Tax (JCT).   Issue a Tax Qualified Invoice (TQI) to the customer under AWS Japan JCT number T6011001106696.   Disburse the collected Japanese Consumption Tax (JCT) to the Channel Partner.   <br />+  The Channel Partner must do the following:   Enter their Japanese Corporate Number and Japanese Consumption Tax (JCT) Number in the Amazon Marketplace Management Portal.   Use the Tax Qualified Invoice (TQI) information available in the Amazon Marketplace Management Portal to remit the collected JCT to the Japanese Tax Authority (JTA).    | 
| Channel Partner Private Offer (CPPO), all sellers and customers in Japan.1.  First transaction   **Seller – **Independent software vendor (ISV) with an address in Japan.   **Customer – **AWS Marketplace Channel Partner with an address in Japan.   <br />2.  Second transaction   **Seller – **Same AWS Marketplace Channel Partner.   **Customer – **AWS account with an address in Japan.    | For the first transaction (from October 6, 2025 (UTC)):+  Collect the 10% Japanese Consumption Tax (JCT) from Channel Partner. <br />+  Issue a Tax Qualified Invoice (TQI) to Channel Partner using AWS Japan JCT number T6011001106696. <br />+  Disburse the collected Japanese Consumption Tax (JCT) to the ISV. <br />For the second transaction:+  According to the Special Agency rule, AWS Japan will do the following:   Collect the 10% Japanese Consumption Tax (JCT).   Issue a Tax Qualified Invoice (TQI) to customers using AWS Japan JCT number T6011001106696.   Disburse the collected Japanese Consumption Tax (JCT) to the Channel Partner.   <br />+  The Channel Partner must do the following:   Enter their Japanese Corporate Number and Japanese Consumption Tax (JCT) Number in the Amazon Marketplace Management Portal.   Use the Tax Qualified Invoice (TQI) information available in the Amazon Marketplace Management Portal to remit the collected JCT to the Japanese Tax Authority (JTA).    | 
| Channel Partner Private Offer (CPPO), ISV and Channel Partner outside Japan.1.  First transaction   **Seller – **Independent software vendor (ISV) with an address outside Japan.   **Customer – **AWS Marketplace Channel Partner with an address outside Japan.   <br />2.  Second transaction   **Seller – **Same AWS Marketplace Channel Partner.   **Customer – **AWS account with an address in Japan.    | For the first transaction, AWS Japan does not issue an invoice or collect Japan Consumption Tax (JCT) as this is outside the scope of JCT.<br />For the second transaction:+  According to the Specified Platform Business rule, AWS Japan will do the following:   Collect the 10% Japanese Consumption Tax (JCT).   Issue a Tax Qualified Invoice (TQI) to the customer under AWS Japan JCT number T6011001106696.   Remit the collected Japan Consumption Tax (JCT) to the Japan Tax Authority (JTA).   <br />To avoid duplication, the Channel Partner should cease collecting or remitting Japanese Consumption Tax (JCT) and issuing Tax Qualified Invoices (TQIs). | 
| Channel Partner Private Offer (CPPO), Channel Partner outside Japan.1.  First transaction   **Seller – **Independent software vendor (ISV) with an address in Japan.   **Customer – **AWS Marketplace Channel Partner with an address outside Japan.   <br />2.  Second transaction   **Seller – **Same AWS Marketplace Channel Partner.   **Customer – **AWS account with an address in Japan.    | For the first transaction, AWS Japan does not issue an invoice or collect Japan Consumption Tax (JCT) as this is outside the scope of JCT.<br />For the second transaction:+  According to the Specified Platform Business rule, AWS Japan will do the following:   Collect the 10% Japanese Consumption Tax (JCT).   Issue a Tax Qualified Invoice (TQI) to the customer under AWS Japan JCT number T6011001106696.   Remit the collected Japan Consumption Tax (JCT) to the Japan Tax Authority (JTA).   <br />To avoid duplication, the Channel Partner should cease collecting or remitting Japanese Consumption Tax (JCT) and issuing Tax Qualified Invoices (TQIs). | 

For more information about VAT, invoicing, and your tax obligations as a seller, see [AWS Marketplace Sellers](https://aws.amazon.com/tax-help/marketplace/) on [Amazon Web Service Tax Help](https://aws.amazon.com/tax-help/).

## India tax requirements
<a name="india-tax-requirements"></a>

For help with India-specific tax requirements, see [Tax help > India](https://aws.amazon.com/tax-help/india/india-marketplace-sellers/) on the AWS website.

## Steps to provide tax information
<a name="provide-tax-information-steps"></a>

Follow these steps to provide your tax information in AWS Marketplace:

1. Sign in to the AWS Marketplace Management Portal at [https://us-east-1.console.aws.amazon.com/partnercentral/home](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Navigate to the **Settings** tab.

1. Select **Go to tax dashboard** in the **Payment information** section.

1. Complete the U.S. tax interview. Follow the on-screen instructions to complete the appropriate tax form based on your location (W-9 form for US-based sellers or W-8 form for non-US sellers).
**Note**  
If you see the error message "Tax interview location does not match the business location," ensure that the banking and tax information provided in Billing and Cost Management matches what is entered into the AWS Marketplace Management Portal. Your tax interview location must match the business location.

1. Review all information for accuracy before submitting.

1. Choose **Submit** to complete the tax information process.

1. (Optional) If you need to complete VAT registration, return to the **Settings** page and choose **Complete VAT information**. This redirects you to the **Tax settings** page of the AWS Billing console.

**Note**  
The tax interview process is managed by a third-party service provider. Your information is securely transmitted and stored in accordance with applicable tax regulations. The VAT information section is only available if you are in an AWS Region that supports VAT.

## Best practices for providing tax information
<a name="tax-information-best-practices"></a>

Consider these best practices when providing your tax information:
+ Ensure all information matches your official tax records to avoid processing delays.
+ Have your tax identification documents ready before starting the process.
+ If you're unsure about any tax requirements, consult with a tax professional before submitting your information.
+ Keep your tax information up to date. If your tax status changes, update your information promptly in the AWS Marketplace Management Portal.
+ For VAT/GST registration, ensure you understand the tax collection and remittance requirements in your jurisdiction.

## Next steps
<a name="next-steps-after-tax"></a>

After providing your tax information, you can proceed to the next step in the registration process: [Step 3: Provide bank account information](provide-bank-information.md). 

After you begin selling and have tax activity, you can access your tax documents such as 1099 forms. For more information, see [Access tax documents](access-tax-documents.md) in [Managing your seller account](seller-account-management.md). 