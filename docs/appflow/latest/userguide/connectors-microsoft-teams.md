# Microsoft Teams connector for Amazon AppFlow

Microsoft Teams is a platform developed by Microsoft that helps teams collaborate through
chat, online meetings, and more. If you're a Microsoft Teams user, your account contains data
about your resources, including teams, groups, and channels.
You can use Amazon AppFlow to transfer data from
Microsoft Teams to certain AWS services or other supported applications.

## Amazon AppFlow support for Microsoft Teams

Amazon AppFlow supports Microsoft Teams as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Microsoft Teams.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Microsoft Teams.

## Before you begin

To use Amazon AppFlow to transfer data from Microsoft Teams to supported destinations, you must meet these
requirements:

- You have a Microsoft account with which you've signed up for the following
  services:
  - Microsoft Teams. For more information about the Microsoft Teams data objects that
    Amazon AppFlow supports, see [Supported objects](#microsoft-teams-objects "#microsoft-teams-objects").
  - Microsoft 365.
  - The Microsoft 365 Developer Program.

- In the Microsoft Azure portal, you've created an app registration for Amazon AppFlow. The
  registered app provides the client credentials that Amazon AppFlow uses to access your data securely
  when it makes authenticated calls to your account. For the steps to register an app, see [Register an application
  with the Microsoft identity platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2 "https://learn.microsoft.com/en-us/graph/auth-register-app-v2") in the Microsoft Graph documentation.
- You've configured your registered app with the following settings:
  - You've added one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from Microsoft Teams. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._
  - You've added the recommended permissions below.
  - You've created a client secret.

Note the following values from your registered app because you provide them to Amazon AppFlow when
you connect to your Microsoft Teams account:

- Application (client) ID
- Directory (tenant) ID
- Client secret

### Recommended permissions

Before Amazon AppFlow can securely access your data in Microsoft Teams, your registered app must
allow the necessary permissions for the Microsoft Graph API. We recommend that you enable the
permissions below so that Amazon AppFlow can access all supported data objects.

If you want to grant fewer permissions, you can omit any permissions that apply to objects
that you don't want to transfer.

You can add permissions to your registered app by using the API permissions page in the
Microsoft Azure portal. Configure your permissions as follows:

- Under **Microsoft APIs**, choose **Microsoft
  Graph**.
- For the permissions type, choose **delegated**. For information about
  delegated permissions, see [Permission types](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#using-the-admin-consent-endpoint "https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#using-the-admin-consent-endpoint") in the Microsoft identity platform documentation.
- Add the following recommended permissions:

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

  For information about these permissions, see the [Microsoft Graph
  permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference "https://learn.microsoft.com/en-us/graph/permissions-reference") in the Microsoft Graph documentation.

- Enable the option to grant admin consent to your app. For more information, see [Admin consent](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#admin-consent "https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#admin-consent") in the Microsoft identity platform documentation.

## Connecting Amazon AppFlow to your Microsoft Teams

account

To connect Amazon AppFlow to Microsoft Teams, provide details from your registered app in
Microsoft Azure so that Amazon AppFlow can access your data. If you haven't yet configured your Microsoft
account for Amazon AppFlow integration, see [Before you begin](#microsoft-teams-prereqs "#microsoft-teams-prereqs").

###### To connect to Microsoft Teams

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Microsoft Teams**.
4. Choose **Create connection**.
5. In the **Connect to Microsoft Teams** window, enter the following
   information about your registered app:
   - **Custom authorization tokens URL** – The directory (tenant)
     ID.
   - **Custom authorization code URL** – The directory (tenant)
     ID
   - The **Client ID** and **Client secret**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. A **Sign in** window opens. 9. Enter your user name and password to sign in to your Microsoft account. 10. On the **Permissions requested** page, choose
**Accept**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Microsoft Teams as the data source, you can select this connection.

## Transferring data from Microsoft Teams with a flow

To transfer data from Microsoft Teams, create an Amazon AppFlow flow, and choose Microsoft Teams as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Microsoft Teams, see [Supported objects](#microsoft-teams-objects "#microsoft-teams-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#microsoft-teams-destinations "#microsoft-teams-destinations").

## Supported destinations

When you create a flow that uses Microsoft Teams as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")

## Supported objects

When you create a flow that uses Microsoft Teams as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                       | **Field**                | **Data type**                                             | **Supported filters**  |
| -------------------------------- | ------------------------ | --------------------------------------------------------- | ---------------------- |
| Calendar Event                   | Allow New Time Proposals | Boolean                                                   |                        |
| Attendees                        | List                     |                                                           |
| Body                             | Struct                   |                                                           |
| Body Preview                     | String                   |                                                           |
| Categories                       | List                     |                                                           |
| Change Key                       | String                   |                                                           |
| Created DateTime                 | DateTime                 |                                                           |
| End                              | Struct                   |                                                           |
| Has Attachments                  | Boolean                  |                                                           |
| Hide Attendees                   | Boolean                  |                                                           |
| ICalUId                          | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| Id                               | String                   |                                                           |
| Importance                       | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| Is AllDay                        | Boolean                  |                                                           |
| Is Cancelled                     | Boolean                  |                                                           |
| Is Draft                         | Boolean                  |                                                           |
| Is Online Meeting                | Boolean                  |                                                           |
| Is Organizer                     | Boolean                  |                                                           |
| Is Reminder On                   | Boolean                  |                                                           |
| Last Modified DateTime           | DateTime                 |                                                           |
| Location                         | Struct                   |                                                           |
| Locations                        | List                     |                                                           |
| Occurrence Id                    | String                   |                                                           |
| Online Meeting                   | Struct                   |                                                           |
| Online Meeting Provider          | String                   |                                                           |
| Online Meeting Url               | String                   |                                                           |
| Organizer                        | Struct                   |                                                           |
| Original End Time Zone           | String                   |                                                           |
| Original Start Time Zone         | String                   |                                                           |
| Recurrence                       | Struct                   |                                                           |
| Reminder Minutes Before Start    | Integer                  |                                                           |
| Response Requested               | Boolean                  |                                                           |
| Response Status                  | Struct                   |                                                           |
| Sensitivity                      | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| Series Master Id                 | String                   |                                                           |
| Show As                          | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| Start                            | Struct                   |                                                           |
| Subject                          | String                   | NOT_EQUAL_TO, EQUAL_TO, CONTAINS                          |
| Transaction Id                   | String                   |                                                           |
| Type                             | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| WebLink                          | String                   |                                                           |
| Channel                          | Created DateTime         | DateTime                                                  |                        |
| Description                      | String                   | NOT_EQUAL_TO, EQUAL_TO, CONTAINS                          |
| Display Name                     | String                   | NOT_EQUAL_TO, EQUAL_TO, CONTAINS                          |
| Email                            | String                   |                                                           |
| Id                               | String                   | NOT_EQUAL_TO, EQUAL_TO, CONTAINS                          |
| Is Favorite By Default           | Boolean                  |                                                           |
| Membership Type                  | String                   |                                                           |
| WebUrl                           | String                   |                                                           |
| Channel Message                  | Attachments              | List                                                      |                        |
| Body                             | Struct                   |                                                           |
| Channel Identity                 | Struct                   |                                                           |
| Chat Id                          | String                   |                                                           |
| Created DateTime                 | DateTime                 |                                                           |
| Deleted DateTime                 | DateTime                 |                                                           |
| Etag                             | String                   |                                                           |
| Event Detail                     | Struct                   |                                                           |
| From                             | Struct                   |                                                           |
| Id                               | String                   |                                                           |
| Importance                       | String                   |                                                           |
| Last Edited DateTime             | DateTime                 |                                                           |
| Last Modified DateTime           | DateTime                 |                                                           |
| Locale                           | String                   |                                                           |
| Mentions                         | List                     |                                                           |
| Message Type                     | String                   |                                                           |
| Policy Violation                 | Struct                   |                                                           |
| Reactions                        | List                     |                                                           |
| Reply To Id                      | String                   |                                                           |
| Subject                          | String                   |                                                           |
| Summary                          | String                   |                                                           |
| WebUrl                           | String                   |                                                           |
| Channel Message Reply            | Attachments              | List                                                      |                        |
| Body                             | Struct                   |                                                           |
| Channel Identity                 | Struct                   |                                                           |
| Chat Id                          | String                   |                                                           |
| Created DateTime                 | DateTime                 |                                                           |
| Etag                             | String                   |                                                           |
| Event Detail                     | Struct                   |                                                           |
| From                             | Struct                   |                                                           |
| Id                               | String                   |                                                           |
| Importance                       | String                   |                                                           |
| Last Edited DateTime             | DateTime                 |                                                           |
| Last Modified DateTime           | DateTime                 |                                                           |
| Locale                           | String                   |                                                           |
| Mentions                         | List                     |                                                           |
| Message Type                     | String                   |                                                           |
| Policy Violation                 | Struct                   |                                                           |
| Reactions                        | List                     |                                                           |
| Reply To Id                      | String                   |                                                           |
| Subject                          | String                   |                                                           |
| Summary                          | String                   |                                                           |
| WebUrl                           | String                   |                                                           |
| dDeleted DateTime                | DateTime                 |                                                           |
| Channel Tab                      | Configuration            | Struct                                                    |                        |
| Display Name                     | String                   | NOT_EQUAL_TO, EQUAL_TO, CONTAINS                          |
| Id                               | String                   | NOT_EQUAL_TO, EQUAL_TO, CONTAINS                          |
| WebUrl                           | String                   |                                                           |
| Chat                             | Chat Type                | String                                                    | NOT_EQUAL_TO, EQUAL_TO |
| Created DateTime                 | DateTime                 |                                                           |
| Id                               | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| Last Updated DateTime            | DateTime                 |                                                           |
| Online Meeting Info              | Struct                   |                                                           |
| Tenant Id                        | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| Topic                            | String                   | NOT_EQUAL_TO, EQUAL_TO                                    |
| WebUrl                           | String                   |                                                           |
| Group                            | Classification           | String                                                    |                        |
| Created DateTime                 | DateTime                 |                                                           |
| Creation Options                 | List                     |                                                           |
| Deleted DateTime                 | DateTime                 |                                                           |
| Description                      | String                   |                                                           |
| Display Name                     | String                   | EQUAL_TO                                                  |
| Expiration DateTime              | DateTime                 |                                                           |
| Group Types                      | List                     |                                                           |
| Id                               | String                   | EQUAL_TO                                                  |
| Is Assignable To Role            | Boolean                  |                                                           |
| Mail                             | String                   | EQUAL_TO                                                  |
| Mail Enabled                     | Boolean                  | EQUAL_TO                                                  |
| Mail Nickname                    | String                   | EQUAL_TO                                                  |
| Membership Rule                  | String                   | EQUAL_TO                                                  |
| Membership Rule Processing State | String                   | EQUAL_TO                                                  |
| On Premises Domain Name          | String                   |                                                           |
| On Premises Last Sync DateTime   | DateTime                 |                                                           |
| On Premises Net Bios Name        | String                   |                                                           |
| On Premises Provisioning Errors  | List                     |                                                           |
| On Premises Sam Account Name     | String                   |                                                           |
| On Premises Sync Enabled         | Boolean                  |                                                           |
| OnPremises Security Identifier   | String                   |                                                           |
| Preferred Data Location          | String                   |                                                           |
| Preferred Language               | String                   |                                                           |
| Proxy Addresses                  | List                     |                                                           |
| Renewed DateTime                 | DateTime                 | EQUAL_TO, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| Resource Behavior Options        | List                     |                                                           |
| Resource Provisioning Options    | List                     |                                                           |
| Security Enabled                 | Boolean                  | EQUAL_TO                                                  |
| Security Identifier              | String                   |                                                           |
| Theme                            | String                   |                                                           |
| Visibility                       | String                   |                                                           |
| Group Member                     | Business Phones          | List                                                      |                        |
| Display Name                     | String                   |                                                           |
| Given Name                       | String                   |                                                           |
| Id                               | String                   | EQUAL_TO                                                  |
| Job Title                        | String                   |                                                           |
| Mail                             | String                   |                                                           |
| Mobile Phone                     | String                   |                                                           |
| Office Location                  | String                   |                                                           |
| Preferred Language               | String                   |                                                           |
| Surname                          | String                   |                                                           |
| User Principal Name              | String                   |                                                           |
| Team                             | Classification           | String                                                    |                        |
| Created DateTime                 | DateTime                 |                                                           |
| Description                      | String                   |                                                           |
| Discovery Settings               | Struct                   |                                                           |
| Display Name                     | String                   |                                                           |
| Fun Settings                     | Struct                   |                                                           |
| Guest Settings                   | Struct                   |                                                           |
| Id                               | String                   |                                                           |
| Internal Id                      | String                   |                                                           |
| Is Archived                      | Boolean                  |                                                           |
| Is Membership Limited To Owners  | Boolean                  |                                                           |
| Member Settings                  | Struct                   |                                                           |
| Messaging Settings               | Struct                   |                                                           |
| Specialization                   | String                   |                                                           |
| Summary                          | String                   |                                                           |
| Visibility                       | Struct                   |                                                           |
| WebUrl                           | String                   |                                                           |
| Team Member                      | Display Name             | String                                                    | NOT_EQUAL_TO, EQUAL_TO |
| Email                            | String                   |                                                           |
| Id                               | String                   |                                                           |
| Roles                            | List                     |                                                           |
| Tenant Id                        | String                   |                                                           |
| User Id                          | String                   |                                                           |
| Visible History Start DateTime   | DateTime                 |                                                           |
