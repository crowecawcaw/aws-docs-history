# Configuring the connector for a CRM with Amazon S3 integration

###### Important

Starting in 2024, AWS Partner Central made this integration type unavailable to new users.

###### Note

The topics in this section assume you've completed the prerequisites for an AWS Partner Central integration, an AWS Marketplace integration, or both.
For more information, refer to [Integration prerequisites](crm-integration-setting-up.md "crm-integration-setting-up.md")
and [Getting started](crm-integration-getting-started.md "crm-integration-getting-started.md") earlier in this guide.

The deprecated CRM with Amazon S3 integration uses an Amazon S3 bucket to transfer leads and
opportunities . We recommend using the Partner Central API integration as shown in the previous
section to create and manage opportunities. However, you can use this configuration if you want
to use the connector to manage leads in Salesforce.

###### Topics

- [Entering connection authentication
  details](#apn-s3-authentication-details "#apn-s3-authentication-details")
- [Entering system configuration settings](#apn-s3-config-settings "#apn-s3-config-settings")
- [Testing the connection](#apn-s3-testing "#apn-s3-testing")
- [Sending and receiving opportunities and leads](#sending-receiving-opportunities-leads "#sending-receiving-opportunities-leads")
- [Production checklist](ace-production-checklist.md "ace-production-checklist.md")
- [Upgrading AWS Partner CRM connector to the new data
  model](connector-upgrade-plan.md "connector-upgrade-plan.md")
- [Sandbox testing with the custom ACE opportunity and
  ACE lead objects](custom-ace-opportunity.md "custom-ace-opportunity.md")
- [Linking AWS Marketplace private offers to ACE
  opportunities](#linking-private-offers-to-ace "#linking-private-offers-to-ace")

## Entering connection authentication

details

Partners start the integration process by entering the details needed to connect to
their Amazon S3 endpoint. Follow each set of steps in the order listed, and complete each set
before proceeding to the next one.

The following tasks are performed from the **AWS guided setup** tab.
For information about using the tab, refer to [Using guided setup](use-guided-setup.md "use-guided-setup.md") earlier in this guide.

###### To enter the authentication details

1. In Salesforce, open the **AWS guided setup** tab. For information
   about opening that tab, refer to [Using guided setup](use-guided-setup.md "use-guided-setup.md") earlier in this guide.
2. Expand **Step 1: AWS connection authentication details** and
   choose **Start.**
3. On the **Named credentials** page, choose **New
   earlier**.
4. In the **New named credential** form, enter the values from the
   following table.

| **Field**                             | **Value**                                                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Label**                             | APN API Connection                                                                                            |
| **URL**                               | [https://s3.us-west-2.amazonaws.com](https://s3.us-west-2.amazonaws.com "https://s3.us-west-2.amazonaws.com") |
| **Identity type**                     | Named Principal                                                                                               |
| **Authentication protocol**           | AWS signature version 4                                                                                       |
| **AWS access key ID**                 | Cloud-Ops provides the ID during the prerequisite steps                                                       |
| **AWS secret access key**             | Cloud-Ops provides the access key during the prerequisite steps                                               |
| **AWS Region**                        | us-west-2                                                                                                     |
| **AWS service**                       | s3                                                                                                            |
| **Generate authorization header**     | checked                                                                                                       |
| **Allow merge fields in HTTP header** | unchecked                                                                                                     |
| **Allow merge fields in HTTP body**   | unchecked                                                                                                     |

1. Choose **Save**.
2. Return to the **AWSGuided setup** page. In the
   **Authentication details** section, choose
   **Review** and confirm the credentials.
3. Keep the **AWSGuided setup** page open and go to the next
   steps.

## Entering system configuration settings

The following steps explain how to enter the correct system configuration settings for
the integration.

1. Expand **Step 2: System configuration settings** and choose
   **Start.**
2. Locate the **AWS Partner CRM Connector Settings**, and choose
   **Manage**.
3. Choose **New**, and then enter the required values from the
   following table.

| **Custom setting field**                    | **Purpose**                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                    | Field isn’t used, but because it’s required, you can set it to any<br>value.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Bucket name**                             | Bucket name that was provisioned for the partner. It’s different for beta<br>and production environments.                                                                                                                                                                                                                                                                                                                                                      |
| **Default account**                         | An 18-digit record ID of the default account that’s used when standard<br>opportunities are used as the target object in Salesforce. Because<br>\*_AccountID_<br>• is required on standard opportunities, the<br>default account field allows new inbound opportunities from AWS to have a<br>default account tied to. This can be any account record in your Salesforce<br>organization that the integration user has access to from the sharing<br>settings. |
| **Outbound batch size**                     | Number of records sent in a single payload from your Salesforce<br>organization to AWS. This is common for both opportunities and leads. We<br>recommend a value between 1–50. For example, if you set the batch size to 50,<br>each opportunity payload sent from your organization to AWS contains 50<br>opportunity records.                                                                                                                                |
| **Retry count**                             | In the event of a failure, this value represents the number of times the<br>transaction is retried.                                                                                                                                                                                                                                                                                                                                                            |
| **Retry cutoff days**                       | If a record continues to fail, this value is the number of days after which<br>a retry is no longer attempted.                                                                                                                                                                                                                                                                                                                                                 |
| **Partner ID**                              | Unique partner identifier that is shared as part of enablement.                                                                                                                                                                                                                                                                                                                                                                                                |
| **Sync log retention**                      | Number of days to retain the synchronization logs.                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Version**                                 | For the new data model, choose version 2. For the previous data model,<br>choose version 1.                                                                                                                                                                                                                                                                                                                                                                    |
| **Create New Account from Default Account** | Enables the connector to create a new account based on the default account<br>provided by the partner. When you select this option, it enables dynamic account<br>creation during the integration process, ensuring that new opportunities or<br>engagements can be associated with appropriate account records even when the<br>exact account doesn't exist in the target system.                                                                             |

4. Choose **Save**.
5. Return to the **AWSGuided setup** page. In the
   **Authentication details** section, choose
   **Review** and confirm the credentials.

## Testing the connection

Before testing the connection, make sure you complete the steps in the previous
sections.

###### To test the connection

1. Expand **Step 3: Test configuration for APN API**.
2. Choose **Test**.

If the connection succeeds, you receive a confirmation message.

## Sending and receiving opportunities and leads

You send and receive opportunities and leads by synchronizing them with Partner Central. To synchronize an opportunity or lead, you must set the **Sync
with Partner Central** field to **True**. Additional
key fields for integration include the **Last APN Sync Date** and the
**Eligible to Sync with APN** fields.

These fields are included for standard opportunities and leads. However, you must
create and map them for any custom source objects.

- **Sync with Partner Central** – Included in the app for
  standard opportunities and leads. If a AWS Partner chooses to map to custom objects, a custom
  boolean field must be created and mapped in the opportunity and lead mappings,
  respectively.
- **Last Sync Date with APN** – Indicates the last time the
  record was successfully sent to or received from APN. This field is autoset when the
  record is successfully sent to APN or an update is received from APN.
- **Eligible to Sync with APN** – A formula field that
  determines if the record is targeted to be sent to APN in the next scheduled job.
  Calculated based on whether the record was modified since the last time the outbound schedule
  ran, and it was updated by a user other than the designated integration user for the
  AWS Partner's organization.

## Linking AWS Marketplace private offers to ACE

opportunities

You can link private offers directly from the AWS delivered ACE opportunity record
page.

1. Sign in to your Salesforce organiziation.
2. In the **App Launcher**, choose **AWS Partner CRM
   connector**.
3. Choose the **ACE Opportunities** tab.
4. Choose an ACE opportunity record.
5. Choose **Link Private Offer**.
6. In **Offer ID Look Up**, choose the private offer.
7. Choose **Save**.
