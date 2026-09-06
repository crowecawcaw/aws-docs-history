

# AWS Partner CRM connector FAQ
<a name="crm-connector-faq"></a>

The topics in this section help answer frequently asked questions about AWS Partner CRM integration and using the CRM connector.

**Note**  
The questions and answers in this FAQ assume that you use Salesforce. For more information about using Salesforce, see the [Salesforce help](https://help.salesforce.com/s/).

**Topics**
+ [General questions](#general-questions)
+ [Setup issues](#setup-issues)
+ [Mapping issues](#mapping-issues)
+ [Synchronization and validation issues](#synchronization-validation)

## General questions
<a name="general-questions"></a>

Expand the following sections for more information about using the AWS Partner CRM connector.

### How do I get started with the AWS Partner CRM connector?
<a name="how-to-get-started"></a>

Contact your partner development manager (PDM) or your AWS point of contact. Your PDM will verify eligibility, help set up the IAM user required for authentication and submit the request internally to set up the Amazon S3 bucket required for you to exchange files. After you have access to the Amazon S3 bucket, you can install the connector and set up the integration by following the instructions in the user guide.

If you already have an AWS Partner ACE integration, [install the connector from the Salesforce AppExchange](install-connector.md), then follow the instructions in [Configuring the connector for a CRM with Amazon S3 integration](s3-config.md).

### Why move to version 3?
<a name="why-move"></a>

Version 3 provides real-time opportunity updates and eliminates the need for schedules. It also provides a set of buttons that enable partners to accept or reject leads and opportunities, update them, and send them to AWS. For information about installing version 3, refer to [Available features](crm-connector-feature-list.md) earlier in this guide.

### What is the latest version of connector?
<a name="latest-version"></a>

Version 3.0.0. You can find it in the Salesforce App Exchange.

### What does it cost to set up the AWS Partner CRM connector?
<a name="setup-costs"></a>

The AWS Partner CRM connector is available for free from the Salesforce App Exchange. It provides the following integration options:
+ A Partner Central API-based integration where the AWS service calls are free.
+ An Amazon S3-based integration where AWS hosts and bears the costs of an Amazon S3 bucket.
**Note**  
You can only use this option if you created a CRM with Amazon S3 integration prior to 2024.

Amazon EventBridge is also free because the events come from an AWS service. However, you may incur additional charges on your AWS account if you forward the events to other event buses from the primary event listener for additional processing.

For more information about the AWS Partner CRM connector, refer to [CRM connector overview](connector-overview.md). For more information about EventBridge, see [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) in the *Amazon EventBridge User Guide*.

### What new features does version 3 provide?
<a name="new-features"></a>

For a list of the features provided by the AWS Partner CRM connector, refer to [Partner Central API features](crm-connector-feature-list.md#partner-central-api-features), earlier in this guide.

### Can I programmatically access the Amazon S3 bucket used to send and receive files?
<a name="s3-programmatic-access"></a>

Yes. Use the `AccessKey` and `SecretAccessKey` credentials of the IAM user from the [CRM Integration onboarding](https://partnercentral.awspartner.com/partnercentral2/s/acecrmintegration) request.

Remember, files are no longer be transferred using the Amazon S3 bucket once you port the integration over to the API based approach. However, leads are still shared using the Amazon S3 bucket based integration.

### I haven't moved to the Salesforce Lightning version. Can I still use the AWS Partner CRM connector?
<a name="sf-lightning-version"></a>

The AWS Partner CRM connector is designed for use with the Salesforce Lightning version, so version 2 may not function as intended.

### Can I use the package directly on my production systems?
<a name="prod-systems"></a>

We recommend that you install the package on production systems only after thoroughly testing in a sandbox environment.

### Who are the intended users of the AWS Partner CRM connector?
<a name="intended-users"></a>

AWS Partner CRM connector is designed for the following user personas:
+ Salesforce administrators or referral administrators who set up the connector.
+ Sales operations users who select, accept, and update opportunities and leads.

### I have an ACE integration. Can I move to the connector?
<a name="move-connector"></a>

Yes. AWS Partners that have an existing integration with ACE can move to the connector. Because the connector uses the same Amazon S3 bucket in the back end, complete the following steps:

1. Disconnect your custom app or solution from the Amazon S3 bucket.

1. Sign in to the AWS account to set up the integration. Obtain or create a secret key and access key for the IAM user that is authorized to access the Amazon S3 bucket. The user name must follow this format: `apn-ace-{partnerName}-AccessUser-prod`. For more information, see [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey) in the *AWS Identity and Access Management User Guide*.
**Note**  
If you're unable to find the AWS account, submit a [support request](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html).

1. To configure the connector to point to the Amazon S3 bucket, choose **Setup**, then **Named Credentials**, then **APN API connection**.

1. Submit a [support request](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) to delete existing objects in the Amazon S3 bucket before scheduling a job in the connector. 
**Important**  
 You must complete this step before completing the integration and setting a synchronization schedule.

1. If the target object is different from the existing object, conduct a data backfill for your existing leads and opportunities. For more information, refer to the CRM integration *Production setup and backfill guide*.
**Note**  
During the integration switchover, all user updates queue in the `Outbound` folder of the Amazon S3 bucket. After the integration is live, the user-update records are synced.

### Is the AWS Partner CRM connector safe to use in my Salesforce organization?
<a name="connector-safe"></a>

The Salesforce application has gone through Salesforce and internal AWS security reviews. The Salesforce security review scans include the following threats:
+ Salesforce Object Query Language (SOQL) and SQL injection
+ Cross-site scripting
+ Non-secure authentication and access control protocols
+ Record-sharing violations and other vulnerabilities specific to the Salesforce platform

The code review uses the [Salesforce Code Analyzer](https://forcedotcom.github.io/sfdx-scanner/) to inspect Salesforce code. Salesforce Code Analyzer uses multiple code analysis engines, including PMD, ESLint, and RetireJS. It identifies a number of potential problems, from inconsistent naming to security vulnerabilities.

For more information on the review process, refer to [AppExchange Security Review](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/security_review_overview.htm) in the Salesforce documentation.

**Note**  
Partner applications are non-Salesforce.com applications as defined in the Salesforce Main Services Agreement. For more information, refer to the Salesforce [Agreements and Terms](https://www.salesforce.com/company/legal/agreements/).

Notwithstanding any security requirements set forth herein or any security review of a partner application that may occur, Salesforce makes no guarantees regarding the quality or security of any partner application, and customers are solely responsible for evaluating the quality, security, and functionality of partner applications to determine their adequacy and appropriateness for customers' installation and use.

While we cannot share specifically what our internal security audit covers, it is geared towards the native AWS components of the integration architecture, to which the Salesforce app connects and covers a number of different threat modeling scenarios such as man-in-the-middle attacks, distributed denial-of-service mitigations, and encryption standards. For more information, submit a support request.

## Setup issues
<a name="setup-issues"></a>

Expand the following sections for information about fixing set up issues with the AWS Partner CRM connector.

### What are the prerequisites for using the AWS Partner CRM connector?
<a name="set-up-prereqs"></a>

For information about the prerequisites for using the CRM connector, see the [Integration prerequisites](crm-integration-setting-up.md) earlier in this guide.

### How do I set up the named credentials for the package?
<a name="set-up-named-credentials"></a>

Follow these steps listed in [Setting up named credentials](guided-setup-apis.md#api-named-credentials) later in this guide.

### What are implications of moving from version 2 to version 3? Are there any breaking changes?
<a name="moving-implications"></a>

Moving from version 2 to version 3 of AWS Partner CRM connector has no immediate implications. All the functionality is backward compatible and works without interruptions.

For opportunity management, if you plan to use the new features, you may need to change some of your sales processes. You should evaluate the following changes and create a transition plan. 
+ Version 3 shares opportunities with AWS in real time. You no longer need to create schedules for sending opportunities to AWS. Opportunity owners on a partner's Salesforce instance must manually send data to AWS. Salesforce users need permissions to push opportunities to AWS. 
+ If you plan to use multi-object mapping, you need a transition plan for getting and posting data from new objects in your Salesforce instance. As a Salesforce admin, you should be aware of consequences of moving from object mapping with all fields mapped in a single object versus fields from a different object mapped to a single object. 

### Moving from an Amazon S3 connection (Asynchronous) to an API based connection (Synchronous), are there additional set up steps?
<a name="moving-from-s3"></a>

Yes. You *must* complete the following items:
+ In the general prerequisites, [Linking your AWS Partner Central and AWS Marketplace accounts](link-pc-mkt-accounts.md). 
+  Create named credentials for the new Partner Central APIs. For more information, refer to [Setting up named credentials](guided-setup-apis.md#api-named-credentials) earlier in this guide. 

### We have not moved to the Salesforce Lightning version. Can we still use the AWS Partner CRM Connector?
<a name="no-lightning"></a>

No. The connector is designed for use with the Salesforce Lightning version, and the app may not function as intended without it.

### We are reaching the limit on scheduled jobs in our Salesforce environment. Can we use external schedulers to trigger synching with AWS?
<a name="sf-job-limit"></a>

NEED TO VALIDATE - AWS Partner CRM Connector is managed package. You can create custom schedule invocation with third party apps against the `InboundSyncScheduler` and `OutboundSyncScheduler` apex classes. Note - With new API based integration, these classes might not work.

## Mapping issues
<a name="mapping-issues"></a>

Expand the following sections as needed for information about fixing object-mapping issues with the AWS Partner CRM connector. 

### How does multi object mapping work?
<a name="m-o-mapping"></a>

For version 3, partners can select the fields of referenced objects one level down while mapping. For example, if your Salesforce standard opportunity object has an internal reference pointing to an account object and a custom AWS sales object, you can select the standard opportunity as the parent object, then map fields from the account and sales objects.

### Can I select more than one object in the mapping tab?
<a name="select-multiple-objects"></a>

No. Instead, you map multiple fields from a selected object.

### How does the connector track the objects it uses to marshal data?
<a name="track-objects"></a>

Version 3 uses the `APNCrmUniqueIdentifier` field to reference a single parent object for mapping. The field contains the AWS record ID. After querying the parent object, the values of all other related objects are marshalled or unmarshalled based on the reference link from the parent object.

### Where can I find the types field for a particular field?
<a name="find-types-field"></a>

Version 3 of the connector works on the version 2 data model. For complete payload information, see the [AWS Partner CRM Integration Samples](https://github.com/aws-samples/partner-crm-integration-samples) on GitHub.

### Does the managed package help set up validation rules on my standard Salesforce object?
<a name="validation-rule-help"></a>

No. The package comes with the ACE custom opportunity object, which includes the field types and validation rules that run against the [standard ACE payload](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Outbound-Sample.json). You can copy the validation rules and fields from an ACE custom opportunity object in your standard object. {{NEED TO VALIDATE}} - With multi-object mapping, you can try adding a reference to an ACE opportunity object inside your standard opportunity object, then copying data into those fields using triggers to kick off validations.

### Why can't I edit the mapping for the Sync with AWS field?
<a name="cant-edit-mapping"></a>

The **Sync with AWS** checkbox determines whether a lead or opportunity synchronizes with AWS when the next scheduled job runs. The **Sync with Partner Central** field is included with the app for standard opportunities and leads. If your target object is a custom object, you must map the **Sync with AWS** field to a custom non-formula boolean field in each object.

### How does the Has Updates for AWS field work?
<a name="has-updates"></a>

The **Has Updates for AWS** formula field determines if a record is sent to AWS Partner in the next scheduled job. **Has Updates for AWS** is set to **True** when the following conditions are true:
+ **Last Modified Date** of the record is later than **Last APN Sync Date**.
+ **Last Modified User** is not the user that scheduled the integration jobs.

### Why can't I map the required APN CRM Unique Identifier field? The menu is unavailable, and I receive the message "No valid field to map"
<a name="map-unique-id-field"></a>

You must use the **Text** data type with a length of 18 characters to match the length of the **API** field.
+ Configuration: Text (18) (External ID) (Unique Case Insensitive)

### What are the connector app's troubleshooting checkpoints for outbound file push from Salesforce to AWS Partner?
<a name="troubleshooting-checkpoints"></a>

The app uses the following checkpoints:
+ **Sync to AWS** must be checked in order to sync with AWS.
+ **Has Update to AWS** must be checked in order to sync with AWS.
+ The user persona for creating the scheduling job must be different from the user persona for used to create and update leads or opportunities.
+ If the previous checks are true but the outbound batch still doesn't run, check the AWS Partner sync logs and add the **outbound IDs** column. Confirm that the sync log contains the ID of the opportunity that you want to push. If the sync log is stuck in the **API Success** state, delete the sync log record and try again.

  When **Expected Monthly AWS Revenue** is not an integer, such as `1041.67` instead of `1041`, the mismatch in data type causes a processing error. To resolve this, delete the sync log stuck in the **API Success** state and correct the data before the next job run.

### Can I configure filters and subscriptions to sync leads and opportunities? Can we add custom filters on status or stage fields?
<a name="configure-syncs"></a>

In Salesforce, you can create or update the formula field to add the dependency from the status or stage fields for a specific value. For example, you can set **Has Updates for AWS** to **True**. You can use the included field on the opportunity as a reference. The following example shows how:

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

### Do I have to map the mandatory fields?
<a name="map-mandatory"></a>

Yes. You must map all mandatory fields in order to schedule an inbound or outbound integration job.

### Can I map lookup fields?
<a name="map-lookup-fields"></a>

We recommend reviewing the fields that you currently enter in Partner Central to determine the most relevant fields (in addition to the required fields). For a list of available fields and their purposes, see the *Field Definition Guide* included in the [ACE CRM Development Kit](https://partnercentral.awspartner.com/partnercentral2/s/resources?Id=0698a00000D11JsAAJ) on Partner Central.

### Should I update the record with derived fields or create them during the mapping process?
<a name="use-derived-fields"></a>

Complex logic and derivations should be done in your Salesforce organization based on your own business logic, then populate the mapped field based on it.

## Synchronization and validation issues
<a name="synchronization-validation"></a>

Expand the following sections as needed for information about fixing synchronization and validation issues with the AWS Partner CRM connector.

### What causes the STORAGE\_LIMIT\_EXCEEDED error?
<a name="storage-exceeded"></a>

This issue happens when you test the connector in a development organization with limited storage. To fix it, clear the sync logs from the console by running the following query:

`List{{awsapn_Sync_Log_c}} syncLogs = [SELECT Id FROM {{awsapn_Sync_Log_c}} WHERE Status IN ('API Success', 'Processed') LIMIT 4000]; delete syncLogs;`

You can also set the sync log retention period to automatically clean up sync log records older than the retention period. For more information about setting the retention period, refer to 

### AWS referred leads or opportunities don't comply with the validation imposed on my custom object. How can I fix this issue?
<a name="validation-compliance"></a>

Some leads and AWS originated opportunities don't comply with the validation rules for each field. To allow partners to accept or reject such referrals, you can correct the data before accepting a record. To accept or reject an object that is non-compliant with the data validations, complete the following steps:

1. Navigate to the sync log details of the failed record.

1. Choose **Edit Payload** to access the JSON view.

1. Update the values of non-compliant fields.

1. Choose **Save Payload** to set up the record for sync for the next job.

If the record is accepted, you must repeat steps 1–4 again after receiving the remaining fields from AWS. For subsequent syncs, the corrected values are used. As an alternative, you can correct the values in the ACE pipeline manager on Partner Central.

### How often does AWS upload leads and opportunities?
<a name="upload-frequency"></a>

AWS uploads leads and opportunities to the Amazon S3 bucket every hour. As a result, actions that require a data update through the integration can take up to an hour to synchronize.

### Why do I get a setFieldLengthWarning message when using the mapping screen?
<a name="field-length-warning"></a>

The following warning appears when a user performing object mapping doesn't have read access to the required fields:

```
pe.setFieldLengthWarning()@ -
/modules/awsapn/fieldMappingRow.js:1:7831
set salesforceFields()@- /modules/awsapn/fieldMappingRow.js:1:5624
```

You must use a system administrator user with permissions to the source and target fields, or a user with the [APN integration permission set](crm-connector-pemissions-sets.md#integration-user).

### What do the Status and Purpose fields in the sync log mean?
<a name="status-purpose"></a>

To determine the state and action on each sync log record, refer to the tables in [Sync logs](crm-connector-sync-logs-and-reports.md#sync-logs).

### Do you provide auditing or archiving?
<a name="audit-archive"></a>

The sync log object tracks all inbound and outbound transactions. You can also specify a retention period for log records in the app configuration.

### Why do I get a throttling exception?
<a name="throttling"></a>

The Partner Central APIs have a [set of quotas](https://docs.aws.amazon.com/partner-central/latest/APIReference/quotas.html#understanding-and-managing-quotas) that ensure fair use and avoid service misuse. You might see the throttling exception when rate limiting kicks in after you reach a quota. Daily quotas reset on a rolling 24-hour cycle. If the default quotas do not meet your requirements, you can use the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard) to request a quota increase.

### I don't see the Send to AWS button on my standard opportunity
<a name="no-button"></a>

The **Send to AWS** button only appears for the **Partner referral** opportunity type.