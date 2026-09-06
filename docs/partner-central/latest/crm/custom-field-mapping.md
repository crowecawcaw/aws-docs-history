

# Field mapping
<a name="custom-field-mapping"></a>

Field mapping is an essential step in the integration process where partners align their customer relationship management (CRM) system’s fields with those defined by Amazon Web Services (AWS). This ensures that both parties accurately exchange and understand data. Below are guidelines to assist in this process.

## Mandatory field mapping
<a name="mandatory-field-mapping"></a>
+ Map each mandatory field to its corresponding field in your CRM system. It’s essential for successful data exchange when you ensure all required fields are mapped. For more information, refer to [Field definitions](resources.md#custom-field-definitions)
  + [Opportunity](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv)
  + [Lead](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Leads-Fields.csv)

## Handling optional fields
<a name="handling-optional-fields"></a>
+ Understand the role of optional fields in the integration process. Decide if you want to map these fields based on your business requirements, and be aware of any possible implications from leaving them unmapped.

## Value mapping
<a name="value-mapping"></a>
+ Align each field value in your CRM with the required AWS Partner Network (APN) Customer Engagement (ACE) list value, as specified in [Field definitions](resources.md#custom-field-definitions). This is important to maintain data consistency and integrity.

## Data type and format validation
<a name="data-type-and-format-validation"></a>
+ Verify that the data types and formats of the fields in your CRM system align with those specified in the AWS *Field definitions*. It’s essential to maintain consistency in data types and formats to prevent data corruption and ensure seamless integration.

## Field length and limitations
<a name="field-length-and-limitations"></a>
+ Notice field length restrictions and other limitations. Ensure that the data from your CRM system fits into the corresponding fields in AWS without being truncated or causing errors.

## Data type and format validation
<a name="data-type-and-format-validation-1"></a>
+ Verify that the field data types and formats in your CRM system align with those specified in [Field definitions](resources.md#custom-field-definitions). It’s crucial to prevent data corruption and ensure seamless integration with consistency in data types and formats.

## Periodic review and update
<a name="periodic-review-and-update"></a>
+ Regularly review and update your field mappings to accommodate changes in your CRM system or AWS requirements. This proactive approach ensures ongoing data exchange accuracy and efficiency.

## Field mapping documentation
<a name="field-mapping-documentation"></a>
+ Maintain comprehensive field mapping documentation. This practice aids in troubleshooting, future updates, and ensuring clarity in how data is transferred between systems.

## Testing and validation
<a name="testing-and-validation"></a>
+ Conduct thorough field mappings testing to validate that data is being transferred and transformed accurately. Address any discrepancies or issues immediately to ensure data integrity.

## Handling unwanted overwrites
<a name="handling-unwanted-overwrites"></a>
+ To prevent AWS data from overwriting specific CRM fields, consider the following: 
  + Creating a custom CRM field for the data you want to protect.
  + Having this custom field reviewed by a sales representative.
  + Once the custom field is approved, adding it to the opportunity record and pipeline.
+ This is particularly important for fields like `MRR` or `Stage`, especially if they signify that a product has launched.

## Managing downstream dependencies
<a name="managing-downstream-dependencies"></a>
+ If there are downstream dependencies in your system that rely on data exchange, consider the following:
  + Creating new fields in your CRM to accommodate the AWS data.
  + Realigning your business processes as necessary to ensure seamless integration and data flow.