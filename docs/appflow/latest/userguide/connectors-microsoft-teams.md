

# Microsoft Teams connector for Amazon AppFlow
<a name="connectors-microsoft-teams"></a>

Microsoft Teams is a platform developed by Microsoft that helps teams collaborate through chat, online meetings, and more. If you're a Microsoft Teams user, your account contains data about your resources, including teams, groups, and channels. You can use Amazon AppFlow to transfer data from Microsoft Teams to certain AWS services or other supported applications.

## Amazon AppFlow support for Microsoft Teams
<a name="microsoft-teams-support"></a>

Amazon AppFlow supports Microsoft Teams as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Microsoft Teams.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Microsoft Teams.

## Before you begin
<a name="microsoft-teams-prereqs"></a>

To use Amazon AppFlow to transfer data from Microsoft Teams to supported destinations, you must meet these requirements:
+ You have a Microsoft account with which you've signed up for the following services:
  + Microsoft Teams. For more information about the Microsoft Teams data objects that Amazon AppFlow supports, see [Supported objects](#microsoft-teams-objects).
  + Microsoft 365.
  + The Microsoft 365 Developer Program.
+ In the Microsoft Azure portal, you've created an app registration for Amazon AppFlow. The registered app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to register an app, see [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2) in the Microsoft Graph documentation.
+ You've configured your registered app with the following settings:
  + You've added one or more redirect URLs for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Microsoft Teams. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
  + You've added the recommended permissions below.
  + You've created a client secret.

Note the following values from your registered app because you provide them to Amazon AppFlow when you connect to your Microsoft Teams account:
+ Application (client) ID
+ Directory (tenant) ID
+ Client secret

### Recommended permissions
<a name="microsoft-teams-permissions"></a>

Before Amazon AppFlow can securely access your data in Microsoft Teams, your registered app must allow the necessary permissions for the Microsoft Graph API. We recommend that you enable the permissions below so that Amazon AppFlow can access all supported data objects.

If you want to grant fewer permissions, you can omit any permissions that apply to objects that you don't want to transfer.

You can add permissions to your registered app by using the API permissions page in the Microsoft Azure portal. Configure your permissions as follows:
+ Under **Microsoft APIs**, choose **Microsoft Graph**.
+ For the permissions type, choose **delegated**. For information about delegated permissions, see [Permission types](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#using-the-admin-consent-endpoint) in the Microsoft identity platform documentation.
+ Add the following recommended permissions:
  + `User.Read`
  + `Offline_access`
  + `User.Read.All`
  + `User.ReadWrite.All`
  + `TeamsTab.ReadWriteForTeam`
  + `TeamsTab.ReadWriteForChat`
  + `TeamsTab.ReadWrite.All`
  + `TeamsTab.Read.All`
  + `TeamSettings.ReadWrite.All`
  + `TeamSettings.Read.All`
  + `TeamMember.ReadWrite.All`
  + `TeamMember.Read.All`
  + `Team.ReadBasic.All`
  + `GroupMember.ReadWrite.All`
  + `GroupMember.Read.All`
  + `Group.ReadWrite.All`
  + `Group.Read.All`
  + `Directory.ReadWrite.All`
  + `Directory.Read.All`
  + `Directory.AccessAsUser.All`
  + `Chat.ReadWrite`
  + `Chat.ReadBasic`
  + `Chat.Read`
  + `ChannelSettings.ReadWrite.All`
  + `ChannelSettings.Read.All`
  + `ChannelMessage.Read.All`
  + `Channel.ReadBasic.All`

  For information about these permissions, see the [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference) in the Microsoft Graph documentation.
+ Enable the option to grant admin consent to your app. For more information, see [Admin consent](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#admin-consent) in the Microsoft identity platform documentation.

## Connecting Amazon AppFlow to your Microsoft Teams account
<a name="microsoft-teams-connecting"></a>

To connect Amazon AppFlow to Microsoft Teams, provide details from your registered app in Microsoft Azure so that Amazon AppFlow can access your data. If you haven't yet configured your Microsoft account for Amazon AppFlow integration, see [Before you begin](#microsoft-teams-prereqs).

**To connect to Microsoft Teams**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Microsoft Teams**.

1. Choose **Create connection**.

1. In the **Connect to Microsoft Teams** window, enter the following information about your registered app:
   + **Custom authorization tokens URL** – The directory (tenant) ID.
   + **Custom authorization code URL** – The directory (tenant) ID
   + The **Client ID** and **Client secret**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**. A **Sign in** window opens.

1. Enter your user name and password to sign in to your Microsoft account.

1. On the **Permissions requested** page, choose **Accept**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Microsoft Teams as the data source, you can select this connection.

## Transferring data from Microsoft Teams with a flow
<a name="microsoft-teams-transfer-data"></a>



To transfer data from Microsoft Teams, create an Amazon AppFlow flow, and choose Microsoft Teams as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Microsoft Teams, see [Supported objects](#microsoft-teams-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#microsoft-teams-destinations).

## Supported destinations
<a name="microsoft-teams-destinations"></a>

When you create a flow that uses Microsoft Teams as the data source, you can set the destination to any of the following connectors: 
+ [Amazon Lookout for Metrics](lookout.md)
+ [Amazon Redshift](redshift.md)
+ [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md)
+ [Amazon S3](s3.md)
+ [HubSpot](connectors-hubspot.md)
+ [Marketo](marketo.md)
+ [Salesforce](salesforce.md)
+ [SAP OData](sapodata.md)
+ [Snowflake](snowflake.md)
+ [Upsolver](upsolver.md)
+ [Zendesk](zendesk.md)
+ [Zoho CRM](connectors-zoho-crm.md)

## Supported objects
<a name="microsoft-teams-objects"></a>

When you create a flow that uses Microsoft Teams as the data source, you can transfer any of the following data objects to supported destinations:



- ** Calendar Event**
  - **** Field**:** Allow New Time Proposals / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Attendees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Body Preview / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Categories / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Change Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** End / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Has Attachments / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Hide Attendees / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ICalUId / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Importance / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Is AllDay / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Cancelled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Draft / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Online Meeting / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Organizer / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Reminder On / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Last Modified DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Location / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Locations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Occurrence Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Online Meeting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Online Meeting Provider / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Online Meeting Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organizer / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Original End Time Zone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Original Start Time Zone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Recurrence / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reminder Minutes Before Start / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Response Requested / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Response Status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Sensitivity / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Series Master Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Show As / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Start / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Subject / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO, CONTAINS
  - **** Field**:** Transaction Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** WebLink / **** Data type**:** String / **** Supported filters**:** 

- ** Channel**
  - **** Field**:** Created DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO, CONTAINS
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO, CONTAINS
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO, CONTAINS
  - **** Field**:** Is Favorite By Default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Membership Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** WebUrl / **** Data type**:** String / **** Supported filters**:** 

- ** Channel Message**
  - **** Field**:** Attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Channel Identity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Chat Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Deleted DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Etag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Event Detail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** From / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Importance / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Edited DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Modified DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mentions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Message Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Policy Violation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reactions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Reply To Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subject / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** WebUrl / **** Data type**:** String / **** Supported filters**:** 

- ** Channel Message Reply**
  - **** Field**:** Attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Channel Identity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Chat Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Etag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Event Detail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** From / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Importance / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Edited DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Modified DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mentions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Message Type  / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Policy Violation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reactions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Reply To Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subject / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** WebUrl / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** dDeleted DateTime / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Channel Tab**
  - **** Field**:** Configuration / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO, CONTAINS
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO, CONTAINS
  - **** Field**:** WebUrl / **** Data type**:** String / **** Supported filters**:** 

- ** Chat**
  - **** Field**:** Chat Type / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Created DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Last Updated DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Online Meeting Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Tenant Id / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Topic / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** WebUrl / **** Data type**:** String / **** Supported filters**:** 

- ** Group**
  - **** Field**:** Classification / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creation Options / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Deleted DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Expiration DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Group Types / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Is Assignable To Role / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Mail / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Mail Enabled / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Mail Nickname / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Membership Rule / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Membership Rule Processing State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** On Premises Domain Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** On Premises Last Sync DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** On Premises Net Bios Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** On Premises Provisioning Errors / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** On Premises Sam Account Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** On Premises Sync Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** OnPremises Security Identifier / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Preferred Data Location / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Preferred Language / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Proxy Addresses / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Renewed DateTime / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Resource Behavior Options / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Resource Provisioning Options / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Security Enabled / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Security Identifier / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Theme / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Visibility / **** Data type**:** String / **** Supported filters**:** 

- ** Group Member**
  - **** Field**:** Business Phones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Given Name  / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Job Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mail / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mobile Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Office Location / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Preferred Language / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Surname / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** User Principal Name / **** Data type**:** String / **** Supported filters**:** 

- ** Team**
  - **** Field**:** Classification / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created DateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Discovery Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fun Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Guest Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Internal Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Archived / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Membership Limited To Owners / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Member Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Messaging Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Specialization / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Visibility / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** WebUrl / **** Data type**:** String / **** Supported filters**:** 

- ** Team Member**
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** NOT\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Roles / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Tenant Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** User Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Visible History Start DateTime / **** Data type**:** DateTime / **** Supported filters**:** 

