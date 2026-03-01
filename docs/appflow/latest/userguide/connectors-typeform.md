# Typeform connector for Amazon AppFlow

Typeform is an online survey tool. If you're a Typeform user, your
account contains data about your survey forms and responses.
You can use Amazon AppFlow to transfer data from
Typeform to certain AWS services or other supported applications.

## Amazon AppFlow support for Typeform

Amazon AppFlow supports Typeform as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Typeform.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Typeform.

## Before you begin

To use Amazon AppFlow to transfer data from Typeform to supported destinations, you must meet these
requirements:

- You have an account with Typeform that contains the data that you want to transfer. For more
  information about the Typeform data objects that Amazon AppFlow supports, see [Supported objects](#typeform-objects "#typeform-objects").
- In the settings of your account, you've created either of the following resources for
  Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when
  it makes authenticated calls to your account.
  - A developer app to provide OAuth 2.0 authentication. For the steps to create a developer
    app, see [Create an application in the Typeform admin panel](https://developer.typeform.com/get-started/applications/#1-create-an-application-in-the-typeform-admin-panel "https://developer.typeform.com/get-started/applications/#1-create-an-application-in-the-typeform-admin-panel") in the documentation
    for Typeform Developers Platform.
  - A personal token. For the steps to create one, see [Personal access token
    for Typeform's APIs](https://developer.typeform.com/get-started/personal-access-token "https://developer.typeform.com/get-started/personal-access-token") in the documentation for Typeform Developers
    Platform.

- If you created a developer app, you've configured it with a redirect URL for
  Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Typeform. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

- If you created a personal token, you've included the scopes that provide access to the
  data objects that you want to transfer. For information about Typeform scopes, see
  [OAuth scopes for your
  applications](https://developer.typeform.com/get-started/scopes/ "https://developer.typeform.com/get-started/scopes/") in the documentation for Typeform Developers Platform.

If you created a developer app, note the client ID and client secret. If you created a
personal token, note the token value. You provide these values to Amazon AppFlow when you connect to your
Typeform account.

## Connecting Amazon AppFlow to your Typeform account

To connect Amazon AppFlow to your Typeform account,
provide details from your Typeform project so that Amazon AppFlow can access your data. If you
haven't yet configured your Typeform project for Amazon AppFlow integration, see [Before you begin](#typeform-prereqs "#typeform-prereqs").

###### To connect to Typeform

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Typeform**.
4. Choose **Create connection**.
5. In the **Connect to Typeform** window, for **Select
   authentication type**, choose how to authenticate Amazon AppFlow with your Typeform
   account when it requests to access your data:
   - Choose **OAuth2** to authenticate Amazon AppFlow with the credentials from a
     developer app. Then, enter values for **Client ID** and **Client
     secret**.
   - Choose **PAT** to authenticate Amazon AppFlow with a personal access token.
     Then, enter the token value for **Personal access token**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Depending on the authentication type that you chose, do one of the following:

    * If you chose **OAuth2**, choose **Continue**. Then, in
     the window that appears, sign in to your Typeform account, and grant access to
     Amazon AppFlow.
    * If you chose **PAT**, choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Typeform as the data source, you can select this connection.

## Transferring data from Typeform with a flow

To transfer data from Typeform, create an Amazon AppFlow flow, and choose Typeform as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Typeform, see [Supported objects](#typeform-objects "#typeform-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#typeform-destinations "#typeform-destinations").

## Supported destinations

When you create a flow that uses Typeform as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Typeform as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**      | **Field** | **Data type**      | **Supported filters** |
| --------------- | --------- | ------------------ | --------------------- |
| Form            | \_links   | Struct             |                       |
| created_at      | String    |                    |
| id              | String    |                    |
| last_updated_at | String    |                    |
| search          | String    | EQUAL_TO, CONTAINS |
| self            | Struct    |                    |
| settings        | Struct    |                    |
| theme           | Struct    |                    |
| title           | String    |                    |
| type            | String    |                    |
| workspace_id    | String    | EQUAL_TO           |
| Form Insight    | fields    | List               |                       |
| form            | Struct    |                    |
| Response        | answers   | List               |                       |
| calculated      | Struct    |                    |
| completed       | Boolean   | EQUAL_TO           |
| hidden          | Struct    |                    |
| landed_at       | String    |                    |
| landing_id      | String    |                    |
| metadata        | Struct    |                    |
| query           | String    | EQUAL_TO, CONTAINS |
| response_id     | String    |                    |
| since           | DateTime  | EQUAL_TO           |
| submitted_at    | String    |                    |
| token           | String    |                    |
| until           | DateTime  | EQUAL_TO           |
