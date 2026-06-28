# Finalize setup and configuration within Salesforce

The remaining activities to upgrade the connector are performed by a **Salesforce Administrator**. Complete activities in Sandbox
first, test, then move to Production.

## Install the latest version of the CRM Connector

Visit the Salesforce AppExchange and [download the latest version](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000IYf0nUAD&tab=e "https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000IYf0nUAD&tab=e") of the AWS Partner CRM
Connector.

## Complete the guided setup in the CRM Connector

Follow [these instructions](p-c-api-integration.md "p-c-api-integration.md") to configure the settings within the AWS Partner
CRM Connector.

## Review and adjust permission sets

With synchronous capability via API, you can now apply permission sets to users
(an ACE User) or user groups (for example, all Partner Sales) to enable co-sell
functionality.

- You **no longer need** the
  `APN Integration User` permission set.
- Use the `APN Business Admin` permission set for the user that
  runs the ACE Integration.
- Use the `AWS Marketplace Admin` permission set for the user
  that runs the Marketplace Integration.

For more information, see [permission sets details](crm-connector-pemissions-sets.md "crm-connector-pemissions-sets.md").

## Review and disable schedules for Amazon S3

With the API-based approach, there is **no longer any need for
scheduled jobs** – the integration runs in real time based on
when updates are made to the ACE Opportunity.

###### To disable scheduled jobs

1. Navigate to the **Schedules** tab within the AWS Partner
   CRM Connector app.
2. Choose **Deactivate All Jobs** and then choose
   **Deactivate** again.

It is also recommended to **delete** the scheduled
records within this tab. To remove any remaining APN scheduled jobs from
Setup:

###### To remove APN scheduled jobs from Setup

1. Navigate to **Setup**. Search for "Scheduled" and select
   the **Scheduled Jobs** menu item.
2. Review the list for any jobs related to an APN sync. If found, choose the
   **Del** link to delete them.

###### Note

You can keep the `CustomLogInteractionBatch` job running. This is
for AppExchange App Analytics and is still relevant for the API version of the
connector.

## Review and adjust your mappings

The "Sync with AWS" fields on the standard opportunity and the ACE Opportunity
are **no longer leveraged** in the integration. Instead,
changes are triggered automatically based on your mapped object.

Key points:

- The **ACE Opportunity object** is recommended
  as a landing area within your Salesforce org – it matches the AWS
  opportunity data points in Partner Central and allows auto-mapping fields.
- If you were already using the ACE Opportunity for your integration
  mapping, no additional changes should be required.
- Partners do not need to perform any manual configuration for ACE
  Opportunity objects – all necessary mappings are available
  out-of-the-box.

For more details, see the [integration mapping section](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/mappings "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/mappings"). The ACE Opportunity data model is
available on [GitHub](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/ACE-Data-Model.xlsx "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/ACE-Data-Model.xlsx").

The latest connector version includes a **flow
template** to help map your standard opportunity to the ACE opportunity
for auto-creation and auto-updates. For more detail, see [flow templates](flow-templates.md "flow-templates.md").

## Review and add required fields and buttons

The connector has introduced new fields and buttons since version 3.0. Some fields
are required for opportunity submission and must be added to your ACE Opportunity
lightning record page.

