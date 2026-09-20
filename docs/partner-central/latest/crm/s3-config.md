

# Configuring the connector for a CRM with Amazon S3 integration
<a name="s3-config"></a>

**Important**  
Starting in 2024, AWS Partner Central made this integration type unavailable to new users. 

**Note**  
The topics in this section assume you've completed the prerequisites for an AWS Partner Central integration, an AWS Marketplace integration, or both. For more information, refer to [Integration prerequisites](crm-integration-setting-up.md) and [Getting started](crm-integration-getting-started.md) earlier in this guide.  
**Recommended:** Complete these activities in a Sandbox environment first, test thoroughly, and then deploy to Production.

The deprecated CRM with Amazon S3 integration uses an Amazon S3 bucket to transfer leads and opportunities . We recommend using the Partner Central API integration as shown in the previous section to create and manage opportunities. However, you can use this configuration if you want to use the connector to manage leads in Salesforce.

**Topics**
+ [Entering connection authentication details](#apn-s3-authentication-details)
+ [Entering system configuration settings](#apn-s3-config-settings)
+ [Testing the connection](#apn-s3-testing)
+ [Sending and receiving opportunities and leads](#sending-receiving-opportunities-leads)
+ [Production checklist](ace-production-checklist.md)
+ [Upgrading AWS Partner CRM connector to the new data model](connector-upgrade-plan.md)
+ [Sandbox testing with the custom ACE opportunity and ACE lead objects](custom-ace-opportunity.md)
+ [Linking AWS Marketplace private offers to ACE opportunities](#linking-private-offers-to-ace)

## Entering connection authentication details
<a name="apn-s3-authentication-details"></a>

Partners start the integration process by entering the details needed to connect to their Amazon S3 endpoint. Follow each set of steps in the order listed, and complete each set before proceeding to the next one.

The following tasks are performed from the **AWS guided setup** tab. For information about using the tab, refer to [Using guided setup](use-guided-setup.md) earlier in this guide.

**To enter the authentication details**

1. In Salesforce, open the **AWS guided setup** tab. For information about opening that tab, refer to [Using guided setup](use-guided-setup.md) earlier in this guide. 

1. Expand **Step 1: AWS connection authentication details** and choose **Start.**

1. On the **Named credentials** page, choose **New earlier**.

1. In the **New named credential** form, enter the values from the following table.


| **Field** | **Value** | 
| --- | --- | 
| Label | APN API Connection  | 
| URL | [https://s3.us-west-2.amazonaws.com](https://s3.us-west-2.amazonaws.com) | 
| Identity type | Named Principal  | 
| Authentication protocol | AWS signature version 4  | 
| AWS access key ID | Cloud-Ops provides the ID during the prerequisite steps  | 
| AWS secret access key | Cloud-Ops provides the access key during the prerequisite steps  | 
| AWS Region | us-west-2  | 
| AWS service | s3  | 
| Generate authorization header | checked  | 
| Allow merge fields in HTTP header | unchecked  | 
| Allow merge fields in HTTP body | unchecked  | 

1. Choose **Save**. 

1. Return to the **AWSGuided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials. 

1. Keep the **AWSGuided setup** page open and go to the next steps.

## Entering system configuration settings
<a name="apn-s3-config-settings"></a>

The following steps explain how to enter the correct system configuration settings for the integration.

1. Expand **Step 2: System configuration settings** and choose **Start.** 

1. Locate the **AWS Partner CRM Connector Settings**, and choose **Manage**. 

1. Choose **New**, and then enter the required values from the following table. 


<table>
<thead>
  <tr><th> <b>Custom setting field</b> </th><th> <b>Purpose</b> </th></tr>
</thead>
<tbody>
  <tr><td><b>Name</b></td><td>Field isn’t used, but because it’s required, you can set it to any value.</td></tr>
  <tr><td><b>Bucket name</b></td><td>Bucket name that was provisioned for the partner. It’s different for beta and production environments. </td></tr>
  <tr><td><b>Default account</b></td><td>An 18-digit record ID of the default account that’s used when standard opportunities are used as the target object in Salesforce. Because <b>AccountID</b> is required on standard opportunities, the default account field allows new inbound opportunities from AWS to have a default account tied to. This can be any account record in your Salesforce organization that the integration user has access to from the sharing settings.</td></tr>
  <tr><td><b>Outbound batch size</b></td><td>Number of records sent in a single payload from your Salesforce organization to AWS. This is common for both opportunities and leads. We recommend a value between 1–50. For example, if you set the batch size to 50, each opportunity payload sent from your organization to AWS contains 50 opportunity records. </td></tr>
  <tr><td><b>Retry count</b></td><td>In the event of a failure, this value represents the number of times the transaction is retried.</td></tr>
  <tr><td><b>Retry cutoff days</b></td><td>If a record continues to fail, this value is the number of days after which a retry is no longer attempted. </td></tr>
  <tr><td><b>Partner ID</b></td><td>Unique partner identifier that is shared as part of enablement. </td></tr>
  <tr><td><b>Sync log retention</b></td><td>Number of days to retain the synchronization logs. </td></tr>
  <tr><td><b>Version</b></td><td>For the new data model, choose version 2. For the previous data model, choose version 1. </td></tr>
  <tr><td><b>Create New Account from Default Account</b></td><td>Enables the connector to create a new account based on the default account provided by the partner. When you select this option, it enables dynamic account creation during the integration process, ensuring that new opportunities or engagements can be associated with appropriate account records even when the exact account doesn't exist in the target system. </td></tr>
</tbody>
</table>


1. Choose **Save**. 

1. Return to the **AWSGuided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials. 

## Testing the connection
<a name="apn-s3-testing"></a>

Before testing the connection, make sure you complete the steps in the previous sections.

**To test the connection**

1. Expand **Step 3: Test configuration for APN API**.

1. Choose **Test**.

If the connection succeeds, you receive a confirmation message. 

## Sending and receiving opportunities and leads
<a name="sending-receiving-opportunities-leads"></a>

You send and receive opportunities and leads by synchronizing them with Partner Central. To synchronize an opportunity or lead, you must set the **Sync with Partner Central** field to **True**. Additional key fields for integration include the **Last APN Sync Date** and the **Eligible to Sync with APN** fields.

These fields are included for standard opportunities and leads. However, you must create and map them for any custom source objects.
+ **Sync with Partner Central** – Included in the app for standard opportunities and leads. If a AWS Partner chooses to map to custom objects, a custom boolean field must be created and mapped in the opportunity and lead mappings, respectively.
+ **Last Sync Date with APN** – Indicates the last time the record was successfully sent to or received from APN. This field is autoset when the record is successfully sent to APN or an update is received from APN.
+ **Eligible to Sync with APN** – A formula field that determines if the record is targeted to be sent to APN in the next scheduled job. Calculated based on whether the record was modified since the last time the outbound schedule ran, and it was updated by a user other than the designated integration user for the AWS Partner's organization.

## Linking AWS Marketplace private offers to ACE opportunities
<a name="linking-private-offers-to-ace"></a>

You can link private offers directly from the AWS delivered ACE opportunity record page.

1. Sign in to your Salesforce organiziation.

1. In the **App Launcher**, choose **AWS Partner CRM connector**.

1. Choose the **ACE Opportunities** tab.

1. Choose an ACE opportunity record.

1. Choose **Link Private Offer**.

1. In **Offer ID Look Up**, choose the private offer.

1. Choose **Save**.