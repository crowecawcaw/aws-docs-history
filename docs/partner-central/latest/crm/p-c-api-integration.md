# Configuring the connector for a Partner Central API integration

The following sections explain how to configure the CRM connector for use with the AWS Partner
Central APIs.

To create and manage opportunities in Salesforce, configure the CRM connector for use with a Partner Central API integration.

###### Note

Managing leads requires an earlier CRM with Amazon S3 integration. For more information, refer to [Configuring the connector for a CRM with Amazon S3 integration](s3-config.md "s3-config.md") later in this guide.

###### Topics

- [Entering connection authentication details](#config-p-c-apis "#config-p-c-apis")
- [Entering the system settings](#p-c-api-system-settings "#p-c-api-system-settings")
- [Testing the connection](#p-c-apis-testing "#p-c-apis-testing")
- [Using flow templates](flow-templates.md "flow-templates.md")

## Entering connection authentication details

Partners start the integration process by entering the details needed to connect to the
Partner Central sales endpoint. Follow each set of steps in the order listed, and complete
each set before proceeding to the next one.

###### To enter connection authentication details

1. In Salesforce, open the **AWS guided setup** tab. For information
   about opening that tab, refer to [Using guided setup](use-guided-setup.md "use-guided-setup.md") earlier in this guide.
2. Expand **Step 1: AWS connection authentication details** and
   choose **Start.**
3. On the **Named credentials** page, choose **New
   earlier**.
4. In the **New named credential** form, enter the values from the
   following table.

| **Field**                             | **Value**                                                                                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Label**                             | AWS Partner Central API                                                                                                                                 |
| **URL**                               | [https://partnercentral-selling.us-east-1.api.aws](https://partnercentral-selling.us-east-1.api.aws "https://partnercentral-selling.us-east-1.api.aws") |
| **Identity type**                     | Named Principal                                                                                                                                         |
| **Authentication protocol**           | AWS signature version 4                                                                                                                                 |
| **AWS access key ID**                 | Cloud-Ops provides the ID during the prerequisite steps                                                                                                 |
| **AWS secret access key**             | Cloud-Ops provides the access key during the prerequisite steps                                                                                         |
| **AWS Region**                        | us-east-1                                                                                                                                               |
| **AWS service**                       | partnercentral-selling                                                                                                                                  |
| **Generate authorization header**     | checked                                                                                                                                                 |
| **Allow merge fields in HTTP header** | checked                                                                                                                                                 |
| **Allow merge fields in HTTP body**   | unchecked                                                                                                                                               |

5. Choose **Save**.
6. Return to the **AWSGuided setup** page. In the
   **Authentication details** section, choose
   **Review** and confirm the credentials.

## Entering the system settings

The following steps explain how to enter the correct system configuration settings for
the integration.

1. In Salesforce, open the **AWS guided setup** tab. For information
   about opening that tab, refer to [Using guided setup](use-guided-setup.md "use-guided-setup.md") earlier in this guide.
2. Expand **Step 2: System configuration settings** and choose
   **Start.**
3. Locate **AWS Partner CRM Connector Settings**, and choose
   **Manage**.
4. Choose **New**, then enter the values from the following table.

| **Custom setting field**                    | **Purpose**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                    | Field isn’t used, but because it’s required, you can set it to any value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Default account**                         | An 18-digit record ID of the default account that’s used when standard<br>opportunities are used as the target object in Salesforce. Because<br>\*_AccountID_<br>• is required on standard opportunities, the<br>default account field allows new inbound opportunities from AWS to have a<br>default account tied to them. This can be any account record in your Salesforce<br>organization that the integration user has access to from the sharing settings.                                                                                                                                    |
| **Create New Account from Default Account** | This setting enables the connector to create a new account based on the<br>default account provided by the partner. When checked, it allows for dynamic<br>account creation during the integration process, ensuring that new opportunities<br>or engagements can be associated with appropriate account records even when the<br>exact account doesn't exist in the target system.                                                                                                                                                                                                                 |
| **Default opportunity**                     | This option stores the 18-digit record ID of a default opportunity for use<br>as a template. For partners using Standard Opportunity and custom objects other<br>than an ACE Opportunity, the default record allows the connector to clone and<br>create new opportunities or AWS referral engagements while bypassing potential<br>required field issues. The connector clones this default record, appends new<br>field values from the incoming data, and creates a new opportunity record. This<br>method integrates data data with custom opportunity objects or unique field<br>requirements. |
| **PC API Sandbox Enabled**                  | Select this option to enable partners to test the connector with the AWS<br>Partner Central API. When selected, users can create test opportunities that are<br>sent to the AWS Sandbox API.                                                                                                                                                                                                                                                                                                                                                                                                        |

5. Choose **Save**.
6. Return to the **AWS guided setup** page. In the
   **Authentication details** section, choose
   **Review** and confirm the credentials.

## Testing the connection

Before testing the connection, ensure that you have completed all the above
steps.

###### To test the AWS Partner Central API connection

1. Expand **Step 4: Test configuration for Partner Central API integration**.
2. Choose **Test**.

If the connection succeeds, you receive a confirmation message.
