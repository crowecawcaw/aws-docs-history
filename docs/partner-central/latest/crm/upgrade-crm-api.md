

# Upgrading from Amazon S3 to API-based integration
<a name="upgrade-crm-api"></a>

**Note**  
The topics in this section assume you've completed the prerequisites for an AWS Partner Central integration, an AWS Marketplace integration, or both. For more information, refer to [Integration prerequisites](crm-integration-setting-up.md) and [Getting started](crm-integration-getting-started.md) earlier in this guide.  
**Recommended:** Complete these activities in a Sandbox environment first, test thoroughly, and then deploy to Production.

This section walks you through upgrading your AWS Partner CRM Connector from Amazon S3-based to API-based integration. The API-based integration replaces the legacy Amazon S3 bucket model with real-time, bidirectional synchronization through IAM roles and APIs.

For a fully interactive walkthrough with screenshots, see the [AWS Partner CRM Connector upgrade workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade/s3toapi) on the AWS Workshops website.

The upgrade involves the following steps:

1. [Prerequisites](#upgrade-prerequisites)

1. [Set up AWS infrastructure](#upgrade-aws-infrastructure)

1. [Finalize setup and configuration within Salesforce](#upgrade-finalize-salesforce)
   + [Review and adjust your mappings](#upgrade-adjust-mappings)
   + [Review and add required fields and buttons](#upgrade-required-fields-buttons)
   + [Review and disable schedules for Amazon S3](#upgrade-disable-schedules)

1. [Cleanup](#upgrade-cleanup)
   + [Deactivate legacy validation rules](#upgrade-deactivate-validation-rules)
   + [Complete backfill of opportunities from AWS to Salesforce](#upgrade-backfill)
+ [Post-migration: Monitoring EventBridge events](#upgrade-post-migration)
+ [Troubleshooting common migration issues](#upgrade-troubleshooting)
+ [Getting help](#upgrade-getting-help)

## Prerequisites
<a name="upgrade-prerequisites"></a>

### Migration order of operations
<a name="upgrade-migration-order"></a>

Partners often ask whether to migrate to the new Partner Central experience in the AWS Console or upgrade from Amazon S3 to API first. Here is the recommended approach:


**Migration order recommendations**  

| Scenario | Recommendation | 
| --- | --- | 
| Currently on Amazon S3, not yet on new Partner Central experience | Migrate to API first, then migrate to new Partner Central experience in parallel or after | 
| Currently on Amazon S3, already on new Partner Central experience | Proceed directly with API migration | 
| Already on API, not yet on new Partner Central experience | Migrate to new Partner Central experience at your convenience | 

**Account linking is the only hard prerequisite**  
Account linking is the only hard prerequisite for Amazon S3-to-API migration. Migrating to the new Partner Central experience is NOT required to start the API upgrade.

Key information:
+ Amazon S3-based integrations are deprecated and no longer available to new users.
+ Partners on Amazon S3 should plan to complete migration to the API as soon as possible to avoid service degradation.
+ Check the AWS Partner CRM Integration documentation for the latest timeline on Amazon S3 backend end-of-life.

### Ensure Partner Central is linked to an AWS account
<a name="upgrade-link-account"></a>

The Amazon S3-based connector authenticated using permissions to a managed Amazon S3 bucket in the AWS management account. The API-based connector instead authenticates via IAM roles on the partner's own linked AWS account to call the Partner Central APIs directly. This is why account linking is the hard technical prerequisite: without it, the connector has no way to reach the Partner Central APIs with the necessary permissions.

**Why this might be missing**  
When AWS released the Partner Central API for Selling in November 2024, account linking was introduced to allow partners to access these APIs programmatically. From connector version 3.0 (also November 2024), account linking became a requirement for API-based sync. Partners who set up their Amazon S3-based connector before this date would not have completed account linking.

Link your Partner Central account to your primary AWS account. Choose your account carefully from the start. While unlinking and re-linking a different account is possible, doing so creates data persistence issues and requires manual reconciliation efforts.

Account selection rules – the AWS account must be:
+ A paid account in good standing (not Free Tier)
+ Owned by the partner's company (not a distributor's account)
+ Have a billing address matching the partner's primary business location
+ NOT a sandbox, developer, personal, or management/payer account

**Account linking is permanent**  
Account linking is permanent after Partner Central migration to the AWS Console. All APN resources (ACE opportunities, history, multi-partner invitations) are permanently tied to this account. Choose carefully.

Resources:
+ [Account Linking section of the upgrade workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade/s3toapi#complete-prerequisites) on the AWS Workshops website
+ [Account linking prerequisites and IAM policy](https://docs.aws.amazon.com/partner-central/latest/getting-started/linking-prerequisites.html)
+ [CRM-specific account linking guide](https://docs.aws.amazon.com/partner-central/latest/crm/link-pc-mkt-accounts.html)
+ [Unlinking accounts](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central#Unlinking-AWS-Partner-Central-and-AWS-accounts) on the Partner Central website

### Optional: Migrate to the new Partner Central experience in AWS Console
<a name="upgrade-optional-pc-migration"></a>

This step is not required for the Amazon S3-to-API connector upgrade. Account linking alone provides the API-based functionality needed. However, migrating to the new Partner Central experience gives your team access to additional capabilities:
+ Partner Central Agents (Co-Sell Agent, Funding Agent, Autonomous Prospecting)
+ A centralized AWS Console experience for managing partner activities alongside your AWS resources
+ Improved visibility into opportunity lifecycle events directly in the console

**Solution ID format change**  
If you migrate to the new Partner Central experience and then create new solutions, those solutions will use the new `soln-*` format. The CRM Connector does not yet support this format; it requires the legacy `S-*` format for the `solutionOffered` field. Legacy solutions created before the migration retain the `S-*` format and continue to work.

See the [Partner Central migration guide](https://docs.aws.amazon.com/partner-central/latest/getting-started/migrating-to-partner-central.html) for more details.

### Pre-migration data cleanup
<a name="upgrade-pre-migration-cleanup"></a>

Before beginning the migration, ensure a clean cut from the Amazon S3-based integration. The most critical step is removing lingering scheduled jobs that can interfere with the API-based connector and the backfill process.

When you deactivate Amazon S3 schedules via the connector UI, the underlying Salesforce Scheduled Jobs (with APN prefix) remain in the system. If these are still present when you start backfill or enable API-based sync, both the old scheduler and the new connector may write to the same records simultaneously, causing duplicate opportunity creation or data conflicts.

**Deactivating in the UI is not sufficient**  
Deactivating schedules in the connector UI is not enough. You must also delete the underlying Scheduled Job entries in Salesforce Setup. See [Review and disable schedules for Amazon S3](#upgrade-disable-schedules) for the full step-by-step.

## Set up AWS infrastructure
<a name="upgrade-aws-infrastructure"></a>

This phase requires a Salesforce Administrator to work with an IT Cloud Admin to set up two new components: a Salesforce External Client App and AWS infrastructure components (EventBridge rules and IAM roles).

### Set up Salesforce External Client App
<a name="upgrade-sf-external-client-app"></a>

With the Amazon S3 version, both sync directions went through a shared Amazon S3 bucket per partner. The API version flips this for inbound updates – Partner Central now pushes events directly to your org in real-time via EventBridge. The External Client App enables an OAuth 2.0 Client Credentials flow so EventBridge can deliver notifications as they happen.

The Salesforce Administrator should follow the instructions in the [Set up External Client App on Salesforce](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/aws-infrastructure#task-1-:-set-up-external-client-app-on-salesforce) section of the workshop.

### Set up AWS components
<a name="upgrade-aws-components"></a>

The AWS infrastructure for the API version includes:
+ **EventBridge** for real-time event processing
+ **IAM roles** for secure authentication

These components replace the Amazon S3 bucket access model used in the previous version.

The IT Cloud Admin should deploy the CloudFormation template by following the instructions in the [Set up AWS Components](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/aws-infrastructure#task-2-:-set-up-aws-components) section of the workshop.

## Finalize setup and configuration within Salesforce
<a name="upgrade-finalize-salesforce"></a>

The remaining configuration is performed by a **Salesforce Administrator**. Complete activities in Sandbox first, test, then move to Production.

Install the latest version of the AWS Partner CRM Connector from the [Salesforce AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000IYf0nUAD&tab=e), then follow [the guided setup instructions](https://docs.aws.amazon.com/partner-central/latest/crm/p-c-api-integration.html) to configure the connector settings.

### Review and adjust your mappings
<a name="upgrade-adjust-mappings"></a>

With the Amazon S3 version, outbound sync relied on `Sync with AWS` and `Has Updates for AWS` fields. These are **no longer used** in the API-based integration.

With the API version, outbound sync is controlled through the **Enable Share with AWS Integration** setting in the AWS Partner CRM Connector custom settings (`Companion_App_Settings__c`). When enabled, ACE Opportunities are automatically shared with AWS whenever a qualifying update occurs.

Key points:
+ The **ACE Opportunity object** is recommended as a landing area – it matches the AWS opportunity data points in Partner Central and allows auto-mapping.
+ If you were already using the ACE Opportunity for your integration mapping, the underlying configuration does not change. However, the upgraded package introduces new fields not present in earlier versions.
+ Review any automations that reference the old Amazon S3-era fields (`Sync_with_AWS__c`, `Has_Updates_for_AWS__c`) to use the new equivalents.

The ACE Opportunity data model is available on [GitHub website](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/ACE-Data-Model.xlsx). For more details, see the [integration mapping section](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/mappings) of the workshop.

The latest connector version includes a **flow template** to help map your standard opportunity to the ACE opportunity. For more detail, see [flow templates](https://docs.aws.amazon.com/partner-central/latest/crm/flow-templates.html).

### Review and add required fields and buttons
<a name="upgrade-required-fields-buttons"></a>

The connector has introduced new fields and buttons since version 3.0\+. You must manually update your lightning record page layout.

Add the following buttons to the ACE Opportunity lightning record page:


**Buttons to add to the ACE Opportunity page**  

| Button | Purpose | 
| --- | --- | 
| Share with AWS | Manually pushes the opportunity to Partner Central via API. | 
| Refresh from AWS | Pulls the latest data from Partner Central into this ACE Opportunity record. | 
| Accept/Reject | Accept or reject AWS-referred opportunities. | 
| Associate/Disassociate | Link or unlink with AWS-approved Partner Solutions, Products, and Marketplace Offers. | 
| Assign | Reassign an opportunity to another user in your Partner Central account. | 

Remove the following legacy buttons from the ACE Opportunity lightning record page:


**Legacy buttons to remove**  

| Button | Reason | 
| --- | --- | 
| Send to AWS | Replaced by Share with AWS. | 
| Link Private Offer | Replaced by Associate/Disassociate. | 

Add the following list view buttons to the ACE Opportunity tab:
+ **Accept Opportunities** – Bulk-accept multiple AWS-referred opportunities.
+ **Assign Opportunities** – Bulk-reassign multiple opportunities.

For new fields, review [all fields added after Connector Version 3.0](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade#all-fields-added-after-connector-version-3.0).

### Review and disable schedules for Amazon S3
<a name="upgrade-disable-schedules"></a>

With the API-based approach, there is **no longer any need for scheduled jobs** – the integration runs in real time.

**To disable scheduled jobs**

1. Navigate to the **Schedules** tab within the AWS Partner CRM Connector app.

1. Choose **Deactivate All Jobs** and then choose **Deactivate** again.

Also **delete** the scheduled records. To remove remaining APN scheduled jobs from Setup:

**To remove APN scheduled jobs from Setup**

1. Navigate to **Setup**. Search for "Scheduled" and select **Scheduled Jobs**.

1. Review the list for any APN-related jobs. Choose **Del** to delete them.

**Keep CustomLogInteractionBatch running**  
Keep the `CustomLogInteractionBatch` job running (AppExchange App Analytics).

**Delete scheduled jobs, do not just deactivate**  
Do not leave jobs in a "deactivated but not deleted" state. Lingering jobs have caused duplicate opportunity creation when combined with API-based real-time sync.

## Cleanup
<a name="upgrade-cleanup"></a>

### Deactivate legacy validation rules
<a name="upgrade-deactivate-validation-rules"></a>

Several legacy validation rules must be deactivated and others must remain active. See [this section of the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/upgrade/upgrade#disable-validation) for the complete step-by-step and validation rules table.

Also ensure the following legacy flows have been **deactivated**:
+ Sync ACE Opportunity to Partner Central API
+ Private Offer Lookup
+ APN Synchronization Failure Notification
+ Updating Private Offer field On ACE Opportunity
+ Updating Ace opportunity field on Sync Log Detail Record
+ Unified Standard-ACE Opportunity Sync Flow (template)

Test your process before moving to production. See [testing from the settings](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/config-int#task-3-:-test-the-setup) and [troubleshooting](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/config-int#task-4-:-troubleshooting) in the workshop.

### Complete backfill of opportunities from AWS to Salesforce
<a name="upgrade-backfill"></a>

Run a backfill to ensure data matches between environments. The `awsapn__Last_Modified_Date__c` field on the ACE Opportunity needs to match the Last Modified Date in Partner Central for future updates to sync. The Amazon S3 integration did not populate this field, so opportunities migrating from Amazon S3 will have it empty – the backfill fills it in.

The backfill offers three modes:


**Backfill modes**  

| Mode | What it does | When to use | 
| --- | --- | --- | 
| Only refresh opportunities missing Last Modified Date | Updates only records where awsapn\_\_Last\_Modified\_Date\_\_c is empty | Recommended for Amazon S3-to-API migration | 
| Only refresh AWS opportunities which already exist in Salesforce | Updates all records that already have an APN CRM ID | Safe alternative for migration | 
| Refresh all AWS opportunities | Pulls entire Partner Central pipeline into Salesforce | Only use on fresh installations | 

**Before running the backfill:**

1. Confirm all APN scheduled jobs are deleted (not just deactivated).

1. Deactivate the "Sync ACE Opportunity to Partner Central API" flow if active.

1. Disable **Enable Share with AWS Integration** in the custom settings (`Companion_App_Settings__c`).

1. Complete the pre-migration data cleanup described in [Pre-migration data cleanup](#upgrade-pre-migration-cleanup).

**After backfill completes:**
+ Re-enable **Enable Share with AWS Integration** – this drives ongoing sync.
+ The "Sync ACE Opportunity to Partner Central API" flow does NOT need to be reactivated.
+ Verify a sample of records to confirm `awsapn__Last_Modified_Date__c` is populated.

For more details, see the [Backfill Opportunities from Partner Central](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/using-the-ace-integration/backfill) section of the workshop.

## Post-migration: Monitoring EventBridge events
<a name="upgrade-post-migration"></a>

After migrating, your Salesforce org receives real-time updates from Partner Central via EventBridge. To verify events are flowing:

1. **CloudWatch Metrics:** Navigate to CloudWatch > Metrics > EventBridge. Check Invocations and FailedInvocations for your API Destination.

1. **Salesforce Sync Logs:** On any ACE Opportunity, check the Sync Log related list for recent inbound entries.

1. **EventBridge Rule Monitoring:** Check the rule created by the CloudFormation template for recent matched events.


**Common EventBridge issues**  

| Symptom | Likely cause | Resolution | 
| --- | --- | --- | 
| No inbound updates in Salesforce | External Client App token expired | Re-authenticate the connected app; verify OAuth credentials in EventBridge API Destination | 
| Events stop after working | Salesforce session timeout | Check API Destination health in EventBridge; reconnect | 
| Partial updates (some fields missing) | Field mapping mismatch | Upgrade to latest connector version; verify field mappings | 

## Troubleshooting common migration issues
<a name="upgrade-troubleshooting"></a>


**Migration troubleshooting**  

| Error / Symptom | Root cause | Resolution | 
| --- | --- | --- | 
| FIELD\_CUSTOM\_VALIDATION\_EXCEPTION when clicking "Refresh from AWS" | Legacy validation rules not deactivated | Deactivate ACEOppNew\_PreventUpdatesWhenPOSubmitted and ACEOpp\_PreventUpdatesWhenPOSubmitted | 
| Duplicate opportunities | Lingering scheduled jobs or multiple integration users | Delete ALL APN scheduled jobs. Verify only one user holds APN Business Admin. | 
| Sync log records growing rapidly | Records failing validation retry every cycle | Identify failing records via sync logs. Fix missing required fields. | 
| Backfill exceeds storage limits | Too many records at once | Run in smaller batches. Monitor storage. | 
| "Refresh from AWS" shows stale data | awsapn\_\_Last\_Modified\_Date\_\_c mismatch | Re-run targeted backfill using "Only refresh opportunities missing Last Modified Date" | 
| Opportunities from Partner Central not appearing | EventBridge connection issue or auto-share disabled | Verify EventBridge API Destination health. Confirm "Enable Share with AWS Integration" is enabled. | 

## Getting help
<a name="upgrade-getting-help"></a>

If you encounter issues that the preceding steps cannot resolve:
+ **Open a support case:** [Partner Central → Support → Open New Case](https://partnercentral.awspartner.com/partnercentral2/s/newsupportcase) → CRM Integration
+ **Migration assistance:** For complex migrations (500\+ opportunities, custom integrations, or prior production incidents), request white-glove support through your Alliance Lead.