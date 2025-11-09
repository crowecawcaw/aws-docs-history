# Google Calendar connector for Amazon AppFlow

Google Calendar is an online calendar service that helps users schedule meetings, set up
events, set reminders, and share their schedules. If you're a Google Calendar user, your
account contains data about your calendar, events, access controls list rules, and more.
You can use Amazon AppFlow to transfer data from
Google Calendar to certain AWS services or other supported applications.

## Amazon AppFlow support for Google Calendar

Amazon AppFlow supports Google Calendar as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Google Calendar.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Google Calendar.

## Before you begin

To use Amazon AppFlow to transfer data from Google Calendar to supported destinations, you must meet these
requirements:

- You have a Google account that you use to sign in and use the Google Calendar app. In
  your Google account, Google Calendar contains the data that you want to transfer.
- You have a Google Cloud Platform account and a Google Cloud project.
- In your Google Cloud project, you've enabled the Google Calendar API. For the steps to
  enable it, see [Enable and
  disable APIs](https://support.google.com/googleapi/answer/6158841 "https://support.google.com/googleapi/answer/6158841") in the API Console Help for Google Cloud Platform.
- In your Google Cloud project, you've configured an OAuth consent screen for external
  users. For information about the OAuth consent screen, see [Setting up your OAuth consent
  screen](https://support.google.com/cloud/answer/10311615# "https://support.google.com/cloud/answer/10311615#") in the Google Cloud Platform Console Help.
- In your Google Cloud project, you've configured an OAuth 2.0 client ID that meets the
  following requirements:

      + You've set the application type to **Web application**.
      + You've added one or more authorized redirect URLs for Amazon AppFlow.


      Redirect URLs have the following format:



      ```
      https://`region`.console.aws.amazon.com/appflow/oauth
      ```

      In this URL, *region* is the code for the AWS Region
       where you use Amazon AppFlow to transfer data from Google Calendar. For example, the code for the US East (N. Virginia)
       Region is `us-east-1`. For that Region, the URL is the following:



      ```
      https://us-east-1.console.aws.amazon.com/appflow/oauth
      ```

      For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
       in the *AWS General Reference.*

  For the steps to create an OAuth 2.0 client ID, see [Setting up OAuth
  2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy= "https://support.google.com/cloud/answer/6158849?hl=en#zippy=") in the Google Cloud Platform Console Help.

Note the client ID and client secret from the settings for your OAuth 2.0 client ID. You
provide these values to Amazon AppFlow when you connect to your Google Cloud project.

## Connecting Amazon AppFlow to your Google Calendar

account

To connect Amazon AppFlow to Google Calendar, provide the client credentials from the OAuth 2.0
client ID from your Google Cloud project. Amazon AppFlow uses these credentials to access your data. If
you haven't yet configured your Google Cloud project for Amazon AppFlow integration, see [Before you begin](#google-calendar-prereqs "#google-calendar-prereqs").

###### To connect to Google Calendar

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Google Calendar**.
4. Choose **Create connection**.
5. In the **Connect to Google Calendar** window, enter the following
   information:
   - **Access type** – Choose **offline**.
   - **Client ID** – The client ID of the OAuth 2.0 client ID in your
     Google Cloud project.
   - **Client secret** – The client secret of the OAuth 2.0 client ID
     in your Google Cloud project.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Google account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Google Calendar as the data source, you can select this connection.

## Transferring data from Google Calendar with a flow

To transfer data from Google Calendar, create an Amazon AppFlow flow, and choose Google Calendar as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Google Calendar, see [Supported objects](#google-calendar-objects "#google-calendar-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#google-calendar-destinations "#google-calendar-destinations").

## Supported destinations

When you create a flow that uses Google Calendar as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Google Calendar as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**               | **Field**        | **Data type**          | **Supported filters** |
| ------------------------ | ---------------- | ---------------------- | --------------------- |
| Access Control List Rule | etag             | String                 |                       |
| id                       | String           |                        |
| kind                     | String           |                        |
| role                     | String           |                        |
| scope                    | Struct           |                        |
| showDeleted              | Boolean          | EQUAL_TO, NOT_EQUAL_TO |
| Calendar                 | accessRole       | String                 |                       |
| backgroundColor          | String           |                        |
| colorId                  | String           |                        |
| conferenceProperties     | Struct           |                        |
| defaultReminders         | List             |                        |
| deleted                  | Boolean          |                        |
| description              | String           |                        |
| etag                     | String           |                        |
| foregroundColor          | String           |                        |
| hidden                   | Boolean          |                        |
| id                       | String           |                        |
| kind                     | String           |                        |
| location                 | String           |                        |
| minAccessRole            | String           | EQUAL_TO               |
| notificationSettings     | Struct           |                        |
| primary                  | Boolean          |                        |
| selected                 | Boolean          |                        |
| showDeleted              | Boolean          | EQUAL_TO, NOT_EQUAL_TO |
| showHidden               | Boolean          | EQUAL_TO, NOT_EQUAL_TO |
| summary                  | String           |                        |
| summaryOverride          | String           |                        |
| timeZone                 | String           |                        |
| Event                    | anyoneCanAddSelf | Boolean                |                       |
| attachments              | List             |                        |
| attendees                | List             |                        |
| attendeesOmitted         | Boolean          |                        |
| colorId                  | String           |                        |
| conferenceData           | Struct           |                        |
| created                  | DateTime         |                        |
| creator                  | Struct           |                        |
| description              | String           |                        |
| end                      | Struct           |                        |
| endTimeUnspecified       | Boolean          |                        |
| etag                     | String           |                        |
| eventType                | String           |                        |
| extendedProperties       | Struct           |                        |
| gadget                   | Struct           |                        |
| guestsCanInviteOthers    | Boolean          |                        |
| guestsCanModify          | Boolean          |                        |
| guestsCanSeeOtherGuests  | Boolean          |                        |
| hangoutLink              | String           |                        |
| htmlLink                 | String           |                        |
| iCalUID                  | String           | EQUAL_TO               |
| id                       | String           |                        |
| kind                     | String           |                        |
| location                 | String           |                        |
| locked                   | Boolean          |                        |
| maxAttendees             | Integer          | EQUAL_TO               |
| orderBy                  | String           | EQUAL_TO               |
| organizer                | Struct           |                        |
| originalStartTime        | Struct           |                        |
| privateCopy              | Boolean          |                        |
| privateExtendedProperty  | String           | EQUAL_TO               |
| q                        | String           | EQUAL_TO               |
| recurrence               | List             |                        |
| recurringEventId         | String           |                        |
| reminders                | Struct           |                        |
| sequence                 | Integer          |                        |
| sharedExtendedProperty   | String           | EQUAL_TO               |
| showDeleted              | Boolean          | EQUAL_TO, NOT_EQUAL_TO |
| singleEvents             | Boolean          | EQUAL_TO, NOT_EQUAL_TO |
| source                   | Struct           |                        |
| start                    | Struct           |                        |
| status                   | String           |                        |
| summary                  | String           |                        |
| timeMax                  | DateTime         | EQUAL_TO               |
| timeMin                  | DateTime         | EQUAL_TO               |
| transparency             | String           |                        |
| updated                  | DateTime         |                        |
| updatedMin               | DateTime         | EQUAL_TO               |
| visibility               | String           |                        |
| My Calendar              | accessRole       | String                 |                       |
| backgroundColor          | String           |                        |
| colorId                  | String           |                        |
| conferenceProperties     | Struct           |                        |
| defaultReminders         | List             |                        |
| deleted                  | Boolean          |                        |
| description              | String           |                        |
| etag                     | String           |                        |
| foregroundColor          | String           |                        |
| hidden                   | Boolean          |                        |
| id                       | String           |                        |
| kind                     | String           |                        |
| location                 | String           |                        |
| notificationSettings     | Struct           |                        |
| primary                  | Boolean          |                        |
| selected                 | Boolean          |                        |
| showDeleted              | Boolean          | EQUAL_TO, NOT_EQUAL_TO |
| showHidden               | Boolean          | EQUAL_TO, NOT_EQUAL_TO |
| summary                  | String           |                        |
| summaryOverride          | String           |                        |
| timeZone                 | String           |                        |
