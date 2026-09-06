

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/partner-central/latest/crm/s3-config.html)

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