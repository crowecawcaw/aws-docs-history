# Upgrading AWS Partner CRM connector to the new data

model

###### Important

Test and approve the new data model upgrade in your sandbox Salesforce organization
before upgrading your production environment. For the new data model and changes between the
old and new models, refer to the following [aws-samples/partner-crm-integration-samples](https://github.com/aws-samples/partner-crm-integration-samples/tree/main/opportunity-samples "https://github.com/aws-samples/partner-crm-integration-samples/tree/main/opportunity-samples") on GitHub:

- **Opportunity-FieldsAndStandardValues-DiffWithPrevVersion-V14.3.xlsx**
- **Opportunity-Fields.xlsx**
- **Opportunity\_-_StandardValues.xlsx**

## Prerequisites

- Use field definitions for new data model guidelines of the ACE CRM integration, and
  migrate any required open opportunities and leads to the new data model.
- Add or remove columns in your custom or standard objects (objects used in
  mapping).
- Ensure that you're using version 2.0 or later of the AWS Partner CRM connector.

###### To upgrade to the new data model

1. Sign in to your Salesforce organization as a system administrator.
2. Deactivate any active schedules.
3. Choose **Setup**, **Custom Settings**,
   **AWS Partner CRM connector Settings**, and then update the version to
   **2.0** or later.

###### Note

Starting with version 2.0, the **Version** field is mandatory.
This field specifies the payload version that partners use to interact with the CRM
Integration. When partners move to version 2.0, they must fully adopt its
specifications. Reverting to previous versions isn't permitted. 4. Choose the **ACE Mapping** tab. 5. Create, review, and update all required field mappings and details. For sandbox
testing, use the custom ACE opportunity and ACE lead object to test the new data model
features. For more information, refer to [Sandbox testing with the custom ACE opportunity and
ACE lead objects](custom-ace-opportunity.md "custom-ace-opportunity.md"). 6. Activate schedules for opportunities and leads. 7. Review the ACE sync logs for synchronization errors and make any corrections. 8. Review the synced opportunities and leads to ensure that the data transformation is
accurate. Alternatively, review the opportunities and leads in ACE to ensure that the
new data model changes are captured accurately. 9. Follow your product deployment process to migrate the changes to your production
Salesforce environment.

###### Note

If you need help, refer to [Getting help](getting-help.md "getting-help.md").
