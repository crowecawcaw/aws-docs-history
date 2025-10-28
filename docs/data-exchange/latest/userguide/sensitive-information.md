# Sensitive categories of information in AWS Data Exchange

When you create a product in AWS Data Exchange, you must specify whether your product contains any
personal data or sensitive categories of information.

Sensitive categories of information include: biometric or genetic data; health data;
racial or ethnic origin; political opinions; religious or philosophical beliefs; sex or sexual
orientation; trade union membership; personal payment or financial information (for example,
credit history); or other similar categories of information.

Personal data is data that identifies or can be used to identify a natural person.

Before accepting a private offer, prospective subscribers will be alerted on the product
detail page that your product contains sensitive categories of personal information and/or
personal information that is not otherwise publicly available.

As part of the process described in [Step 5: Publish a new product](publish-data-product.md#publish-products "publish-data-product.md#publish-products"), you choose the options for your product's
**Sensitive information** configuration. Choose one of the following
options:

- Option 1 – **No personal data that is not otherwise publicly available,
  and no sensitive categories of information**

Choose this option if your product does not contain any personal data that is not
otherwise publicly available, and no sensitive categories of information.

Examples include financial market data, weather patterns, or public company
filings.

- Option 2 – **No personal data but contains sensitive categories of
  information**

Choose this option if your product contains non-personal sensitive
information.

Examples include aggregated diversity data or anonymized financial data.

- Option 3 – **Personal data (i) with sensitive categories of information
  and/or (ii) not otherwise publicly available and does not include Protected Health
  Information (PHI) under the Health Insurance Portability and Accountability Act of 1996
  (HIPAA)**

Choose this option if your product contains personal data that is not otherwise
publicly available. The product must not include protected health information (PHI)
subject to HIPAA.

Examples include PII such as email addresses, Social Security numbers, biometrics, or
mobile IDs.

###### Note

This option is only available to eligible providers enrolled in the Extended
Provider Program who have agreed to the Extended Provider Program Addendum to the Terms
and Conditions for AWS Marketplace Providers. For more information, see [Extended Provider Program (EPP)](providing-data-sets.md#epp "providing-data-sets.md#epp").

- Option 4 – **Protected Health Information (PHI) subject to the Health
  Insurance Portability and Accountability Act of 1996 (HIPAA)**

Choose this option if your product contains protected health information (PHI) subject
to HIPAA.

Examples include PHI such as patient information disclosed by a covered entity.

###### Important

Option 4 is only available for private products. Public products may not contain
such data.

###### Note

Option 4 is only available to the following eligible providers:

    + Eligible providers enrolled in the Extended Provider Program who have agreed to
     the Extended Provider Program Addendum to the Terms and Conditions for AWS Marketplace
     Providers. For more information, see [Extended Provider Program (EPP)](providing-data-sets.md#epp "providing-data-sets.md#epp").
    + Eligible providers who have agreed to the AWS Business Associate Addendum, as
     well as the AWS Data Exchange Addendum to the AWS Business Associate Addendum.

###### Warning

If you are not enrolled in the Extended Provider Program, listing a product with data or
information described in Option 3 and Option 4 is a violation of our [Publishing guidelines for AWS Data Exchange](publishing-guidelines.md "publishing-guidelines.md"). AWS removes any
product that breaches these guidelines and can suspend the provider from future use of the
service.

For more information about creating a product and setting the sensitivity status of the
data, see [Step 5: Publish a new product](publish-data-product.md#publish-products "publish-data-product.md#publish-products").
