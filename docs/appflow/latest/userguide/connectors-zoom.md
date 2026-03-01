# Zoom connector for Amazon AppFlow

Zoom is an online video conferencing solution for individuals and teams. If
you're a Zoom user, your account contains data about your resources, such as users,
groups, and rooms. You can use Amazon AppFlow to transfer data from
Zoom to certain AWS services or other supported applications.

## Amazon AppFlow support for Zoom

Amazon AppFlow supports Zoom as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Zoom.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Zoom.

**Supported Zoom plans**

Amazon AppFlow supports only paid plans for Zoom, such as Pro, Business, or
Enterprise. You can’t use Amazon AppFlow to transfer data from a Zoom account that
subscribes to the free Basic plan. For more information about Zoom plans, see
[Plans & Pricing](https://zoom.us/pricing "https://zoom.us/pricing") on the Zoom
website.

## Before you begin

To use Amazon AppFlow to transfer data from Zoom to supported destinations, you must meet these
requirements:

- You have an account with Zoom that contains the data that you want to transfer. For more
  information about the Zoom data objects that Amazon AppFlow supports, see [Supported objects](#zoom-objects "#zoom-objects").
- In the Zoom App Marketplace, you've created an OAuth app for Amazon AppFlow. This
  app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes
  authenticated calls to your account. For more information, see [Build an App](https://marketplace.zoom.us/docs/guides/build/ "https://marketplace.zoom.us/docs/guides/build/") in the
  Zoom Developers Docs.
- You've configured If the app with the following settings:
  - You've disabled the option to publish to the Zoom App Marketplace.
  - You've added the recommended scopes below.
  - You've added one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from Zoom. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._

Note the values for client ID and client secret from your OAuth app settings. You provide
these values to Amazon AppFlow when you connect to your Zoom account.

### Recommended scopes

Your OAuth app must allow the necessary scopes for the Zoom APIs. These
scopes permit Amazon AppFlow to securely access your data in Zoom. We recommend that you
enable the scopes below so that Amazon AppFlow can access all supported data objects.

If you want to allow fewer scopes, you can omit any scopes that apply to objects that you
don't want to transfer.

You can add scopes by managing your app in the Zoom App Marketplace.

- `group:master`
- `group:read:admin`
- `group:write:admin`
- `report:master`
- `report:read:admin`
- `report_chat:read:admin`
- `role:master`
- `role:read:admin`
- `role:write:admin`
- `room:master`
- `room:read:admin`
- `room:write:admin`
- `user:master`
- `user:read:admin`
- `user:write:admin`

For more information about these scopes, see [OAuth Scopes](https://marketplace.zoom.us/docs/guides/auth/oauth/oauth-scopes/ "https://marketplace.zoom.us/docs/guides/auth/oauth/oauth-scopes/") in
the Zoom Developers Docs.

## Connecting Amazon AppFlow to your Zoom account

To connect Amazon AppFlow to your Zoom account, provide the client credentials from
your OAuth app. Amazon AppFlow uses these credentials to access your data. If you haven't yet configured
your Zoom account for Amazon AppFlow integration, see [Before you begin](#zoom-prereqs "#zoom-prereqs").

###### To connect to Zoom

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Zoom**.
4. Choose **Create connection**.
5. In the **Connect to Zoom** window, for **Client
   ID** and **Client secret**, enter the client credentials from your
   OAuth app.
6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. A **Sign in** window opens. 9. Enter your user name and password to sign in to your Zoom account. 10. When prompted, verify your sign-in attempt with a one-time passcode. 11. Authorize Amazon AppFlow to access your Zoom account.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Zoom as the data source, you can select this connection.

## Transferring data from Zoom with a flow

To transfer data from Zoom, create an Amazon AppFlow flow, and choose Zoom as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Zoom, see [Supported objects](#zoom-objects "#zoom-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#zoom-destinations "#zoom-destinations").

## Supported destinations

When you create a flow that uses Zoom as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Zoom as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**          | **Field**       | **Data type** | **Supported filters** |
| ------------------- | --------------- | ------------- | --------------------- |
| Daily Report        | Date            | String        |                       |
| Meeting Minutes     | Integer         |               |
| Meetings            | Integer         |               |
| Month Year          | Date            | EQUAL_TO      |
| New Users           | Integer         |               |
| Participants        | Integer         |               |
| Group               | Id              | String        |                       |
| Name                | String          |               |
| Total Members       | Integer         |               |
| Group Admin         | Email           | String        |                       |
| Name                | String          |               |
| Group Member        | Email           | String        |                       |
| First Name          | String          |               |
| Id                  | String          |               |
| Last Name           | String          |               |
| Type                | Integer         |               |
| Role                | Description     | String        |                       |
| Id                  | String          |               |
| Name                | String          |               |
| Total Members       | Integer         |               |
| User                | Created At      | String        |                       |
| Custom Attributes   | List            |               |
| Department          | String          |               |
| Email               | String          |               |
| Employee Unique Id  | String          |               |
| First Name          | String          |               |
| Group Ids           | ByteArray       |               |
| Host Key            | String          |               |
| IM Group Ids        | ByteArray       |               |
| Id                  | String          |               |
| Last Client Version | String          |               |
| Last Login Time     | String          |               |
| Last Name           | String          |               |
| Personal Meeting ID | Integer         |               |
| Plan United Type    | String          |               |
| Role Id             | String          | EQUAL_TO      |
| Status              | String          | EQUAL_TO      |
| Timezone            | String          |               |
| Type                | Integer         |               |
| Verified            | Integer         |               |
| Zoom Room           | Activation Code | String        |                       |
| Id                  | String          |               |
| Location Id         | String          | EQUAL_TO      |
| Name                | String          |               |
| Room Id             | String          |               |
| Status              | String          | EQUAL_TO      |
| Type                | String          | EQUAL_TO      |
| Unassigned Rooms    | Boolean         | EQUAL_TO      |
