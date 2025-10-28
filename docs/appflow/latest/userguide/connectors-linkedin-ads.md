# LinkedIn Ads connector for Amazon AppFlow

LinkedIn Ads is an ad platform that helps organizations and brands to reach audiences
throughout the user community of professionals on LinkedIn. If you use LinkedIn Ads, your
account contains data about your ads and campaigns. You can use Amazon AppFlow to transfer data from
LinkedIn Ads to certain AWS services or other supported applications.

## Amazon AppFlow support for LinkedIn Ads

Amazon AppFlow supports LinkedIn Ads as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from LinkedIn Ads.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to LinkedIn Ads.

**Supported API version**

Amazon AppFlow retrieves your LinkedIn Ads data by sending requests to version 202212 of
the LinkedIn API.

## Before you begin

To use Amazon AppFlow to transfer data from LinkedIn Ads to supported destinations, you must meet these
requirements:

- You have a LinkedIn account and a LinkedIn Page. For the steps to create a page, see
  [Create a LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a543852/create-a-linkedin-page?lang=en "https://www.linkedin.com/help/linkedin/answer/a543852/create-a-linkedin-page?lang=en") on LinkedIn Help.
- In LinkedIn Developers, you've created an app, and you've configured it with the following
  settings:
  - The app is associated with your LinkedIn Page.
  - The app includes the Marketing Developer Platform product.
  - The app Auth settings have one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from LinkedIn Ads. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._

