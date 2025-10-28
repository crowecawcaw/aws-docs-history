# AWS Partner CRM connector FAQ

The topics in this section help answer frequently asked questions about AWS Partner CRM integration and using the CRM connector.

###### Note

The questions and answers in this FAQ assume that you use Salesforce. For more information
about using Salesforce, see the [Salesforce
help](https://help.salesforce.com/s/ "https://help.salesforce.com/s/").

###### Topics

- [General questions](#general-questions "#general-questions")
- [Setup issues](#setup-issues "#setup-issues")
- [Mapping issues](#mapping-issues "#mapping-issues")
- [Synchronization and validation issues](#synchronization-validation "#synchronization-validation")

## General questions

Expand the following sections for more information about using the AWS Partner CRM connector.

Contact your partner development manager (PDM) or your AWS point of contact. Your PDM will verify eligibility, help set up the IAM user required for authentication and
submit the request internally to set up the Amazon S3 bucket required for you to exchange files. After you have access to the Amazon S3 bucket, you can install the connector and set up the integration
by following the instructions in the user guide.

If you already have an AWS Partner ACE integration, [install the connector from the Salesforce AppExchange](install-connector.md "install-connector.md"), then follow the instructions in
[Configuring the connector for a CRM with Amazon S3 integration](s3-config.md "s3-config.md").

Version 3 provides real-time opportunity updates and eliminates the need for schedules. It also provides a set of buttons that enable partners to accept or reject leads and opportunities, update them,
and send them to AWS. For information about installing version 3, refer to [Available features](crm-connector-feature-list.md "crm-connector-feature-list.md") earlier in this guide.

Version 3.0.0. You can find it in the Salesforce App Exchange.

The AWS Partner CRM connector is available for free from the Salesforce App Exchange. It provides the following integration options:

- A Partner Central API-based integration where the AWS service calls are free.
- An Amazon S3-based integration where AWS hosts and bears the costs of an Amazon S3 bucket.

###### Note

You can only use this option if you created a CRM with Amazon S3 integration prior to 2024.
Amazon EventBridge is also free because the events come from an AWS service. However, you may incur additional charges on your AWS account if you forward the
events to other event buses from the primary event listener for additional processing.

For more information about the AWS Partner CRM connector, refer to [CRM connector overview](connector-overview.md "connector-overview.md"). For more information about EventBridge, see
[What is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the _Amazon EventBridge User Guide_.

For a list of the features provided by the AWS Partner CRM connector, refer to
[Partner Central API features](crm-connector-feature-list.md#partner-central-api-features "crm-connector-feature-list.md#partner-central-api-features"), earlier in this guide.

Yes. Use the `AccessKey` and `SecretAccessKey` credentials of the IAM user from the
[CRM Integration onboarding](https://partnercentral.awspartner.com/partnercentral2/s/acecrmintegration "https://partnercentral.awspartner.com/partnercentral2/s/acecrmintegration") request.

Remember, files are no longer be transferred using the Amazon S3 bucket once you port the integration over to the API based approach. However, leads
are still shared using the Amazon S3 bucket based integration.

The AWS Partner CRM connector is designed for use with the Salesforce Lightning version, so version 2 may not function as intended.

We recommend that you install the package on production systems only after thoroughly testing in a sandbox environment.

AWS Partner CRM connector is designed for the following user personas:

- Salesforce administrators or referral administrators who set up the connector.
- Sales operations users who select, accept, and update opportunities and leads.
  Yes. AWS Partners that have an existing integration with ACE can move to the connector. Because the connector uses the same Amazon S3 bucket in the back end, complete the following steps:

1. Disconnect your custom app or solution from the Amazon S3 bucket.
2. Sign in to the AWS account to set up the integration. Obtain or create a secret key and access key for the IAM user that is authorized to access the Amazon S3 bucket.
   The user name must follow this format: `apn-ace-{partnerName}-AccessUser-prod`. For more information, see
   [Manage access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey")
   in the _AWS Identity and Access Management User Guide_.

###### Note

If you're unable to find the AWS account, submit a [support request](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md"). 3. To configure the connector to point to the Amazon S3 bucket, choose **Setup**, then **Named Credentials**, then **APN API connection**. 4. Submit a [support request](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") to delete existing objects in the Amazon S3 bucket before scheduling a job in the connector.

###### Important

You must complete this step before completing the integration and setting a synchronization schedule. 5. If the target object is different from the existing object, conduct a data backfill for your existing leads and opportunities.
For more information, refer to the CRM integration _Production setup and backfill guide_.

###### Note

During the integration switchover, all user updates queue in the `Outbound` folder of the Amazon S3 bucket. After the integration is live, the user-update records are synced.
The Salesforce application has gone through Salesforce and internal AWS security
reviews. The Salesforce security review scans include the following threats:

- Salesforce Object Query Language (SOQL) and SQL injection
- Cross-site scripting
- Non-secure authentication and access control protocols
- Record-sharing violations and other vulnerabilities specific to the Salesforce platform
  The code review uses the [Salesforce
  Code Analyzer](https://forcedotcom.github.io/sfdx-scanner/ "https://forcedotcom.github.io/sfdx-scanner/") to inspect Salesforce code. Salesforce Code Analyzer uses multiple
  code analysis engines, including PMD, ESLint, and RetireJS. It identifies a number of
  potential problems, from inconsistent naming to security vulnerabilities.

For more information on the review process, refer to
[AppExchange Security Review](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/security_review_overview.htm "https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/security_review_overview.htm") in the Salesforce documentation.

###### Note

Partner applications are non-Salesforce.com applications as defined in the Salesforce Main Services Agreement. For more information, refer to the Salesforce
[Agreements and Terms](https://www.salesforce.com/company/legal/agreements/ "https://www.salesforce.com/company/legal/agreements/").

Notwithstanding any security requirements set forth herein or any security review of a partner application that may occur, Salesforce makes no guarantees regarding the quality or
security of any partner application, and customers are solely responsible for evaluating the quality, security, and functionality of partner applications to determine their adequacy
and appropriateness for customers' installation and use.

While we cannot share specifically what our internal security audit covers, it is geared towards the native AWS components of the integration architecture, to
which the Salesforce app connects and covers a number of different threat modeling scenarios such as man-in-the-middle attacks, distributed denial-of-service mitigations,
and encryption standards. For more information, submit a support request.

## Setup issues

Expand the following sections for information about fixing set up issues with the AWS Partner CRM connector.

For information about the prerequisites for using the CRM connector, see the [Integration prerequisites](crm-integration-setting-up.md "crm-integration-setting-up.md") earlier in this guide.

Follow these steps listed in [Setting up named credentials](guided-setup-apis.md#api-named-credentials "guided-setup-apis.md#api-named-credentials") later in this guide.

Moving from version 2 to version 3 of AWS Partner CRM connector has no immediate implications. All the functionality is backward compatible and works without interruptions.

For opportunity management, if you plan to use the new features, you
may need to change some of your sales processes. You should evaluate
the following changes and create a transition plan.

- Version 3 shares opportunities with AWS in real time. You no longer need to create schedules for sending opportunities to AWS.
  Opportunity owners on a partner's Salesforce instance must manually
  send data to AWS. Salesforce users need permissions
  to push opportunities to AWS.
- If you plan to use multi-object mapping, you need a transition plan for getting and posting data from new
  objects in your Salesforce instance. As a Salesforce
  admin, you should be aware of consequences of moving from object
  mapping with all fields mapped in a single object versus fields from a
  different object mapped to a single object.
  Yes. You _must_ complete the following items:

- In the general prerequisites,
  [Linking your AWS Partner Central and AWS Marketplace accounts](link-pc-mkt-accounts.md "link-pc-mkt-accounts.md").
- Create named credentials for the new Partner Central APIs. For more information, refer to [Setting up named credentials](guided-setup-apis.md#api-named-credentials "guided-setup-apis.md#api-named-credentials") earlier in this guide.
  No. The connector is designed for use with the Salesforce Lightning version, and the app may not function as intended without it.

NEED TO VALIDATE - AWS Partner CRM Connector is managed package. You can create custom schedule invocation with third party apps against the
`InboundSyncScheduler` and `OutboundSyncScheduler` apex classes. Note - With new API based integration, these classes might not work.

## Mapping issues

Expand the following sections as needed for information about fixing object-mapping issues with the AWS Partner CRM connector.

For version 3, partners can select the fields of referenced objects one level down
while mapping. For example, if your Salesforce standard opportunity object has an internal
reference pointing to an account object and a custom AWS sales object, you can select
the standard opportunity as the parent object, then map fields from the account and sales
objects.

No. Instead, you map multiple fields from a selected object.

Version 3 uses the `APNCrmUniqueIdentifier` field to reference a single parent object for mapping.
The field contains the AWS record ID. After querying the parent object, the values of all other related objects are marshalled or
unmarshalled based on the reference link from the parent object.

Version 3 of the connector works on the version 2 data model. For complete payload information, see the [AWS Partner CRM Integration Samples](https://github.com/aws-samples/partner-crm-integration-samples "https://github.com/aws-samples/partner-crm-integration-samples") on GitHub.

No. The package comes with the ACE custom opportunity object, which includes the field
types and validation rules that run against the [standard ACE payload](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Outbound-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Outbound-Sample.json"). You can copy the validation rules and fields from an ACE
custom opportunity object in your standard object. `NEED TO
 VALIDATE` - With multi-object mapping, you can try adding a reference to an
ACE opportunity object inside your standard opportunity object, then copying data into
those fields using triggers to kick off validations.

The **Sync with AWS** checkbox determines whether a lead or
opportunity synchronizes with AWS when the next scheduled job runs.
The **Sync with Partner Central** field is included with the app for
standard opportunities and leads. If your target object is a custom object, you must map
the **Sync with AWS** field to a custom non-formula boolean field in
each object.

The **Has Updates for AWS** formula field determines if a record is
sent to AWS Partner in the next scheduled job. **Has Updates for
AWS** is set to **True** when the following conditions are
true:

- **Last Modified Date** of the record is later than **Last APN Sync Date**.
- **Last Modified User** is not the user that scheduled the integration jobs.
  You must use the **Text** data type with a length of 18 characters to match the length of the
  **API** field.

- Configuration: Text (18) (External ID) (Unique Case Insensitive)
  The app uses the following checkpoints:

- **Sync to AWS** must be checked in order to sync with
  AWS.
- **Has Update to AWS** must be checked in order to sync with
  AWS.
- The user persona for creating the scheduling job must be different from the user
  persona for used to create and update leads or opportunities.
- If the previous checks are true but the outbound batch still doesn't run, check the
  AWS Partner sync logs and add the **outbound IDs** column. Confirm that the
  sync log contains the ID of the opportunity that you want to push. If the sync log is
  stuck in the **API Success** state, delete the sync log record and
  try again.

When **Expected Monthly AWS Revenue** is not an integer, such as
`1041.67` instead of `1041`, the mismatch in data type causes
a processing error. To resolve this, delete the sync log stuck in the
**API Success** state and correct the data before the next job
run.
In Salesforce, you can create or update the formula field to add the dependency from the status or stage
fields for a specific value. For example, you can set **Has Updates for
AWS** to **True**. You can use the included field on the
opportunity as a reference. The following example shows how:

```
IF(
   OR(
      AND
      (
         OR(LastModifiedDate > awsapn_Last_APN_Sync_Date_c,LastModifiedDate = awsapn_Last_APN_Sync_Date_c),
         awsapn_Sync_with_Partner_Central_c,
         NOT(ISNULL(awsapn_Last_APN_Sync_Date_c))
      ),
      AND(ISNULL(awsapn_Last_APN_Sync_Date_c),awsapn_Sync_with_Partner_Central_c)
   )
   , true , false
)
```

Yes. You must map all mandatory fields in order to schedule an inbound or outbound integration job.

We recommend reviewing the fields that you currently enter in Partner Central to determine
the most relevant fields (in addition to the required fields). For a list of available
fields and their purposes, see the _Field Definition Guide_ included in
the [ACE CRM Development Kit](https://partnercentral.awspartner.com/partnercentral2/s/resources?Id=0698a00000D11JsAAJ "https://partnercentral.awspartner.com/partnercentral2/s/resources?Id=0698a00000D11JsAAJ") on Partner Central.

Complex logic and derivations should be done in your Salesforce organization based on your own business logic, then populate the mapped field based on it.

## Synchronization and validation issues

Expand the following sections as needed for information about fixing synchronization and validation issues with the AWS Partner CRM connector.

This issue happens when you test the connector in a development organization with limited storage. To fix it, clear the sync logs from the console by running the following query:

`List`awsapn_Sync_Log_c`syncLogs = [SELECT Id FROM
`awsapn_Sync_Log_c` WHERE Status IN ('API Success',
 'Processed') LIMIT 4000]; delete syncLogs;`

You can also set the sync log retention period to automatically clean up sync log records older than the retention period. For more information about setting the retention period, refer to

Some leads and AWS originated opportunities don't comply with the validation rules
for each field. To allow partners to accept or reject such referrals, you can correct the
data before accepting a record. To accept or reject an object that is non-compliant with
the data validations, complete the following steps:

1. Navigate to the sync log details of the failed record.
2. Choose **Edit Payload** to access the JSON view.
3. Update the values of non-compliant fields.
4. Choose **Save Payload** to set up the record for sync for the next job.
   If the record is accepted, you must repeat steps 1–4 again after receiving the
   remaining fields from AWS. For subsequent syncs, the corrected values are used.
   As an alternative, you can correct the values in the ACE pipeline manager on Partner
   Central.

AWS uploads leads and opportunities to the Amazon S3 bucket every hour. As a result,
actions that require a data update through the integration can take up to an hour to
synchronize.

The following warning appears when a user performing object mapping doesn't have read access to the required fields:

```
pe.setFieldLengthWarning()@ -
/modules/awsapn/fieldMappingRow.js:1:7831
set salesforceFields()@- /modules/awsapn/fieldMappingRow.js:1:5624
```

You must use a system administrator user with permissions to the source and target fields, or a user with the [APN integration permission set](crm-connector-pemissions-sets.md#integration-user "crm-connector-pemissions-sets.md#integration-user").

To determine the state and action on each sync log record, refer to the tables in [Sync logs](crm-connector-sync-logs-and-reports.md#sync-logs "crm-connector-sync-logs-and-reports.md#sync-logs").

The sync log object tracks all inbound and outbound transactions. You can also specify a retention period for log records
in the app configuration.

The Partner Central APIs have a [set of quotas](../APIReference/quotas.md#understanding-and-managing-quotas "../APIReference/quotas.md#understanding-and-managing-quotas") that ensure fair use and avoid service misuse. You might see the
throttling exception when rate limiting kicks in after you reach a quota. Daily quotas
reset on a rolling 24-hour cycle. If the default quotas do not meet your requirements, you
can use the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard") to request a quota increase.

The **Send to AWS** button only appears for the **Partner referral** opportunity type.
