# Release notes

This section contains the release history for the AWS Partner Customer Relationship Management (CRM) Connector for Salesforce.

###### Topics

- [Version 3.19 (June 23, 2026)](#3.19 "#3.19")
- [Version 3.18 (April 16, 2026)](#3.18 "#3.18")
- [Version 3.17 (March 31, 2026)](#3.17 "#3.17")
- [Version 3.16 (February 26, 2026)](#3.16 "#3.16")
- [Version 3.15 (February 6, 2026)](#3.15 "#3.15")
- [Version 3.14 (December 17, 2025)](#3.14 "#3.14")
- [Version 3.13 (October 30, 2025)](#3.13 "#3.13")
- [Version 3.12 (September 16, 2025)](#3.12 "#3.12")
- [Version 3.11 (September 10, 2025)](#3.11 "#3.11")
- [Version 3.10 (August 6, 2025)](#3.10 "#3.10")
- [Version 3.8 (April 17, 2025)](#3.8 "#3.8")
- [Version 3.6 (March 18, 2025)](#3.6 "#3.6")
- [Version 3.5 (January 22, 2025)](#3.5 "#3.5")
- [Version 3.1 (December 2, 2024)](#3.1 "#3.1")
- [Version 3.0 (November 14, 2024)](#version-3.0-november-14-2024 "#version-3.0-november-14-2024")
- [Version 2.2 (April 24, 2024)](#2.2 "#2.2")
- [Version 2.1 (April 18, 2024)](#2.1 "#2.1")
- [Version 2.0 (November 29, 2023)](#2.0 "#2.0")
- [Version 1.7 (October 12, 2022)](#1.7 "#1.7")
- [Version 1.6 (January 13, 2023)](#1.6 "#1.6")
- [Version 1.5 (January 13, 2023)](#1.5 "#1.5")
- [Version 1.4 (December 7, 2022)](#1.4 "#1.4")

## Version 3.19 (June 23, 2026)

AWS Partner CRM Connector version 3.19 contains the following feature and
bug fix.

### New features

**AWS next steps visibility on opportunities**

- The **ACE Opportunity** page now includes a read-only **AWS Next Step** field. This field shows the AWS seller's next steps that AWS Partner Central provides. It appears separately from your own **Next Step** field. You no longer need to leave Salesforce to see what AWS recommends on an opportunity.

### Bug fixes

- Fixed an issue where the connector created an opportunity on the AWS side but did not save the identifier back to Salesforce. This left the record unlinked, so you could not refresh, submit, or manage it. The connector now always writes the AWS opportunity identifier back to Salesforce after it creates the opportunity.

## Version 3.18 (April 16, 2026)

AWS Partner CRM Connector version 3.18 contains the following bug fix and
known issue.

### Bug fixes

- Fixed an issue where duplicate ACE Opportunity records were intermittently created when the **Solution offered** field was populated during opportunity creation, either via flow or manual entry. The duplicate record's name was set to the original record's ID, and the original record was not linked to AWS Partner Central. This issue affected connector versions 3.14–3.17

### Known issues

**Validation rules remain active after upgrading from connector versions 3.14–3.17**

The validation rules `ACEOppNew_PreventUpdatesWhenPOSubmitted`, `ACEOpp_PreventUpdatesWhenPOSubmitted`, and `ACEOppNew_MandatorySolutionOffered` were originally shipped as active in a previous connector version. These rules were changed to inactive in the package source, but Salesforce managed package upgrades do not overwrite the active property on validation rules. This is expected Salesforce behavior — the `active` property is classified as subscriber-and-developer editable, meaning it is set only on initial install and is not updated during upgrades.

Any customer who installed the connector when these validation rules were active will still have them active after upgrading. This can cause `FIELD_CUSTOM_VALIDATION_EXCEPTION` errors that block updates and **Refresh from AWS** on ACE Opportunity records when ownership is Partner Referral and status is Submitted.

To resolve this issue, manually deactivate the validation rules in your Salesforce organization:

1. Navigate to **Setup** → **Object Manager** → **ACE Opportunity** → **Validation Rules**
2. Locate `ACEOppNew_PreventUpdatesWhenPOSubmitted`, `ACEOpp_PreventUpdatesWhenPOSubmitted`, and `ACEOppNew_MandatorySolutionOffered`
3. Edit each rule and uncheck **Active**, then save

## Version 3.17 (March 31, 2026)

AWS Partner CRM Connector version 3.17 contains the following features and
improvements.

### New features

**EUR currency support for European Sovereign Cloud opportunities**

- Partners can now create and manage opportunities using EUR currency for the European Sovereign Cloud (ESC) region
- New **AWS Partition** field on the **ACE Opportunity** page to designate ESC opportunities
- Currency fields automatically default to USD when no currency is specified
- When the currency code is set to EUR, the AWS partition field value must be set to `aws-eusc`. EUR currency is only valid for the `aws-eusc` partition and cannot be used with any other partition

**Backfill tool — targeted backfill for S3-to-API migration**

- New sync mode option: `Only refresh opportunities missing Last Modified Date`
- Partners migrating from S3-based to API-based integrations can selectively backfill legacy opportunities without refreshing their entire pipeline. Deactivate all S3-based scheduled jobs before running the backfill (**Setup** → **Scheduled Jobs** → Delete jobs with `APN` prefix)
- Added confirmation step to ensure S3-based scheduled jobs are deactivated before running backfill

### Bug fixes

- Fixed an issue where adding a solution or AWS product value using the field (instead of the **Associate** button) and then submitting the opportunity would fail validation, and the solution value would disappear on page refresh
- Fixed an issue where certain picklist values containing special dash characters in **Closed Lost Reason** and **Sub Use Case** fields caused API errors when submitting opportunities. Existing data is automatically corrected on upgrade
- Updated the `Unified Standard-ACE Sync Flow` template defaults: changed `Partner_Primary_Need_From_AWS` from "Do Not Need Support from AWS Sales Rep" to "Co-Sell - Architectural Validation", and added `solutionOffered` and `otherSolutionOffered` fields with default value "Other" to support solution tracking on ACE Opportunities
- Relaxed the validation rule that prevented updates to ACE Opportunity records when ownership is Partner Referral and the opportunity status is Submitted. This was incorrectly blocking the connector from updating records during the sync process

## Version 3.16 (February 26, 2026)

AWS Partner CRM Connector version 3.16 contains the following features and
improvements.

### Bug fixes

- Fixed an issue where solution fields were not persisting during opportunity creation. In version 3.15, when partners created opportunities with solution fields populated, the solutions were not being associated with the opportunity in AWS Partner Central. The connector now properly chains the CreateOpportunity and AssociateOpportunity API calls to ensure solutions are correctly associated during opportunity creation
- Fixed a permission gap where the **Source Opportunity** field was missing edit permissions in the **APN Business Admin** permission set. This field, added in version 3.10 for the `Unified Standard-ACE Opportunity Sync Flow`, now has proper read and edit access, enabling business administrators to use automations that create ACE Opportunity records from Standard Opportunity records
- Fixed an issue where postal code was incorrectly enforced as a mandatory field for all countries, including those without postal code systems (such as United Arab Emirates, Hong Kong, and Bonaire). The postal code field is now optional, aligning with the AWS Partner Central API specification and allowing partners to create opportunities for customers in countries that do not use postal codes

## Version 3.15 (February 6, 2026)

AWS Partner CRM Connector version 3.15 contains the following features and
improvements.

### AWS Partner Central API

**Automatic AWS data sharing enhancement**

- Enhanced automatic record synchronization with AWS to work seamlessly on both opportunity creation and updates
- Eliminates the need for the `Sync ACE Opportunity to Partner Central API` flow for data sharing

**Refresh from AWS capabilities**

- Added ability to refresh opportunity data directly from AWS Partner Central without the need for events
- Allows partners to pull the latest updates from AWS Partner Central on demand through a button on the **ACE Opportunity** page layout
- Ensures data consistency between Salesforce and AWS Partner Central

### Bug fixes

- Fixed an issue where opportunities with "Other" specified in the **Industry** field were not being included in the API payload when syncing to AWS Partner Central, causing opportunities to remain stuck in draft status
- Fixed a scientific notation formatting issue in currency and revenue fields that was causing API validation failures for large monetary values

## Version 3.14 (December 17, 2025)

AWS Partner CRM Connector version 3.14 contains the following features and
improvements.

### AWS Partner Central API

**Opportunity data backfill**

- Added dedicated **backfill** feature that allows partners to initiate data synchronization directly from the connector interface for all existing opportunities from AWS Partner Central to Salesforce
- Implemented user defined criteria for opportunity selection based on stages and other filtering options

**Opportunity association enhancement**

- Consolidated the four-field approach into three clear, searchable fields with consistent behavior
- Implemented searchable dropdown fields with type-ahead functionality for **Solutions**, **AWS Products**, and **AWS Marketplace offer**
- Improved **AWS Products** field to display friendly names (e.g. “AWS Amplify”) while maintaining correct API identifiers

**Opportunity owner assignment on creation**

- Added support for setting opportunity owner during opportunity creation through the CreateOpportunity API
- Implemented proper mapping of OpportunityTeam members with BusinessTitle “OpportunityOwner”

### Bug fixes

- Fixed validation issue on OpportunityTeamMember email validation to share payload with AWS only when First Name, Last Name or Phone Number is provided
- Updated National Security field logic to share selected picklist values correctly
- Updated tooltips for Partner Account Manager fields

## Version 3.13 (October 30, 2025)

AWS Partner CRM Connector version 3.13 contains the following features and
improvements.

### AWS Partner Central API

**Bulk accept and bulk assign opportunities**

- Added ability to **accept** or **assign** multiple ACE Opportunities simultaneously, improving efficiency in opportunity management

**Opportunity synchronization logs**

- Users of the AWS Partner Central API integration can now view corresponding synchronization logs directly within the ACE Opportunity object. This feature provides visibility into the synchronization process for each opportunity

### Bug fixes

- Resolved an issue where the Customer DUNS number field (`customerDuns`) was rejected during opportunity submission due to data type mismatch
- Increased the error message field (`awsapn__Error_Message__c`) size from 32KB to 128KB in sync log details to prevent truncation of error messages and avoid disruption to Apex job processing during high-volume synchronization errors
- Fixed an issue where opportunities would appear as submitted but remain stuck in draft status when postal or zip codes were in invalid format. The connector now surfaces async API validation errors, allowing partners to correct postal or zip code formatting before submitting to AWS
- Resolved an issue where opportunities with "Other" specified in the Solution Offering field would remain stuck in Draft status instead of progressing to Submitted. The connector now properly handles "Other" solution values and correctly parses API responses to allow opportunity progression through the ACE validation process. Partners can now also associate valid solutions even when they have "Other" in the other solution description field

## Version 3.12 (September 16, 2025)

AWS Partner CRM Connector version 3.12 contains the following features and
improvements.

### Bug fixes

- Set the `Unified_Standard_ACE_Sync` flow template to be in a **draft** state as opposed to an active state. Some customers were experiencing installation errors with the flow template in an active state.

## Version 3.11 (September 10, 2025)

AWS Partner CRM Connector version 3.11 contains the following features and
improvements.

### AWS Partner Central API

**Enhanced logging**

- Expanded detailed logging capabilities for AWS Partner Central API integration and opportunity synchronization processes
- Added additional troubleshooting information for opportunity synchronization processes

### Bug fixes

- Fixed an issue preventing disassociation of solutions/offers/services from the Solution Offered field
- Increased maximum number of Solution Listings that can be synchronized from AWS Partner Central from 50 to 100
- Fixed visibility issues for solutions in Solution Offerings when solutions are in a 'delete' state
- Resolved an issue causing duplicate opportunities to appear in Salesforce when changes were made in AWS Partner Central
- Fixed display of full names in AWS Partner Success Manager and AWS ISV Success Manager fields in the ACE object

## Version 3.10 (August 6, 2025)

AWS Partner CRM Connector version 3.10 contains the following features and
improvements.

### AWS Partner Central API

**Automatic AWS data sharing**

- New **Enable Share with AWS Integration** setting in AWS Partner Central custom settings
- Automatic record syncing with AWS when updates occur
- Eliminates need for manual **Share with AWS** button clicks
- Seamless data flow to AWS on record updates

**Simplified entity association**

- Built-in functionality to associate offers and products on their respective field without having to click on **Associate** or **Disassociate**
- Automatic backend API call handling based on selection

**Streamlined invitation management**

- Accept/reject invitations directly from **Partner acceptance status** field dropdown
- Automatic backend API call handling based on selection

**Automation improvements - New Unified Standard-ACE Opportunity Sync flow template**

- Enables automated synchronization between standard Salesforce opportunities and ACE opportunities
- Supports co-sell opportunity sharing when using the CRM connector
- Includes pre-configured field mappings for standard opportunity fields
- Handles both creation and updates of ACE opportunities
- Features automatic state/country mapping and default value handling

## Version 3.8 (April 17, 2025)

AWS Partner CRM Connector version 3.8 contains the following features and
improvements.

### Bug fixes

- Fixed an issue where the **APN CRM ID** was not getting updated on the Opportunity post synchronization.
- Fixed an issue when trying to refresh Marketplace products where a seller had more than 50 listed products.
- Fixed an issue where the AWS Sales Rep and AWS Account Manager fields in the ACE object were not displaying the full name.

## Version 3.6 (March 18, 2025)

AWS Partner CRM Connector version 3.6 contains the following features and
improvements.

### AWS Marketplace

- Added support for 8 decimal places (increased from 3) in
  pay-as-you-go pricing for software as a service (SaaS) products, which aligns with AWS Marketplace
  pricing standards.

### Bug fixes

- Partners can now create opportunities directly in Partner
  Central. These opportunities automatically sync with the partner's
  Salesforce organization via AWS Partner CRM connector. This improves the
  referral process and enhances collaborations between partners and
  AWS.
- Fixed an issue where an opportunity sync fails with
  `NUMBER_VALUE` and can't be converted to a string when
  SaaS revenue recognition program (SRRP) fields are updated.
- Resolved data sharing issue to prevent AWS referrals from
  being incorrectly processed as partner opportunities during APN
  synchronization.
- Fixed `ReviewStatus` field from changing to null on
  an approved opportunity after updating an allowed field.
- Implemented new field mapping for `Next Step
 History` to accommodate larger data volumes and
  prevent sync failures.
- Resolved ACE opportunity activation flow issues by implementing
  proper update logic for `APN CRM Unique Identifier` field
  in an ACE opportunity record.
- Updated and corrected guided setup instructions for a better
  user experience.

###### Note

If you upgrade to version 3.6, you must map the `Next Step
 History` field on the **ACE Mappings**
tab.

## Version 3.5 (January 22, 2025)

AWS Partner CRM Connector version 3.5 contains the following features and
improvements.

### AWS Partner Central API

- You can now enable sandbox catalog using the **PC API Sandbox Enabled** checkbox in **Custom Settings**, **AWS Partner CRM Connector Settings**.
- Updated product catalog.

### AWS Marketplace

- You can now import details of resale authorizations created outside the CRM connector.
- Added support to view up to 8 decimal points, where applicable.

### Bug fixes

- Fixed issue with a new installation of CRM connector Version 3.1, sync failure reporting with error message `Field Level Security error on field: awspn_Campaign name_new_c`.
- Fixed issue with duplicate AWS Markeplace product names causing upsert failure.
- Fixed issue preventing the **ACE opportunity** tab from being set as the default view for the ACE permission sets.

## Version 3.1 (December 2, 2024)

AWS Partner CRM Connector version 3.1 contains the following features and
improvements.

### Bug fixes

- Fixed the production URL for AWS Partner Central API.
- Fixed issues with change to Engagement Invitation Payload.

## Version 3.0 (November 14, 2024)

AWS Partner CRM connector 3.0 contains the following
features and improvements:

### Core features

###### Multi-object mapping

- Partners can now map fields from multiple Salesforce objects, including lookup and
  master-detail relationships, to the APN opportunity and lead schemas.
- Improved UI for mapping fields, including expandable views for
  lookup fields.
- Support for up to two levels of object relationships in a single mapping.

### ACE CRM Integration features

###### AWS Partner Central API Support

- The ACE integration user is not required for AWS Partner Central
  integrations
- Inbound and outbound synchronization schedules between Salesforce
  and AWS Partner Network (APN) are no longer required.
- The AWS Partner CRM connector handles synchronous errors.

###### AWS Partner Central API support for AWS originated opportunities (AO) and partner-originated opportunities

- Partners can use the **Share with AWS**
  button to create and update opportunities.
- Partners can use the **Approval Status** button to accept or reject AWS referred
  opportunities.
- Partners can use the **Associate or Disassociate** buttons to associate or disassociate opportunities with
  Partner Solutions, AWS Products, and AWS Marketplace Offers throughout the opportunity
  lifecycle.
- Partners can use the **Assign** button to reassign opportunities
  to other users in their Partner Central account.
- Partners can use the **Solution offering** tab to view a list of available solutions.
- Partners can view the events on the **AWS Marketplace
  Notification** tab, such as **Opportunity
  Created**, **Opportunity Updated**, or
  **Engagement Invitation Created**.
- Three new fields added for opportunities:

  - `Opportunity Engagement Invitation ARN`
  - `Opportunity Type`
  - `Visibility`

### Bug fixes

- Fixed an issue where the connector, upon receiving inbound data,
  overrides the account associated with opportunities to a
  default account provided in the custom settings, leading to
  internal Salesforce conflicts and validation errors
- Fixed an issue where the connector encountered errors in inbound and
  outbound sync logs due to an invalid `SalesActivity` field value of
  `Finalized Deployment Needs`.
- Fixed an issue when trying to refresh shared resale authorizations.

## Version 2.2 (April 24, 2024)

AWS Partner CRM connector version 2.2 contains the following features and
improvements.

### Core features

Enhancements to the existing resale authorization feature to support non-legacy products.

## Version 2.1 (April 18, 2024)

AWS Partner CRM connector version 2.1 contains the following features and
improvements.

### Core features

Channel Partners can create a synchronization schedule for shared resale authorizations.

### AWS Marketplace integration for ISV sellers and Channel Partners

- You can modify the usage duration on released offers for eligible products.
- Support for future dated agreements (FDA) for private offers.
- You can import details of private offers created outside of the CRM connector.
- You can save private offers and resale authorizations as drafts.
- You can retrieve and view agreements for private offers and public offers.
- You can create agreement-based offers across multiple seller accounts for SaaS Contract
  products and SaaS Contract products with consumption accounts.

### ACE CRM integration

- Enhanced Salesforce Lightning record form for AWS delivered ACE opportunity objects.
- You can surface sync log detail records per opportunity on AWS delivered ACE opportunity objects.
- You can link available AWS Marketplace private offers to an opportunity on the AWS delivered ACE opportunity object.

## Version 2.0 (November 29, 2023)

### Core features

- Modularized Application–single SF AppExchange app for both ACE CRM Integration and AWS Marketplace Seller integration features

### APN Customer Engagements (ACE) integration

- Support for new data model (v14) with the ACE CRM integration.
- Creates custom objects for ACE opportunities and leads which contains all the attributes/values as defined by the ACE CRM integration with new data model validations on the custom opportunity objects.
- One-click automapping capability for new ACE custom objects to expedite mapping with installed custom objects for opportunities and leads.
- Fix for mapping missing attributes on opportunities.
- Fix for associating AWS opportunities to an account if using a standard opportunity for mapping.

### AWS Marketplace integration

- As an ISV seller:

  - Synchronize available MP Products into Salesforce organization.
  - Create, view and manage ISV Private Offers on SaaS, AMI, and Container products.
  - Cancel and modify private offers.
  - Clone private offers to create new offers.
  - Create resale authorizations on SaaS, AMI, and container products.
  - Cancel and modify resale authorizations.
  - Clone resale authorizations.
  - Receive notifications when buyers subscribe to private offers.
  - View dashboard of private offers and shared resale authorizations created through the
    connector.

- As an AWS Channel Partner:

  - Synchronize and view shared resale authorizations created by the ISV seller.
  - Create and manage AWS Channel Partner private offers for SaaS, AMI, and container products from shared resale authorizations.

## Version 1.7 (October 12, 2022)

### Change log

**User interface**

- Add AWS Partner Network review comments optional field to mapping screen.
- Move the help section to the **Guided setup** page.

**Bug fixes**

- Fix an issue where incorrect payload was being displayed in `synclog` detail
  source record in partial failure case.
- Fix an issue where partners already updated the partner CRM unique identifiers in ACE to
  auto correct based on target object in organization.
- Fix an issue to stop opportunity updates being sent that have not yet been approved after
  the initial create request to AWS Partner. This is to prevent validation error responses
  being received back from AWS Partner due to the opportunity not being in approved
  status.

**Known issues**

Not applicable.

## Version 1.6 (January 13, 2023)

### Change log

**User interface**

- Add component to allow partners to raise support cases through AWS Partner Central. This is
  available on the **Guided Setup** page in the app.
- Administrators can correct data received in inbound payload to fix incorrect picklist values so they can be processed.

**Sync log cleanup**

Old sync log records are cleaned up automatically based on the application custom setting **Sync Log Retention**. This feature allows partners to configure how long they want to retain inbound and outbound synchronization log records.

**Bug fixes**

- Update validation message when an unmapped picklist value is present in inbound payload
  to indicate the incorrect value.
- Update outbound job filter to utilize configured retry count and retry days in
  application custom setting to auto retry the transaction once data is corrected, until
  number of retries is exceeded.

**Known issues**

Not applicable.

## Version 1.5 (January 13, 2023)

### Change log

**User interface**

- Update labels on scheduling modal.
- Update validation error messages on scheduling screen to provide more context to users on
  scheduling failures.
- Update the title of the application in all references with "AWS Partner CRM connector".
- **Opportunity/lead** page

  - Update **Eligible to Sync with APN** field label to **Has
    Updates for AWS**.
  - Update **Sync with Partner Central** field label to **Sync
    with AWS**.

- **Guided Setup** page

  - Update **Enter Authentication details** field label to **Set
    up the APN AWS connection**.
  - Update **SPMS** field label to **Partner ID**.
  - Update **Map APN AWS** fields to **Salesforce**
    fields.

- **Mapping** page

  - Update **ACE pipeline manager** fields to **AWS**
    fields.
  - Update **Enable APN updates** fields to **Enable Inbound
    Updates** fields.

- **Sync Logs** page

  - Replace references to "APN" with "AWS" (direction).
  - Update the following sync log purpose fields labels: **Inbound
    Orchestration** to **Inbound File Retrieval**,
    **Inbound Orchestration—Record Retrieval** to
    **Inbound Record Retrieval**, and **Outbound
    Orchestration** to **Outbound File Retrieval**.

**Instantaneous synchronization**

Administrators can initiate a specific outbound synchronization for a single record
through an added quick action. The quick action **Send to AWS** was
added to the standard opportunity and lead object for reference. It can be added to any
integrated standard or custom object to provide the option to immediately invoke the
synchronization for a single record outside of the scheduled jobs.

**Bug fixes**

- Fix an issue on the sync log that showed an incorrect FLS exception error.
- Fix an issue on the Lead object when the `campaignMemberStatus` field is
  mapped.
- Fix a mapping issue where the `awsFieldEngagement` and
  `awsAccountId` fields were being excluded from the outbound mapping, when
  mapped.
- Update bundled dashboards from dynamic to static so they don't use the installed organization's
  limit for dynamic dashboards.

**Known issues**

Not applicable.

## Version 1.4 (December 7, 2022)

### Change log

**User interface**

- Simplify interface for sync logs.
- Simplify interface for mapping modal.
- Add confirmation modal to reset button on **Mapping** screen.
- Disable **Next** option on picklist mapping until all fields are completed.
- Add help text to tab titles in mapping modal.
- Update app label from **APN CRM Administration** to **AWS Partner CRM
  connector**.

**Reports and dashboards**

Add new reports and dashboards for tracking sync log statuses.

**Flow template**

Add flow template to the package for setting custom push notification to business
administrators on sync log errors.

**Bug fixes**

- Fix issue on date offset with UTC in mapping.
- Fix an issue when a partially processed sync log was picked for reprocessing, when
  encountering an error, the status on the sync log doesn’t change to
  **Error**.
- Update eligible `to sync` formula on standard opportunity and lead.
- Hide read-only fields.
- Update to loading spinners.
- Update label for modal subtitle.
- Retain `apnValues_ on _tab3` in the mapping modal.
- Update the **Edit** option so it takes the user to the current
  page.
- Disable tab selection unless in `read-only` mode.
- Disable `field required` error when optional.
- Change modal checkmarks to green.
- Add mapping tab components and utilities.
- Add new dashboard and dashboard folder for sync logs.
- Remove permission for deprecated custom report tab.

**Known issues**

Error when mapping the `CampaignMemberStatus` on the Lead object. Currently, AWS Partners can skip mapping this non-mandatory field when mapping leads. Fix will be in the next version.
