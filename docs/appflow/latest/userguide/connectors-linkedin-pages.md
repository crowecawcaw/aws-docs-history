# LinkedIn Pages connector for Amazon AppFlow

LinkedIn Pages is a solution for organizations to post industry updates, job
opportunities, and information. If you're a LinkedIn Pages user, your account contains data
about your pages, followers, and engagement. You can use Amazon AppFlow to transfer data from
LinkedIn Pages to certain AWS services or other supported applications.

## Amazon AppFlow support for LinkedIn Pages

Amazon AppFlow supports LinkedIn Pages as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from LinkedIn Pages.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to LinkedIn Pages.

**Supported API version**

Amazon AppFlow retrieves your LinkedIn Pages data by sending requests to version 202212 of
the LinkedIn API.

## Before you begin

To use Amazon AppFlow to transfer data from LinkedIn Pages to supported destinations, you must meet these
requirements:

- You have a LinkedIn account and a LinkedIn Page. For the steps to create a page, see
  [Create a LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a543852/create-a-linkedin-page?lang=en "https://www.linkedin.com/help/linkedin/answer/a543852/create-a-linkedin-page?lang=en") on LinkedIn Help.
- In LinkedIn Developers, you've created an app, and you've configured it as follows:
  - The app is associated with your LinkedIn Page.
  - The app includes the Marketing Developer Platform product.
  - The app Auth settings include one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from LinkedIn Pages. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._

From the Auth settings for your app, note the client ID and client secret. You provide these
values to Amazon AppFlow when you connect to LinkedIn Pages.

## Connecting Amazon AppFlow LinkedIn Pages

To connect Amazon AppFlow to LinkedIn Pages, provide the client credentials from your LinkedIn
Developers app so that Amazon AppFlow can access your data. If you haven't yet configured your LinkedIn
account for Amazon AppFlow integration, see [Before you begin](#linkedin-pages-prereqs "#linkedin-pages-prereqs").

###### To connect to LinkedIn Pages

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **LinkedIn Pages**.
4. Choose **Create connection**.
5. In the **Connect to LinkedIn Pages** window, enter the following
   information:
   - **Client ID** – The client ID from the Auth settings of your
     LinkedIn Developers app.
   - **Client secret** – The client secret from the Auth settings of
     your LinkedIn Developers app.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your LinkedIn account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses LinkedIn Pages as the data source, you can select this connection.

## Transferring data from LinkedIn Pages with a flow

To transfer data from LinkedIn Pages, create an Amazon AppFlow flow, and choose LinkedIn Pages as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for LinkedIn Pages, see [Supported objects](#linkedin-pages-objects "#linkedin-pages-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#linkedin-pages-destinations "#linkedin-pages-destinations").

## Supported destinations

When you create a flow that uses LinkedIn Pages as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses LinkedIn Pages as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                   | **Field**                           | **Data type**     | **Supported filters** |
| ---------------------------- | ----------------------------------- | ----------------- | --------------------- | ------------------------------------ | ------ | -------- |
| Follower Statistics          | Follower Counts By Association Type | List              |                       |
| Follower Counts By Country   | List                                |                   |                       | Follower Counts By Function          | List   |          |
| Follower Counts By Industry  | List                                |                   |                       | Follower Counts By Region            | List   |          |
| Follower Counts By Seniority | List                                |                   |                       | Follower Counts By Staff Count Range | List   |          |
| Follower Gain                | Struct                              |                   |                       | Organizational Entity                | String |          |
| Start                        | DateTime                            | EQUAL_TO, BETWEEN |                       | Time Granularity Type                | String | EQUAL_TO |
| Time Range                   | Struct                              |                   |
| Page Statistics              | Organization                        | String            |                       |
| Page Statistics By Country   | List                                |                   |                       | Page Statistics By Function          | List   |          |
| Page Statistics By Industry  | List                                |                   |                       | Page Statistics By Region            | List   |          |
| Page Statistics By Seniority | List                                |                   |                       | Page Statistics By Staff Count Range | List   |          |
| Start                        | DateTime                            | EQUAL_TO, BETWEEN |                       | Time Granularity Type                | String | EQUAL_TO |
| Time Range                   | Struct                              |                   |                       | Total Page Statistics                | Struct |          |
| Share Statistics             | Organizational Entity               | String            |                       |
| Start                        | DateTime                            | EQUAL_TO, BETWEEN |                       | Time Granularity Type                | String | EQUAL_TO |
| Time Range                   | Struct                              |                   |                       | Total Share Statistics               | Struct |          |