1. Review [all fields added after Connector Version 3.0](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade#all-fields-added-after-connector-version-3.0 "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade#all-fields-added-after-connector-version-3.0") and add them to
   your ACE Opportunity page layout as indicated.
2. Review [current ACE Opportunity features](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/buttons "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/buttons") to understand available
   buttons and related lists.
3. Review [the configurations required to enable these features](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade/upgrade "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade/upgrade") and
   complete the steps for your org.

## Deactivate legacy validation rules

Several legacy validation rules must be deactivated and others must remain active.
Review the full list and ensure each validation rule in your org matches the expected
status before proceeding. See [this section](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade/upgrade#disable-validation "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade/upgrade#disable-validation") to walk through the necessary steps.

The following table lists the validation rules and their expected status.

Validation rules status| Rule name | Error location | Status |
| --- | --- | --- |
| `ACEOpp_PreventUpdatesWhenPOSubmitted` | Top of Page | Deactivate |
| `ACEOppNew_CustomerBusinessProblemLength` | Customer business problem (legacy field) | Deactivate |
| `ACEOppNew_CustomerBusinessProblemNew` | Customer business problem | Deactivate |
| `ACEOppNew_MandatoryclosedLostReason` | Closed lost reason | Active |
| `ACEOppNew_MandatorycompetitiveTrackingOt` | Competitive tracking other | Active |
| `ACEOppNew_MandatorycontractEndDate` | Contract end date | Active |
| `ACEOppNew_MandatorycontractStartDate` | Contract start date | Active |
| `ACEOppNew_MandatorycustomerCompanyName` | Customer company name | Active |
| `ACEOppNew_MandatorycustomerSoftwareVal` | Customer software value | Active |
| `ACEOppNew_MandatorycustomerSoftwareValue` | Customer software value currency | Active |
| `ACEOppNew_MandatorycustomerWebsite` | Customer website | Active |
| `ACEOppNew_MandatoryIndustryOther` | Industry other | Deactivate |
| `ACEOppNew_MandatoryisMarketingDevelopmen` | Is marketing development funded | Active |
| `ACEOppNew_MandatoryIsOppFromMarketingAct` | Is opportunity from marketing activity | Active |
| `ACEOppNew_MandatoryNullawsSFCampaignName` | AWS Salesforce campaign name | Active |
| `ACEOppNew_MandatoryNULLisMarketingDev` | Is marketing development funded (null check) | Active |
| `ACEOppNew_MandatoryNullmarketingChannel` | Marketing activity channel | Active |
| `ACEOppNew_MandatoryNullmarketingusecase` | Marketing activity use case | Active |
| `ACEOppNew_MandatoryotherSolutionOffered` | Other solution offered | Active |
| `ACEOppNew_MandatoryparentOppId` | Parent opportunity ID | Deactivate |
| `ACEOppNew_MandatorypartnerAcceptanceStat` | Partner acceptance status | Deactivate |
| `ACEOppNew_MandatoryprocurementType` | Procurement type | Active |
| `ACEOppNew_MandatoryrejectionReason` | Rejection reason | Active |
| `ACEOppNew_MandatorySalesActivities` | Sales activities | Active |
| `ACEOppNew_MandatorySolutionOffered` | Solution offered | Deactivate |
| `ACEOppNew_MandatoryState` | State | Deactivate |
| `ACEOppNew_PostalCode` | Top of Page (postal code) | Deactivate |
| `ACEOppNew_PreventUpdatesWhenPOSubmitted` | Top of Page (prevent updates) | Deactivate |
| `ACEOppNew_RequireFieldsForAWSReferral` | Top of Page (AWS Referral required fields) | Active |
| `ACEOppNew_TargetCloseDate` | Top of Page (target close date) | Active |

## Deactivate legacy ACE custom flows

Ensure the following flows have been **deactivated**:

- Sync ACE Opportunity to Partner Central API
- Private Offer Lookup
- APN Synchronization Failure Notification
- Updating Private Offer field On ACE Opportunity
- Updating Ace opportunity field on Sync Log Detail Record
- Unified Standard-ACE Opportunity Sync Flow (template)

## Test data flow and mapping to ensure API sync

Test your process to ensure no issues before moving the integration to production.
The following resources can help with testing:

- [Testing from the settings](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/config-int#task-3-:-test-the-setup "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/config-int#task-3-:-test-the-setup")
- [Testing from an ACE Opportunity](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/mappings#task-3-:-test-the-integration "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/mappings#task-3-:-test-the-integration") (Do not submit test
  opportunities in production)
- [Testing from your standard opportunity](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/flows#task-3-:-test-the-flow "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/flows#task-3-:-test-the-flow")

If any issues arise, [troubleshoot](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/config-int#task-4-:-troubleshooting "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/config-int#task-4-:-troubleshooting") by reviewing the ACE Sync Logs and the AWS Marketplace
Notifications.

## Complete backfill of opportunities from AWS to Salesforce

Run a backfill process to ensure complete data within your Salesforce org and avoid
disruption in future updates. The backfill process refreshes your Salesforce data
with Partner Central data.

Key notes:

- The `awsapn__Last_Modified_Date__c` field on the ACE
  Opportunity needs to match the Last Modified Date in Partner Central for future
  updates to sync – this is a **new field that did
  not exist in the Amazon S3 version**.
- The backfill process can pull all AWS opportunities into Salesforce, or
  refresh only ones that already have an APN CRM ID. Additional filters can be
  set to define your dataset.

**Before running the backfill:**

- Deactivate the "Sync ACE Opportunity to Partner Central API" flow if
  active.
- Uncheck the "Auto Share to AWS" option in the AWS Partner CRM
  Connector Settings custom setting.
- Re-enable "Auto Share to AWS" **after** the
  backfill is complete, as this drives the syncing automation.

###### Note

Review Salesforce governor limits and process in batches or after-hours as
needed.

For more details, follow the [Backfill Opportunities from Partner Central](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/backfill "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/backfill") section.

To receive guided support during the backfill process, open a case in Partner Central:
**Partner Central** →
**Support** → [Open New Support Case](https://partnercentral.awspartner.com/partnercentral2/s/newsupportcase "https://partnercentral.awspartner.com/partnercentral2/s/newsupportcase") → **CRM
Integration**.
