# Intercom connector for Amazon AppFlow

Intercom is a customer engagement solution. It helps organizations learn who is
using a website or product so that the organization can engage those users with targeted messages
and support. If you're an Intercom user, then your account contains data about your
contacts, conversations, customer segments, and more. You can use Amazon AppFlow to transfer data from
Intercom to certain AWS services or other supported applications.

## Amazon AppFlow support for Intercom

Amazon AppFlow supports Intercom as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Intercom.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Intercom.

## Before you begin

To use Amazon AppFlow to transfer data from Intercom to supported destinations, you must meet these
requirements:

- You have an account with Intercom that contains the data that you want to transfer. For more
  information about the Intercom data objects that Amazon AppFlow supports, see [Supported objects](#intercom-objects "#intercom-objects").
- In your Intercom account, you've created an app for Amazon AppFlow. The app provides
  the credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls
  to your account. For the steps to create an app, see [How do I create
  an app?](https://www.intercom.com/help/en/articles/1827298-how-do-i-create-an-app "https://www.intercom.com/help/en/articles/1827298-how-do-i-create-an-app") in the Intercom Help Center.
- You've configured the app with a redirect URL for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Intercom. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

###### Note

You must add your connecting profile region redirect URL (or URLs) to the list of redirect URLs in your Intercom app. If you don’t make this addition, the app defaults to the first redirect URL in the list, and your connection will fail. For more information, see
[Redirect URLs](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/setting-up-oauth/#redirect-urls " https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/setting-up-oauth/#redirect-urls ")  
in the Intercom Developer Platform Help Center.

From the settings for your app, note the client ID and client Secret. You provide these
values to Amazon AppFlow when you connect to your Intercom account.

## Connecting Amazon AppFlow to your Intercom account

To connect Amazon AppFlow to your Intercom account, provide the client credentials from
your Intercom app so that Amazon AppFlow can access your data. If you haven't yet configured
your Intercom account for Amazon AppFlow integration, see [Before you begin](#intercom-prereqs "#intercom-prereqs").

###### To connect to Intercom

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Intercom**.
4. Choose **Create connection**.
5. In the **Connect to Intercom** window, enter the following
   information:

   - **Authorization tokens URL** — Choose the URL based on the data
     host region where you use Intercom (Europe, US, Australia).
   - **Authorization code URL** — Choose the URL based on the data
     host region where you use Intercom (Europe, US, Australia).
   - **Client ID** — The client ID from your Intercom
     app.
   - **Client secret** — The client secret from your
     Intercom app.
   - ****Instance URL**** — Choose the
     URL based on the data host region where you use Intercom (Europe, US,
     Australia).

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Intercom account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Intercom as the data source, you can select this connection.

## Transferring data from Intercom with a flow

To transfer data from Intercom, create an Amazon AppFlow flow, and choose Intercom as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Intercom, see [Supported objects](#intercom-objects "#intercom-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#intercom-destinations "#intercom-destinations").

## Supported destinations

When you create a flow that uses Intercom as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Intercom as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                     | **Field**         | **Data type**                                        | **Supported filters**                                |
| ------------------------------ | ----------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| Admin                          | Avatar            | Struct                                               |                                                      |
| Away Mode Enabled              | Boolean           |                                                      |
| Away Mode Reassign             | Boolean           |                                                      |
| Email                          | String            |                                                      |
| Has Inbox Seat                 | Boolean           |                                                      |
| Id                             | String            |                                                      |
| Job Title                      | String            |                                                      |
| Name                           | String            |                                                      |
| Team Ids                       | List              |                                                      |
| Type                           | String            |                                                      |
| Company                        | App Id            | String                                               |                                                      |
| Company Id                     | String            |                                                      |
| Created At                     | Date              |                                                      |
| Custom Attributes              | Struct            |                                                      |
| Id                             | String            |                                                      |
| Industry                       | String            |                                                      |
| Last Request At                | Date              |                                                      |
| Monthly Spend                  | Integer           |                                                      |
| Name                           | String            |                                                      |
| Plan                           | Struct            |                                                      |
| Remote Created At              | Date              |                                                      |
| Segments                       | Struct            |                                                      |
| Session Count                  | Integer           |                                                      |
| Size                           | Integer           |                                                      |
| Tags                           | Struct            |                                                      |
| Type                           | String            |                                                      |
| Updated At                     | Date              |                                                      |
| User Count                     | Integer           |                                                      |
| Website                        | String            |                                                      |
| Contact                        | Android App Name  | String                                               | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Android App Version            | String            |                                                      |
| Android Device                 | String            |                                                      |
| Android Last Seen At           | Date              |                                                      |
| Android Os Version             | String            |                                                      |
| Android Sdk Version            | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Avatar                         | String            |                                                      |
| Browser                        | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Browser Language               | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Browser Version                | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| City                           | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Companies                      | List              |                                                      |
| Country                        | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Created At                     | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Custom Attributes              | Struct            |                                                      |
| Email                          | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| External Id                    | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Has Hard Bounced               | Boolean           | EQUAL\_TO                                            |
| Id                             | String            | EQUAL\_TO, NOT\_EQUAL\_TO                            |
| Ios App Name                   | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Ios App Version                | String            |                                                      |
| Ios Device                     | String            |                                                      |
| Ios Last Seen At               | Date              |                                                      |
| Ios Os Version                 | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Ios Sdk Version                | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Language Override              | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Last Contacted At              | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Last Email Clicked At          | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Last Email Opened At           | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Last Replied At                | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Last Seen At                   | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Location                       | Struct            |                                                      |
| Marked Email As Spam           | Boolean           | EQUAL\_TO                                            |
| Name                           | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Notes                          | List              |                                                      |
| Opted Out Subscription Types   | Struct            |                                                      |
| Os                             | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Owner Id                       | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Phone                          | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Referrer                       | Struct            |                                                      |
| Region                         | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Role                           | String            | EQUAL\_TO, NOT\_EQUAL\_TO                            |
| SMS Content                    | Boolean           |                                                      |
| Signed Up At                   | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Social Profiles                | List              |                                                      |
| Tags                           | List              |                                                      |
| Type                           | String            |                                                      |
| Unsubscribed From Emails       | Boolean           | EQUAL\_TO                                            |
| Unsubscribed From SMS          | Boolean           |                                                      |
| Updated At                     | Date              | GREATER\_THAN, LESS\_THAN, EQUAL\_TO                 |
| Utm Campaign                   | String            |                                                      |
| Utm Content                    | String            |                                                      |
| Utm Medium                     | String            |                                                      |
| Utm Source                     | String            |                                                      |
| Utm Term                       | String            |                                                      |
| Workspace Id                   | String            |                                                      |
| Conversation                   | Admin Assignee Id | Integer                                              | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Contacts                       | List              |                                                      |
| Conversation Parts             | List              |                                                      |
| Conversation Rating            | Struct            |                                                      |
| Count assignments              | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Count conversation parts       | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Count reopens                  | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Created At                     | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Custom Attributes              | Struct            |                                                      |
| First Contact Reply            | Struct            |                                                      |
| First admin reply at           | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| First assignment at            | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| First close at                 | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| First contact reply at         | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Id                             | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Last admin reply at            | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Last assignment admin reply at | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Last assignment at             | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Last close at                  | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Last closed by Id              | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Last contact reply at          | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Median time to reply           | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Open                           | Boolean           | EQUAL\_TO                                            |
| Priority                       | String            | EQUAL\_TO, NOT\_EQUAL\_TO                            |
| Rating admin id                | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Rating contact id              | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Rating remark                  | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Rating requested at            | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Rating requested at            | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Rating score                   | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Read                           | Boolean           | EQUAL\_TO                                            |
| Sla Applied                    | Struct            |                                                      |
| Snoozed Until                  | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Source                         | Struct            |                                                      |
| Source Id                      | String            | EQUAL\_TO, NOT\_EQUAL\_TO                            |
| Source author email            | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Source author id               | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Source author name             | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Source author type             | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Source body                    | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Source delivered as            | String            | EQUAL\_TO, NOT\_EQUAL\_TO                            |
| Source subject                 | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Source type                    | String            | EQUAL\_TO, NOT\_EQUAL\_TO                            |
| Source url                     | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| State                          | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Statistics                     | Struct            |                                                      |
| Tags                           | List              |                                                      |
| Team Assignee Id               | String            | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO                  |
| Teammates                      | List              |                                                      |
| Time to admin reply            | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Time to assignment             | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Time to first close            | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Time to last close             | Integer           | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN |
| Title                          | String            |                                                      |
| Topics                         | List              |                                                      |
| Type                           | String            |                                                      |
| Updated At                     | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Waiting Since                  | DateTime          | GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO |
| Data Attribute                 | Admin Id          | String                                               |                                                      |
| Api Writable                   | Boolean           |                                                      |
| Archived                       | Boolean           |                                                      |
| Created At                     | Date              |                                                      |
| Custom                         | Boolean           |                                                      |
| Data Type                      | String            |                                                      |
| Description                    | String            |                                                      |
| Full Name                      | String            |                                                      |
| Id                             | Integer           |                                                      |
| Label                          | String            |                                                      |
| Model                          | String            |                                                      |
| Name                           | String            |                                                      |
| Options                        | List              |                                                      |
| Type                           | String            |                                                      |
| Ui Writable                    | Boolean           |                                                      |
| Updated At                     | Date              |                                                      |
| Segment                        | Count             | Integer                                              |                                                      |
| Created At                     | Date              |                                                      |
| Id                             | String            |                                                      |
| Name                           | String            |                                                      |
| Person Type                    | String            |                                                      |
| Type                           | String            |                                                      |
| Updated At                     | Date              |                                                      |
| Tag                            | Id                | String                                               |                                                      |
| Name                           | String            |                                                      |
| Type                           | String            |                                                      |
| Team                           | Admin Ids         | List                                                 |                                                      |
| Id                             | String            |                                                      |
| Name                           | String            |                                                      |
| Type                           | String            |                                                      |
