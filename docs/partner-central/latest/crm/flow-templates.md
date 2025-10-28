# Using flow templates

Flow templates are pre-built Salesforce flows that integrate Salesforce with AWS Partner Central using the AWS Partner Central API integration method.
These templates include data synchronization, field mapping, and error handling configurations.

## Available templates

**Unified Standard-ACE Opportunity Sync Flow Template**

The Unified Standard-ACE Opportunity Sync flow template maps Salesforce Standard Opportunity fields to ACE Opportunity
fields, converts state and country formats, and prevents duplicate entries. It includes default values for required fields.

- Revenue, close dates, and next steps are synchronized between Salesforce and AWS Partner Central.
- By default, synchronization is triggered when "Create ACE" is added to the opportunity description. You can modify this trigger mechanism by using a checkbox or button.
- This template provides a foundation for developing flows that align with your business requirements and field mappings.
- This template is for use with AWS Partner Central API integration only and is not compatible with other integration methods.

Find this template in Salesforce Flow Builder by searching for "Unified Standard-ACE Opportunity Sync Flow Template".

**Prerequisites**

This template requires an active AWS Partner Central API integration. You must have appropriate permissions in Salesforce and configured fields in both systems. Familiarity with Salesforce Flow and AWS Partner Central API is recommended.

**Accessing the template**

To locate the flow template:

1. In your Salesforce org, choose **Setup**.
2. Search for **Flows**.
3. On the Flows page, search for the "Unified Standard-ACE Opportunity Sync Flow" template.

Create a copy of the template to customize for your requirements. Test modifications in a sandbox environment before deploying to production.

**Key features**

The template includes field mapping between Standard Opportunity and ACE Opportunity objects, state and country format conversion, and duplicate entry prevention. You can configure custom triggers and default
value handling for required fields.

**Implementation considerations**

- Follow best practices when customizing flow templates.
- Test modifications and consider impact on existing processes.
- Common customizations include adding custom fields or adjusting trigger mechanisms.
- Test thoroughly in a sandbox environment before deploying to production.
- Consider performance implications when dealing with large data volumes or complex business logic.
