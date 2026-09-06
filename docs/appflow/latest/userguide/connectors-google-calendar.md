

# Google Calendar connector for Amazon AppFlow
<a name="connectors-google-calendar"></a>

Google Calendar is an online calendar service that helps users schedule meetings, set up events, set reminders, and share their schedules. If you're a Google Calendar user, your account contains data about your calendar, events, access controls list rules, and more. You can use Amazon AppFlow to transfer data from Google Calendar to certain AWS services or other supported applications.

## Amazon AppFlow support for Google Calendar
<a name="google-calendar-support"></a>

Amazon AppFlow supports Google Calendar as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Google Calendar.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Google Calendar.

## Before you begin
<a name="google-calendar-prereqs"></a>

To use Amazon AppFlow to transfer data from Google Calendar to supported destinations, you must meet these requirements:
+ You have a Google account that you use to sign in and use the Google Calendar app. In your Google account, Google Calendar contains the data that you want to transfer.
+ You have a Google Cloud Platform account and a Google Cloud project.
+ In your Google Cloud project, you've enabled the Google Calendar API. For the steps to enable it, see [Enable and disable APIs](https://support.google.com/googleapi/answer/6158841) in the API Console Help for Google Cloud Platform.
+ In your Google Cloud project, you've configured an OAuth consent screen for external users. For information about the OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615#) in the Google Cloud Platform Console Help.
+ In your Google Cloud project, you've configured an OAuth 2.0 client ID that meets the following requirements:
  + You've set the application type to **Web application**.
  + You've added one or more authorized redirect URLs for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Google Calendar. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

  For the steps to create an OAuth 2.0 client ID, see [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy=) in the Google Cloud Platform Console Help.

Note the client ID and client secret from the settings for your OAuth 2.0 client ID. You provide these values to Amazon AppFlow when you connect to your Google Cloud project.

## Connecting Amazon AppFlow to your Google Calendar account
<a name="google-calendar-connecting"></a>

To connect Amazon AppFlow to Google Calendar, provide the client credentials from the OAuth 2.0 client ID from your Google Cloud project. Amazon AppFlow uses these credentials to access your data. If you haven't yet configured your Google Cloud project for Amazon AppFlow integration, see [Before you begin](#google-calendar-prereqs).

**To connect to Google Calendar**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Google Calendar**.

1. Choose **Create connection**.

1. In the **Connect to Google Calendar** window, enter the following information:
   + **Access type** – Choose **offline**.
   + **Client ID** – The client ID of the OAuth 2.0 client ID in your Google Cloud project.
   + **Client secret** – The client secret of the OAuth 2.0 client ID in your Google Cloud project.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Google account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Google Calendar as the data source, you can select this connection.

## Transferring data from Google Calendar with a flow
<a name="google-calendar-transfer-data"></a>

To transfer data from Google Calendar, create an Amazon AppFlow flow, and choose Google Calendar as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Google Calendar, see [Supported objects](#google-calendar-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#google-calendar-destinations).

## Supported destinations
<a name="google-calendar-destinations"></a>

When you create a flow that uses Google Calendar as the data source, you can set the destination to any of the following connectors: 
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
<a name="google-calendar-objects"></a>

When you create a flow that uses Google Calendar as the data source, you can transfer any of the following data objects to supported destinations:



- ** Access Control List Rule**
  - **** Field**:** etag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** role / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** scope / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** showDeleted / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO

- ** Calendar**
  - **** Field**:** accessRole / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** backgroundColor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** colorId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** conferenceProperties / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** defaultReminders / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** etag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** foregroundColor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** hidden / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** location / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** minAccessRole / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** notificationSettings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** primary / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** selected / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** showDeleted / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** showHidden / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** summaryOverride / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** timeZone / **** Data type**:** String / **** Supported filters**:** 

- ** Event**
  - **** Field**:** anyoneCanAddSelf / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** attendees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** attendeesOmitted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** colorId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** conferenceData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** creator / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** end / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** endTimeUnspecified / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** etag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** eventType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** extendedProperties / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** gadget / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** guestsCanInviteOthers / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** guestsCanModify / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** guestsCanSeeOtherGuests / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** hangoutLink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** htmlLink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** iCalUID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** location / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** maxAttendees / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** orderBy / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** organizer / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** originalStartTime / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** privateCopy / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** privateExtendedProperty / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** q / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** recurrence / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** recurringEventId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reminders / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** sequence / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** sharedExtendedProperty / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** showDeleted / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** singleEvents / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** source / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** start / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** timeMax / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** timeMin / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** transparency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updated / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updatedMin / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** visibility / **** Data type**:** String / **** Supported filters**:** 

- ** My Calendar**
  - **** Field**:** accessRole / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** backgroundColor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** colorId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** conferenceProperties / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** defaultReminders / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** etag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** foregroundColor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** hidden / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** location / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** notificationSettings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** primary / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** selected / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** showDeleted / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** showHidden / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** summaryOverride / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** timeZone / **** Data type**:** String / **** Supported filters**:** 

