

# Best practices
<a name="best-practices"></a>

 Use these best practices to optimize your custom integration development and maintenance.

## General best practices
<a name="general-best-practices"></a>

1. Map all *mandatory* fields because they are the required fields in the AWS Partner Network (APN) Customer Engagement (ACE) submission form.

1. Connect with your current ACE Pipeline Manager user to understand what the process looks like. Capture any unique processes/field uses, so you can build it into your experience.

1. Consider creating separate sales pipeline stages for Amazon Web Services (AWS)-reported sales stages (example: Stage, Target Close Date, Expected Monthly AWS revenue, Next Steps). If we have different stage definitions, we might override your sales stages. When you create separate sales stages, it allows you to manage your pipeline appropriately, but still have visibility into what AWS is projecting.

1. For partner referred opportunities, the ACE team must approve/reject them before we accept any updates.

1. For AWS referred opportunities, the partner must accept or reject the opportunities.

## Data exchange protocols
<a name="data-exchange-protocols"></a>

1. **Input conventions**: Separate multi-select picklist entries with semicolons and omit spaces.

1. **Attention to detail**: Field names and values are case-sensitive, so maintain accuracy.

1. **Deletion procedures**: Execute field removal by transmitting the value `null` for the chosen field.

1. **Synchronization**: The synchronization processes operate on an hourly basis, causing potential delays in data reflections. Updates to AWS can take up to one hour to reflect in the AWS customer relationship management (CRM). Avoid sending multiple documents per hour.

## Field-specific best practices
<a name="field-specific-best-practices"></a>

1. **Inbound modifications**: To protect the integrity of your data, disable modifications for fields such as `stage`, `closedDate`, and `closedLostReason`. To track AWS values without affecting your local Salesforce values, use these read-only fields: `awsStage`, `awsCloseDate`, and `awsClosedLostReason`.

1. **Customer mapping and validation**: Ensure customer website accuracy because it’s pivotal for AWS CRM mapping. Pair it with the customer name for superior CRM account mapping.

1. **Project description clarity**: Furnish a clear description detailing customer challenges and solution alignments. AWS uses this to validate the opportunity.

1. **Provisioning**: (Optional) When you provision end-customer contact specifics, it enables AWS to retrace leads and campaigns. This leads to enhanced funding verdicts.

## Additional best practices
<a name="additional-best-practices"></a>

1. Adhere to the latest payload field definition guidelines.

1. Maintain sandbox bucket naming consistency with the specified format.

1. Use the recommended naming pattern for the production bucket.

1. Prioritize sandbox environment testing before live deployment.

1. Maintain distinct identifiers for records between AWS and partner CRMs.

1. Post-processing, delete files in the outbound Amazon Simple Storage Service (Amazon S3) folder. Originals remain in the archives.

1. To prevent errors, set up field level validations at the source.