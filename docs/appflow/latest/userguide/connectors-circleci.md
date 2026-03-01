# CircleCI connector for Amazon AppFlow

CircleCI is a continuous integration and continuous delivery platform. If you're a
CircleCI user, your account contains data about your projects, pipelines, workflows, and
more. You can use Amazon AppFlow to transfer data from
CircleCI to certain AWS services or other supported applications.

## Amazon AppFlow support for CircleCI

Amazon AppFlow supports CircleCI as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from CircleCI.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to CircleCI.

## Before you begin

To use Amazon AppFlow to transfer data from CircleCI to supported destinations, you must meet these
requirements:

- You have an account with CircleCI that contains the data that you want to transfer. For more
  information about the CircleCI data objects that Amazon AppFlow supports, see [Supported objects](#circleci-objects "#circleci-objects").
- In the user settings for your account, you've created a personal API token. For the steps
  to do this, see [Creating a personal API token](https://circleci.com/docs/managing-api-tokens/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--uscan-en-dsa-maxConv-auth-nb&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQiA4OybBhCzARIsAIcfn9lS-1gBgq0NRzEsA_b20-dhUG8aEHQqIu9wdXFEhSfg0kHsXEhufi8aAtPGEALw_wcB#creating-a-personal-api-token "https://circleci.com/docs/managing-api-tokens/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--uscan-en-dsa-maxConv-auth-nb&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQiA4OybBhCzARIsAIcfn9lS-1gBgq0NRzEsA_b20-dhUG8aEHQqIu9wdXFEhSfg0kHsXEhufi8aAtPGEALw_wcB#creating-a-personal-api-token") in the CircleCI Docs site.

You provide the personal API token to Amazon AppFlow in the settings for your CircleCI
connection.

## Connecting Amazon AppFlow to your CircleCI account

To connect Amazon AppFlow to your CircleCI account, provide your personal API token so
that Amazon AppFlow can access your data. If you haven't yet configured your CircleCI account
for Amazon AppFlow integration, see [Before you begin](#circleci-prereqs "#circleci-prereqs").

###### To connect to CircleCI

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **CircleCI**.
4. Choose **Create connection**.
5. In the **Connect to CircleCI** window, for **CircleCI
   Token**, enter the personal API token from the user settings of your
   CircleCI account
6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses CircleCI as the data source, you can select this connection.

## Transferring data from CircleCI with a flow

To transfer data from CircleCI, create an Amazon AppFlow flow, and choose CircleCI as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for CircleCI, see [Supported objects](#circleci-objects "#circleci-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#circleci-destinations "#circleci-destinations").

## Supported destinations

When you create a flow that uses CircleCI as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses CircleCI as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                   | **Field**          | **Data type**     | **Supported filters** |
| ---------------------------- | ------------------ | ----------------- | --------------------- |
| Context                      | Created At         | String            |                       |
| ID                           | String             |                   |
| Name                         | String             |                   |
| Owner Type                   | String             | EQUAL_TO          |
| Organization Summary Metric  | All Projects       | List              |                       |
| Org Data                     | Struct             |                   |
| Org Project Data             | List               |                   |
| Project Names                | String             | EQUAL_TO          |
| Reporting Window             | String             | EQUAL_TO          |
| Pipeline                     | Branch             | String            | EQUAL_TO              |
| Created At                   | String             |                   |
| Errors                       | List               |                   |
| ID                           | String             |                   |
| Number                       | Integer            |                   |
| Project Slug                 | String             |                   |
| State                        | String             |                   |
| Trigger                      | Struct             |                   |
| Trigger Parameters           | Struct             |                   |
| Updated At                   | String             |                   |
| VCS                          | Struct             |                   |
| Pipeline Workflow            | Canceled By        | String            |                       |
| Created At                   | String             |                   |
| Errored By                   | String             |                   |
| ID                           | String             |                   |
| Name                         | String             |                   |
| Pipeline ID                  | String             |                   |
| Pipeline Number              | Integer            |                   |
| Project Slug                 | String             |                   |
| Started By                   | String             |                   |
| Status                       | String             |                   |
| Stopped At                   | String             |                   |
| Tag                          | String             |                   |
| Project Branch               | Branches           | List              |                       |
| Org ID                       | String             |                   |
| Project ID                   | String             |                   |
| Workflow Name                | String             | EQUAL_TO          |
| Project Flaky Test           | Classname          | String            |                       |
| File                         | String             |                   |
| Job Name                     | String             |                   |
| Job Number                   | Integer            |                   |
| Pipeline Number              | Integer            |                   |
| Source                       | String             |                   |
| Test Name                    | String             |                   |
| Time Wasted                  | Integer            |                   |
| Times Flaked                 | Integer            |                   |
| Workflow Created At          | String             |                   |
| Workflow ID                  | String             |                   |
| Workflow Name                | String             |                   |
| Project Summary Metric       | All Branches       | List              |                       |
| All Workflows                | List               |                   |
| Branches                     | String             | EQUAL_TO          |
| Organization ID              | String             |                   |
| Project Data                 | Struct             |                   |
| Project ID                   | String             |                   |
| Project Workflow Branch Data | List               |                   |
| Project Workflow Data        | List               |                   |
| Reporting Window             | String             | EQUAL_TO          |
| Workflow Names               | String             | EQUAL_TO          |
| Schedule                     | Actor              | Struct            |                       |
| Created At                   | String             |                   |
| Description                  | String             |                   |
| ID                           | String             |                   |
| Name                         | String             |                   |
| Parameters                   | Struct             |                   |
| Project Slug                 | String             |                   |
| Timetable                    | Struct             |                   |
| Updated At                   | String             |                   |
| Workflow Job Timeseries      | Branch             | String            | EQUAL_TO              |
| Granularity                  | String             | EQUAL_TO          |
| Max Ended At                 | String             |                   |
| Metrics                      | Struct             |                   |
| Min Started At               | String             |                   |
| Name                         | String             |                   |
| Start End Date               | DateTime           | EQUAL_TO, BETWEEN |
| Timestamp                    | String             |                   |
| Workflow Metric and Trend    | All Branches       | Boolean           | EQUAL_TO              |
| Branches                     | String             | EQUAL_TO          |
| Metrics                      | Struct             |                   |
| Trends                       | Struct             |                   |
| Workflow Names               | List               |                   |
| Workflow Recent Run          | All Branches       | Boolean           | EQUAL_TO              |
| Branch                       | String             | EQUAL_TO          |
| Created At                   | String             |                   |
| Credits Used                 | Integer            |                   |
| Duration                     | Integer            |                   |
| ID                           | String             |                   |
| Is Approval                  | Boolean            |                   |
| Start End Date               | DateTime           | EQUAL_TO, BETWEEN |
| Status                       | String             |                   |
| Stopped At                   | String             |                   |
| Workflow Summary Metric      | All Branches       | Boolean           | EQUAL_TO              |
| Branch                       | String             | EQUAL_TO          |
| Metrics                      | Struct             |                   |
| Name                         | String             |                   |
| Project ID                   | String             |                   |
| Reporting Window             | String             | EQUAL_TO          |
| Window End                   | String             |                   |
| Window Start                 | String             |                   |
| Workflow Test Metric         | Average Test Count | Integer           |                       |
| Branch                       | String             | EQUAL_TO          |
| Most Failed Tests            | List               |                   |
| Most Failed Tests Extra      | Integer            |                   |
| Slowest Tests                | List               |                   |
| Slowest Tests Extra          | Integer            |                   |
| Test Runs                    | List               |                   |
| Total Test Runs              | Integer            |                   |