- From your LinkedIn account, you've created a LinkedIn Campaign Manager account, which you
  use to manage your ads on LinkedIn. For the steps to create an account, see [Create an ad account in Campaign Manager as a new advertiser](https://www.linkedin.com/help/linkedin/answer/a426102/create-an-ad-account-in-campaign-manager-as-a-new-advertiser?lang=en "https://www.linkedin.com/help/linkedin/answer/a426102/create-an-ad-account-in-campaign-manager-as-a-new-advertiser?lang=en") on LinkedIn Help.

From the Auth settings for your app, note the client ID and client secret. You provide these
values to Amazon AppFlow when you connect to LinkedIn Ads.

## Connecting Amazon AppFlow to LinkedIn Ads

To connect Amazon AppFlow to LinkedIn Ads, provide the client credentials from your LinkedIn
Developers app so that Amazon AppFlow can access your data. If you haven't yet configured your LinkedIn
account for Amazon AppFlow integration, see [Before you begin](#linkedin-ads-prereqs "#linkedin-ads-prereqs").

###### To connect to LinkedIn Ads

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **LinkedIn Ads**.
4. Choose **Create connection**.
5. In the **Connect to LinkedIn Ads** window, enter the following
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
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. 9. In the window that appears, sign in to your LinkedIn account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses LinkedIn Ads as the data source, you can select this connection.

## Transferring data from LinkedIn Ads with a flow

To transfer data from LinkedIn Ads, create an Amazon AppFlow flow, and choose LinkedIn Ads as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for LinkedIn Ads, see [Supported objects](#linkedin-ads-objects "#linkedin-ads-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#linkedin-ads-destinations "#linkedin-ads-destinations").

## Supported destinations

When you create a flow that uses LinkedIn Ads as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses LinkedIn Ads as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                                  | **Field**             | **Data type**     | **Supported filters** |
| ------------------------------------------- | --------------------- | ----------------- | --------------------- | -------------------------------------------- | ---------- | -------- |
| Ad Account                                  | Change Audit Stamp    | Struct            |                       |
| Currency                                    | String                |                   |                       | Field                                        | String     | EQUAL_TO |
| ID                                          | Long                  | EQUAL_TO          |                       | Name                                         | String     | EQUAL_TO |
| Notified On Campaign Optimization           | Boolean               |                   |                       | Notified On Creative Approval                | Boolean    |          |
| Notified On Creative Rejection              | Boolean               |                   |                       | Notified On End Of Campaign                  | Boolean    |          |
| Notified On New Features Enabled            | Boolean               |                   |                       | Order                                        | String     | EQUAL_TO |
| Reference                                   | String                | EQUAL_TO          |                       | Serving Status                               | List       |          |
| Status                                      | String                | EQUAL_TO          |                       | Test                                         | Boolean    | EQUAL_TO |
| Type                                        | String                | EQUAL_TO          |                       | Version                                      | Struct     |          |
| Ad Analytics                                | Action Click          | Long              |                       |
| Ad Unit Click                               | Long                  |                   |                       | Approximate Unique Impression                | Long       |          |
| Card Click                                  | Long                  |                   |                       | Card Impression                              | Long       |          |
| Click                                       | Long                  |                   |                       | Comment                                      | Long       |          |
| Comment Like                                | Long                  |                   |                       | Company Page Click                           | Long       |          |
| Conversion Value In Local Currency          | BigDecimal            |                   |                       | Cost In Local Currency                       | BigDecimal |          |
| Cost In USD                                 | BigDecimal            |                   |                       | Date Range                                   | Struct     | EQUAL_TO |
| External Website Conversion                 | Long                  |                   |                       | External Website Post Click Conversion       | Long       |          |
| External Website Post View Conversion       | Long                  |                   |                       | Follow                                       | Long       |          |
| Full Screen Play                            | Long                  |                   |                       | Impression                                   | Long       |          |
| Landing Page Click                          | Long                  |                   |                       | Lead Generation Mail Contact Info Share      | Long       |          |
| Lead Generation Mail Interested Click       | Long                  |                   |                       | Like                                         | Long       |          |
| One Click Lead                              | Long                  |                   |                       | One Click Lead Form Open                     | Long       |          |
| Open                                        | Long                  |                   |                       | Other Engagement                             | Long       |          |
| Pivot                                       | String                |                   |                       | Pivot Value                                  | String     |          |
| Pivot Value List                            | List                  |                   |                       | Reaction                                     | Long       |          |
| Send                                        | Long                  |                   |                       | Share                                        | Long       |          |
| Start                                       | DateTime              | EQUAL_TO, BETWEEN |                       | Text URL Click                               | Long       |          |
| Total Engagement                            | Long                  |                   |                       | Video Completion                             | Long       |          |
| Video First Quartile Completion             | Long                  |                   |                       | Video Midpoint Completion                    | Long       |          |
| Video Start                                 | Long                  |                   |                       | Video Third Quartile Completion              | Long       |          |
| Video View                                  | Long                  |                   |                       | Viral Card Click                             | Long       |          |
| Viral Click                                 | Long                  |                   |                       | Viral Comment                                | Long       |          |
| Viral Comment Like                          | Long                  |                   |                       | Viral Company Page Click                     | Long       |          |
| Viral External Website Conversion           | Long                  |                   |                       | Viral External Website Post Click Conversion | Long       |          |
| Viral External Website Post View Conversion | Long                  |                   |                       | Viral Follow                                 | Long       |          |
| Viral Full Screen Play                      | Long                  |                   |                       | Viral Impression                             | Long       |          |
| Viral Job Application                       | BigDecimal            |                   |                       | Viral Landing Page Click                     | Long       |          |
| Viral Like                                  | Long                  |                   |                       | Viral One Click Lead                         | Long       |          |
| Viral One Click Lead Form Open              | Long                  |                   |                       | Viral Other Engagement                       | Long       |          |
| Viral Reaction                              | Long                  |                   |                       | Viral Share                                  | Long       |          |
| Viral Total Engagement                      | Long                  |                   |                       | Viral Video Completion                       | Long       |          |
| Viral Video First Quartile Completion       | Long                  |                   |                       | Viral Video Midpoint Completion              | Long       |          |
| Viral Video Start                           | Long                  |                   |                       | Viral Video Third Quartile Completion        | Long       |          |
| Viral Video View                            | Long                  |                   |                       | viral Card Impression                        | Long       |          |
| Ad Creative                                 | Campaign              | String            | EQUAL_TO              |
| Change Audit Stamp                          | Struct                |                   |                       | Field                                        | String     | EQUAL_TO |
| ID                                          | Long                  | EQUAL_TO          |                       | Order                                        | String     | EQUAL_TO |
| Reference                                   | String                | EQUAL_TO          |                       | Review                                       | List       |          |
| Serving Status                              | List                  |                   |                       | Sort                                         | String     | EQUAL_TO |
| Status                                      | String                | EQUAL_TO          |                       | Test                                         | Boolean    | EQUAL_TO |
| Type                                        | String                | EQUAL_TO          |                       | Variable                                     | Struct     |          |
| Version                                     | Struct                |                   |
| Campaign                                    | Account               | String            | EQUAL_TO              |
| Associated Entity                           | String                | EQUAL_TO          |                       | Audience Expansion Enabled                   | Boolean    |          |
| Campaign Group                              | String                | EQUAL_TO          |                       | Change Audit Stamp                           | Struct     |          |
| Cost Type                                   | String                |                   |                       | Creative Selection                           | String     |          |
| Daily Budget                                | Struct                |                   |                       | Field                                        | String     | EQUAL_TO |
| Format                                      | String                |                   |                       | ID                                           | Long       | EQUAL_TO |
| Locale                                      | Struct                |                   |                       | Name                                         | String     | EQUAL_TO |
| Objective Type                              | String                |                   |                       | Offsite Delivery Enabled                     | Boolean    |          |
| Offsite Preferences                         | Struct                |                   |                       | Optimization Target Type                     | String     |          |
| Order                                       | String                | EQUAL_TO          |                       | Pacing Strategy                              | String     |          |
| Run Schedule                                | Struct                |                   |                       | Serving Status                               | List       |          |
| Status                                      | String                | EQUAL_TO          |                       | Story Delivery Enabled                       | Boolean    |          |
| Targeting Criteria                          | Struct                |                   |                       | Test                                         | Boolean    | EQUAL_TO |
| Total Budget                                | Struct                |                   |                       | Type                                         | String     | EQUAL_TO |
| Unit Cost                                   | Struct                |                   |                       | Version                                      | Struct     |          |
| Campaign Group                              | Account               | String            | EQUAL_TO              |
| Allowed Campaign Type                       | List                  |                   |                       | Backfilled                                   | Boolean    |          |
| Change Audit Stamp                          | Struct                |                   |                       | Field                                        | String     | EQUAL_TO |
| ID                                          | Long                  | EQUAL_TO          |                       | Name                                         | String     | EQUAL_TO |
| Order                                       | String                | EQUAL_TO          |                       | Run Schedule                                 | Long       |          |
| Serving Status                              | List                  |                   |                       | Status                                       | String     | EQUAL_TO |
| Test                                        | Boolean               | EQUAL_TO          |                       | Total Budget                                 | Struct     |          |
| Share Statistic                             | Organizational Entity | String            |                       |
| Start                                       | DateTime              | EQUAL_TO, BETWEEN |                       | Time Range                                   | Struct     |          |
| Total Share Statistic                       | Struct                |                   |
