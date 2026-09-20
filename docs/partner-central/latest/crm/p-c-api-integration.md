

# Configuring the connector for a Partner Central API integration
<a name="p-c-api-integration"></a>

The following sections explain how to configure the CRM connector for use with the AWS Partner Central APIs.

To create and manage opportunities in Salesforce, configure the CRM connector for use with a Partner Central API integration.

**Note**  
Managing leads requires an earlier CRM with Amazon S3 integration. For more information, refer to [Configuring the connector for a CRM with Amazon S3 integration](s3-config.md) later in this guide.

**Topics**
+ [Entering connection authentication details](#config-p-c-apis)
+ [Entering the system settings](#p-c-api-system-settings)
+ [Testing the connection](#p-c-apis-testing)
+ [Using flow templates](flow-templates.md)

## Entering connection authentication details
<a name="config-p-c-apis"></a>

Partners start the integration process by entering the details needed to connect to the Partner Central sales endpoint. Follow each set of steps in the order listed, and complete each set before proceeding to the next one.

**To enter connection authentication details**

1. In Salesforce, open the **AWS guided setup** tab. For information about opening that tab, refer to [Using guided setup](use-guided-setup.md) earlier in this guide. 

1. Expand **Step 1: AWS connection authentication details** and choose **Start.**

1. On the **Named credentials** page, choose **New earlier**. 

1. In the **New named credential** form, enter the values from the following table. 


<table>
<thead>
  <tr><th><b>Field</b> </th><th><b>Value</b> </th></tr>
</thead>
<tbody>
  <tr><td><b>Label</b> </td><td>AWS Partner Central API </td></tr>
  <tr><td><b>URL</b> </td><td><a href="https://partnercentral-selling.us-east-1.api.aws">https://partnercentral-selling.us-east-1.api.aws</a> </td></tr>
  <tr><td><b>Identity type</b></td><td>Named Principal </td></tr>
  <tr><td><b>Authentication protocol</b></td><td>AWS signature version 4 </td></tr>
  <tr><td><b>AWS access key ID</b></td><td>Cloud-Ops provides the ID during the prerequisite steps </td></tr>
  <tr><td><b>AWS secret access key</b></td><td>Cloud-Ops provides the access key during the prerequisite steps </td></tr>
  <tr><td><b>AWS Region</b></td><td>us-east-1 </td></tr>
  <tr><td><b>AWS service</b></td><td>partnercentral-selling </td></tr>
  <tr><td><b>Generate authorization header</b></td><td>checked </td></tr>
  <tr><td><b>Allow merge fields in HTTP header</b></td><td>checked </td></tr>
  <tr><td><b>Allow merge fields in HTTP body</b></td><td>unchecked </td></tr>
</tbody>
</table>


1. Choose **Save**. 

1. Return to the **AWSGuided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials. 

## Entering the system settings
<a name="p-c-api-system-settings"></a>

The following steps explain how to enter the correct system configuration settings for the integration.

1. In Salesforce, open the **AWS guided setup** tab. For information about opening that tab, refer to [Using guided setup](use-guided-setup.md) earlier in this guide. 

1. Expand **Step 2: System configuration settings** and choose **Start.** 

1. Locate **AWS Partner CRM Connector Settings**, and choose **Manage**. 

1. Choose **New**, then enter the values from the following table. 


<table>
<thead>
  <tr><th><b>Custom setting field</b> </th><th> <b>Purpose</b> </th></tr>
</thead>
<tbody>
  <tr><td><b>Name</b> </td><td>Field isn’t used, but because it’s required, you can set it to any value. </td></tr>
  <tr><td><b>Default account</b> </td><td>An 18-digit record ID of the default account that’s used when standard opportunities are used as the target object in Salesforce. Because <b>AccountID</b> is required on standard opportunities, the default account field allows new inbound opportunities from AWS to have a default account tied to them. This can be any account record in your Salesforce organization that the integration user has access to from the sharing settings. </td></tr>
  <tr><td><b>Create New Account from Default Account</b> </td><td>This setting enables the connector to create a new account based on the default account provided by the partner. When checked, it allows for dynamic account creation during the integration process, ensuring that new opportunities or engagements can be associated with appropriate account records even when the exact account doesn't exist in the target system. </td></tr>
  <tr><td><b>Default opportunity</b></td><td>This option stores the 18-digit record ID of a default opportunity for use as a template. For partners using Standard Opportunity and custom objects other than an ACE Opportunity, the default record allows the connector to clone and create new opportunities or AWS referral engagements while bypassing potential required field issues. The connector clones this default record, appends new field values from the incoming data, and creates a new opportunity record. This method integrates data data with custom opportunity objects or unique field requirements.</td></tr>
  <tr><td><b>PC API Sandbox Enabled</b> </td><td>Select this option to enable partners to test the connector with the AWS Partner Central API. When selected, users can create test opportunities that are sent to the AWS Sandbox API. </td></tr>
</tbody>
</table>


1. Choose **Save**. 

1. Return to the **AWS guided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials.

## Testing the connection
<a name="p-c-apis-testing"></a>

Before testing the connection, ensure that you have completed all the above steps.

**To test the AWS Partner Central API connection**

1. Expand **Step 4: Test configuration for Partner Central API integration**.

1. Choose **Test**.

If the connection succeeds, you receive a confirmation message.